from invoke import task

@task
def push(ctx):
	ctx.run("git push && git push heroku")

@task
def run(ctx):
	ctx.run("python app.py")

@task
def setPath():
	import os, inspect, sys
	cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
	if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)