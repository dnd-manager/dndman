from invoke import task

@task
def debug(ctx):
    from dndman.utils.event import Event
    from dndman.app import app
    # from dndman.discord_integration.discord_integration import DiscordBotThread
    
    comm_event = Event()
    
    # create seperate thread for bot
    # botThread = DiscordBotThread(comm_event=comm_event)
    # botThread.start()

    # run flask on the main thread
    app.create_event(comm_event)
    app.run("localhost", 8000, debug=True)

@task
def sass(ctx):
    ctx.run(
        "sass ./dndman/static/styles/style.scss ./dndman/static/styles/style.css --watch"
    )
