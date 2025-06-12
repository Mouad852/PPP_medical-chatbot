# Base de données simulée pour le chatbot médical

# Mapping des symptômes vers les maladies et spécialités
symptom_disease_mapping = {
    # Cardiologie
    "douleur thoracique, essoufflement": {
        "maladie": "Problème cardiaque possible",
        "specialite": "Cardiologie"
    },
    "palpitations, fatigue": {
        "maladie": "Troubles du rythme cardiaque",
        "specialite": "Cardiologie"
    },
    "douleur poitrine, sueurs": {
        "maladie": "Syndrome coronarien aigu possible",
        "specialite": "Cardiologie"
    },
    
    # Médecine générale
    "fièvre, toux, fatigue": {
        "maladie": "Syndrome grippal",
        "specialite": "Médecine générale"
    },
    "maux de tête, fièvre": {
        "maladie": "Syndrome fébrile",
        "specialite": "Médecine générale"
    },
    "nausées, vomissements, diarrhée": {
        "maladie": "Gastro-entérite",
        "specialite": "Médecine générale"
    },
    "fatigue, perte d'appétit": {
        "maladie": "Asthénie",
        "specialite": "Médecine générale"
    },
    
    # Dermatologie
    "éruption cutanée, démangeaisons": {
        "maladie": "Dermatite allergique",
        "specialite": "Dermatologie"
    },
    "boutons, acné": {
        "maladie": "Acné",
        "specialite": "Dermatologie"
    },
    "plaques rouges, squames": {
        "maladie": "Psoriasis possible",
        "specialite": "Dermatologie"
    },
    "taches brunes, grain de beauté": {
        "maladie": "Lésion pigmentaire",
        "specialite": "Dermatologie"
    },
    
    # Rhumatologie
    "douleurs articulaires, raideurs": {
        "maladie": "Arthrite",
        "specialite": "Rhumatologie"
    },
    "mal de dos, sciatique": {
        "maladie": "Lombalgie",
        "specialite": "Rhumatologie"
    },
    "douleur genou, gonflement": {
        "maladie": "Arthrose du genou",
        "specialite": "Rhumatologie"
    },
    
    # Ophtalmologie
    "vision floue, maux de tête": {
        "maladie": "Troubles de la réfraction",
        "specialite": "Ophtalmologie"
    },
    "yeux rouges, larmoiement": {
        "maladie": "Conjonctivite",
        "specialite": "Ophtalmologie"
    },
    "douleur oeil, vision trouble": {
        "maladie": "Glaucome possible",
        "specialite": "Ophtalmologie"
    },
    
    # ORL
    "mal de gorge, fièvre": {
        "maladie": "Angine",
        "specialite": "ORL"
    },
    "oreilles bouchées, surdité": {
        "maladie": "Bouchon cerumen",
        "specialite": "ORL"
    },
    "sinusite, congestion nasale": {
        "maladie": "Sinusite",
        "specialite": "ORL"
    },
    
    # Gynécologie
    "douleurs pelviennes, règles irrégulières": {
        "maladie": "Troubles gynécologiques",
        "specialite": "Gynécologie"
    },
    "pertes vaginales, démangeaisons": {
        "maladie": "Infection vaginale",
        "specialite": "Gynécologie"
    },
    
    # Neurologie
    "maux de tête, vertiges": {
        "maladie": "Céphalées",
        "specialite": "Neurologie"
    },
    "tremblements, rigidité": {
        "maladie": "Troubles neurologiques",
        "specialite": "Neurologie"
    },
    "perte de mémoire, confusion": {
        "maladie": "Troubles cognitifs",
        "specialite": "Neurologie"
    }
}

# Base de données des médecins par ville et spécialité
doctors = {
    "Casablanca": {
        "Cardiologie": [
            {
                "nom": "Dr. Ahmed Benali",
                "disponibilites": ["2025-06-15", "2025-06-17", "2025-06-20", "2025-06-22"]
            },
            {
                "nom": "Dr. Fatima Alaoui",
                "disponibilites": ["2025-06-16", "2025-06-18", "2025-06-21", "2025-06-23"]
            },
            {
                "nom": "Dr. Youssef Tazi",
                "disponibilites": ["2025-06-14", "2025-06-19", "2025-06-24"]
            }
        ],
        "Médecine générale": [
            {
                "nom": "Dr. Aicha Bennani",
                "disponibilites": ["2025-06-13", "2025-06-15", "2025-06-17", "2025-06-19"]
            },
            {
                "nom": "Dr. Omar Idrissi",
                "disponibilites": ["2025-06-14", "2025-06-16", "2025-06-18", "2025-06-20"]
            },
            {
                "nom": "Dr. Nadia Hakim",
                "disponibilites": ["2025-06-15", "2025-06-21", "2025-06-22"]
            }
        ],
        "Dermatologie": [
            {
                "nom": "Dr. Laila Chraibi",
                "disponibilites": ["2025-06-16", "2025-06-18", "2025-06-20"]
            },
            {
                "nom": "Dr. Karim Fassi",
                "disponibilites": ["2025-06-17", "2025-06-19", "2025-06-21"]
            }
        ],
        "Rhumatologie": [
            {
                "nom": "Dr. Rachid Ouali",
                "disponibilites": ["2025-06-15", "2025-06-22", "2025-06-24"]
            }
        ],
        "Ophtalmologie": [
            {
                "nom": "Dr. Samira Nejjar",
                "disponibilites": ["2025-06-14", "2025-06-17", "2025-06-20"]
            }
        ],
        "ORL": [
            {
                "nom": "Dr. Hassan Benomar",
                "disponibilites": ["2025-06-16", "2025-06-19", "2025-06-23"]
            }
        ],
        "Neurologie": [
            {
                "nom": "Dr. Amina Sekkat",
                "disponibilites": ["2025-06-18", "2025-06-21", "2025-06-25"]
            }
        ]
    },
    
    "Rabat": {
        "Cardiologie": [
            {
                "nom": "Dr. Mustapha Alami",
                "disponibilites": ["2025-06-14", "2025-06-16", "2025-06-18"]
            },
            {
                "nom": "Dr. Zineb Cherkaoui",
                "disponibilites": ["2025-06-15", "2025-06-17", "2025-06-19"]
            }
        ],
        "Médecine générale": [
            {
                "nom": "Dr. Said Benjelloun",
                "disponibilites": ["2025-06-13", "2025-06-15", "2025-06-17"]
            },
            {
                "nom": "Dr. Khadija Lamrani",
                "disponibilites": ["2025-06-14", "2025-06-16", "2025-06-18"]
            }
        ],
        "Dermatologie": [
            {
                "nom": "Dr. Abdelali Berrada",
                "disponibilites": ["2025-06-17", "2025-06-20", "2025-06-22"]
            }
        ],
        "Gynécologie": [
            {
                "nom": "Dr. Latifa Benkirane",
                "disponibilites": ["2025-06-15", "2025-06-18", "2025-06-21"]
            }
        ],
        "ORL": [
            {
                "nom": "Dr. Khalid Elouardi",
                "disponibilites": ["2025-06-16", "2025-06-19", "2025-06-22"]
            }
        ]
    },
    
    "Marrakech": {
        "Cardiologie": [
            {
                "nom": "Dr. Bouchra Skalli",
                "disponibilites": ["2025-06-15", "2025-06-18", "2025-06-21"]
            }
        ],
        "Médecine générale": [
            {
                "nom": "Dr. Abdellah Tounsi",
                "disponibilites": ["2025-06-14", "2025-06-16", "2025-06-19"]
            },
            {
                "nom": "Dr. Malika Essaadi",
                "disponibilites": ["2025-06-15", "2025-06-17", "2025-06-20"]
            }
        ],
        "Dermatologie": [
            {
                "nom": "Dr. Youssef Bennani",
                "disponibilites": ["2025-06-16", "2025-06-19", "2025-06-23"]
            }
        ],
        "Rhumatologie": [
            {
                "nom": "Dr. Amina Lahlou",
                "disponibilites": ["2025-06-17", "2025-06-20", "2025-06-24"]
            }
        ]
    },
    
    "Fès": {
        "Médecine générale": [
            {
                "nom": "Dr. Driss Benali",
                "disponibilites": ["2025-06-13", "2025-06-15", "2025-06-18"]
            },
            {
                "nom": "Dr. Souad Filali",
                "disponibilites": ["2025-06-14", "2025-06-17", "2025-06-20"]
            }
        ],
        "Cardiologie": [
            {
                "nom": "Dr. Mohamed Tazi",
                "disponibilites": ["2025-06-16", "2025-06-19", "2025-06-22"]
            }
        ],
        "Neurologie": [
            {
                "nom": "Dr. Hind Zouani",
                "disponibilites": ["2025-06-15", "2025-06-18", "2025-06-21"]
            }
        ]
    },
    
    "Tanger": {
        "Médecine générale": [
            {
                "nom": "Dr. Tarik Benhamou",
                "disponibilites": ["2025-06-14", "2025-06-16", "2025-06-19"]
            }
        ],
        "ORL": [
            {
                "nom": "Dr. Siham Kadiri",
                "disponibilites": ["2025-06-15", "2025-06-18", "2025-06-21"]
            }
        ],
        "Ophtalmologie": [
            {
                "nom": "Dr. Aziz Berrada",
                "disponibilites": ["2025-06-17", "2025-06-20", "2025-06-23"]
            }
        ]
    }
}