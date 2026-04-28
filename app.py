import streamlit as st
from rag_pipeline import load_pdf, split_text, create_vector_store, ask_question

st.set_page_config(page_title="RAG PDF Questioner")

st.title("📄 RAG PDF Questioner")

# Initialize session state
if "db" not in st.session_state:
    st.session_state.db = None

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None and st.session_state.db is None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    with st.spinner("Processing PDF... ⏳"):
        docs = load_pdf("temp.pdf")
        chunks = split_text(docs)
        st.session_state.db = create_vector_store(chunks)

    st.success("PDF processed! Now ask questions 👇")

# 👉 SHOW QUESTION BOX AFTER PROCESSING
if st.session_state.db is not None:
    query = st.text_input("Ask a question about your PDF:")

    if query:
        with st.spinner("Thinking... 🤖"):
            answer = ask_question(st.session_state.db, query)

        st.write("### 🤖 Answer:")
        st.write(answer)