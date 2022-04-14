import lightbulb

from dotenv import load_dotenv
from os import getenv

from hikari import GuildChannel, GuildTextChannel
from lightbulb import BotApp

output_channel: GuildTextChannel = None

load_dotenv()
bot_app = BotApp(token=getenv("BOT_TOKEN"), default_enabled_guilds=(901223088195244072))

@bot_app.command
@lightbulb.option("channel", "Channel", type=GuildChannel)
@lightbulb.command("set_channel", "Set channel for output information")
@lightbulb.implements(lightbulb.SlashCommand)
async def set_channel(ctx: lightbulb.Context):
    guild = ctx.get_guild()
    if guild is not None:
        channel = guild.get_channel(ctx.options.channel)
        if isinstance(channel, GuildTextChannel):
            output_channel = channel
            await ctx.respond("Setup successful!")
        else:
            await ctx.respond("Channel given is not a text chanenl!")

if __name__ == "__main__":
    bot_app.run()

async def send_message(message: str):
    print("hallo 2")
    if output_channel is not None:
        print ("hallo 3")
        await output_channel.send(message)