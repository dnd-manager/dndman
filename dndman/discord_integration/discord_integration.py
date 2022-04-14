from threading import Thread
from typing import Any, Callable, Iterable, Mapping
import lightbulb

from dotenv import load_dotenv
from os import getenv

from hikari import GuildChannel, GuildTextChannel
from lightbulb import BotApp

from dndman.utils.event import Event

class DnDManBotApp(BotApp):
    def create_event(self, event: Event):
        self.event = event

    def add_event_listener(self, event_id: str, listener):
        self.event.add_listener(event_id, listener)

    def invoke_event(self, event_id: str, *argv):
        self.event.invoke(event_id, argv)

output_channel: GuildTextChannel = None

load_dotenv()
bot_app = DnDManBotApp(token=getenv("BOT_TOKEN"), default_enabled_guilds=(901223088195244072))

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

class DiscordBotThread(Thread):
    def __init__(self, group: None = None, target: Callable[..., Any] | None = ..., name: str | None = ..., args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = ..., *, daemon: bool | None = ..., comm_event: Event) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.comm_event = comm_event

    def run(self):
        async def send_message(*argv):
            print("hallo 2")
            if output_channel is not None:
                print ("hallo 3")
                await output_channel.send(argv)

        bot_app.create_event(self.comm_event)
        bot_app.add_event_listener("send_msg", send_message)
        bot_app.run()
        return super().run()