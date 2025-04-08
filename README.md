
This is an intelligent PDF chatbot built using **LangChain**, **Gemini (Google Generative AI)**, and **Streamlit**. It allows users to upload PDF files and interact with them conversationally using natural language. It uses `GoogleGenerativeAIEmbeddings` to embed content and `gemini-1.5-pro` to answer queries based on context.

## 🔥 Features

- 📁 Upload and process PDF documents
- 🧠 Uses Google Generative AI (`gemini-1.5-pro`) to answer questions
- 🧩 Splits PDF into smart chunks for better context handling
- ⚡ Fast and lightweight vector store using `InMemoryVectorStore`
- 💬 Chat UI with persistent conversation using Streamlit
- 🛡️ Graceful fallback if no relevant context is found

---

## 🛠️ Tech Stack

- `LangChain`
- `Google Generative AI` (Gemini)
- `Streamlit`
- `PDFPlumber`
- `LangChain Text Splitter & Vector Store`

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/chat-with-pdf.git
cd chat-with-pdf
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set up API Key
You need a Google Generative AI API key. Create a .env file or use Streamlit secrets.

For .env:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
Or if you're using st.secrets:

python
Copy
Edit
st.secrets["GOOGLE_API_KEY"]
Then in code:

python
Copy
Edit
import os
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
4. Run the app
bash
Copy
Edit
streamlit run app.py
🧪 Usage
Launch the app in your browser.

Upload a PDF using the sidebar.

Ask any question related to the PDF.

View intelligent answers based on document content.

📂 Folder Structure
csharp
Copy
Edit
chat-with-pdf/
├── app.py
├── pdfs/
├── requirements.txt
└── README.md
