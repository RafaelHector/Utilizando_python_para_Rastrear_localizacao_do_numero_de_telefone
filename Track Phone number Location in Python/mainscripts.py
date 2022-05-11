import phonenumbers
from test import number #Importando do 2° arquivo

from phonenumbers import geocoder #função de phonenumbers
ch_nmber = phonenumbers.parse(number, "CH") #Variável, parse é o número  #"C" Country, "H" History
print(geocoder.description_for_number(ch_nmber, "BR")) #Descrição para o número, () estará o argumento Input e o país +55

from phonenumbers import carrier #carrier tem a função como a de um servidor 
service_nmber = phonenumbers.parse(number, "RO") #variável com 2 argumentos
print(carrier.name_for_number(service_nmber, "BR")) #chamando "carrier"
#Não sei se seria a limitação da biblioteca, mas por algum motivo o país não aparaceu em conjunto do estado... devo pesquisar mais afundo.