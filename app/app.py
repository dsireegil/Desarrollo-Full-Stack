from flask import Flask, jsonify, request

app = Flask(__name__)


tareas = []

# GET
@app.route('/tareas', methods=['GET'])
def get_tareas():
    return jsonify(tareas)

# POST
@app.route('/tareas', methods=['POST'])
def create_tarea():
    data = request.get_json()

    tarea = {
        "id": len(tareas) + 1,
        "titulo": data["titulo"],
        "descripcion": data["descripcion"]
    }

    tareas.append(tarea)

    return jsonify({
        "message": "Tarea creada correctamente",
        "tarea": tarea
    }), 201

# PUT
@app.route('/tareas/<int:id>', methods=['PUT'])
def update_tarea(id):
    data = request.get_json()

    for tarea in tareas:
        if tarea["id"] == id:
            tarea["titulo"] = data["titulo"]
            tarea["descripcion"] = data["descripcion"]
            return jsonify({
                "message": "Tarea actualizada",
                "tarea": tarea
            })

    return jsonify({"message": "Tarea no encontrada"}), 404

# DELETE
@app.route('/tareas/<int:id>', methods=['DELETE'])
def delete_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            tareas.remove(tarea)
            return jsonify({"message": "Tarea eliminada"})

    return jsonify({"message": "Tarea no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
