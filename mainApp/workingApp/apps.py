from django.apps import AppConfig


class WorkingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workingApp'
    def ready(self):
        import workingApp.signals
