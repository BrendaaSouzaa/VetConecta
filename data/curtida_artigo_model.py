from dataclasses import dataclass

@dataclass
class CurtidaArtigo:
    id_usuario: int
    id_artigo: int
    data_curtida: str  # formato DATE (YYYY-MM-DD)
