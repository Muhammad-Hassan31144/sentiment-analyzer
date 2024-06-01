# Sentiment Analysis App

This application uses a pre-trained BERT model for sentiment analysis. The model is `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face.

## Project Structure

- **app.py**: The main file containing the Streamlit application code.
- **requirements.txt**: Lists the Python dependencies for your project.

## Purpose

The purpose of this application is to provide a simple interface for users to input text and receive sentiment analysis results using a pre-trained BERT model. This can be useful for various NLP tasks such as understanding customer feedback, social media analysis, and more.

## How to Deploy

### Deployment on Streamlit Cloud

1. **Push your code to a GitHub repository**:
    Ensure your repository structure is similar to the following:

    ```
    sentiment-analysis-app/
    ├── app.py
    ├── requirements.txt
    └── README.md
    ```

2. **Go to [Streamlit Cloud](https://share.streamlit.io/)** and sign in with your GitHub account.

3. **Click on “New app”**.

4. **Select your repository** and specify the branch (usually `main` or `master`).

5. **Enter the file path** to your `app.py` file (e.g., `app.py`).

6. **Click “Deploy”**.

Streamlit Cloud will then build and deploy your app. Once it’s ready, you will be provided with a URL where you can access your live sentiment analysis app.