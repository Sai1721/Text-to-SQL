# Natural Language to SQL Query Generator using Gemini API

This Streamlit application uses Google Gemini API to convert natural language questions into SQL queries and fetch data from a SQLite database.

## Demo
![Demo Video](demo.webm)

## Features
- Converts English questions into SQL queries using Google Gemini API.
- Retrieves data from a SQLite database (`student.db`).
- Simple and interactive UI using Streamlit.

## Tech Stack
- Python
- Streamlit
- Google Gemini API
- SQLite
- `google-generativeai` (Gemini API)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- A SQLite database (`student.db` with `STUDENT` table)
- A Google API key for Gemini

### Clone the Repository
```sh
git clone https://github.com/Sai1721/Text-to-SQL
```

### Set Up a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Configuration

### Setting Up Environment Variables
1. Create a `.env` file in the project directory.
2. Add your Google API key:
```ini
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the Application
```sh
streamlit run app.py
```

## File Structure
```
📂 Text-to-SQL
│── 📄 app.py          # Main Streamlit application
│── 📄 requirements.txt # Dependencies
│── 📄 .env            # Environment variables
│── 📄 student.db      # SQLite database
│── 📄 README.md       # Project documentation
```

## Deployment on Streamlit Community Cloud

1. **Push the project to GitHub**:
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. **Go to [Streamlit Community Cloud](https://share.streamlit.io/)**.
3. **Sign in** and click on "New App".
4. **Connect your GitHub repository**.
5. **Select the `app.py` file** as the entry point.
6. **Click 'Deploy'**.

## Example Queries
| User Question | Generated SQL Query |
|--------------|--------------------|
| How many students are there? | `SELECT COUNT(*) FROM STUDENT;` |
| Show students in Data Science class. | `SELECT * FROM STUDENT WHERE CLASS='Data Science';` |
