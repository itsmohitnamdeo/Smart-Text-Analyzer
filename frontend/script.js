const API_URL = "http://127.0.0.1:8000/analyze";

function showLoader() {
    document.getElementById("loading").classList.remove("hidden");
}

function hideLoader() {
    document.getElementById("loading").classList.add("hidden");
}

function setResult(text) {
    document.getElementById("result").textContent = text;
}

async function analyze(type) {
    const text = document.getElementById("inputText").value.trim();
    if (!text) return alert("Please enter text!");

    setResult("");
    showLoader();

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        const data = await response.json();
        hideLoader();

        let output = "";

        switch (type) {
            case "summary":
                output = data.summary;
                break;

            case "bullet":
                output = data.bullet_summary.join("\n");
                break;

            case "keywords":
                output = data.keywords.join(", ");
                break;

            case "sentiment":
                output = "Sentiment: " + data.sentiment;
                break;

            case "ner":
                output = JSON.stringify(data.entities, null, 2);
                break;

            case "topic":
                output = "Topic: " + data.topic;
                break;

            case "detailed":
                output = JSON.stringify(data.detailed, null, 2);
                break;

            default:
                output = "Invalid option!";
        }

        setResult(output);

    } catch (err) {
        hideLoader();
        setResult("Server error: " + err);
    }
}
