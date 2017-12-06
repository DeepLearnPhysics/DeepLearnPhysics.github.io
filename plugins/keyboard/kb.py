from pelican import signals

import logging
import re

logging.Logger(__name__)


def content_object_init(instance):
    """
    Provides the key plugin, make sure that you have Keys.css, http://michaelhue.com/keyscss/
    imported inside your HTML. How to use:

        So you hit [kb:CTRL] + [kb:ALT] + [kb:DEL] when in doubt

    Note, that light keyboard keys are enabled by default.
    """
    if instance._content is not None:  # 1
        content = instance._content
        new_content = re.sub(r"\[kb:(.+?)\]", r'<kbd class="light">\1</kbd>', content)  # 2
        instance._content = new_content
        return instance

def register():
    signals.content_object_init.connect(content_object_init)  # 3
