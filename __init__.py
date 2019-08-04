#!/usr/bin/env python


from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.textinput import TextInput


class Adaptive_TextInput(TextInput):
    """
    Text input that grows when in focus and shrinks to the number of lines (if defined) by synopsis_line_limit.

    Copyright AGPL-3.0 2019 S0AndS0
    """

    def __init__(self, synopsis_line_limit = None, **kwargs):
        super(Adaptive_TextInput, self).__init__(**kwargs)
        self.synopsis_line_limit = synopsis_line_limit
        self.synopsis_text = ''
        self.full_text = ''
        self.old_height = self.height
        self.trigger_refresh_y_dimension = None
        self.schedule_set_trigger_refresh_y_dimension = Clock.create_trigger(lambda _: self._set_trigger_refresh_grids_y_dimension(), 0)
        self.schedule_trigger_refresh_y_dimension = Clock.create_trigger(lambda _: self.trigger_refresh_y_dimension(), 0)

    def _refresh_overflow_values(self, text):
        """
        If `synopsis_line_limit` is set then `_split_smart` and `_get_text_width` methods from TextInput are used
        to generate synopsis text, otherwise both `full_text` and `synopsis_text` values will be the same.
        """
        self.full_text = u"{0}".format(text)

        if self.synopsis_line_limit is not None and type(self.synopsis_line_limit) is int:
            lines, lines_flags = self._split_smart(text)
            synopsis_line = ''.join(lines[:self.synopsis_line_limit])
            text_width = self._get_text_width(synopsis_line, self.tab_width, self._label_cached)
            available_width = self.width - self.padding[0] - self.padding[2]
            if len(lines) > self.synopsis_line_limit and (text_width + 4) > available_width:
                self.synopsis_text = u"{0}...".format(synopsis_line[:-4])
            else:
                self.synopsis_text = u"{0}".format(synopsis_line)
        else:
            self.synopsis_text = u"{0}".format(text)

    def _refresh_text_value(self):
        """ Sets `self.text` to either `self.full_text` or `self.synopsis_text` based off `self.focus` value. """
        if self.focus is True:
            self.text = u"{0}".format(self.full_text)
        elif len(self.synopsis_text) > 0:
            self.text = u"{0}".format(self.synopsis_text)

    def _find_trigger_refresh_y_dimension(self):
        """ Returns first match of `<widget>.trigger_refresh_y_dimension` method when available or False otherwise. """
        for element in self.walk_reverse():
            if hasattr(element, 'trigger_refresh_y_dimension'):
                return element.trigger_refresh_y_dimension
        else:
            return False

    def _set_trigger_refresh_grids_y_dimension(self, *args):
        """
        Sets trigger_refresh_y_dimension to return value of `_find_trigger_refresh_y_dimension`
        while absorbing extra arguments passed by Clock.
        """
        self.trigger_refresh_y_dimension = self._find_trigger_refresh_y_dimension()

    def _propagate_height_updates(self):
        """
        Triggers grid layouts to update to height changes of this widget.

        Note this ignores errors if 'trigger_refresh_y_dimension' is
        not set/callable or is 'False', otherwise something else went wrong
        and any other errors will bubble-up.
        """
        try:
            self.trigger_refresh_y_dimension()
        except TypeError as e:
            if not self.trigger_refresh_y_dimension:
                raise e

    def on_focused(self, instance, value):
        """ Triggers updates to methods that are interested in `self.focus` status. """
        self._refresh_text_value()
        self._propagate_height_updates()

    def animate(self, instance, value):
        animation = Animation(height = instance.old_height)
        animation += Animation(height = value, duration = 1.5)
        animation.repeat = False
        return Clock.create_trigger(lambda _: animation.start(instance), 0)

    def on_height(self, instance, value):
        """ Triggers updates for grid layout heights related to this widget. """
        self._propagate_height_updates()

    def on_width(self, instance, value):
        """ Updates line wrapping and text overflow values. """
        self._refresh_overflow_values(text = self.full_text)
        self._refresh_text_value()

    def on_text(self, instance, value):
        """
        Updates text values via `self._refresh_overflow_values(text = value)` only if focused; issues will arise
        though if an external process inserts text without calling `_refresh_overflow_values` method after.
        """
        if self.focus is True:
            self._refresh_overflow_values(text = value)

    def on_parent(self, instance, value):
        """ Waits for parenting to set customized text values because `self.text` maybe set after initialization. """
        self._refresh_overflow_values(text = self.text)
        self._refresh_text_value()
        self.schedule_set_trigger_refresh_y_dimension()
        self.schedule_trigger_refresh_y_dimension()
