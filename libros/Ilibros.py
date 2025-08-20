from abc import ABC, abstractmethod
from typing import List
from Libros import Libros

class ILibros(ABC):
    @abstractmethod
    def libros(self) -> List[Libros]:
        pass

    @abstractmethod
    def agregar_libro(self, l: Libros) -> bool:
        pass

    @abstractmethod
    def modificar_libro(self, l: Libros) -> bool:
        pass

    @abstractmethod
    def eliminar_libro(self, l: Libros) -> bool:
        pass

    @abstractmethod
    def busca_libro(self, l: Libros) -> bool:
        pass

    # Nuevos métodos
    @abstractmethod
    def contar_por_estado(self) -> dict:
        pass

    @abstractmethod
    def libros_por_genero(self, genero: str) -> List[Libros]:
        pass