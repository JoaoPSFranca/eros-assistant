from unittest.mock import MagicMock, patch
from eros import brain

def test_get_chat_response_sends_prompt_and_returns_text(mocker):
    mocker.patch('eros.brain.genai.GenerativeModel')
    mocker.patch('eros.brain.genai.configure')
    brain.initialize_brain(api_key="fake_key")
    mock_chat_session = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Esta é uma resposta de teste."
    mock_chat_session.send_message.return_value = mock_response
    user_prompt = "Olá, mundo!"
    response = brain.get_chat_response(mock_chat_session, user_prompt)
    mock_chat_session.send_message.assert_called_once_with(user_prompt)
    assert response == "Esta é uma resposta de teste."