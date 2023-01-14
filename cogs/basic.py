import discord
from discord.ext import commands
from discord import app_commands as appc
import random

class events(commands.Cog, name='basic'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def please(self):
        game = discord.Game("Grandma loves you")
        await self.bot.change_presence(status=discord.Status.idle, activity=game)
        print("GrandmaBot booted successfully!")
    
    @commands.Cog.listener("on_message")
    async def uhYes(self, message: discord.Message):
        if (message.author.id == 1063865095710588967):
            return
        
        messageContent = message.content.lower()
        channel = message.channel
        
        grandmaYes = [
            "gammy",
            "gams",
            "gramma",
            "grammy",
            "grandma",
            "grams",
            "grandmaw",
            "grandmama",
            "nana",
            "meemaw",
            "mimi",
            "grandmom",
            "grannie",
            "granny",
            "gran",
            "mammy",
            "babushka",
            "grandmother",
            "madear",
            "oma"
        ]

        emojiIDList = [
            "<:GrandmaBlush:1054819990617989240>",
            "<:GrandmaBruh:1054815826366177300>",
            "<:GrandmaClose:1054821412919070812>",
            "<:GrandmaPeek:1054815878241325078>",
            "<:GrandmaScrunkly:1062559680532058463>",
            "<:GrandmaSleep:1054826793703579698>",
            "<:GrandmaStare:1054824842609827950>",
            "<:GrandmaYell:1054818627477577808>",
            "<:mgStormy:860562519302078494>"
        ]


        flag=False
        messageContentArray = messageContent.split(" ")
        for i in messageContentArray:
            if i in grandmaYes:
                flag=True
                break
        
        if (flag):
            emoji = random.choice(emojiIDList)
            await channel.send(emoji)
    
async def setup(bot):
    await bot.add_cog(events(bot))
