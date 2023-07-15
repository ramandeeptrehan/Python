import requests
import json

def get_stackoverflow_questions():
    questions = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    return questions

response = get_stackoverflow_questions()
print(response) #just gives the response code
data = response.json() #exactly what we see in POSTMAN
#print(data)

#Fetch only items from response data
items_data = data['items'] 
print(items_data)

#Iterate over items and print title of each question
for item_data in items_data:
    print(item_data['title'])
    print(item_data['link'])