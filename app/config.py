from pydantic_settings import BaseSettings
  
class Setting(BaseSettings):
    database_url: str
    model_name: str = "all-MiniLM-L6-v2"
    chunk_size: int = 500
    chunk_overlap: int = 50
    chroma_db_path: str = "./chroma_db"

    class Config:
        env_file = ".env"
  
settings = Setting()