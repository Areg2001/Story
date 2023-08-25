from hugchat import hugchat
from rest_framework.response import Response


def construct_prompt(text):
    return "\n\n write a story in about 300-500 words and divide the story into paragraphs with newline. " + text

def start_chat(user_input):
    chatbot = hugchat.ChatBot(cookie_path='/Users/aregmelqonyan/Desktop/Story/backend/api/cookies/picsart.project.tei@gmail.com.json')

    conversation_id = chatbot.new_conversation()
    chatbot.change_conversation(conversation_id)

    try:
        prompt2 = chatbot.chat(construct_prompt(user_input))
    except Exception as e:
        prompt2 = 'Something went wrong... wait a little bit and try again.'
    return prompt2