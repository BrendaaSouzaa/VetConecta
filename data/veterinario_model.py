from dataclasses import dataclass

@dataclass
class Veterinario:
    id_usuario: int
    crmv: str
    verificado: bool
    bio: str
    