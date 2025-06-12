from flask import Flask, render_template, request, redirect, url_for, session
import re
from data import symptom_disease_mapping, doctors

app = Flask(__name__)
app.secret_key = 'demo_medical_chatbot_2025'

def analyze_symptoms(symptoms_text):
    """Analyse les symptômes et retourne la maladie et spécialité correspondantes"""
    symptoms_lower = symptoms_text.lower().strip()
    
    # Recherche exacte d'abord
    for symptom_key, result in symptom_disease_mapping.items():
        if symptoms_lower == symptom_key.lower():
            return result
    
    # Recherche par mots-clés si pas de correspondance exacte
    best_match = None
    max_matches = 0
    
    for symptom_key, result in symptom_disease_mapping.items():
        symptom_words = set(symptom_key.lower().split(', '))
        input_words = set(re.findall(r'\b\w+\b', symptoms_lower))
        
        matches = len(symptom_words.intersection(input_words))
        if matches > max_matches and matches > 0:
            max_matches = matches
            best_match = result
    
    return best_match if best_match else {
        "maladie": "Consultation générale recommandée", 
        "specialite": "Médecine générale"
    }

@app.route('/')
def index():
    """Page d'accueil - Analyse des symptômes"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Traite l'analyse des symptômes"""
    symptoms = request.form.get('symptoms', '').strip()
    
    if not symptoms:
        return render_template('index.html', error="Veuillez entrer vos symptômes")
    
    # Analyser les symptômes
    result = analyze_symptoms(symptoms)
    
    # Stocker les résultats dans la session
    session['symptoms'] = symptoms
    session['maladie'] = result['maladie']
    session['specialite'] = result['specialite']
    
    return render_template('index.html', 
                         symptoms=symptoms,
                         maladie=result['maladie'],
                         specialite=result['specialite'],
                         show_results=True)

@app.route('/appointment')
def appointment():
    """Page de prise de rendez-vous"""
    # Vérifier si l'utilisateur vient de l'analyse
    if 'specialite' not in session:
        return redirect(url_for('index'))
    
    return render_template('appointment.html',
                         specialite=session.get('specialite'),
                         maladie=session.get('maladie'))

@app.route('/find_doctors', methods=['POST'])
def find_doctors():
    """Recherche les médecins disponibles"""
    city = request.form.get('city', '').strip()
    specialite = session.get('specialite')
    
    if not city:
        return render_template('appointment.html', 
                             specialite=specialite,
                             maladie=session.get('maladie'),
                             error="Veuillez entrer votre ville")
    
    # Rechercher les médecins
    available_doctors = []
    city_lower = city.lower()
    
    # Recherche flexible par ville
    for city_key, specialties in doctors.items():
        if city_lower in city_key.lower() or city_key.lower() in city_lower:
            if specialite in specialties:
                for doctor in specialties[specialite]:
                    available_doctors.append({
                        'nom': doctor['nom'],
                        'ville': city_key,
                        'disponibilites': doctor['disponibilites']
                    })
    
    return render_template('appointment.html',
                         specialite=specialite,
                         maladie=session.get('maladie'),
                         city=city,
                         doctors=available_doctors,
                         show_doctors=True)

@app.route('/book/<doctor_name>/<date>')
def book_appointment(doctor_name, date):
    """Confirme la réservation"""
    return render_template('confirmation.html',
                         doctor_name=doctor_name,
                         date=date,
                         specialite=session.get('specialite'),
                         maladie=session.get('maladie'))

@app.route('/reset')
def reset():
    """Remet à zéro la session"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)