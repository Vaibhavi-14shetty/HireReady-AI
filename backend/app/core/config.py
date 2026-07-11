from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SUPABASE_URL: str = "https://merjspskxtfatjispopf.supabase.co"
    SUPABASE_SERVICE_ROLE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1lcmpzcHNreHRmYXRqaXNwb3BmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MzQzMjk3MCwiZXhwIjoyMDk5MDA4OTcwfQ.rE2j7WDyB30XRMlw10lTiTY4Myvoigp6foG0r-KigHY"

    DATABASE_URL: str = "postgresql://postgres:[YOUR-PASSWORD]@db.merjspskxtfatjispopf.supabase.co:5432/postgres"

    GEMINI_API_KEY: str = ""

    SECRET_KEY: str = "d6bf8cc28050a4b0ed896e6932ddc39216a7429a8afbbce137d90d9408136fa7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
