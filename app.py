import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}

history=[]


## for previous messages

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model":"Infilev",
        "prompt":final_prompt,
        "stream":False  
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)


interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch()



# First you need to install the Ollama by    "ollama run codellama"


# (Optional: to make sure that model file run correctly)
# After creation of the modelfile

# go to cmd and go to the path where the modelfile is loacted and 

# run    "ollama create Infilev -f modelfile"

# modelfile is created so that the model can behave in a particular way
