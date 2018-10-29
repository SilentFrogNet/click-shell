"""
click_shell.decorators

Decorators to make using click_shell simpler and more similar to click.
"""

import click

from .core import Shell, add_shell_only_command


def shell(name=None, **attrs):
    """Creates a new :class:`Shell` with a function as callback.  This
    works otherwise the same as :func:`command` just that the `cls`
    parameter is set to :class:`Shell`.
    """
    attrs.setdefault('cls', Shell)
    return click.command(name, **attrs)


# def shell_only(cmd=None, **attrs):
#     # TODO: not working! :(
#     shell = attrs.get('shell', None)
#     name = attrs.get('name', None)
#     def decorator(f):
#         if shell:
#             add_shell_only_command(shell, f, name=name)
#         return cmd
#     return decorator