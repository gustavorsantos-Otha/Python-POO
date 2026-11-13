from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Produto", style="red")
tabela.add_column("Preço", style="Blue")

tabela.add_row("Lápis", "1,50")
tabela.add_row("Borracha", "2,00")

print(tabela)