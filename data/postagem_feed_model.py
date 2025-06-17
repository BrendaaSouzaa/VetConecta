from dataclasses import dataclass
from typing import Optional

@dataclass
class PostagemFeed:
    id_postagem_feed: int
    id_tutor: int
    imagem: Optional[str]
    descricao: str
    data_postagem: str

    