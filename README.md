# 🏥 Assistant Médical IA - Démo

Une application web de démonstration simulant un assistant médical intelligent utilisant Flask et Python.

## 🚀 Fonctionnalités

### Page 1 - Analyse des Symptômes
- ✅ Saisie des symptômes par l'utilisateur
- ✅ Analyse automatique et diagnostic probable
- ✅ Recommandation de spécialité médicale
- ✅ Proposition de prise de rendez-vous

### Page 2 - Prise de Rendez-vous
- ✅ Recherche par ville
- ✅ Liste des médecins disponibles par spécialité
- ✅ Affichage des créneaux disponibles
- ✅ Réservation de rendez-vous

### Page 3 - Confirmation
- ✅ Récapitulatif du rendez-vous
- ✅ Informations importantes
- ✅ Contact du cabinet

## 📁 Structure du projet

```
medical-chatbot/
├── app.py                 # Application Flask principale
├── data.py               # Base de données simulée
├── requirements.txt      # Dépendances Python
├── templates/           # Templates HTML
│   ├── index.html       # Page d'analyse des symptômes
│   ├── appointment.html # Page de prise de rendez-vous
│   └── confirmation.html# Page de confirmation
└── README.md           # Ce fichier
```

## 🛠️ Installation

### Prérequis
- Python 3.7 ou plus récent
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
   ```bash
   # Créer un dossier pour le projet
   mkdir medical-chatbot
   cd medical-chatbot
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv venv
   
   # Sur Windows
   venv\Scripts\activate
   
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Créer la structure des dossiers**
   ```bash
   mkdir templates
   ```

5. **Placer les fichiers dans la bonne structure**
   - `app.py` à la racine
   - `data.py` à la racine
   - `requirements.txt` à la racine
   - Les fichiers HTML dans le dossier `templates/`

## 🚀 Lancement de l'application

1. **Démarrer le serveur Flask**
   ```bash
   python app.py
   ```

2. **Ouvrir votre navigateur**
   - Aller à l'adresse : `http://localhost:5000`
   - L'application devrait s'afficher

## 📝 Utilisation

### 1. Analyse des Symptômes
1. Saisissez vos symptômes dans le champ de texte
2. Cliquez sur "Analyser mes symptômes"
3. Consultez le diagnostic et la spécialité recommandée
4. Cliquez sur "Prendre rendez-vous" si souhaité

### 2. Prise de Rendez-vous
1. Entrez votre ville
2. Consultez la liste des médecins disponibles
3. Choisissez une date disponible
4. Confirmez votre rendez-vous

### 3. Exemples de symptômes testables
- `fièvre, toux, fatigue` → Médecine générale
- `douleur thoracique, essoufflement` → Cardiologie  
- `éruption cutanée, démangeaisons` → Dermatologie
- `douleurs articulaires, raideurs` → Rhumatologie
- `mal de gorge, fièvre` → ORL
- `maux de tête, vertiges` → Neurologie

### 4. Villes disponibles
- Casablanca
- Rabat
- Marrakech
- Fès
- Tanger

## 🔧 Personnalisation

### Ajouter de nouveaux symptômes
Modifiez le fichier `data.py` dans la section `symptom_disease_mapping` :

```python
symptom_disease_mapping = {
    "vos symptômes": {
        "maladie": "Nom de la maladie",
        "specialite": "Spécialité médicale"
    }
}
```

### Ajouter des médecins
Modifiez le fichier `data.py` dans la section `doctors` :

```python
doctors = {
    "Votre Ville": {
        "Spécialité": [
            {
                "nom": "Dr. Nom Médecin",
                "disponibilites": ["2025-06-15", "2025-06-16"]
            }
        ]
    }
}
```


