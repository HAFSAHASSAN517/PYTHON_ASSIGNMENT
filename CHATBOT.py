import os
import json
from google import genai

def ai_chatbot():
    # 1. Initialize client inside the function
    client = genai.Client()
    
    chat_history = []
    print("=" * 50)
    print("CLI Chatbot, enter 'exit' or 'quit' to exit the chat")
    print("=" * 50)
    
    while True:
        user_input = input("\n you :").strip()
        if not user_input:
            continue
            
        if user_input.lower() in ["exit", "quit"]:
            print("exiting the chatbot ...")
            break
            
        chat_history.append({"role": "user", "content": user_input})
        
        try:
            # client is accessible here because it is in the same function scope
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents=user_input
            ) 
            bot_reply = response.text
            print(f"bot: {bot_reply}")
            
            # Save the bot's response to history as well
            chat_history.append({"role": "model", "content": bot_reply})
            
        except Exception as e:
            print(f"Error occurred while processing the request: {str(e)}")
            break
            
    # File saving logic inside the function body
    output_file = "chat_history.json"
    with open(output_file, "w") as f:
        json.dump(chat_history, f, indent=4)   
        
    if os.path.exists(output_file):
        print(f"Chat history saved to {output_file}")  

if __name__ == "__main__":
     ai_chatbot()