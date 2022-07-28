class BadRequestException(Exception):
    def __init__(self, message='Bad request. Please try again'):
        self.message=message
        super().__init__(self.message)