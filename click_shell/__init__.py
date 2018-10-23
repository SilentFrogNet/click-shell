"""
click-shell

An extension to click that easily turns your click app into a shell utility
"""

from .core import make_click_shell, Shell, add_shell_only_command
from .decorators import shell, shell_only


__all__ = [
    'make_click_shell',
    'shell',
    'Shell',
    'add_shell_only_command',
    'shell_only',
]
