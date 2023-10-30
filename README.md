<!DOCTYPE html>

<h1>🤖 Autonomous Agent for Mistral-LLM Interaction 🚀</h1>

<p>Welcome to this inventive project! The main goal here is to introduce individuals to the realm of autonomous agents. To achieve this, we're establishing a setup akin to ChatGPT, powered by the Mistral Language Model (LLM), facilitated by the use of Ctransformers. Through a user-friendly web interface, users can input a prompt, engage with the model, and receive a response from it—this is the visible part of the interaction. Yet, behind the curtain, an autonomous agent diligently operates. This agent archives each prompt and response, fostering an environment where users are essentially conversing with a robot that holds a semblance of memory. Ctransformers play a crucial role here, as they enable the running of LLM models on a CPU, although in this setup, a GPU is utilized for better performance. This arrangement not only promotes a more engaging and dynamic dialogue but also unveils the fascinating capabilities and potential of autonomous agents in enriching user experiences with language models. 🤖</p>

<h2>🧠 Understanding Autonomous Agents</h2>

<img src="illustration.png" alt="Illustration of Autonomous Agent" style="width:100%; max-width:600px; display:block; margin:auto;">

<p>Autonomous Agents are self-driven entities that can perceive their environment, make decisions, and take actions without human intervention. In this project, the agent acts as an intermediary between the user and the Mistral LLM, ensuring a seamless interaction while keeping track of important information. 🕵️</p>

<h2>💡 Project Significance</h2>

<p>This project serves as a great starting point for anyone interested in exploring the world of autonomous agents and language models. It's structured in a way that allows easy modifications, be it tweaking the prompts or enhancing the code. Your contributions are highly encouraged! 🛠️</p>

<h2>🔎 About Mistral LLM</h2>


<p>Mistral is a Large Language Model developed by Mistral AI, with 7 billion parameters. Despite having fewer parameters, Mistral 7B v0.1 performs better than Llama 2 13B in various benchmarks. It's designed with unique features like Sliding Window Attention. The model is free to use, and its weights are available for download. Mistral can operate on both GPU and CPU, thanks to Ctransformers</p>

<h2>🚀 Getting Started</h2>

<pre>
📂 Project Directory Structure:
    
    project-root/
    ├── app.py
    ├── templates/
    │   └── index.html
    ├── static/
    │   └── styles.css
    └── mistral.py
</pre>


<p>Before you begin, ensure you have the Mistral model downloaded. You can download it from <a href="https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/tree/main" target="_blank">here</a>. Although this project is set up with Mistral, feel free to explore with other models as per your requirements.</p>

<p>Follow these steps to launch the project:</p>
<ol>
    <li><strong>Clone the Repository:</strong> Get the project on your local machine using the command <code>git clone https://github.com/GhaithMag/My_First_Auto_Agent.git</code>.</li>
    <li><strong>Navigate to the Project Root:</strong> Move to the project's root directory.</li>
    <li><strong>Install Dependencies:</strong> Install all the necessary dependencies to ensure the project runs smoothly.</li>
    <li><strong>Launch the Project:</strong> Run the command <code>python app.py</code> to launch the project. Once launched, access the web interface by navigating to <code>http://127.0.0.1:5000.</code></li>
    <li><strong>Docker Option (Optional):</strong> If you have Docker installed, it's an option to build and run the project using Docker commands. However, the recommended way to get started is by using Flask with the above <code>python app.py</code> command.</li>
</ol>
</body>
</html>
