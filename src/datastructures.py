"""
update this file to implement the requested API endpoints
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # Inicializar con los 3 miembros de la familia Jackson
        self._members = []
        
        # Agregar los miembros iniciales
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })
        
        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })
        
        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    # Este método genera un 'id' único al agregar miembros a la lista
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Si el miembro no tiene id, generar uno automáticamente
        if "id" not in member:
            member["id"] = self._generate_id()
        else:
            # Si viene con id, actualizar el _next_id si es necesario
            if member["id"] >= self._next_id:
                self._next_id = member["id"] + 1
        
        # Agregar el apellido automáticamente
        member["last_name"] = self.last_name
        
        # Agregar el miembro a la lista
        self._members.append(member)
        
        return member

    def delete_member(self, id):
        # Buscar el miembro con el id proporcionado y eliminarlo
        for i, member in enumerate(self._members):
            if member["id"] == id:
                deleted_member = self._members.pop(i)
                return deleted_member
        
        # Si no se encuentra, retornar None
        return None

    def get_member(self, id):
        # Buscar y retornar el miembro con el id proporcionado
        for member in self._members:
            if member["id"] == id:
                return member
        
        # Si no se encuentra, retornar None
        return None

    def get_all_members(self):
        return self._members