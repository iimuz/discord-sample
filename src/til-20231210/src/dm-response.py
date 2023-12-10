"""DiscordでDMに対して返答するスクリプト.

利用例: `python src/dm-response.py`
"""
import os

import discord


class DiscordClient(discord.Client):
    """DiscordのDMに対して反応するためのクライアント."""

    async def on_ready(self):
        """準備完了時の動作."""
        print("Logged on as", self.user)

    async def on_message(self, message):
        """メッセージ取得時の動作."""
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")


if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN", "")

    intents = discord.Intents.default()
    intents.message_content = True
    client = DiscordClient(intents=intents)
    client.run(TOKEN)
