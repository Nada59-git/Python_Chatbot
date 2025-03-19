# Python Chatbot using Google Gemini API

## Description
This project is a simple chatbot powered by **Google Gemini AI**. It allows users to engage in a conversation with an AI model using the Google Generative AI API. The chatbot continuously interacts with the user and provides responses based on the input.

## Features
- ✅ Uses **Google Gemini AI (gemini-1.5-pro)** for natural conversations.
- ✅ Supports continuous chat in a loop until the user exits.
- ✅ Simple and easy-to-use interface.
- ✅ Implements API authentication for secure communication.

## Limitations
- ❌ Requires **internet connection** to interact with the Google Gemini API.
- ❌ **Limited API quota** (depends on your Google AI API plan).
- ❌ Can only generate responses based on text input (no image/audio support).
- ❌ No memory retention – the chatbot does not remember past interactions once restarted.

## Setup Instructions
### 1. Install Dependencies
Ensure you have Python installed and install the required package:
```sh
pip install google-generativeai
```

### 2. Get a Google API Key
- Visit [Google AI Studio](https://ai.google.dev/) to get an API key.
- Replace `API_KEY` in the script with your actual API key.

### 3. Run the Chatbot
```sh
python chatbot.py
```

## Example Conversation
```
You: Hello!
Chatbot: Hi there! How can I assist you today?

You: Tell me a joke.
Chatbot: Why did the computer go to therapy? Because it had too many bugs!

You: Bye
Chatbot: Goodbye!
```


