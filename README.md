# 💬 Natural Language to SQL Query Generator (with Gemini AI + MySQL)

> A Smart AI-powered system that converts human language questions into SQL queries and retrieves relevant data from a MySQL database. Built using Google Gemini Pro and Streamlit.

---

## 🎥 Demo

Watch a short demo video below to see it in action:  

<video controls src="full_demo.mp4" title="Title"></video>
---

## 🚀 Features

- ✅ **Gemini Pro Integration** – Uses Google's Gemini 2.0 Flash for converting natural language to optimized SQL queries.
- ✅ **MySQL Backend Support** – Connects securely to a MySQL database.
- ✅ **JOIN Handling** – Supports complex queries with proper JOIN logic.
- ✅ **Dynamic Query Execution** – Executes generated queries in real-time.
- ✅ **Beautiful Result Display** – Tabular view with download as CSV option.
- ✅ **Secure Admin Panel** – Password-protected panel to upload data via CSV.
- ✅ **Auto Query Log** – Stores user questions and generated queries in a log.

---

## 🛠️ Tech Stack

| Technology     | Purpose                          |
|----------------|----------------------------------|
| Streamlit      | Frontend Interface               |
| Google Gemini  | AI Query Generator               |
| MySQL          | Backend Database                 |
| Python         | Logic, Execution, Integration    |
| .env           | Secures environment variables    |

---

## 📁 Project Structure

📦project-root/
├── app.py # Main Streamlit app
├── agent.py # Gemini API interaction
├── .env # Environment variables
├── requirements.txt # Python dependencies
├── query_log.csv # Logs of past queries
├── uploads/ # Admin-uploaded CSVs
└── README.md # This file


---

## 🔒 Security Notes

- API keys and database credentials are securely loaded using `.env` files.
- Admin data upload panel is password-protected.
- No sensitive data or internal SQL logic is exposed in this repo.

---

## 🧪 Sample Use Cases

- 🔢 Average marks of each class  
- 🧑‍🏫 List of students and instructors  
- 📅 Who was absent on a given date  
- 📊 Total students in each section  
- ✍️ Update a student name using plain English

---

## ⚙️ Setup Instructions

> ⚠️ Codebase is **not exposed** for privacy and intellectual property reasons.

If you'd like to collaborate or request access for academic/research purposes, please reach out via email.

---

## 🤝 Author

**Sairaman Mathivelan**  
President, Dept. of Artificial Intelligence & Data Science  
📫 [LinkedIn](https://www.linkedin.com/in/sairaman-mathivelan) • ✉️ sairaman@example.com

---

## 📄 License

This project is licensed for demo and educational purposes.  
For commercial use or source access, please contact the author.
