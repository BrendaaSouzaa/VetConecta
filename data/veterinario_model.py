from dataclasses import dataclass

@dataclass
class Veterinario:
    id_veterinario: int
    crmv: str
    verificado: bool
    bio: str
    