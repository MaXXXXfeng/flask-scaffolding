import click
from flask import current_app
from flask.cli import FlaskGroup, run_command

from proj import create_app, config


def create(group):
    app = current_app or create_app()
    group.app = app
    return app


@click.group(cls=FlaskGroup, add_default_commands=False, create_app=create)
def manager():
    pass


manager.add_command(run_command, 'run')
manager.add_command(run_command, 'runserver')
