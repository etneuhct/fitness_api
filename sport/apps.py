from django.apps import AppConfig


class SportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sport'

    def ready(self):
        import sport.signals
        return super(SportConfig, self).ready()