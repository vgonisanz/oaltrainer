import typer

from oaltrainer.core import Core

def main():
	core = Core()
	core.run("resources/ak-47_fire-01.wav")

if __name__ == "__main__":
	typer.run(main)
