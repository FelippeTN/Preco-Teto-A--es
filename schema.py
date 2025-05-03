from pydantic import BaseModel, Field, validator
import re

class StockName(BaseModel):
    ticker_name: str = Field(..., description="Ticker name (e.g., BBAS3.SA)")
    
    @validator("ticker_name")
    def validate_ticker(cls, v):
        pattern = r"^[A-Z]{4}[0-9](\.SA)?$"
        if not re.match(pattern, v):
            raise ValueError("Ticker inválido. Use o formato 'BBAS3' ou 'BBAS3.SA'")
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "ticker_name": "BBAS3.SA",
            }
        }