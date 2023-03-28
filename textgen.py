import openai
import os

def textgeneration(userprompt):
    if len(userprompt) == 0: # Ensure a prompt was entered
        exit("A prompt was not entered.")
    userprompt = "Write an ending to this Shakespeare play: " + userprompt
    if len(userprompt) > 1024: # Ensure input length is less than the maximum accepted by model
        userprompt = userprompt[0:499]
    
    apikeyfile = open("chatgptapi.txt", "r")
    apikey = apikeyfile.readline()
    openai.api_key = apikey

    #Generate response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=userprompt,
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response