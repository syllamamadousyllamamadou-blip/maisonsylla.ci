from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# On crée notre application
app = FastAPI()

# On autorise notre site web à discuter avec cette application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Notre nouvelle liste de produits avec des emojis en guise d'images !
@app.get("/api")
def lire_produits():
    return [
        {"id": 1, "nom": "T-shirt Super Python", "prix": 25.00, "image": "🐍"},
        {"id": 2, "nom": "Tasse du Développeur", "prix": 15.50, "image": "☕"},
        {"id": 3, "nom": "Clavier Mécanique", "prix": 120.00, "image": "⌨️"}
    ]
