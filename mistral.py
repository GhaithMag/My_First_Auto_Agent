from ctransformers import AutoModelForCausalLM

class Mistral:
   
    def __init__(self, model_path, model_file, model_type, gpu_layers, temperature, context_length, max_new_tokens):
        self.cllm = AutoModelForCausalLM.from_pretrained(
            model_path,
            model_file=model_file,
            model_type=model_type,
            gpu_layers=gpu_layers,
            temperature=temperature,
            context_length=context_length,
            max_new_tokens=max_new_tokens
        )
        
        self.agent_answer = ""
        self.summary_prompt = ""
    
    
    def user_prompt(self, context, details):
        user_prompt = f"""<s>[INST] So, these are the pieces of information you have gathered so far: {{
        {self.summary_prompt}
        }}[/INST]
        {context} </s>
        [INST] {details}[/INST]"""
        
        self.agent_answer = self.cllm(user_prompt)
        print(f"Agent Answer after user_prompt: {self.agent_answer}") 
        return self.agent_answer
    
   
    def agent_summary(self):
        print(f"Voici le summary prompt avant l'appel: {self.summary_prompt}") 
        text_agent_prompt = f"""<s> [INST] As an agent trained to filter out crucial information, your mission is to evaluate both the latest prompt response and the last summary you provided. Then, distill only the essential details for future discussions. Below is the most recent prompt answer: [/INST]
        "{self.agent_answer}"
        And here's the previous summary that encapsulates what has been discussed so far: {self.summary_prompt}</s>
        [INST] Ensure your response stays within 1,000 tokens [/INST]"""
        
        self.summary_prompt = self.cllm(text_agent_prompt)
        print(f"Voici le summary prompt après l'appel: {self.summary_prompt}") 
        return self.summary_prompt
