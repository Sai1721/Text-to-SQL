from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3 
import pandas as pd
import datetime
from datetime import datetime

import google.generativeai as genai

# Admin credentials from .env
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

##configure our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load google gemini model and provide sql query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('models/gemini-2.0-flash')
    response = model.generate_content([prompt[0],question])
    return response.text

#function to retrieve queery from sql database
import mysql.connector

def read_sql_query(sql):
    try:
        print("Trying to connect to MySQL with:")
        print(f"Host: {os.getenv('MYSQL_HOST')}")
        print(f"User: {os.getenv('MYSQL_USER')}")
        print(f"Password: {os.getenv('MYSQL_PASSWORD')}")
        print(f"Database: {os.getenv('MYSQL_DATABASE')}")

        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")
        return []

#define the prompt
prompt = ["""
You are an expert in converting English questions to accurate and optimized SQL queries.

Assume the database contains the following tables:

1. **STUDENT**  
   - NAME (VARCHAR)  
   - CLASS (VARCHAR)  
   - SECTION (VARCHAR)  
   - MARKS (INT)  

2. **COURSE**  
   - CLASS (VARCHAR)  
   - COURSE_NAME (VARCHAR)  
   - INSTRUCTOR (VARCHAR)  

3. **ATTENDANCE**  
   - NAME (VARCHAR)  
   - DATE (DATE)  
   - STATUS (VARCHAR: Present/Absent)  

---

### Examples:

- Q: "How many students are there in each class?"  
  A: `SELECT CLASS, COUNT(*) FROM STUDENT GROUP BY CLASS;`

- Q: "Show all students along with their instructor names."  
  A: `SELECT STUDENT.NAME, COURSE.INSTRUCTOR FROM STUDENT JOIN COURSE ON STUDENT.CLASS = COURSE.CLASS;`

- Q: "Who are the students with attendance marked as Absent on 2024-03-15?"  
  A: `SELECT NAME FROM ATTENDANCE WHERE DATE = '2024-03-15' AND STATUS = 'Absent';`

- Q: "Give me average marks for each class."  
  A: `SELECT CLASS, AVG(MARKS) FROM STUDENT GROUP BY CLASS;`
  
- Q: "Change the name of student from Alice Smith to Alicia Smith"  
  A: `UPDATE STUDENT SET NAME = 'Alicia Smith' WHERE NAME = 'Alice Smith';`


---

### Rules:
- Use proper JOINs when data needs to be pulled from multiple tables.
- Only generate the SQL query. Do **not** include any explanation or the word 'SQL'.
- Do **not** surround the SQL with quotes or triple backticks.
- Keep column and table names **case-sensitive** and accurate.

""" ]


##Streamlit app


# Set app title and favicon
st.set_page_config(
    page_title="EduSQL: Student Database App",
    page_icon=":books:",
    layout="wide"
)

# Custom CSS for background images and UI improvements
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

main_bg_path = "sql bg.jpeg"         # Your main background image file
sidebar_bg_path = "sidebar bg1.png"   # Your sidebar background image file

main_bg_base64 = get_base64_of_bin_file(main_bg_path)
sidebar_bg_base64 = get_base64_of_bin_file(sidebar_bg_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{main_bg_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stSidebar"] {{
        background-image: url("data:image/jpg;base64,{sidebar_bg_base64}");
        background-size: cover;
        background-position: center;
    }}
    .main-card {{
        background: rgba(255,255,255,0.85);
        border-radius: 18px;
        padding: 2.5rem 2rem 2rem 2rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
    }}
    .stTextInput>div>div>input, .stSelectbox>div>div>div>input {{
        background: #f7fafc;
        border-radius: 8px;
        border: 1.5px solid #b3b3b3;
        padding: 0.5rem 1rem;
        font-size: 1.1rem;
    }}
    .stButton>button {{
        background-color: #2e7dff;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        border: none;
        transition: background 0.2s;
    }}
    .stButton>button:hover {{
        background-color: #1b4fa3;
        color: #fff;
    }}
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
        color: #1b4fa3;
        font-weight: 700;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# App title (remove LLM name)
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>EduSQL: Student Database App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #444; margin-top: 0;'>Query and manage your student database with ease</h4>", unsafe_allow_html=True)

# Wrap your main content in a card for better readability
st.markdown('<div class="main-card">', unsafe_allow_html=True)
# ...your main Streamlit code (inputs, outputs, etc.)...
# At the very end of your main content, close the card:
st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.title("💡 Example Queries")
st.sidebar.markdown("""
- Average marks of each class  
- List of students and instructors  
- Who was absent on 2024-03-15?  
- Total students in each section
""")
st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Admin Panel")

enable_admin = st.sidebar.checkbox("Enable Admin Upload")

def connect_to_database():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
    
if enable_admin:
    username = st.sidebar.text_input("👤 Username")
    password = st.sidebar.text_input("🔑 Password", type="password")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.sidebar.success("✅ Admin authenticated")

        uploaded_file = st.sidebar.file_uploader("📁 Upload CSV File", type=["csv"])
        table_name = st.sidebar.text_input("🗃️ Table Name to Insert Into")

        if uploaded_file and table_name:
            try:
                df = pd.read_csv(uploaded_file)

                conn = connect_to_database()
                cursor = conn.cursor()

                # Upload using pandas SQLAlchemy
                import sqlalchemy
                engine = sqlalchemy.create_engine(
                    f'mysql+mysqlconnector://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_HOST")}/{os.getenv("MYSQL_DATABASE")}'
                )
                df.to_sql(table_name, con=engine, if_exists='append', index=False)

                st.sidebar.success(f"✅ Uploaded to table `{table_name}` successfully.")
                st.write("📊 Preview of Uploaded Data")
                st.dataframe(df, use_container_width=True)

            except Exception as e:
                st.sidebar.error(f"❌ Upload failed: {e}")

    elif username or password:
        st.sidebar.error("❌ Invalid admin credentials")

# Add this block for test/example queries
example_questions = {
    "Show student names and marks": "Show all student names and their marks",
    "Average marks of each class": "Provide the average marks of all students class wise",
    "List students and instructors": "List all students and their instructors",
    "Absent on specific date": "Show who was absent on 2024-03-15",
    "Change student name": "Change the name of student from Alice Smith to Alicia Smith",
    "Update marks": "Update marks of John Doe to 95",
    "Delete student": "Remove student named Robert Brown",
    "Insert new student": "Add a new student John Wayne in class 10B with 85 marks"
}

st.sidebar.subheader("🎯 Test Queries")
selected_example = st.sidebar.selectbox("Choose a sample query", [""] + list(example_questions.values()))
if selected_example:
    st.session_state.input = selected_example
    
st.header("To Handle SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

    
#if submit is clicked
# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)

    st.subheader("Generated SQL Query")
    st.code(response, language='sql')

    try:
        conn = connect_to_database()
        cur = conn.cursor()

        # Check if the query starts with SELECT
        if response.strip().lower().startswith("select"):
            cur.execute(response)
            rows = cur.fetchall()
            cols = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=cols)

            st.success("Query executed successfully!")
            st.subheader("📊 Results:")
            st.dataframe(df, use_container_width=True)

            if not df.empty:
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("⬇️ Download Results as CSV", csv, "query_results.csv", "text/csv")
        else:
            # Non-select queries: UPDATE, INSERT, DELETE
            cur.execute(response)
            conn.commit()
            st.success("✅ Query executed successfully. Database updated.")

        # Logging the query
        with open("query_log.csv", "a") as log:
            log.write(f"{datetime.now()}, {question}, {response}\n")

        cur.close()
        conn.close()

    except Exception as e:
        st.error(f"Error executing query: {e}")

