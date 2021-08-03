"""linebot.models.error module."""

from __future__ import unicode_literals

from .base import Base


class Error(Base):
    """Error response of LINE messaging API.

    https://developers.line.biz/en/reference/messaging-api/#error-response
    """

    def __init__(self, message=None, details=None, **kwargs):
        """__init__ method.

        :param str message: Summary of the error
        :param details: ErrorDetail instance list
        :type details: list[T <= :py:class:`linebot.models.error.ErrorDetail`]
        :param kwargs:
        """
        super(Error, self).__init__(**kwargs)

        self.message = message

        new_details = []
        if details:
            for detail in details:
                new_details.append(
                    self.get_or_new_from_json_dict(detail, ErrorDetail)
                )
        self.details = new_details


class ErrorDetail(Base):
    """ErrorDetail response of LINE messaging API."""

    def __init__(self, message=None, property=None, **kwargs):
        """__init__ method.

        :param str message: Details of the error message
        :param str property: Related property
        :param kwargs:
        """
        super(ErrorDetail, self).__init__(**kwargs)

        self.message = message
        self.property = property
