from typing import Annotated

from fastapi import Header, HTTPException

async def get_token_header(bearer_token: Annotated[str, Header()]):
    if not isinstance(bearer_token, str):
        raise HTTPException(status_code=400, detail="Bearer Token header invalid")
