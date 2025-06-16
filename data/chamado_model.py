from dataclasses import dataclass

@dataclass
class Chamado:
    id: int
    id_usuario: int
    titulo: str
    descricao: str
    status: str  # valores possíveis: 'aberto', 'em andamento', 'resolvido'
    data: str  # formato DATE
