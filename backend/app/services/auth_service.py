from app.core.supabase import supabase


class AuthService:
    @staticmethod
    def signup(email: str, password: str):
        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
            }
        )
        return response
