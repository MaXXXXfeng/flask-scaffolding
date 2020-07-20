import click
import os
import os.path
import sh

HERE = os.path.abspath(os.path.dirname(__file__))


@click.group()
def cli():
    pass


def get_scaffoldings():
    dirs = os.scandir(os.path.join(HERE, 'flask_scaffolding/scaffoldings'))
    names = []
    for entry in dirs:
        if entry.is_dir():
            names.append(entry.name)
    return names


@cli.command()
@click.option('-p', '--path', default='./', help='path of the project you want to create')
@click.argument('project_name')
def create(path, project_name):
    '''create a flask scaffolding '''
    scaffolding = 'basic'
    scaffoldings = get_scaffoldings()
    if scaffolding not in scaffoldings:
        click.echo('%s template not found' % scaffolding, err=True)
        return
    project_dir = os.path.join(path, project_name)
    print('project dir is',project_dir)
    sh.mkdir('-p', project_dir)
    sh.cp('-rf', os.path.join(HERE, f'flask_scaffolding/scaffoldings/{scaffolding}/'), project_dir)
    for f in sh.find(project_dir, '-name', '*.py'):
        sh.sed('-i', '', '-e', 's/%s/%s/g' % ('proj', project_name), f.strip())
    for f in sh.find(project_dir, '-name', 'Dockerfile*'):
        sh.sed('-i', '', '-e', 's/%s/%s/g' % ('proj', project_name), f.strip())
        sh.sed('-i', '', '-e', 's/%s/%s/g' % ('PROJ', project_name.upper()), f.strip())
    sh.mv(os.path.join(project_dir, 'proj'), os.path.join(project_dir, project_name))


@cli.command()
def list():
    '''list all the scaffolding names'''
    scaffolding = get_scaffoldings()
    for t in scaffolding:
        print(t)


if __name__ == '__main__':
    cli()
