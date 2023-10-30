from flask import Flask, request, jsonify, render_template
from mistral import Mistral  # Replace "mistral_interface" with your file's name
import asyncio


model_path = "your path to mistral-7b-instruct-v0.1.Q6_K.gguf"
model_path ='your path to mistral-7b-instruct-v0.1.Q6_K.gguf'
model_file = "mistral-7b-instruct-v0.1.Q6_K.gguf"
model_type = "mistral"
gpu_layers = 10000
temperature = 0
context_length = 6000
max_new_tokens = 6000

mistral = Mistral(model_path, model_file, model_type, gpu_layers, temperature, context_length, max_new_tokens)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response/', methods=['POST'])
async def get_response():
    data = request.get_json()
    context = data['context']
    detail = data['detail']

    if len(context) + len(detail) > 4000:
        return jsonify({"error": "Token limit exceeded"})

  
    user_response = await asyncio.to_thread(lambda: mistral.user_prompt(context, detail))
    mistral.agent_summary()
    
    return jsonify({"response": user_response})

if __name__ == '__main__':
    app.run(debug=True)
