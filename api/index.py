from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # Obligatoire pour autoriser notre page HTML à lire ces données
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        
        # Voici nos "produits" gérés par Python
        produits = [
            {"id": 1, "nom": "T-shirt Super Python", "prix": 25.00},
            {"id": 2, "nom": "Tasse du Développeur", "prix": 15.50},
            {"id": 3, "nom": "Clavier Mécanique", "prix": 120.00}
        ]
        
        self.wfile.write(json.dumps(produits).encode('utf-8'))
        return
