import requests
import json
import gradio as gr

# https://github.com/ollama/ollama

url="http://localhost:11434/api/generate" #api

headers={

    'Content-Type':'application/json' #api documentation for messages
}

history=[] #save prev info
def generate_response(prompt):
    history.append(prompt)
    final_prompt= "\n".join(history) #append history
    data= {
        "model": "Jarvis",
        "prompt": final_prompt,
        "stream": False    #remove unnecessary values
    }
    response = requests.post(url,headers=headers, data=json.dumps(data))
    if response.status_code==200: #successful
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)


# Front-end
interface=gr.Interface(
    title="Programming Code Assistant App",
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch(share=True)