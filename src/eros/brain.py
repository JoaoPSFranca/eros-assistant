import google.generativeai as genai
from google.generativeai.generative_models import ChatSession

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

MODEL_NAME = "gemini-2.5-pro"
_model: genai.GenerativeModel | None = None


def initialize_brain(api_key: str):
    global _model
    try:
        genai.configure(api_key=api_key)
        _model = genai.GenerativeModel(
            model_name=MODEL_NAME, generation_config=generation_config
        )
    except Exception as e:
        raise RuntimeError(f"Falha ao inicializar o modelo Gemini: {e}")


def start_chat_session() -> ChatSession:
    if _model is None:
        mesage = "O cérebro não foi inicializado. "
        "Chame initialize_brain() primeiro."
        raise RuntimeError(mesage)
    chat = _model.start_chat(history=[])
    return chat


def get_chat_response(chat: ChatSession, prompt: str) -> str:
    try:
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao comunicar com a API do Gemini: {e}")
        return (
            "Desculpe, tive um problema para me conectar ao meu cérebro."
            " Tente novamente."
        )
