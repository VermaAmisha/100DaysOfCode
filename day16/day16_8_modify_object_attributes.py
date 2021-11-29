
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("S.no.",[1,2,3,4,5])
table.add_column("Pokemon Name", ['Squirtle', 'Pikachu', 'Whismur', 'Slurpuff', 'Mothy'])  
table.add_column("Type", ['Water', 'Electric','Normal','Fairy', 'Flying'])

print(table)
