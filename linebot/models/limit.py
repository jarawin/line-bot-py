"""linebot.models.recipient module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Limit(with_metaclass(ABCMeta, Base)):
    """Limit.

    https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message

    """

    def __init__(self, max=None, up_to_remaining_quota=False, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Limit, self).__init__(**kwargs)

        self.max = max
        self.up_to_remaining_quota = up_to_remaining_quota
