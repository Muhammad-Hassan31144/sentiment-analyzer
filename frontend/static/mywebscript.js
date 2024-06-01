function validateInput(text) {
    const regex = /^[a-zA-Z0-9\s.,!?']+$/; // Allow letters, numbers, spaces, and some punctuation
    return regex.test(text) && text.length > 0 && text.length <= 500;
}

function RunSentimentAnalysis() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    
    if (!validateInput(textToAnalyze)) {
        document.getElementById("system_response").innerHTML = "Invalid input! Please enter a valid text.";
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "/api/sentimentAnalyzer?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}