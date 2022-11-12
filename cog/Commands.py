import gspread
import discord
from discord import app_commands
from discord.ext import commands
from json_module import *
from manager import manage_serverid, manage_key, manage_sheetid
from mk8dx import data
from oauth2client.service_account import ServiceAccountCredentials 


#ID = int(manage_serverid())
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(manage_key(), scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = manage_sheetid()
ws = gc.open_by_key(SPREADSHEET_KEY).sheet1

dict = data._ALL_TRACK_DICT
track_list = []
loop = 0
track_dict2list = list(dict.values())

for track_enum in track_dict2list:
    if len(track_list) == 0:
        track_list.append(track_enum)
        loop += 1
        continue
    elif track_enum != track_list[loop - 1]:
        track_list.append(track_enum)
        loop += 1

class Commands(commands.Cog):

    @app_commands.command(
    name = "nita_save",
    description = "記録の登録"
        )
    async def nita_save(
        self,
        interaction :discord.Interaction,
        track :str,
        result :str ) -> None:
        global track_list
        if str.isdigit(track) == True:
            if int(track) <= len(track_list):
                track_enum = track_list[int(track) - 1]
            else:
                await interaction.response.send_message("コースの指定に間違いがあります")
                return
        else:
            track_enum = data.Track.from_nick(track)
            if track_enum == None:
                await interaction.response.send_message("コースの指定に間違いがあります")
                return
        track_name = track_enum.full_name_ja

        if str.isdigit(result) == True:
            if len(result) == 6:
                result_sprit = f"{result[0:1]}:{result[1:3]}.{result[3:6]}"
            elif result == "343351520877608960":
                await interaction.response.send_message("😉😉😉😉😉😉")
                return
            elif result == "851845432871354408":
                await interaction.response.send_message("🐼🌸🐼🌸🐼🌸")
                return
            else:
                await interaction.response.send_message("タイムの指定に間違いがあります")
                return
        else:
            await interaction.response.send_message("タイムの指定に間違いがあります")
            return

        userid_list = ws.row_values(2)
        userid = interaction.user.id
        user_name = interaction.user.name
        track_id = track_list.index(track_enum)
        track_row = int(track_id) + 3
        result = f"{result[0:3]}.{result[3:6]}"

        if str(userid) in userid_list:
            users_col = userid_list.index(str(userid)) + 1
            ws.update_cell(track_row,users_col, result)
            ws.update_cell(1,users_col, user_name)
        else:
            ws.update_cell(1,int(len(userid_list)) + 1, user_name)
            ws.update_cell(2,int(len(userid_list)) + 1, str(userid))
            ws.update_cell(track_row, int(len(userid_list)) + 1, result)

        await interaction.response.send_message(f"以下のコースとタイムを記録しました\n```{track_name} : {result_sprit} ({interaction.user})```")
        return

    @app_commands.command(
    name = "nita_delete",
    description = "記録の削除"
        )
    async def nita_delete(
        self,
        interaction :discord.Interaction,
        track :str) -> None:
        global track_list
        if str.isdigit(track) == True:
            if int(track) <= len(track_list):
                track_enum = track_list[int(track) - 1]
            else:
                await interaction.response.send_message("コースの指定に間違いがあります")
                return
        else:
            track_enum = data.Track.from_nick(track)
            if track_enum == None:
                await interaction.response.send_message("コースの指定に間違いがあります")
                return
        track_name = track_enum.full_name_ja

        userid_list = ws.row_values(2)
        userid = interaction.user.id
        user_name = interaction.user.name
        track_id = track_list.index(track_enum)
        track_row = int(track_id) + 3

        if str(userid) in userid_list:
            users_col = userid_list.index(str(userid)) + 1
            pre_result = ws.cell(track_row,users_col).value
            if pre_result == None:
                await interaction.response.send_message("記録が登録されていません")
                return
            result_sprit = f"{pre_result[0:1]}:{pre_result[1:3]}.{pre_result[3:6]}"
            ws.update_cell(track_row,users_col, "")
            ws.update_cell(1,users_col, user_name)
        else:
            await interaction.response.send_message("ユーザーが登録されていません")
            return

        await interaction.response.send_message(f"以下のコースとタイムを削除しました\n~~```{track_name} : {result_sprit} ({interaction.user})```~~")
        return

    @app_commands.command(
    name = "nita_help",
    description = "helpコマンド"
        )
    async def nita_help(
        self,
        interaction :discord.Interaction) -> None:

        await interaction.response.send_message("--本botの使い方--\n・登録\n/nita_save track result\n例 :``` /nita_save DKJ 200000 ```(自分のDKJが2:00.000の場合)\n\n・削除\n/nita_delete track\n(例 :``` /nita_delete DKJ)```\n\n・記録はここから見れます\nhttps://docs.google.com/spreadsheets/d/1sVFF_JeOHCpBR93iE3IvQfq2u2TgE3pVgU1QkSSLIjA/edit?usp=sharing\ntrackによるコース指定は即時のSheat Botと同様で、resultには必ず記号なしの6桁でタイムを入力してください")
        return

def shard(bot: commands.AutoShardedBot):
    count = bot.shard_count
    for i in range(count):
        info = bot.get_shard(i)
        close = info.latency
        print(str(close))

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Commands(bot),
        #guilds=[discord.Object(id = ID)]
        )
