from dataclasses import dataclass
from datetime import date

@dataclass
class Seguida:
    id_veterinario: int
    id_tutor: int
    data_inicio: date
# verificar se data_inicio est´CORRETO