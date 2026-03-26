from fastapi import FastAPI, HTTPException

app = FastAPI()

meus_livroz = {}

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
def post_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    if id_livro in meus_livroz:
        raise HTTPException(status_code=400, detail="Esse livro já está cadastrado!")
    else:
        meus_livroz[id_livro] = {"nome_livro": nome_livro, "autor_livro": autor_livro, "ano_livro": ano_livro}
        return {"message": "O livro foi adicionado com sucesso!"}
    
@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    meu_livro = meus_livroz.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        if nome_livro:
            meu_livro["nome_livro"] = nome_livro
        if autor_livro:
            meu_livro["autor_livro"] = autor_livro
        if ano_livro:
            meu_livro["ano_livro"] = ano_livro
        
        return {"message": "As informações do seu livro foram atualizadas com sucesso!"}

@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in meus_livroz:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        del meus_livroz[id_livro]

        return {"message": "Livro deletado com sucesso!!"}