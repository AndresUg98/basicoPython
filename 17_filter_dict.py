matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]


print(matches)
print(len(matches))


newList = list(filter(lambda team : team['home_team_result'] == 'Win', matches))

print(newList)
print(len(newList))


#Para resolver este desafío, tu reto es usar la función filter de 
#Python y una función lambda para filtrar una lista de palabras, 
#retornando una lista solo con las que cumplan con la condición de 
#tener 4 o más letras.

#La función filter_by_length recibirá como entrada una lista 
#con palabras. Finalmente, la función retornará la lista filtrada.

def filter_by_length(words):
   answer = list(filter(lambda word: len(word) >= 4, words))
   return answer

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)