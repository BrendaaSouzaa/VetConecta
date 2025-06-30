from dataclasses import dataclass

from data.usuario_model import Usuario

@dataclass
class Veterinario(Usuario):
    pass
    crmv: str
    verificado: bool
    bio: str
    id_veterinario: int = 0