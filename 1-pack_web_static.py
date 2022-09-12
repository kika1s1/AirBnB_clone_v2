#!/usr/bin/python3
"""
Fabric script generates .tgz archive from contents of web_static directory
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ return archive path if successful """
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(
            cur_time))
        return ("versions/web_static_{}.tgz".format(cur_time))
    except:
        return None
