from dataclasses import dataclass

@dataclass
class Administrador:
    id_usuario: int
    nivel_acesso: int  # padrão: 1
