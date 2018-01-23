# -*- coding: utf-8 -*-

import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Application(Flask):
    def __init__(self):
        super(Application, self).__init__(
            __name__, static_folder='../static'
        )

        # 生产环境配置
        if 'APP_CONFIG' in os.environ:
            self.config.from_envvar('APP_CONFIG', silent=False)
        else:
            dev_cfg = os.path.abspath(os.path.join(
                os.path.basename(__file__), '../dev.cfg'))
            self.config.from_pyfile(dev_cfg, silent=True)

    def setup_logger(self):
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '[%(asctime)s %(levelname)-8s %(module)s:%(lineno)d <%(process)d>]'
            ' %(message)s'))
        handler.setLevel(logging.INFO)
        app.logger.setLevel(logging.INFO)
        app.logger.addHandler(handler)

    def ready(self):
        db.init_app(self)

        self.setup_logger()

app = Application()
