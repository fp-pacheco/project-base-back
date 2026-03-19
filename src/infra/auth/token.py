from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import jwt
from fastapi import HTTPException, status

from src.core.settings import Settings

BR_TZ = ZoneInfo("America/Sao_Paulo")
ALGORITHM = "HS256"
TOKEN_EXPIRATION_DAYS = 7


def decode(token: str) -> dict:
    try:
        return jwt.decode(token, Settings.JWT_SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado",
        ) from err
    except jwt.DecodeError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token malformado ou inválido",
        ) from err


def encode(payload: dict) -> str:
    now = datetime.now(tz=BR_TZ)
    exp = now + timedelta(days=TOKEN_EXPIRATION_DAYS)

    return jwt.encode(
        {**payload, "iat": int(now.timestamp()), "exp": int(exp.timestamp())},
        Settings.JWT_SECRET_KEY,
        algorithm=ALGORITHM,
    )
