import ollama

stream = ollama.chat(
    model='mistral', 
    messages=[{'role': 'user', 'content': 'Who is the richest person in histroy?'}], 
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)