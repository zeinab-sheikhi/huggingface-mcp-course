import gradio as gr

from mcp.client.stdio import StdioServerParameters
from smolagents import InferenceClientModel, CodeAgent, ToolCollection
from smolagents.mcp_client import MCPClient

if __name__ == "__main__":
    try:
        mcp_client = MCPClient(
            {
                "url": "http://localhost:7860/gradio_api/mcp/sse",
                "transport": "sse",
            },
        )

        tools = mcp_client.get_tools()

        # create a simple agent to use the tools to answer questions
        model = InferenceClientModel()
        agent = CodeAgent(model=model, tools=[*tools])

        demo = gr.ChatInterface(
            fn=lambda message, history: str(agent.run(message)),
            type="messages",
            examples=["Prime Factorization of 68"],
            title="Agent with MCP tools",
            description="This is a simple agent that uses MCP tools to answer questions.",
        )

        demo.launch()
    finally:
        # MCP Client is a long-lived object that needs to be closed when the program exits.
        mcp_client.disconnect()
