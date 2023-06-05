from dotenv import load_dotenv
import os

load_dotenv(".env")

try:
  BOT_TOKEN = os.getenv('BOT_TOKEN')
  BOT_OWNERS = [int(x) for x in os.getenv('BOT_OWNERS').split(",")]
except (TypeError, ValueError) as ex:
  print("Error while reading config:", ex)
