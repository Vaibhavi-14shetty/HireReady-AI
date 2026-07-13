from fastapi import APIRouter, HTTPException

from app.schemas.user import UserSignup
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/signup")
def signup(user: UserSignup):
    try:
        result = AuthService.signup(
            user.email,
            user.password,
        )

        return {
            "message": "User created successfully",
            "user": result.user.email if result.user else None,
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get("/ping")
def ping():
    return {"status": "ok"}
