class WWPException(Exception):
    """Base exception."""


class DatabaseException(WWPException):
    pass


class NetworkException(WWPException):
    pass


class SecurityException(WWPException):
    pass