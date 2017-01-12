# from fabric.api import env
from fabric.api import lcd
from fabric.api import local
from fabric.exceptions import NetworkError
import json
import os
from uuid import uuid4

from loktar.cmd import exec_command_with_retry
from loktar.constants import GITHUB_INFO
from loktar.constants import MAX_RETRY_GITHUB
from loktar.exceptions import PrepareEnvFail
from loktar.log import Log


def prepare_test_env(branch, **kwargs):
    """Prepare the test environment

    Args:
        branch (str): Name of the branch the repository should be checkout to.

    Keyword Args:
        github_organization (str): this is the github organization for get back the repository, default value None.
                                   Also can be set by environment variable LOKTAR_GITHUB_INFO_ORGANIZATION
        github_repository (str): this is the target repository to download, default value None
                                 Also can be set by environment variable LOKTAR_GITHUB_INFO_REPOSITORY

    Raises:
        PrepareEnvFail: Failed to prepare the environment.
    """
    logger = Log()
    unique_name_dir = str(uuid4())
    unique_path_dir = "/tmp/{0}".format(unique_name_dir)
    archive = "{0}.tar.gz".format(unique_name_dir)
    logger.info("Preparing the test environment")

    github_organization = kwargs.get("github_organization", GITHUB_INFO["organization"])
    github_repository = kwargs.get("github_repository", GITHUB_INFO["repository"])

    os.mkdir(unique_path_dir)
    try:
        if not exec_command_with_retry("git clone -b {0} --single-branch git@github.com:{1}/{2}.git {3}"
                                       .format(branch, github_organization, github_repository, unique_path_dir),
                                       0,
                                       MAX_RETRY_GITHUB):
            raise PrepareEnvFail("The git clone can't the repository: {}/{}, check if you have the correct crendentials"
                                 .format(github_organization, github_repository))

        with lcd(unique_path_dir):
            if not exec_command_with_retry("git fetch origin master", 0, MAX_RETRY_GITHUB):
                raise PrepareEnvFail

            if branch != "master":
                if not exec_command_with_retry("git config --global user.email 'you@example.com'", 0, MAX_RETRY_GITHUB):
                    raise PrepareEnvFail

                if not exec_command_with_retry("git config --global user.name 'Your Name'", 0, MAX_RETRY_GITHUB):
                    raise PrepareEnvFail

                if not exec_command_with_retry("git merge --no-ff --no-edit FETCH_HEAD", 0, MAX_RETRY_GITHUB):
                    raise PrepareEnvFail

                local("rm -rf {0}/.git".format(unique_path_dir))

        with lcd("/tmp"):
            if not exec_command_with_retry("tar -czf {0} {1}".format(archive, unique_name_dir), 0, MAX_RETRY_GITHUB):
                raise PrepareEnvFail

        logger.info("The test env is ready!")

    except NetworkError as exc:
        logger.error(exc)
        raise
    except PrepareEnvFail:
        local("rm -rf {0}*".format(unique_path_dir))
        raise

    return "/tmp/{0}".format(archive)


def get_config(package_name, test_env_path, full=False):
    """Retrieve the test configuration

    Args:
        package_name: Name of the package for which to apply ``full=False``
        test_env_path: the location of the cloned test environment.
        full (boolean): See ``Returns`` section

    Returns:
        if ``full`` True, return the complete config.json file.
        Otherwise, return a dict with keys: ``['artifact_name', 'artifact_type', 'test_type']``
    """
    pkg_config = {}
    logger = Log()

    with lcd('{0}'.format(test_env_path)):
        config = json.loads(local('cat config.json', capture=True))

    logger.info('Parsing configuration')
    if not full:
        for package in config['packages']:
            if package['artifact_name'] == package_name:
                pkg_config = package
                break
    else:
        pkg_config = config

    logger.info('Conf is ok and has keys {0}'.format(pkg_config.keys()))
    return pkg_config
