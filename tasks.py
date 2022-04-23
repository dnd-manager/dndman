import time
from invoke import task

@task
def main(ctx):
    from dndman.utils.event import Event
    from dndman.app import FlaskWebThread
    
    comm_event = Event()
    
    webThread = FlaskWebThread(comm_event=comm_event)
    webThread.start()

    time.sleep(1)
    
    from dndman.discord_integration.discord_integration import DiscordBotThread

    botThread = DiscordBotThread(comm_event=comm_event)
    botThread.start()

    # keep main thread running
    while True:
        pass


@task
def debug(ctx):
    from dndman.utils.event import Event
    comm_event = Event()
    # create seperate thread for bot
    from dndman.discord_integration.discord_integration import DiscordBotThread
    botThread = DiscordBotThread(comm_event=comm_event)
    botThread.start()

    # run flask on the main thread
    from dndman.app import app
    app.create_event(comm_event)
    app.run("localhost", 8000, debug=True)


@task
def sass(ctx):
    ctx.run(
        "sass ./dndman/static/styles/style.scss ./dndman/static/styles/style.css --watch"
    )
