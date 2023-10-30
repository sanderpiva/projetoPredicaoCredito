#import requests

#url = 'http://localhost:5000/api'
#r = requests.post(url,json={'person_age':56, 'person_income':50000, 'person_emp_length':4, 'loan_amnt':15000})

#print(r.json())

import requests

url = 'http://localhost:5000/api'
data = {'person_age': 56, 'person_income': 50000, 'person_emp_length': 4, 'loan_amnt': 15000}

response = requests.post(url, json=data)

# Verifique se a resposta foi bem-sucedida (código de status 200)
if response.status_code == 200:
    try:
        # Tente decodificar o JSON
        result = response.json()
        print(result)
    except requests.exceptions.JSONDecodeError as e:
        print("Erro ao decodificar JSON:", e)
else:
    print("Erro na solicitação. Código de status:", response.status_code)
