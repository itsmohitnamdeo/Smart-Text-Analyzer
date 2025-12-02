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

## Images 

- Summary
<img width="1362" height="619" alt="summary" src="https://github.com/user-attachments/assets/80086232-d391-45ee-807f-0a2aedb8e06f" />
- Keywords
<img width="971" height="481" alt="keywords" src="https://github.com/user-attachments/assets/83817d6e-ad73-4e9d-93da-550668ee2e3b" />
- DetailedAnalysis
<img width="998" height="584" alt="detailed" src="https://github.com/user-attachments/assets/9fcdda03-1494-423a-9c71-103a2c559f86" />
- Bullet Summary
<img width="973" height="534" alt="bullet_summary" src="https://github.com/user-attachments/assets/d8acf725-cc1b-4a0b-8e89-b87200d8cad0" />
- Sentiment
<img width="945" height="482" alt="sentiment" src="https://github.com/user-attachments/assets/753aed44-4092-4b9c-82d4-c990e06cc318" />
- Named Entities
<img width="1004" height="624" alt="named_entities" src="https://github.com/user-attachments/assets/17aa0296-7768-49bc-8500-97117e86b5a9" />


## Contact

If you have any questions, suggestions, or need assistance related to the Smart Text Analyzer, feel free to reach out to Me.

- MailId - namdeomohit198@gmail.com
- Mob No. - 9131552292
- Portfolio : https://itsmohitnamdeo.github.io
- Linkedin : https://www.linkedin.com/in/mohit-namdeo
