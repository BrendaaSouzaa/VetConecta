from dataclasses import dataclass

@dataclass
class Usuario:
    id_usuario: int
    crmv: str
    verificacao: str
    bio: str
    