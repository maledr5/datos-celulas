from invoke import task

@task
def push(ctx):
	ctx.run("git push && git push heroku")

@task
def run(ctx):
	ctx.run("python app.py")
