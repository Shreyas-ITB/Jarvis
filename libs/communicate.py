import requests
from dotenv import load_dotenv
import os
from freeGPT import gpt3

load_dotenv(r"..\.env")

batch_size = os.getenv("BATCH_SIZE")
temperature = os.getenv("TEMPERATURE")
top_k = os.getenv("TOP_K")
top_p = os.getenv("TOP_P")
n_keep = os.getenv("N_KEEP")
n_predict = os.getenv("N_PREDICT")
stop = os.getenv("STOP")
threads = os.getenv("THREADS")
as_loop = bool(os.getenv("AS_LOOP"))
interactive = bool(os.getenv("INTERACTIVE"))

def chatwithgpt(prompt):
    resp = gpt3.Completion.create(prompt=prompt)
    return str(resp['text'])

def post_prompt(instruction):
    prompt = """Jarvis, an intelligent AI assistant, the epitome of refinement and courtesy in the AI world. 
            As he engages in conversation, his responses are graced with a gracious 'Sir,' 
            adding a touch of chivalry to his articulate and insightful answers. He answers all the
            conversations and questions very easily, providing near to accurate or accurate answers.
         """
    try:
        prompt += f"\n\n### Instruction:\n\n${instruction}\n\n### Response:\n\n"
        url = f"http://127.0.0.1:8080/completion"
        data = {
            "prompt": prompt,
            "batch_size": batch_size,
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p,
            "n_keep": n_keep,
            "n_predict": n_predict,
            "stop": [stop],
            "exclude": [],
            "threads": threads,
            "as_loop": as_loop,
            "interactive": interactive
        }
        response = requests.post(url, json=data)
        
        message = ""
        while True:
            response = requests.get(f"http://127.0.0.1:8080/next-token")
            message += response.text

            if stop in response:
                print("completed")
                prompt += message
                break
        return message
    except Exception as e:
        print(f"An Error Occured! {e}")