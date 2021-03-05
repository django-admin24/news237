from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals
