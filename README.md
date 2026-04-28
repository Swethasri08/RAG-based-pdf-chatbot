# 🤖 RAG-based PDF Chatbot

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-0.0.350+-green.svg)](https://python.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sophisticated **Retrieval-Augmented Generation (RAG)** chatbot that allows you to upload and interact with PDF documents using natural language queries. Powered by OpenAI's GPT models and LangChain framework.

## ✨ Features

- 📄 **Multi-PDF Support**: Upload and chat with multiple PDF documents simultaneously
- 🧠 **Intelligent Context-Aware Responses**: Maintains conversation history and context
- 🔍 **Smart Document Retrieval**: Finds relevant information from your documents using vector similarity search
- 💬 **Interactive Chat Interface**: User-friendly Streamlit-based chat interface
- ⚡ **Fast Processing**: Efficient document chunking and embedding generation
- 🔒 **Secure**: Local processing of documents with optional API key configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (get yours at [platform.openai.com](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Swethasri08/RAG-based-pdf-chatbot.git
   cd RAG-based-pdf-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The application will open in your web browser at `http://localhost:8501`

## 📖 How to Use

1. **Upload PDF Files**: Use the sidebar to upload one or more PDF documents
2. **Wait for Processing**: The system will automatically process and index your documents
3. **Start Chatting**: Type your questions about the document content in the chat interface
4. **Get Intelligent Responses**: Receive context-aware answers based on your uploaded documents

## 🏗️ Architecture

```
RAG-based PDF Chatbot/
├── app.py              # Main Streamlit application
├── config.py           # Configuration settings
├── utils.py            # Utility functions for document processing
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md          # This file
```

### Key Components

- **Document Processing**: Uses `PyPDFLoader` to extract text from PDFs
- **Text Splitting**: Employs `RecursiveCharacterTextSplitter` for optimal chunking
- **Embedding Generation**: Creates vector embeddings using OpenAI's embedding models
- **Vector Storage**: Utilizes FAISS for efficient similarity search
- **Conversational Chain**: Implements `ConversationalRetrievalChain` for context-aware responses

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `MODEL_NAME` | OpenAI model to use | `gpt-3.5-turbo` |
| `TEMPERATURE` | Response randomness (0-1) | `0.7` |
| `MAX_TOKENS` | Maximum response tokens | `1000` |
| `CHUNK_SIZE` | Document chunk size | `1000` |
| `CHUNK_OVERLAP` | Chunk overlap for context | `200` |

### Customization

You can customize the chatbot's behavior by modifying:

- **Prompt Template**: Edit the prompt in `app.py` to change response style
- **Chunk Parameters**: Adjust `CHUNK_SIZE` and `CHUNK_OVERLAP` in `.env`
- **Model Selection**: Change `MODEL_NAME` to use different OpenAI models

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

1. Clone your forked repository
2. Create a virtual environment and install dependencies
3. Copy `.env.example` to `.env` and configure your API keys
4. Make your changes
5. Test thoroughly with different PDF files
6. Submit a pull request

## 🐛 Troubleshooting

### Common Issues

**Q: Getting "OpenAI API key not found" error**
- A: Make sure you've set up your `.env` file correctly with a valid OpenAI API key

**Q: PDF processing is slow**
- A: Large PDFs take longer to process. Try with smaller files first or adjust chunk size

**Q: Chat responses are not relevant**
- A: Try adjusting the `TEMPERATURE` parameter or rephrase your questions

**Q: Memory errors with large documents**
- A: Reduce the `CHUNK_SIZE` in your `.env` file or process documents individually

### Performance Tips

- Use PDFs under 50MB for optimal performance
- Clear conversation history periodically for better memory management
- Adjust chunk size based on your document complexity

## 📚 Technology Stack

- **Frontend**: Streamlit - Fast, interactive web applications
- **Backend**: Python 3.8+
- **AI/ML**: 
  - LangChain - Framework for building LLM applications
  - OpenAI GPT Models - Language understanding and generation
  - FAISS - Vector similarity search
- **Document Processing**: PyPDF2, tiktoken
- **Environment**: python-dotenv

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://python.langchain.com/) for the amazing framework
- [OpenAI](https://openai.com/) for powerful language models
- [Streamlit](https://streamlit.io/) for the intuitive web interface
- [FAISS](https://faiss.ai/) for efficient vector search

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](https://github.com/Swethasri08/RAG-based-pdf-chatbot/issues)
3. Create a new issue with detailed information
4. Join our community discussions

---

**Made with ❤️ using RAG (Retrieval-Augmented Generation)**

[⭐ Star this repository if it helped you!](https://github.com/Swethasri08/RAG-based-pdf-chatbot)
