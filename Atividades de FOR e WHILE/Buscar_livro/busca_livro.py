livros= ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O hobbit", "Cem Anos de Solidão"]

for livro in livros:
    if livro == "O hobbit":
        print(f'Livro encontrado: {livro}')
        break

livros=[
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O hobbit", "estoque": 2},
    {"nome": "Cem Anos de Solidão", "estoque": 0}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f'Livro disponível: {livro["nome"]} - Estoque: {livro["estoque"]}')