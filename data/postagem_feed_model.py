from dataclasses import dataclass

@dataclass
class PostagemFeed:
    id_usuario: int 
    id_artigo: int
    data_curtida: str

    #Chave extrangeira em ususario e artigo
    