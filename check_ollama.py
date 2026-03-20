from smolagents import LiteLLMModel, CodeAgent

# 1. Setup the connection to your local Ollama "brain"
model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",  
    api_base="http://127.0.0.1:11434",  # This is your local server address
    num_ctx=8192,
)

# 2. Initialize the agent
agent = CodeAgent(tools=[], model=model)

# 3. Ask it a question to see if it responds
print("--- Asking the local model a question ---")
agent.run("What is 2 + 2? Answer in one word.")