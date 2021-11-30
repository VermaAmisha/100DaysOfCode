
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("S.no.",[1,2,3,4,5])
table.add_column("Friends", ['Shashwat', 'Amisha', 'Deepal', 'Sonam', 'Ankita'])  
table.add_column("Birthdays", ['12th March', '26th December','19th November','10th August', '15th January'])

print(table)
