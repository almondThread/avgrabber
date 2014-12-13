import click
from core import core

#def echo(obj):
#    click.echo(str(obj).encode('utf8'))


@click.group()
def app():
    pass

@app.command(short_help='Show goods matched by query')
@click.option('--query', '-q', multiple=True)
def search(query):
    core.multiple_search(query)

if __name__ == '__main__':
    app()