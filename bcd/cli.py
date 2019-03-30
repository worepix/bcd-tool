import click
import os
import sys

@click.group()
@click.pass_context
def cli(some=None):
    pass

@cli.command("rename", help="Rename files in actual folder to proper naming")
@click.option("--category", "-c", help="Category name in documentation")
@click.option("--article", "-a", help="Article name in documentation")
def rename(category, article):
    if category == None:
        category = input("Enter article category name:\n")

    if article == None:
        article = input("Enter article name:\n")

    actual_dir = os.listdir(os.getcwd())

    for file in actual_dir:
        os.rename(file, "_{0}_{1}_{2}".format(category, article, file))



def main():
    '''Application entry point.'''
    try:
        cli(),
    except KeyboardInterrupt:
        pass
    except Exception as e:
        click.echo(str(e), err=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
