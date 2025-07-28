"""Password Management Commands for API Library"""

import sys
import click
from .auth import PasswordManager

def setup_password_command():
    """Entry point for setuppassword command."""
    password_manager = PasswordManager()
    
    if not password_manager.is_first_time_user():
        click.echo("Nah Nope password already Exists")
        sys.exit(1)
    
    success, message = password_manager.setup_password()
    
    if success:
        click.echo(f"✅ {message}")
    else:
        click.echo(f"❌ {message}")
        sys.exit(1)

def check_auth_status_command():
    """Entry point for checkauth command."""
    password_manager = PasswordManager()
    
    if password_manager.is_first_time_user():
        click.echo("Setup a password first dude use command 'setuppassword'")
    else:
        click.echo("Naish password is set")
        click.echo("Rememebr the pass you cant change it again once gone 'BOOM' all gone.")