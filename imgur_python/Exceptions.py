
class ImgurException(Exception):
    """ Base exception class for Imgur-Python """

class ImgurBadRequest(ImgurException):
    """ Raised when a request is returned with HTTP 400: Bad Request """

class ImgurUnauthorized(ImgurException):
    """ Raised when a request is returned with HTTP 401: Unauthorized """

class ImgurForbidden(ImgurException):
    """ Raised when a request is returned with HTTP 403: Forbidden """

ExceptionLUT = {
    400 : ImgurBadRequest,
    401 : ImgurUnauthorized,
    403 : ImgurForbidden,
}
