#from crypt import methods
from flask import Flask, jsonify, request
app = Flask(__name__) 

# Datos de ejemplo 
contratistas = [ {"id": 1, "name": "Contractor 1", "offers": [], "address": "avenida cordoba 775"} ] 
profesionales = [{"id": 1, "name": "Professional 1", "services": [], "address": "reconquista 775"} ] 
ofertas = [{"id": 1, "contractor_id": 1, "title": "Plumbing Work", "description": "Fix the sink", "status": "open"} ] 
servicios = [{"id": 1, "professional_id": 1, "title": "Electrician", "description": "Certified electrician available for wiring and repairs"} ] 

@app.route("/") 
def index(): 
    return "¡Bienvenido al Mercado de Trabajo! Aquí, los contratistas pueden publicar ofertas de empleo y los profesionales pueden ofrecer sus servicios." 

# Rutas para contratistas 
@app.route("/contratistas") 
def get_contratistas(): 
    return jsonify(contratistas) 
@app.route("/contratistas", methods=["POST"]) 
def add_contratista(): 
    contratista_details = request.get_json() 
    new_contratista = { 
        "id": len(contratistas) + 1, 
        "name": contratista_details["name"], 
        "offers": [] 
    } 
    contratistas.append(new_contratista) 
    return jsonify({"message": "Contractor successfully created"}), 200 

# Rutas para profesionales 
@app.route("/profesionales") 
def get_profesionales(): 
    return jsonify(profesionales) 

@app.route("/profesionales", methods=["POST"]) 
def add_profesional(): 
    profesional_details = request.get_json() 
    new_profesional = { 
        "id": len(profesionales) + 1, 
        "name": profesional_details["name"], 
        "services": [] 
    } 
    profesionales.append(new_profesional) 
    return jsonify({"message": "Professional successfully created"}), 200 

# Rutas para ofertas de trabajo 
@app.route("/ofertas",methods=["GET"]) 
def get_ofertas(): 
    return jsonify(ofertas)  

@app.route("/ofertas", methods=["POST"]) 
def add_oferta(): 
    oferta_details = request.get_json() 
    new_oferta = { 
        "id": len(ofertas) + 1, 
        "contractor_id": oferta_details["contractor_id"], 
        "title": oferta_details["title"], 
        "description": oferta_details["description"], 
        "status": "open" 
    } 
    ofertas.append(new_oferta) 
    return jsonify({"message": "Offer successfully created"}), 200 

@app.route("/ofertas/<int:id>", methods=["PUT"]) 
def update_oferta(id): 
    oferta_details = request.get_json() 
    for oferta in ofertas: 
        if oferta["id"] == id: 
            oferta["title"] = oferta_details["title"] 
            oferta["description"] = oferta_details["description"] 
            oferta["status"] = oferta_details["status"] 
            return jsonify({"message": "Offer successfully updated"}), 200 
    return jsonify({"message": "Offer not found"}), 400 

# Rutas para servicios ofrecidos 

@app.route("/servicios",methods=["GET"])
def get_servicios(): 
    return jsonify(servicios) 

@app.route("/servicios", methods=["POST"]) 
def add_servicio(): 
    servicio_details = request.get_json() 
    new_servicio= { 
        "id": len(servicios) + 1, 
        "professional_id": servicio_details["professional_id"], 
        "title": servicio_details["title"], 
        "description": servicio_details["description"] 
    } 
    servicios.append(new_servicio) 
    return jsonify({"message": "Service successfully created"}), 200 

@app.route("/servicios/<int:id>", methods=["PUT"]) 
def update_servicio(id): 
    servicio_details = request.get_json() 
    for servicio in servicios: 
        if servicio["id"] == id: 
            servicio["title"] = servicio_details["title"] 
            servicio["description"] = servicio_details["description"] 
            return jsonify({"message": "Service successfully updated"}), 200 
    return jsonify({"message": "Service not found"}), 400 




if __name__ == "__main__": 
    app.run(debug=True, port=4000) 