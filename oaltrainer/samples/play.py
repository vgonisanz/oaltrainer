import typer

from oaltrainer.core import Core

def main():
	core = Core()
	core.run()

if __name__ == "__main__":
	typer.run(main)
