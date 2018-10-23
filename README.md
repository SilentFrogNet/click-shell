[![GitHub tag](https://img.shields.io/github/tag/SilentFrogNet/click-shell.svg?label=version)](https://github.com/SilentFrogNet/click-shell/releases)
[![GitHub issues](https://img.shields.io/github/issues/SilentFrogNet/click-shell.svg?colorB=yellow)](https://github.com/SilentFrogNet/click-shell/issues)


# click-shell

This is a enhanced version of click-shell. 
In particular it adds the function `add_shell_only_command` that allow to add a command to the shell that is hidden in the command called with parameters.

click-shell is an extension to [click](http://click.pocoo.org/) that easily turns your click app into a shell utility.
It is built on top of the built in python [cmd](https://docs.python.org/2/library/cmd.html) module, with modifications to make it work with click.


## Installation

From git

`pip install git+git://github.com/SilentFrogNet/click-shell.git`


## Features

* Adds a "shell" mode **with command completion** to any click app
* Just a one line change for most click apps


## Usage

Simply replace `@click.group` with `@click_shell.shell` on the root level command:


```python
from click_shell import shell

# @click.group()  # no longer
@shell(prompt='my-app > ', intro='Starting my app...')
def my_app():
    pass

@my_app.command()
def the_command():
    print 'the_command is running'
    
...
```

When run, you should expect an output like so:

```bash
$ python my_app.py
Starting my app...
my-app > 
```


### Note

It should be noted that this decorator **only** alters functionality if no arguments are
passed on the command line.  If you try to run a command directly
(like ``python my_app.py the_command`` in the above example), your app will function
identically to how it did before.


For more advanced usage, check out our docs at http://click-shell.readthedocs.org/
