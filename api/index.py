from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def lire_produits():
    # Catalogue avec gestion des PROMOTIONS, STOCK et NOUVELLE CATÉGORIE "Divers"
    return [
        {
            "id": 1, 
            "nom": "Ensemble Coton Premium", 
            "description": "Confort absolu, coupe moderne pour homme.",
            "prix": 45000, 
            "ancien_prix": 60000, # Affichera un prix barré
            "stock": 3,           # Affichera "Plus que 3 en stock"
            "categorie": "Homme",
            "badge": "PROMO",
            "image": "https://images.unsplash.com/photo-1617137968427-85924c800a22?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 2, 
            "nom": "Robe de Soirée Élégante", 
            "description": "Design exclusif, parfaite pour vos événements. Finitions soignées.",
            "prix": 65000, 
            "ancien_prix": None, 
            "stock": 12,
            "categorie": "Femme",
            "badge": "EXCLUSIVITÉ",
            "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 3, 
            "nom": "Baskets Urbaines", 
            "description": "Style streetwear, robustes et confortables.",
            "prix": 35000, 
            "ancien_prix": None,
            "stock": 4, # Créera un sentiment d'urgence
            "categorie": "Homme",
            "badge": "",
            "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 4, 
            "nom": "T-shirt Coton Enfant", 
            "description": "Doux pour la peau, résistant aux jeux.",
            "prix": 15000, 
            "ancien_prix": 20000,
            "stock": 25,
            "categorie": "Enfants",
            "badge": "BEST-SELLER",
            "image": "https://images.unsplash.com/photo-1519241047957-be31d7379a5d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 5, 
            "nom": "Parfum Signature", 
            "description": "Notes boisées et florales. Tenue longue durée.",
            "prix": 55000, 
            "ancien_prix": None,
            "stock": 2,
            "categorie": "Divers",
            "badge": "NOUVEAU",
            "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        }
    ]
