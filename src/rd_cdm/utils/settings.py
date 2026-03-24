from __future__ import annotations
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class ValidationSettings(BaseSettings):
    """
    Environment-driven settings for validation steps.
    """
    model_config = ConfigDict(env_prefix="", extra="ignore")

    bioportal_api_key: str = ""  # set via BIOPORTAL_API_KEY env var or .env file