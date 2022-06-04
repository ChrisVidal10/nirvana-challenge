class UserNotFoundError(Exception):
    """Exception raised when the user is not found.

    Attributes:
        member_id -- User's member Id
        message -- explanation of the error
    """

    def __init__(self, member_id, message="Not found"):
        self.member_id = member_id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Member Id #{self.member_id} {self.message}"
