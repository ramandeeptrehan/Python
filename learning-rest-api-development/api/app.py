import requests
import json

def get_stackoverflow_questions():
    questions = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    return questions

response = get_stackoverflow_questions()
print(response) #just gives the response code
print(response.json()) #exactly what we see in POSTMAN