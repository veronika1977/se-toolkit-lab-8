from typing import List


class Settings:
    app_name: str = "SE Toolkit Lab 8"
    debug: bool = True
    address: str = "0.0.0.0"
    port: int = 5000
    reload: bool = True

    api_key: str = "test-key-123"

    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:5000"]

    enable_interactions: bool = True
    enable_learners: bool = True

    autochecker_api_url: str = "http://localhost:8888"
    autochecker_email: str = "test@example.com"
    autochecker_password: str = "testpass"

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "labdb"
    db_user: str = "labuser"
    db_password: str = "labpass"


settings = Settings()
