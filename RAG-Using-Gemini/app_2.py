import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import ChatPromptTemplate


template = """
You are an helpful assistant. 
If you don't know the answer, just say that you don't know.
For greetings dont use the context to response.
Question: {question} 
Context: {context} 
"""

pdfs_directory = 'chat-with-pdf/pdfs/'

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store = InMemoryVectorStore(embeddings)
 
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# Loading PDF
def upload_pdf(file):
    # Ensure the directory exists
    os.makedirs(pdfs_directory, exist_ok=True)

    # Save file using os.path.join for safety
    save_path = os.path.join(pdfs_directory, file.name)

    with open(save_path, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()

    return documents

# Spliting loaded pdf
def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )

    return text_splitter.split_documents(documents)

# Indexing pdf
def index_docs(documents):
    vector_store.add_documents(documents)

def retrieve_docs(query):
    return vector_store.similarity_search(query)

def answer_question(question, documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    return chain.invoke({"question": question, "context": context})

# Header
st.title("Birlasoft Assistant")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type="pdf",
    accept_multiple_files=False
)


if uploaded_file:
    upload_pdf(uploaded_file)

    documents = load_pdf(os.path.join(pdfs_directory, uploaded_file.name))
    chunked_documents = split_text(documents)
    index_docs(chunked_documents)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accepting user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        related_documents = retrieve_docs(prompt)
        answer = answer_question(prompt, related_documents)
        response = answer.content
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})