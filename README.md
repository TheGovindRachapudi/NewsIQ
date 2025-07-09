# 📰 NewsIQ

This is a Gradio-powered web app that analyzes any news article URL and extracts:

- 🧠 Title  
- ✍️ Authors  
- 📅 Publication Date  
- 📝 Summary  
- 💬 Sentiment (using TextBlob)  
- 🏷️ Top 10 Keywords

## 🌐 Live Demo 
https://huggingface.co/spaces/WLCODING/news-analyzer

## 🚀 How to Run Locally

```bash
git clone https://github.com/TheGovindRachapudi/ai-news-analyzer.git
cd news-analyzer-app
pip install -r requirements.txt
python -m textblob.download_corpora
python app.py
