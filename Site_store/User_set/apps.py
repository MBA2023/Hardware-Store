from django.apps import AppConfig


class UserSetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User_set'

    def ready(self):
        import User_set.signals
