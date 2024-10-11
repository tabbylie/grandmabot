import discord
from discord.ext import commands
from discord import app_commands as appc
import random
import json

class events(commands.Cog, name='basic'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def please(self):
        game = discord.Game("Grandma loves you")
        await self.bot.change_presence(status=discord.Status.idle, activity=game)
        print("GrandmaBot booted successfully!")

    @commands.Cog.listener("on_message")
    async def grandma(self, message: discord.Message):
        if message.author.id == 1200496974282113024:
            return
        
        with (open("words_emojis.json")) as f:
            data = json.load(f)
        
        
        emojiIDList = data["emojiIDList"]

        grandmaYes = data["grandmaWords"]

        def remove_punctuation(test_str):
            # Using filter() and lambda function to filter out punctuation characters
            result = ''.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), test_str))
            return result
        
        messaged = remove_punctuation(message.content)
        messaged = messaged.lower()
        for i in grandmaYes:
            if i in messaged:
                await message.channel.send(random.choice(emojiIDList))
                return        

    def check_if_me(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 720010567309328465 or interaction.user.id == 445049757618929664

    @appc.command(name="add", description="Adds emojis/words!")
    @appc.describe(toAdd="Emoji or Word?", emoji="The emoji to add!", word="The Word to add!")
    @appc.choices(toAdd=[
        appc.Choice(name="Emoji", value="emoji"),
        appc.Choice(name="Word", value="word")
    ])
    @appc.rename(toAdd="type")
    @appc.check(check_if_me)
    async def add(self, interaction: discord.Interaction, toAdd: appc.Choice[str], emoji: str="default", word: str="default"):
        if (toAdd.value == "emoji"):
            if (emoji != "default"):
                with open("words_emojis.json") as f:
                    data = json.load(f)
                emojis = data["emojiIDList"]
                emojis.append(emoji)
                data["emojiIDList"] = emojis
                with open("words_emojis.json", "w") as f:
                    json.dump(data, f, indent=4)
                await interaction.response.send_message("Success!! Should be added now! Meow!")
            else:
                await interaction.response.send_message("You must give an emoji first! Try /add type:emoji, emoji:[the emoji to add]")
        elif (toAdd.value == "word"):
            if (word != "default"):
                with open("words_emojis.json") as f:
                    data = json.load(f)
                words = data["grandmaWords"]
                words.append(word.lower())
                data["grandmaWords"] = words
                with open("words_emojis.json", "w") as f:
                    json.dump(data, f, indent=4)
                await interaction.response.send_message("Success!! Should be added now! Meow!")
            else:
                await interaction.response.send_message("You must give a word first! Try /add type:word word:[the word to add]")
        else:
            await interaction.response.send_message("Incorrect type! Sorry!")

async def setup(bot):
    await bot.add_cog(events(bot))

