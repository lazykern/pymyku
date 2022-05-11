from requests import HTTPError

class TokenExpired(HTTPError):
    '''The access token has expired.'''
    pass
