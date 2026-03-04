# AI Chat Assitant Rule Based ChatBot

import datetime
import time

name = input("Welcome, Enter your name : ")

presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning ", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon ", name)
elif 17 <= presentHour <= 22:
    print("Good Evening ", name)
else:
    print("Good Night ", name)

print("Namaste! Welcome to Your Cool ChatBot")

print("You can ask me basic question, Type 'bye' to exit from bot")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "hello": "Hi, Welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "Who are you": "I am a smart AI Chatbot",
    "motivate me": "Be a priority, Not an option!",
    "happy": "Great to hear that",
}

# Method/Function to get response pf Chatbot

def getResponseOfBot(userQuestion) :
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    
    return "Sorry, I am not able to tell that. I am learn that soon"

# Take use input

while True:
    userInput = input("Please ask your question :")

    reply = getResponseOfBot(userInput)

    print("Bot Response :", reply)

    if "bye" in userInput.lower():
        break
