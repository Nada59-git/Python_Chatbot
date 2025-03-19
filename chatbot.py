import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)# Replace with your actual API key
# Initialize the Gemini Pro model
model = genai.GenerativeModel("gemini-1.5-pro")

# Start a chat session
chat = model.start_chat()

# Chat loop
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break
    response = chat.send_message(message)
    print('Chatbot:', response.text)  # Ensure response.text is valid