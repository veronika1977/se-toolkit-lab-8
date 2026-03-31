import os
from typing import List


class Settings:
    app_name: str = "SE Toolkit Lab 8"
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"
    address: str = os.getenv("ADDRESS", "0.0.0.0")
    port: int = int(os.getenv("PORT", "5000"))
    reload: bool = os.getenv("RELOAD", "true").lower() == "true"

    api_key: str = os.getenv("LMS_API_KEY", "test-key-123")

    cors_origins: List[str] = os.getenv("CORS_ORIGINS", "[]")

    enable_interactions: bool = os.getenv("BACKEND_ENABLE_INTERACTIONS", "true").lower() == "true"
    enable_learners: bool = os.getenv("BACKEND_ENABLE_LEARNERS", "true").lower() == "true"

    autochecker_api_url: str = os.getenv("AUTOCHECKER_API_URL", "http://localhost:8888")
    autochecker_email: str = os.getenv("AUTOCHECKER_API_LOGIN", "test@example.com")
    autochecker_password: str = os.getenv("AUTOCHECKER_API_PASSWORD", "testpass")

    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT", "5432"))
    db_name: str = os.getenv("DB_NAME", "labdb")
    db_user: str = os.getenv("DB_USER", "labuser")
    db_password: str = os.getenv("DB_PASSWORD", "labpass")


settings = Settings()
