## clase cliente que hereda de persona
from persona_package import persona

class Cliente(persona.Persona):

    codigo_cliente = 0
    tipo_cliente = ""
    estado = "Activo"
    fecha_alta = ""
    fecha_baja = ""


    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
       
    def set_datos_cliente(self, codigo_cliente, tipo_cliente, fecha_alta):
        self.codigo_cliente = codigo_cliente
        self.tipo_cliente = tipo_cliente
        self.fecha_alta = fecha_alta

    def get_codigo_cliente(self):
        return self.codigo_cliente
    
    def set_codigo_cliente(self, codigo_cliente):
        self.codigo_cliente = codigo_cliente
    
    def get_tipo_cliente(self):
        return self.tipo_cliente
    
    def set_tipo_cliente(self, tipo_cliente):
        self.tipo_cliente = tipo_cliente

    def get_estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado

    def get_fecha_alta(self):
        return self.fecha_alta
    
    def set_fecha_alta(self, fecha_alta):
        self.fecha_alta = fecha_alta

    def get_fecha_baja(self):
        return self.fecha_baja
    
    def set_fecha_baja(self, fecha_baja):
        self.fecha_baja = fecha_baja
    

    def __str__(self):
        return super().__str__() + ", codigo: " + str(self.codigo_cliente) + ", tipo: " + self.tipo_cliente + ", estado: " + self.estado + ", fecha alta: " + self.fecha_alta




