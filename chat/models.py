from django.db import models
from django.utils.six import python_2_unicode_compatible
from channels import Group

@python_2_unicode_compatible
class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def str(self):
        return self.title

    def websocket_group(self):
        """
        Returns the Channels Group that sockets should
        subscribe to for receiving messages as they are Generatedself.
        """
        return Group("room-%s" % self.id)
