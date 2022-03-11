from invoke import task


@task
def debug(ctx):
    from dndman import app

    app.run("localhost", 8000, debug=True)


@task
def sass(ctx):
    ctx.run(
        "sass ./dndman/static/styles/style.scss ./dndman/static/styles/style.css --watch"
    )
