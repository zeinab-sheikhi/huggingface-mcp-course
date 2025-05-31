from huggingface_hub import Agent

agent = Agent(
    model="Qwen/Qwen2.5-72B-Instruct",
    provider="nebius",
    servers=[
        {
            "command": "npx", 
            "args": [
                "mcp-remote", 
                "http://localhost:7860/gradio_api/mcp/sse",
            ]
        }
    ]
)
