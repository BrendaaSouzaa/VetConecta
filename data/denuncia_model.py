from dataclasses import dataclass
from typing import Optional

@dataclass
class Denuncia:
    id_denuncia: Optional[int] 
    id_usuario: int
    id_admin: Optional[int]
    motivo: str
    data_denuncia: str
    status: str
