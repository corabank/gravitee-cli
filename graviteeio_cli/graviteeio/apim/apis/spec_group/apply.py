import click
from graviteeio_cli.exeptions import GraviteeioError

@click.command()
@click.argument('api_id', required=False, metavar='[API ID]')
@click.option('--file', '-f', type=click.Path(exists=True), required=False,
              help="Spec file")
@click.option('--set', '-s', multiple=True,
              help="Overload the value(s) of value file eg: `--set proxy.groups[0].name=mynewtest`")
@click.option('--debug', '-d', is_flag=True,
              help="Do not perform any changes. Show the datas genereted")
@click.option('--config-path', type=click.Path(exists=True), required=False, default="./",
              help="Config folder")
@click.pass_obj
def apply(obj, api_id, file, set, debug, config_path):
    """
    This command allow to create/update an API from spec API like Swagger or OpenApiSpec (OAS)
    """
    api_client = obj['api_client']

    try:
        with open(file, 'r') as f:
            api_spec = f.read()
    except FileNotFoundError:
        raise GraviteeioError("Missing values file {}".format(file))

    if api_id:
        resp = api_client.update_oas(api_id, api_spec)
        click.echo("API {} is updated".format(api_id))
    else:
        click.echo("Start Create")
        resp = api_client.create_oas(api_spec)
        click.echo("API has been created with id {}".format(resp["id"]))

    pass