from dataclasses import dataclass

from data.postagem_artigo_model import PostagemArtigo
from data.usuario_model import Usuario

@dataclass
class Comentario:
    id: int
    id_usuario: Usuario
    id_artigo: PostagemArtigo
    texto: str
    data_comentario: str
    data_moderacao: str | None