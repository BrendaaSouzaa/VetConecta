from dataclasses import dataclass

@dataclass
class Administrador:
    id_admin: int
    nome: str
    email: str
    senha: str
    

from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Chamado:
    id: int
    id_usuario: int
    id_admin: Optional[int]
    titulo: str
    descricao: str
    status: str  # Esperado: 'aberto', 'em andamento' ou 'resolvido'
    data: date
