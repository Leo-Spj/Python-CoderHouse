## clase cliente que hereda de persona
from persona_package import persona

class Cliente(persona.Persona):

    codigo_cliente = 0
    tipo_cliente = ""
    estado = ""
    fecha_alta = ""
    fecha_baja = ""


    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
       
    def set_cliente(self, codigo_cliente, tipo_cliente, estado, fecha_alta, fecha_baja):
        self.codigo_cliente = codigo_cliente
        self.tipo_cliente = tipo_cliente
        self.estado = estado
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja





