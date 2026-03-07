from rich import print
from rich.table import Table

tabela1 = Table(title="Tabela de preços")

tabela1.add_column('Nome')
tabela1.add_column('Preço')
tabela1.add_row('Lápis','U$: 1,20 ')

print(tabela1)