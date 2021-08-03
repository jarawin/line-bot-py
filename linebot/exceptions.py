"""linebot.exceptions module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass


class BaseError(with_metaclass(ABCMeta, Exception)):
    """Base Exception class."""

    def __init__(self, message='-'):
        """__init__ method.

        :param str message: Human readable message
        """
        self.message = message

    def __repr__(self):
        """repr."""
        return str(self)

    def __str__(self):
        """str.

        :rtype: str
        """
        return '<{0} [{1}]>'.format(
            self.__class__.__name__, self.message)


class InvalidSignatureError(BaseError):
    """When Webhook signature does NOT match, this error will be raised."""

    def __init__(self, message='-'):
        """__init__ method.

        :param str message: Human readable message
        """
        super(InvalidSignatureError, self).__init__(message)


class LineBotApiError(BaseError):
    """When LINE Messaging API response error, this error will be raised."""

    def __init__(
            self,
            status_code,
            headers,
            request_id=None,
            accepted_request_id=None,
            error=None
    ):
        """__init__ method.

        :param int status_code: HTTP status code
        :param headers: Response headers
        :type headers: dict[str, str]
        :param str request_id: (optional) Request ID. A unique ID is generated for each request
        :param str accepted_request_id: (optional) The same request has already been accepted
        :param error: (optional) Error class object.
        :type error: :py:class:`linebot.models.error.Error`
        """
        super(LineBotApiError, self).__init__(error.message)

        self.status_code = status_code
        self.headers = headers
        self.request_id = request_id
        self.accepted_request_id = accepted_request_id
        self.error = error

    def __str__(self):
        """str.

        :rtype: str
        """
        if self.accepted_request_id:
            return "{0}: status_code={1}, request_id={2}, " \
                   "accepted_request_id={3}, error_response={4}, headers={5}" \
                .format(self.__class__.__name__,
                        self.status_code,
                        self.request_id,
                        self.accepted_request_id,
                        self.error,
                        self.headers)
        return '{0}: status_code={1}, request_id={2}, error_response={3}, headers={4}'.format(
            self.__class__.__name__, self.status_code, self.request_id, self.error,
            self.headers)