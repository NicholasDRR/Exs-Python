import copy

dictionary = {
    'nome': 'Nicholas',
    'sobrenome': 'Ribeiro',
    'list': [0, 1, 2],
 }
#print(len(dictionary))
#print(list(dictionary.keys()))
#print(list(dictionary.items()))

#for key, value in dictionary.items():
#   print(key, value)

dictionary.setdefault('idade', 18)
#print(dictionary['idade'])

dictionary2 = copy.deepcopy(dictionary)
dictionary2['list'][0]= 1

#print(dictionary.get('cidade', 'Cidade inexistente'))
#print(dictionary2)
#print(dictionary)

ultimoitem = dictionary.popitem()
sobrenome = dictionary.pop('sobrenome')

dictionary.update(
   {
   'nome': 'nomenovo',
   'idade': 18,
   
}
)

dictionary.update(nome='novonome', idade=10)


print(dictionary)