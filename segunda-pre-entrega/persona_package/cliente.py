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
       
    def set_datos_cliente(self, codigo_cliente, tipo_cliente, estado, fecha_alta):
        self.codigo_cliente = codigo_cliente
        self.tipo_cliente = tipo_cliente
        self.estado = estado
        self.fecha_alta = fecha_alta

    def __str__(self):
        return super().__str__() + ", codigo: " + str(self.codigo_cliente) + ", tipo: " + self.tipo_cliente + ", estado: " + self.estado + ", fecha alta: " + self.fecha_alta




