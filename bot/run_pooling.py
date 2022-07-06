import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.settings')
django.setup()

from mobile_bot.handlers.dispatcher import run_pooling

if __name__ == "__main__":
    run_pooling()
