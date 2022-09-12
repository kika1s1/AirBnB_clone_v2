#!/usr/bin/python3
"""
Fabric script generates .tgz archive from contents of web_static directory
"""

from fabric.api import local, env, run, put
from datetime import datetime
import os


env.hosts = ['54.152.200.18', '54.224.57.104']


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


def do_deploy(archive_path):
    """ return `True` if successful """

    if os.path.exists(archive_path):
        return None
    else:
        return False

    pathname = "/data/web_static"
    filename = os.path.basename(archive_path)
    name = os.path.splitext(filename)

    try:
        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            filename, name))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web/static/releases/{}".format(name))
        run("rm -rf /data/web_static/relases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/releases/{} {}/current".format(pathname, name))
        return True
    except:
        return False


def deploy():
    """ returns value of do_deploy """
    archive = do_pack()
    if archive is True:
        return do_deploy(archive)
    else:
        return False
