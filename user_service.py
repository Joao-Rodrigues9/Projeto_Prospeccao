class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, name: str, email: str) -> dict:
        if "@" not in email:
            raise ValueError("Invalid email format")
        
        if self.repository.find_by_email(email):
            raise ValueError("User already exists")
            
        return self.repository.save({"name": name, "email": email})