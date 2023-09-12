import langchain
from langchain.chat_models import ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader
import os
from dotenv import dotenv_values
from langchain.llms import OpenAI


env_vars = dotenv_values('.env')

# loader = TextLoader('profile.txt')

os.environ["OPENAI_API_KEY"] = env_vars["OPENAI_KEY"]

def generate_response(query):
    with open("chat.txt", "a") as f:
        # append the query by user
        string_save_data = "user: "
        string_save_data += str(query)
        # add new line
        string_save_data += "\n"
        f.write(string_save_data)

    chatgpt = ChatOpenAI(model_name='gpt-3.5-turbo')
    gpt3 = OpenAI(model_name='text-davinci-003')

    loader = TextLoader('chat.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])

    response = index.query(query)
    return response    


# Start a conversation
while True:
    # Get the user's input
    user_input = input("You: ")
    
    # Generate a response
    response = generate_response(user_input)
    with open("chat.txt", "a") as f:
        # append the query by user
        string_save_data = "bot: "
        string_save_data += str(response)
        # add new line
        string_save_data += "\n"
        f.write(string_save_data)

    # Print the response
    print("Bot: ", response)
