from rest_framework.exceptions import APIException, _get_error_details


class SyncPriceException(APIException):
    def __init__(self, detail=None, code=None, url=None):
        if url is None:
            raise ValueError('APIException requires an url')

        if detail is None:
            detail = "{} {}".format(self.default_detail, url)
        if code is None:
            code = self.default_code

        self.detail = _get_error_details(detail, code)



class SyncFieldException(APIException):
    def __init__(self, detail=None, code=None, url=None, field_name=None):
        if url is None:
            raise ValueError('APIException requires an url')
        if field_name is None:
            raise ValueError('APIException requires a field name')

        if detail is None:
            detail = {
                'reasone': "Couln't scrapped ! May be your Regex pattern Invalid or something else",
                'url': url,
                'field_name': field_name
            }
        if code is None:
            code = self.default_code

        self.detail = _get_error_details(detail, code)


class InvalidDomainError(SyncPriceException):
    def __init__(self, detail=None, code=None, url=None):
        if url is None:
            raise ValueError('APIException requires an url')

        if detail is None:
            detail = "{} {}".format(self.default_detail, url)
        if code is None:
            code = self.default_code

        self.detail = _get_error_details(detail, code)

    status_code = 400
    default_detail = 'Your requested url is not valid'



class NotListedDomainError(SyncPriceException):
    status_code = 400
    default_detail = "Your requested website are not listed in our system"
   

class SKUnProductNotMatchedError(SyncPriceException):
    status_code = 400
    default_detail = "No SKU is matched with your given url and sku"
    

class UnknownError(SyncPriceException):
    status_code = 520
    default_detail = "Unknown Error Ocuured"
    



class NotFoundError(SyncPriceException):
    status_code = 404
    default_detail = "Your requested url not found"
    


class DoesNotExistError(APIException):
    status_code = 404
    default_detail = "Item doesn't exist with your given product id"

class NotURLGivenError(APIException):
    status_code = 404
    default_detail = 'Scrapper method requires url as argument'
    