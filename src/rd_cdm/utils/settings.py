from __future__ import annotations
from pydantic_settings import BaseSettings

class ValidationSettings(BaseSettings):
    """
    Environment-driven settings for validation steps.
    """
    bioportal_api_key: str = ""  # set in CI/locally; validation step will check emptiness

    class Config:
        env_prefix = ""   # BIOPORTAL_API_KEY
        env_file = ".env"
