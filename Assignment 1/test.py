dict = {'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)], 'Craiova': [('Dobreta', 120), ('RimnicuVilcea', 146), ('Pitesti', 138)], 'Eforie': [('Hirsova', 86)], 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)], 'Giurgiu': [('Bucharest', 90)], 'Mehadia': [('Lugoj', 70), ('Dobreta', 75)], 'Neamt': [('lasi', 87)], 'Sibiu': [('Oradea', 151), ('Arad', 140), ('RimnicuVilcea', 80), ('Fagaras', 99)], 'Oradea': [('Zerind', 71), ('Sibiu', 151)], 'Pitesti': [('RimnicuVilcea', 97), ('Craiova', 138), ('Bucharest', 101)], 'RimnicuVilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)], 'Dobreta': [('Mehadia', 75), ('Craiova', 120)], 'Hirsova': [('Urziceni', 98), ('Eforie', 86)], 'lasi': [('Vaslui', 92), ('Neamt', 87)], 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)], 'Timisoara': [('Arad', 118), ('Lugoj', 111)], 'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)], 'Vaslui': [('Urziceni', 142), ('lasi', 92)], 'Zerind': [('Oradea', 71), ('Arad', 75)], 'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)]}

print(dict.keys())
if "Neamt" in dict.keys():
  print("yes")
else:
  print("no")