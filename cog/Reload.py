import os
from discord.ext import commands
from manager import manage_serverid

#ID = int(manage_serverid())

def sort_files(path):
    files = os.listdir(path)
    file = []
    dir = []
    for name in files:
        if os.path.isfile(os.path.join(path,name)):
            base,ext = os.path.splitext(name)
            if ext == ".py":
                file.append(base)
        elif os.path.isdir(os.path.join(path,name)):
            if name != "pycache":
                dir.append(name)
    return file,dir

class Reload(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, name = "reload_all"):
        path = os.path.abspath(os.path.dirname(__file__))
        if name == "reload_all":
            cog_file,cog_dir = sort_files(path)
            for file in cog_file:
                file_name = "cog." + file
                await self.bot.reload_extension(file_name)
            await ctx.send("Reloaded", ephemeral=True)
            return
        cog_path = os.path.join(path,f"{name}.py")
        if os.path.isfile(cog_path):
            file_name = "cog." + name
            await self.bot.reload_extension(file_name)
            await ctx.send(f"{name} を再読み込みしました", ephemeral=True)
        else:
            await ctx.send("ホンマなにやってんの？", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Reload(bot),
        #guilds=[discord.Object(id = ID)]
        )
