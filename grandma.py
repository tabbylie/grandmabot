import discord
from discord.ext import commands
from discord import app_commands as appc
import json

with open("config.json", "r") as f:
    data = json.load(f)

MY_GUILD = discord.Object(id=data["GUILD_ID"])




class MyClient(commands.Bot):
    def __init__(self, *, prefix,  intents: discord.Intents, initial_extensions: list[str]):
        super().__init__(command_prefix=prefix, intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.initial_extensions = initial_extensions

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.all()

bot = MyClient(prefix="!>", intents=intents, initial_extensions=['cogs.basic'])
cmds = bot.tree

@cmds.command(name="pingg", description="yes")
async def pingg(interaction: discord.Interaction):
    await interaction.response.send_message("pong! <:GrandmaBlush:1054819990617989240>")

@cmds.command(name="off", description="turns off bot")
async def off(interaction: discord.Interaction):
    if interaction.user.id != 445049757618929664:
        await interaction.response.send_message("Sorry, only <@445049757618929664> can use this command!")
    else:
        await interaction.response.send_message("Success!", ephemeral=True)
        await bot.close()


bot.run(data["token"])
