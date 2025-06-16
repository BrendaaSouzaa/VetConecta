from dataclasses import dataclass

from data.categoria_artigo_model import CategoriaArtigo
from data.veterinario_model import Veterinario

@dataclass
class PostagemArtigo:
    id: int
    id_veterinario: Veterinario[id:int]
    titulo: str
    conteudo: str
    categoria_id: CategoriaArtigo[id:int]
    data_publicacao: str
    visualizacoes: int
    # Chave estrangeira em veterinario e categoria_artigo
    # Toda chave extrangeira deve ser importado sua tabela!!!