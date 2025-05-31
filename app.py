import gradio as gr
from textblob import TextBlob


def sentiment_analysis(text: str) -> dict:
    """
    Analyze the sentiment of a given text.

    Args:
        text (str): The text to analyze
    
    Returns:
        dict: A dictionary containing polarity, subjectivity, and sentiment.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment

    return {
        "ploarity": round(sentiment.polarity, 2),
        "subjectivity": round(sentiment.subjectivity, 2),
        "assessment": "positiive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }


# create the gradio interface
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text to analyze..."),
    outputs=gr.JSON(),
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of text using TextBlob",
)

# Launch the interface and MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
