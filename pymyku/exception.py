from requests import HTTPError


class InvalidSubjectID(Exception):
    '''The subject ID is not valid.'''
    pass


class TokenExpired(HTTPError):
    '''The access token has expired.'''
    pass
