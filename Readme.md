# Data Science Tutor

## Overview
The **AI-Powered Data Science Tutor** is a Streamlit web application that leverages Google Generative AI (Gemini-1.5 Pro) and LangChain to assist users in learning Data Science. It provides detailed explanations, examples, and maintains chat history using an SQLite database.

## Features
- Interactive chatbot powered by **Google Generative AI**.
- Stores conversation history in an **SQLite database**.
- Streamlit-based **simple UI** for user interaction.
- Provides **detailed responses** with examples for Data Science topics.
- Ensures queries stay within the Data Science domain.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Streamlit
- LangChain
- Google Generative AI (Gemini API access)

### Steps
1. **Clone the repository**:
   ```bash
   git clone <repo-link>
   cd <repo-folder>
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup API Key
Create a `.streamlit/secrets.toml` file and add your API key:
```toml
[API]
API_KEY = "your-google-genai-api-key"
```

## Running the App
Run the Streamlit application:
```bash
streamlit run app.py
```

## Usage
- Enter a query related to **Data Science**.
- Click the **Submit** button.
- The AI tutor will generate a response.
- Chat history is maintained across sessions.

## Future Enhancements
- Improve response accuracy with fine-tuned models.
- Implement user authentication.
- Support multiple AI models.


