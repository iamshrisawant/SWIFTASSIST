from core.model import roadside_chat

print("🛠️ Welcome to SWIFTASSIST Roadside Chatbot!")
print("💬 Type your issue or question (type 'exit' to quit):")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        break
    response = roadside_chat(user_input)
    print("Assistant:", response)
