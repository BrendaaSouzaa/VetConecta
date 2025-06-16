from dataclasses import dataclass

@dataclass
class PostagemArtigo:
    id: int
    id_veterinario: int
    titulo: str
    conteudo: str
    categoria_id: int
    data_publicacao: str
    visualizacoes: int
    # Chave estrangeira em veterinario e categoria_artigo