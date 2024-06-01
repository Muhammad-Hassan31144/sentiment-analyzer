# Sentiment Analysis App

This application uses a pre-trained BERT model for sentiment analysis. The model is `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face.

## Project Structure

- **api/**: Contains the backend serverless function written in Python.
  - `sentimentAnalyzer.py`: The main file containing the handler function for the serverless function.
- **frontend/**: Contains the static files for the frontend.
  - `index.html`: The main HTML file for the frontend.
  - `static/`: Contains JavaScript files.
    - `mywebscript.js`: The JavaScript file containing the code for running the sentiment analysis.
  - `styles/`: Contains CSS files.
    - `main.css`: Your main CSS file for styling.
- **vercel.json**: Configuration file for Vercel to define builds and routes.
- **requirements.txt**: Lists the Python dependencies for your project.

## Purpose

The purpose of this application is to provide a simple interface for users to input text and receive sentiment analysis results using a pre-trained BERT model. This can be useful for various NLP tasks such as understanding customer feedback, social media analysis, and more.

## How to Deploy

### Frontend Deployment on Vercel

1. **Install Vercel CLI**:
    ```bash
    npm install -g vercel
    ```

2. **Login to Vercel**:
    ```bash
    vercel login
    ```

3. **Deploy**:
    ```bash
    vercel
    ```

Follow the prompts to deploy your project. Vercel will automatically detect your configuration and deploy both the frontend and backend.

## Model Information

This application uses the `distilbert-base-uncased-finetuned-sst-2-english` model from Hugging Face for sentiment analysis. This model is a distilled version of BERT, fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset.

## License

This project is licensed under the MIT License.
