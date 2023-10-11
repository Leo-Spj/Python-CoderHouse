class Persona:

    nombre = ""
    apellido = ""
    edad = 0
    fecha_nacimiento = ""
    id = 0
    estado_civil = ""
    nacionalidad = ""
    direccion = ""
    telefono = ""
    email = ""
    estudios = []
    experiencia_laboral = []
    habilidades = []
    idiomas = []


    def __init__(self, nombre, apellido, edad):
        self.nombre =  nombre
        self.apellido = apellido
        self.edad = int(edad)


    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido

    def set_edad(self, edad):
        self.edad = int(edad)

    def get_edad(self):
        return self.edad

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_id(self, id):
        self.id = int(id)

    def get_id(self):
        return self.id
    
    def set_estado_civil(self, estado_civil):
        self.estado_civil = estado_civil

    def get_estado_civil(self):
        return self.estado_civil
    
    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def get_nacionalidad(self):
        return self.nacionalidad
    
    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_direccion(self):
        return self.direccion
    
    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_telefono(self):
        return self.telefono
    
    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email
    
    def set_estudios(self, estudios):
        self.estudios.append(estudios)

    def get_estudios(self):
        return self.estudios
    
    def set_experiencia_laboral(self, experiencia_laboral):
        self.experiencia_laboral.append(experiencia_laboral)

    def get_experiencia_laboral(self):
        return self.experiencia_laboral
    
    def set_habilidades(self, habilidades):
        self.habilidades.append(habilidades)

    def get_habilidades(self):
        return self.habilidades
    
    def set_idiomas(self, idiomas):
        self.idiomas.append(idiomas)

    def get_idiomas(self):
        return self.idiomas
    
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", Apellido: " + self.apellido + ", Edad: " + str(self.edad) 