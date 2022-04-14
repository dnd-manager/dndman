from invoke import task

@task
def debug(ctx):
    from dndman import app
    from dndman.utils.event import Event

    comm_event = Event()

    app.create_event(comm_event)
    app.run("localhost", 8000, debug=True)


@task
def sass(ctx):
    ctx.run(
        "sass ./dndman/static/styles/style.scss ./dndman/static/styles/style.css --watch"
    )
