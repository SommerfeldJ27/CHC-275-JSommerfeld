from openai import OpenAI

client = OpenAI(api_key="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")

print("AI Bot: Hello! Type 'quit' to exit.")

conversation = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("AI Bot: Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )

    bot_reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": bot_reply})

    print("AI Bot:", bot_reply)