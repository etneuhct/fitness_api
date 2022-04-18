from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class NotificationObj:

    def __init__(self, room_id, message):
        self.message_type = 'notification'
        self.channel = f"room"
        self.message = message


def send_notification(notification):
    """

    :param notification:
    :return:
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("notification",
                                            {
                                                'type': notification.message_type,
                                                'message': notification.message})
