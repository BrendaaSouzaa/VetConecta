from dataclasses import dataclass
from data.veterinario_model import Veterinario

@dataclass
class VerificacaoCRMV:
    id: int
    veterinario: Veterinario
    data_verificacao: str
    status_verificacao: str
    