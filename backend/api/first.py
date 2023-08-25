from hugchat.login import Login
from hugchat import hugchat

# login hugging chat
sign = Login('picsart.project.tei@gmail.com', 'Story teller123')
cookies = sign.login()

# save cookies
sign.saveCookiesToDir('cookies/')

# create a chatbot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
print(chatbot.chat('write a story about a guy who hated math then met Gauss and fell in love with math in about 300-400 words. Separate the story in paragraphs.',
                   return_full_text=True))