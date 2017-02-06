from fabric.api import cd
from fabric.api import local
from fabric.api import lcd
from fabric.api import get
from fabric.api import put
from fabric.api import run
from fabric.api import settings

from loktar.log import Log

logger = Log()


def exec_command_with_retry(cmd, remote, max_retry):
    """Execute and retry a command"""
    with settings(warn_only=True):
        id_try = 0
        launch = local if remote == 0 else run
        while id_try < max_retry:
            result = launch(cmd)
            if result.succeeded:
                return True
            else:
                id_try += 1

        logger.error("The command : {0} failed after {1} retries".format(cmd, max_retry))
        return False


def exe(cmd, remote=True):
    """Execute a command

    Args:
        cmd (str): Command to execute
        remote (bool): Give the context execution remote (True) or local (False)

    Returns:
        bool: True if everything went well, False otherwise
    """
    launch = run if remote else local
    with settings(warn_only=True):
        result = launch(cmd)
        if result.failed:
            logger.error(result)
            return False
        return True


def cwd(path, remote=True):
    mv = lcd if remote is False else cd
    return mv(path)


def transfer_file(action, remote_path=None, local_path=None):
    if remote_path is not None and local_path is not None:
        if action == "GET":
            rc = get(remote_path, local_path)
        elif action == "PUSH":
            try:
                rc = put(local_path, remote_path)
            except ValueError:
                logger.error("Maybe a test in another job failed, so the tar was deleted or a network problem.")
        else:
            logger.info("Action : {0} unknown".format(action))
            return False
    else:
        logger.error("remote_path and local_path have to be set")
        return False

    if rc.failed:
        logger.error(rc)
        return False

    logger.info("File transfile is finished")
    return True
