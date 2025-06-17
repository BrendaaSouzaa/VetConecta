from dataclasses import dataclass
from data.categoria_artigo_model import CategoriaArtigo
from data.veterinario_model import Veterinario

@dataclass
class PostagemArtigo:
    id: int
    id_veterinario: Veterinario[id:int]
    titulo: str
    conteudo: str
    categoria_artigo: CategoriaArtigo[id:int]
    data_publicacao: str
    visualizacoes: int