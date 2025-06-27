import gradio as gr
from newspaper import Article
from textblob import TextBlob

# ----------------- Core Logic -----------------
def analyze_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        blob = TextBlob(article.text)
        polarity = blob.sentiment.polarity
        sentiment = (
            "🟢 Positive" if polarity > 0
            else "🔴 Negative" if polarity < 0
            else "⚪ Neutral"
        )

        keywords = ", ".join(article.keywords[:10])  # top 10 keywords

        return (
            article.title or "N/A",
            ", ".join(article.authors) or "N/A",
            str(article.publish_date) or "N/A",
            article.summary or "N/A",
            f"{sentiment} (Polarity: {polarity:.2f})",
            keywords or "N/A"
        )
    except Exception as e:
        return ("Error", "Error", "Error", "Error", f"❌ {str(e)}", "Error")

# ----------------- Custom CSS -----------------
custom_css = """
.gradio-container {
    background-color: #6699CC !important;
    padding: 40px;
    font-family: 'Inter', 'Segoe UI', sans-serif;
    min-height: 100vh;
}

.gradio-container .wrap {
    background-color: #ffffff;
    max-width: 900px;
    margin: auto;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}

h1, h2, h3, .title, .description {
    color: #222222 !important;
    text-align: center;
    margin-bottom: 25px;
    font-weight: 600;
}

textarea, input[type=text] {
    background-color: #fefefe !important;
    color: #000000 !important;
    border: 1px solid #ccc !important;
    border-radius: 10px !important;
    padding: 12px;
    font-size: 15px;
    transition: box-shadow 0.3s ease;
}

textarea:focus, input:focus {
    outline: none;
    box-shadow: 0 0 10px #336699;
}

.gr-button {
    background: linear-gradient(135deg, #336699, #4477aa) !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    padding: 12px 28px !important;
    font-size: 16px !important;
    margin-top: 20px;
    transition: background 0.3s ease;
}

.gr-button:hover {
    background: linear-gradient(135deg, #4477aa, #5588cc) !important;
}
"""

# ----------------- Gradio App -----------------
iface = gr.Interface(
    fn=analyze_article,
    inputs=gr.Textbox(
        label="🔗 Paste News Article URL",
        placeholder="https://example.com/news/article",
        lines=1
    ),
    outputs=[
        gr.Textbox(label="🧠 Title", lines=2),
        gr.Textbox(label="✍️ Authors", lines=1),
        gr.Textbox(label="📅 Publication Date", lines=1),
        gr.Textbox(label="📝 Summary", lines=6),
        gr.Textbox(label="💬 Sentiment", lines=1),
        gr.Textbox(label="🏷️ Keywords", lines=2),
    ],
    title="📰 AI-Powered News Article Analyzer",
    description="Enter a news article URL to extract title, authors, date, summary, sentiment, and keywords.",
    theme="default",
    css=custom_css
)

iface.launch()
