import click
from avgrabber import api

#def print_csv(data_line):
#    d = normalize_data(data_line)
#    order = ('date', 'title', 'price', 'link', 'id')
#    data = [d[x] for x in order]
#    print(', '.join(data))

#def echo(obj):
#    click.echo(str(obj).encode('utf8'))


@click.group()
def app():
    pass

#################### NEW ##########################
@app.group()
def new():
    pass


@new.command(short_help='Create new project')
@click.argument('name', help="Unique project identifier")
@click.argument('query', help="Comma separated query strings. E.g. 'PS4,Playstation,PS3'")
def project(name, query):
    p = api.new_project(name, query)
    if p:
        print("Project %s (query='%s') has been created" % (name, query))
    else:
        print('Error')


#################### LIST ##########################
@app.group()
def list():
    pass

@list.command(short_help='List all projects')
def projects():
    projects = api.list_projects()
    for p in projects:
        print("%s (query=%s)" % (p['name'], p['query']))


@list.command(short_help='List all updates of project')
@click.argument('project', help='Project unique name')
def updates(project):
    updates = api.list_updates(project)
    for u in updates:
        pass


#################### UPDATE ##########################
@app.command(short_help='Load updated data from site')
@click.argument('project', help='Project unique name')
def update(project):
    ads = api.update_project(project)

    for ad in ads:
        placed = ad['placed'].strftime('%d.%m.%Y')
        print(", ".join([placed, ad['title'], str(ad['price']), ad['url']]))


if __name__ == '__main__':
    app()