"""Utility module to help with common scripting needs."""

import sys


DEFAULT_PROMPT = 'This script may modify the database. Proceed? (yes/no): '


def require_db_write_acknowledgement(prompt=DEFAULT_PROMPT):
    """
    Require acknowledgement to modify the database.

    Inform the command line user that proceeding will modify the database,
    and require typed acknowledgement to proceed.
    """
    proceed = False

    while not proceed:
        sys.stdout.write(prompt)
        response = raw_input()
        if response == 'no':
            sys.stdout.write('Okay. Goodbye!\n')
            sys.exit(0)
        elif response != 'yes':
            sys.stdout.write('Please try again, '
                             'responding "yes" or "no"\n')
            continue
        else:
            proceed = True

    return
