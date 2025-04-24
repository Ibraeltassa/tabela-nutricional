from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cache import get_cache, set_cache  # Funções personalizadas para usar o Redis como cache

app = FastAPI(
    title="API de Tabela Nutricional",
    description="Fornece informações nutricionais de ingredientes para integração com a API de receitas",
    version="1.0.0"
)

# Modelo da resposta (estrutura esperada da resposta da API)
class IngredientInfo(BaseModel):
    nome: str
    calorias: float
    proteinas: float
    carboidratos: float
    gorduras: float
    quantidade_base: str

# Dados simulados (mock) - baseados nos ingredientes das receitas do projeto
# Cada entrada representa os valores por 100g ou unidade padrão
fake_nutritional_data = {
    "frango": {
        "nome": "Frango cozido",
        "calorias": 165,
        "proteinas": 31,
        "carboidratos": 0,
        "gorduras": 3.6,
        "quantidade_base": "100g"
    },
    "batata": {
        "nome": "Batata inglesa cozida",
        "calorias": 77,
        "proteinas": 2,
        "carboidratos": 17,
        "gorduras": 0.1,
        "quantidade_base": "100g"
    },
    "tomate": {
        "nome": "Tomate",
        "calorias": 18,
        "proteinas": 0.9,
        "carboidratos": 3.9,
        "gorduras": 0.2,
        "quantidade_base": "100g"
    },
    "arroz": {
        "nome": "Arroz branco cozido",
        "calorias": 130,
        "proteinas": 2.7,
        "carboidratos": 28,
        "gorduras": 0.3,
        "quantidade_base": "100g"
    },
    "cebola": {
        "nome": "Cebola crua",
        "calorias": 40,
        "proteinas": 1.1,
        "carboidratos": 9.3,
        "gorduras": 0.1,
        "quantidade_base": "100g"
    },
    "ovo": {
        "nome": "Ovo de galinha",
        "calorias": 143,
        "proteinas": 13,
        "carboidratos": 1.1,
        "gorduras": 10,
        "quantidade_base": "100g"
    },
    "banana": {
        "nome": "Banana prata",
        "calorias": 89,
        "proteinas": 1.1,
        "carboidratos": 23,
        "gorduras": 0.3,
        "quantidade_base": "100g"
    },
    "azeite": {
        "nome": "Azeite de oliva",
        "calorias": 884,
        "proteinas": 0,
        "carboidratos": 0,
        "gorduras": 100,
        "quantidade_base": "100g"
    },
    "óleo": {
        "nome": "Óleo vegetal",
        "calorias": 884,
        "proteinas": 0,
        "carboidratos": 0,
        "gorduras": 100,
        "quantidade_base": "100g"
    },
    "sal": {
        "nome": "Sal de cozinha",
        "calorias": 0,
        "proteinas": 0,
        "carboidratos": 0,
        "gorduras": 0,
        "quantidade_base": "1g"
    }
    # ➕ Adicione mais ingredientes conforme for integrando com a API de receitas
}

# Endpoint principal: retorna os dados nutricionais de um ingrediente
@app.get("/nutritional-info/{ingredient_id}", response_model=IngredientInfo)
async def get_nutritional_info(ingredient_id: str):
    """
    Busca informações nutricionais de um ingrediente.
    - Primeiro verifica se existe no cache Redis.
    - Caso contrário, busca nos dados simulados e armazena no cache.
    """
    
    # Tenta pegar do cache (caso já tenha sido buscado anteriormente)
    cached_data = get_cache(ingredient_id)
    if cached_data:
        return cached_data

    # Busca local (dados mockados em memória)
    data = fake_nutritional_data.get(ingredient_id.lower())
    if not data:
        # Se não encontrar, retorna erro 404
        raise HTTPException(status_code=404, detail="Ingrediente não encontrado")

    # 💾 Salva no cache para uso futuro
    set_cache(ingredient_id, data)

    # Retorna os dados
    return data
