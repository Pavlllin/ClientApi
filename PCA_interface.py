import click
from request_client import  PastebinClientApi

@click.command()
@click.option('--login')
@click.option('--passw')
@click.option('--url')
@click.option('--path')
def start(login,passw,url,path):
    api = PastebinClientApi(login, passw, url)
    api.create_note_from_file(path)

if __name__ == '__main__':
    start()