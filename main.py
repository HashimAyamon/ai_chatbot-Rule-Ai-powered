import google.generativeai as genai


AI_KEY = "your Key"
genai.configure(api_key=AI_KEY)

# Create model only once
model = genai.GenerativeModel("gemini-1.5-flash")


def chatbot(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("🤖 AI Chatbot (type 'exit' to stop)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break
        
        response = chatbot(user_input)
        print("Bot:", response)
