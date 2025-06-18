from dataclasses import dataclass
from datetime import date

@dataclass
class CurtidaFeed:
    id_usuario: int
    id_postagem_feed: int
    data_curtida: date
