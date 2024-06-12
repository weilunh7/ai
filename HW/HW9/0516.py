import os
from groq import Groq

client = Groq(
    api_key="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"
)

try:
    print('Try to remove old output...')
    os.remove('./chat.md')
    print('Old output file removed.')
except FileNotFoundError:
    print('file: chat.md not found, create one.')

question = "Hello!"
messages = []

while question.lower() != "exit":
    messages.append({
        "role": "user",
        "content": question + "翻譯成繁體中文",
    })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content
    messages.append({
        "role": "assistant",
        "content": response,
    })

    with open('chat.md', 'a', encoding='UTF-8') as f:
        f.write("Prompt: \n" +
                question + "\n\n" +
                "Response: \n" +
                response + "\n\n")

    print("\n" + response + "\n")
    question = input("Prompt (exit to exit): ")
