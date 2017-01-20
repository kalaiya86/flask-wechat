#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-18 16:25:22
# @Author  : Kelly (weiqin.wang_c@chinapnr.com)
# @Link    : ${link}
# @Version : $Id$

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO


api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print ('Current database version:' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))