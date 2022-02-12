from email.message import Message
import os

from discord import Webhook, RequestsWebhookAdapter
from dotenv import load_dotenv

load_dotenv()

MESSAGE = 'Hey there!'

webhook = Webhook.from_url(os.getenv('WEBHOOK_URL'), adapter=RequestsWebhookAdapter())
webhook.send(MESSAGE)