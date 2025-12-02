# Smart Text Analyzer

A web-based AI-powered text analysis tool that provides multiple insights from any text. The application supports **summarization, bullet summaries, keyword extraction, sentiment analysis, named entity recognition, topic detection, and detailed analysis**.

This project is built using **FastAPI** for the backend, **Hugging Face Transformers** for summarization, **NLTK & spaCy** for NLP processing, and a **responsive HTML/CSS/JS frontend**.

---

## 🔹 Features

- **Summary:** Generates a concise summary of your text.
- **Bullet Summary:** Converts the summary into bullet points.
- **Keywords:** Extracts the top keywords from the text.
- **Sentiment:** Determines if the text sentiment is positive, neutral, or negative.
- **Named Entities:** Identifies names, locations, organizations, and other entities.
- **Topic Detection:** Detects the main topic of the text.
- **Detailed Analysis:** Provides sentence count, word count, character count, keywords, entities, and sentiment.
- **Responsive UI:** Works seamlessly across devices with decorative button boxes and loading indicators.

---

## 🔹 Demo

Live demo: [Smart Text Analyzer](https://github.com/itsmohitnamdeo/Smart-Text-Analyzer)

---

## 🔹 Installation & Setup

### Prerequisites

- Python 3.10+
- pip
- Virtual environment (recommended)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/itsmohitnamdeo/Smart-Text-Analyzer.git
cd Smart-Text-Analyzer/backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the FastAPI backend:
```bash
uvicorn app:app --reload
```

5. Open the frontend:

Open `index.html` in a browser (or use Live Server in VS Code) and enter text for analysis.

---

## 🔹 API Endpoints

- **POST /analyze**  
  Request Body:
  ```json
  { "text": "Your text here" }
  ```
  Response:
  ```json
  {
      "summary": "...",
      "bullet_summary": [...],
      "keywords": [...],
      "sentiment": "...",
      "entities": {...},
      "topic": "...",
      "detailed": {...}
  }
  ```

- **GET /health**  
  Health check endpoint. Returns:
  ```json
  { "status": "running" }
  ```

---

## 🔹 Technologies Used

- **Backend:** FastAPI, Python, Hugging Face Transformers, NLTK, spaCy
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** GitHub Pages for frontend (optional)

---


## Contact

If you have any questions, suggestions, or need assistance related to the Smart Text Analyzer, feel free to reach out to Me.

- MailId - namdeomohit198@gmail.com
- Mob No. - 9131552292
- Portfolio : https://itsmohitnamdeo.github.io
- Linkedin : https://www.linkedin.com/in/mohit-namdeo