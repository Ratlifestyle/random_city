class ExistingUserException(Exception):
    def __init__(self, message='User already exists. Please login'):
        self.message=message
        super().__init__(self.message)