# Discord API Ops
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from dagster import op, RetryPolicy, Backoff, Out, In
from logger import dagster_logger

# Get the API endpoint and credentials.
load_dotenv()
DISCORD_BOT_NAME = os.getenv("BOT_NAME")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")


# Define the op to send a Discord message.
@op(
    name="send_discord_message",
    description="Sends a message to a Discord channel.",
    ins={"message": In(pd.DataFrame)},
    out=Out(bool),
    retry_policy=RetryPolicy(
        max_retries=3,
        delay=2.0,
        backoff=Backoff.EXPONENTIAL,
    ),
)
def send_discord_message(message: pd.DataFrame) -> bool:
    """Sends a message to a specific Discord channel using a bot."""
    try:
        # Logging the Discord bot sending message.
        dagster_logger.info(f"INFO: {DISCORD_BOT_NAME} sent message to Discord.")

        # Convert the dataframe into markdown.
        message = f"```{message.to_markdown(index=False)}```"

        # Construct the URL and headers.
        url = f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages"
        headers = {
            "Authorization": f"Bot {DISCORD_BOT_TOKEN}",
            "Content-Type": "application/json",
        }
        data = {"content": message}

        # Post the message.
        response = requests.post(url, json=data, headers=headers)

        # Validate the message was sent.
        if response.status_code == 200 or response.status_code == 201:
            dagster_logger.info("INFO: Message sent successfully.")
            return True

    except Exception as e:
        raise e
