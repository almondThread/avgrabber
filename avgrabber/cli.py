import click
from avgrabber import api
from avgrabber.grabber.utils import normalize_data

def print_csv(data_line):
    d = normalize_data(data_line)
    order = ('date', 'title', 'price', 'link', 'id')
    data = [d[x] for x in order]
    print(', '.join(data))

#def echo(obj):
#    click.echo(str(obj).encode('utf8'))


@click.group()
def app():
    pass

@app.command(short_help='Show goods matched by query')
@click.option('--query', '-q', multiple=True)
def search(query):
    ads = api.search(query)

    for ad in ads:
        placed = ad['placed'].strftime('%d.%m.%Y')
        print(", ".join([placed, ad['title'], str(ad['price']), ad['url']]))

if __name__ == '__main__':
    app()