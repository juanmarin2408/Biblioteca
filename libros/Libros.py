class Libros:
    def __init__(self, anio=None, referencia=None, autor=None, nombre=None,
                 genero=None, estado=None, fecha_inicio=None, fecha_fin=None):
        self.anio = anio
        self.referencia = referencia
        self.autor = autor
        self.nombre = nombre
        self.genero = genero
        self.estado = estado
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        return (f"Libro(referencia='{self.referencia}', nombre='{self.nombre}', autor='{self.autor}', "
                f"anio={self.anio}, genero='{self.genero}', estado='{self.estado}', "
                f"fecha_inicio={self.fecha_inicio}, fecha_fin={self.fecha_fin})")

    def __eq__(self, other):
        if not isinstance(other, Libros):
            return False
        return self.referencia == other.referencia
