import click
from wrapper import TerraformWrapper

@click.group()
def cli():
    pass

@cli.command()
def generate():
    terraform_wrapper = TerraformWrapper()
    terraform_wrapper.generate_terraform()

@cli.command()
def apply():
    terraform_wrapper = TerraformWrapper()
    terraform_wrapper.apply()

if __name__ == "__main__":
    cli()
