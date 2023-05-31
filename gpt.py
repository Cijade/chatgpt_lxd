import os
import openai
import requests
import json



defaultkey = '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'

class GPT():

    def __init__(self):
        self.key = defaultkey
    
    def askgpt(self,question):
        
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.key
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                
                {"role": "user", "content": question}],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        response = response.json()
        text = response['choices'][0]['message']['content']
        
        return text

    def getkey(self):
        return defaultkey