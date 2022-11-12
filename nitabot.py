import asyncio
import discord
from discord.ext import commands
from manager import manage_token, manage_serverid


intents=discord.Intents.all()
#ID = int(manage_serverid())

class nitabot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            shard_id = [0],
            shard_count = 1
        )
        self.initial_extensions = [
            "cog.Reload",
            "cog.Commands"
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)

        #await bot.tree.sync(guild = discord.Object(id = ID))
        await bot.tree.sync()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!!!")
        print()
        while True:
            joinserver = str(len(bot.guilds))
            await bot.change_presence(activity = discord.Activity(name = joinserver +" servers" , type=discord.ActivityType.watching))
            await asyncio.sleep(200)

bot = nitabot()

TOKEN = manage_token()

bot.run(TOKEN)
