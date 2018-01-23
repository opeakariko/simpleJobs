# -*- coding: utf-8 -*-

import sys
from simple import app
app.ready()

def main():
    try:
        args = sys.argv
        job_name = args.pop(1)
        mod_name = 'simple.jobs.%s' % job_name
        mod = __import__(mod_name, fromlist=['*'])
        mod.run(*sys.argv[1:])
        return 0

    except Exception:
        raise

if __name__ == '__main__':
    with app.app_context():
        sys.exit(main())
