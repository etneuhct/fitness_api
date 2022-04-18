from django.db.models.signals import post_save

from notification.send_notification import send_notification, NotificationObj
from sport.models import Biking


class BikingSignals:

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        if created:
            send_notification(NotificationObj(message={"biking": instance.id}, room_id='room'))


post_save.connect(BikingSignals.post_save, sender=Biking)
