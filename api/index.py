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
    # Catalogue mis à jour pour un rendu professionnel en Franc CFA
    return [
        {
            "id": 1, 
            "nom": "Sac en Cuir Artisanal", 
            "description": "Fait main avec passion. Élégant et robuste pour votre quotidien.",
            "prix": 25000, 
            "image": "👜"
        },
        {
            "id": 2, 
            "nom": "Collier Traditionnel", 
            "description": "Authenticité et raffinement pour sublimer vos tenues.",
            "prix": 12500, 
            "image": "📿"
        },
        {
            "id": 3, 
            "nom": "Ensemble Coton Bio", 
            "description": "Confort absolu et respect de l'environnement.",
            "prix": 18000, 
            "image": "👕"
        },
        {
            "id": 4, 
            "nom": "Sandales Tressées", 
            "description": "Légères et confortables, parfaites pour la saison.",
            "prix": 15000, 
            "image": "👡"
        }
    ]
