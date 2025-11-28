# ayurai_chatbot.py
# Simple command-line Ayurveda chatbot backend

ayurveda_syllabus = {
    "Basics": [
        "Definition and aims of Ayurveda",
        "Panchamahabhuta (Five elements)",
        "Tridosha (Vata, Pitta, Kapha)",
        "Sapta Dhatu",
        "Malas",
        "Agni and Ama"
    ],
    "Anatomy & Physiology": [
        "Sharir Rachana",
        "Sharir Kriya",
        "Ojus and Prana",
        "Srotas system"
    ],
    "Pharmacology": [
        "Dravyaguna (Herbal properties)",
        "Rasa, Guna, Virya, Vipaka",
        "Ayurvedic formulations"
    ],
    "Therapies": [
        "Panchakarma",
        "Snehana",
        "Swedana",
        "Vamana, Virechana, Basti"
    ]
}

challenge_questions = [
    "Explain Tridosha with an example.",
    "What happens when Agni is low?",
    "Describe Panchakarma in short.",
    "What is Ama and how does it form?",
    "Which dosha increases in winter season?"
]

def answer_custom(question):
    q = question.lower()
    if "dosha" in q:
        return "Doshas are Vata, Pitta, and Kapha — fundamental energies of the body."
    elif "agni" in q:
        return "Agni represents digestive fire responsible for metabolism."
    elif "panchakarma" in q:
        return "Panchakarma is a five-step detox therapy."
    elif "ama" in q:
        return "Ama is toxin formed due to weak digestion."
    else:
        return "No exact answer available, but it's related to Ayurveda."
