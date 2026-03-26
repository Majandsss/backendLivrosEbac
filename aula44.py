from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

meus_livroz = {}

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

@app.get("/")
def hello_world():
    return {"Hello": "World!"}

@app.get("/livros")
def get_livros():
    if not meus_livroz:
        return {"message": "Não existe nenhum livro!"}
    else:
        return {"livros": meus_livroz}
    
@app.post("/adiciona")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meus_livroz:
        raise HTTPException(status_code=400, detail="Esse livro já está cadastrado!")
    else:
        meus_livroz[id_livro] = livro.model_dump()
        return {"message": "O livro foi adicionado com sucesso!"}
    
@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, livro: Livro):
    meu_livro = meus_livroz.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        meu_livro[id_livro] = livro.model_dump()
        
        return {"message": "As informações do seu livro foram atualizadas com sucesso!"}

@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in meus_livroz:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        del meus_livroz[id_livro]

        return {"message": "Livro deletado com sucesso!!"}