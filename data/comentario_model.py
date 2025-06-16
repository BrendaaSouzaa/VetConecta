from dataclasses import dataclass

@dataclass
class Comentario:
    id: int
    id_usuario: int
    id_artigo: int
    texto: str
    data_comentario: str  # formato DATE
    data_moderacao: str | None  # pode ser nulo se ainda não moderado
