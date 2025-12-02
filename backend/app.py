from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import nltk
from nltk.corpus import stopwords
from collections import Counter
import spacy
import re

app = FastAPI(title="AI Text Intelligence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str


nltk.download("punkt")
nltk.download("stopwords")

nlp = spacy.load("en_core_web_sm")

MODEL_ID = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)


def abstractive_summary(text):
    words = text.split()
    word_count = len(words)

    if word_count <= 40:
        max_new = 30
    elif word_count <= 120:
        max_new = 60
    else:
        max_new = 120

    result = summarizer(
        text,
        max_new_tokens=max_new,     
        do_sample=False
    )[0]["summary_text"]

    return result.strip()


def extractive_summary(text, top=3):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    if len(sentences) <= top:
        return text

    words = nltk.word_tokenize(text.lower())
    freq = Counter(w for w in words if w.isalpha() and w not in stopwords.words("english"))

    scored = {
        sent: sum(freq.get(w.lower(), 0) for w in nltk.word_tokenize(sent))
        for sent in sentences
    }

    ranked = sorted(scored, key=scored.get, reverse=True)
    return " ".join(ranked[:top])

def sentiment_analysis(text):
    pos = ["good", "great", "excellent", "amazing", "positive", "love"]
    neg = ["bad", "poor", "negative", "terrible", "hate", "worst"]

    score = sum(1 for w in text.lower().split() if w in pos) - \
            sum(1 for w in text.lower().split() if w in neg)

    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"


def keywords(text):
    words = nltk.word_tokenize(text.lower())
    filtered = [w for w in words if w.isalpha() and w not in stopwords.words("english")]
    freq = Counter(filtered)
    return [k for k, v in freq.most_common(5)]


def entities(text):
    doc = nlp(text)
    output = {}
    for e in doc.ents:
        output.setdefault(e.label_, set()).add(e.text)
    return {k: list(v) for k, v in output.items()}


def topic_detection(text):
    mapping = {
        "health": ["doctor", "hospital", "patient"],
        "finance": ["market", "stock", "investment"],
        "tech": ["api", "server", "database", "code"],
    }
    text_lower = text.lower()
    for topic, keys in mapping.items():
        if any(k in text_lower for k in keys):
            return topic.capitalize()
    return "General"


def detailed_analysis(text):
    return {
        "sentence_count": len(nltk.sent_tokenize(text)),
        "word_count": len(text.split()),
        "char_count": len(text),
        "keywords": keywords(text),
        "entities": entities(text),
        "sentiment": sentiment_analysis(text)
    }

@app.post("/analyze")
def analyze(req: TextRequest):
    text = req.text.strip()
    if not text:
        raise HTTPException(400, "Text cannot be empty")

    extractive = extractive_summary(text)
    abstractive = abstractive_summary(extractive)

    return {
        "summary": abstractive,
        "bullet_summary": ["• " + s for s in nltk.sent_tokenize(abstractive)],
        "keywords": keywords(text),
        "sentiment": sentiment_analysis(text),
        "entities": entities(text),
        "topic": topic_detection(text),
        "detailed": detailed_analysis(text)
    }


@app.get("/health")
def health():
    return {"status": "running"}
