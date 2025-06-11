from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    id_veterinario: int
    data_verificacao: str
    status_verificacao: str
    # Chave estrangeira em veterinario