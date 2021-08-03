"""linebot.models.emojis module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Background(with_metaclass(ABCMeta, Base)):
    """Background."""

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Background, self).__init__(**kwargs)

        self.type = None


class LinearGradientBackground(Background):
    """LinearGradientBackground."""

    def __init__(self, angle, start_color, end_color,
                 center_color=None, center_position=None, **kwargs):
        """__init__ method.

        :param str type: The type of background used
        :param str angle: The angle at which a linear gradient moves
        :param str start_color: The color at the gradient's starting point
        :param str end_color: The color at the gradient's ending point
        :param str center_color: The color in the middle of the gradient
        :param str center_position: The position of the intermediate color stop
        :param kwargs:
        """
        super(LinearGradientBackground, self).__init__(**kwargs)
        self.type = 'linearGradient'
        self.angle = angle
        self.start_color = start_color
        self.end_color = end_color
        self.center_color = center_color
        self.center_position = center_position
