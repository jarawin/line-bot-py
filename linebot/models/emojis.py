"""linebot.models.emojis module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Emojis(with_metaclass(ABCMeta, Base)):
    """Emojis.

    https://developers.line.biz/en/reference/messaging-api/#text-message

    """

    def __init__(self, index=None, length=None, product_id=None, emoji_id=None, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Emojis, self).__init__(**kwargs)

        self.index = index
        self.length = length
        self.product_id = product_id
        self.emoji_id = emoji_id
