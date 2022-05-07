from requests.exceptions import HTTPError


class InvalidSubjectID(Exception):
    pass


class TokenExpired(HTTPError):
    '''Raised when the access token has expired.'''
    pass
