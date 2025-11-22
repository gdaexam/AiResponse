import g4f

MESSAGES = []
def get_response(query):
    MESSAGES.append({"role": "user", "content": query})
    response = g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=MESSAGES)
    MESSAGES.append({"role": "assistant", "content": response})
    return response

while True:
    prompt = input("Введите запрос в одну строку: ")
    print(f"Ответ: {get_response(prompt)}")
    print()
