from dataclasses import dataclass

@dataclass
class Denuncia:
    id: int
    id_usuario: int
    id_comentario: int | None  # pode ser nulo
    motivo: str
    data_envio: str  # formato DATETIME
    status: str  # padrão: 'pendente'
