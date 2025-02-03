# BongAI Chatbot

A conversational AI chatbot built with Streamlit, LangChain, and OpenAI's GPT-3.5. BongAI provides an intuitive interface for users to interact with a sophisticated AI assistant powered by state-of-the-art language models.

## Features

- Real-time chat interface built with Streamlit
- Integration with OpenAI's GPT-3.5-turbo model
- Conversation history management
- Vector store implementation using FAISS for efficient information retrieval
- Environment variable management for secure API key handling

## Prerequisites

Before running the application, make sure you have:

- Python 3.7+
- An OpenAI API key
- The required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bongai.git
cd bongai
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Start chatting with BongAI through the text input interface

## Project Structure

```
bongai/
├── app.py              # Main application file
├── .env               # Environment variables (not tracked in git)
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## Dependencies

- streamlit
- langchain
- langchain-community
- langchain-openai
- python-dotenv
- faiss-cpu
- openai

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT-3.5 model
- LangChain for the conversational AI framework
- Streamlit for the web interface framework
- FAISS for vector storage capabilities

## Contact

For any questions or feedback, please open an issue in the GitHub repository.

---

Made with ❤️ using Streamlit, LangChain, and OpenAI
