from dataclasses import dataclass
from datetime import date

@dataclass
class CurtidaFeed:
    id_usuario: int
    id_feed: int
    data_curtida: date
