# 📝 AI Text Summarizer

A Python-Flask app using Hugging Face Transformers to instantly summarize text. This tool provides a simple web UI and a JSON API, aiming to reduce reading time by 60% by distilling long articles into concise summaries.

---

## ✨ Features

* **Simple Web Interface:** A clean, easy-to-use UI to paste text and get a summary.
* **JSON API:** A `/summarize` endpoint for programmatic use in other applications.
* **Efficient Model:** Built on `sshleifer/distilbart-cnn-12-6` for a good balance of speed and accuracy.

## 🛠️ Tech Stack

* **Backend:** Flask
* **ML Model:** Hugging Face Transformers (`pipeline`)
* **Frontend:** HTML, CSS, JavaScript (with `fetch` API)
* **Language:** Python 3

