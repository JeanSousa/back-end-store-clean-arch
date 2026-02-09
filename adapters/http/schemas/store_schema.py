from pydantic import BaseModel, Field, field_validator

class StoreGetRequest(BaseModel):
    store_id: int 

    @field_validator("store_id")
    @classmethod
    def validate_store_id(cls, value: int):
        if not value.is_integer():
            raise ValueError("O campo store_id deve ser um inteiro")
        return value


