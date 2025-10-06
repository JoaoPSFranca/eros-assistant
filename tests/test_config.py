import pytest

from eros.config import Settings


def test_settings_init_succeeds_with_key(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test_key_123")
    s = Settings()
    assert s.GEMINI_API_KEY == "test_key_123"


def test_settings_init_fails_without_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="GEMINI_API_KEY não foi encontrada"):
        Settings()
