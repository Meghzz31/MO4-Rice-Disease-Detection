import requests

def template_constants(request):
    # Define your global constants here
    return {
        'APP_NAME': 'Rice Leaf Disease Detection',
    }


def chat_with_rasa(request,user_message):   
    rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
    response = requests.post(rasa_url, json={"sender": request.session['userId'],"message": user_message})
    rasa_data = response.json()
    return rasa_data