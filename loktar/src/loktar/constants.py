from smart_getenv import getenv
from fabric.api import env

env.disable_known_hosts = True
env.warn_only = True

RUN_DB = {
    "db": getenv("LOKTAR_RUN_DB_DB", type=str, default="loktar_ci"),
    "table": getenv("LOKTAR_RUN_DB_TABLE", type=str, default="run"),
    "host": getenv("LOKTAR_RUN_DB_HOST", type=str, default="elasticsearch"),
    "port": getenv("LOKTAR_RUN_DB_PORT", type=int, default=9200)
}


# DEBIAN PACKAGE INFORMATION
CODE_NAME = getenv("LOKTAR_CODE_NAME", type=str, default="rc")
COMPENANT = getenv("LOKTAR_COMPENANT", type=str, default="main")
DEBIAN_REPOSITORY = getenv("LOKTAR_DEBIAN_REPOSITORY", type=str, default=None)

# About retry on command or http requests ...
MAX_RETRY_PYTHON_UPLOAD = getenv("LOKTAR_MAX_RETRY_PYTHON_UPLOAD", type=int, default=3)
MAX_RETRY_DEBIAN_UPLOAD = getenv("LOKTAR_MAX_RETRY_DEBIAN_UPLOAD", type=int, default=3)
MAX_RETRY_DOCKER_BUILD = getenv("LOKTAR_MAX_RETRY_DOCKER_BUILD", type=int, default=3)
MAX_RETRY_DOCKER_PUSH = getenv("LOKTAR_MAX_RETRY_DOCKER_PUSH", type=int, default=3)
MAX_RETRY_GITHUB = getenv("LOKTAR_MAX_RETRY_GITHUB", type=int, default=3)

CONSUL = getenv("CONSUL_HOST", type=str, default=None)

ARTIFACTORY_INFO = {
    "login": {
        "user": getenv("LOKTAR_ARTIFACTORY_INFO_LOGIN_USER", type=str, default=None),
        "password": getenv("LOKTAR_ARTIFACTORY_INFO_LOGIN_PASSWORD", type=str, default=None)
    }
}

GITHUB_INFO = {
    "login": {
        "user": getenv("LOKTAR_GITHUB_INFO_LOGIN_USER", type=str, default=None),
        "password": getenv("LOKTAR_GITHUB_INFO_LOGIN_PASSWORD", type=str, default=None)
    },
    "organization": getenv("LOKTAR_GITHUB_INFO_ORGANIZATION", type=str, default=None),
    "repository": getenv("LOKTAR_GITHUB_INFO_REPOSITORY", type=str, default=None),
    "notification": {
        "pending": getenv("LOKTAR_GITHUB_INFO_NOTIFICATION_PENDING",
                          type=str,
                          default="The build is running. If i was you I would leave quickly"),
        "success": getenv("LOKTAR_GITHUB_INFO_NOTIFICATION_SUCCESS",
                          type=str,
                          default="The build succeded! You're not so bad after all"),
        "error": getenv("LOKTAR_GITHUB_INFO_NOTIFICATION_ERROR",
                        type=str,
                        default="Error! I won't lie, you're really bad"),
        "failure": getenv("LOKTAR_GITHUB_INFO_NOTIFICATION_FAILLURE",
                          type=str,
                          default="Failure. Nobody is happy."),
        "unknown": getenv("LOKTAR_GITHUB_INFO_NOTIFICATION_UNKNOWN",
                          type=str,
                          default="Unknown state, so 42.")
    },
    "default_master_branch": getenv("LOKTAR_GITHUB_DEFAULT_MASTER_BRANCH", type=str, default="master"),
    "manifest_path": getenv("LOKTAR_GITHUB_MANIFEST_PATH", type=str, default="Manifest")
}
GITHUB_TOKEN = getenv("LOKTAR_GITHUB_TOKEN", type=str, default=None)
GITHUB_API_COMMITS = {
    "url": "https://api.github.com/repos/LOKTAR_/{1}/git/commits".format(GITHUB_INFO["organization"],
                                                                         GITHUB_INFO["repository"]),
    "headers": {
        "Authorization": "token {0}",
        "Accept": getenv("LOKTAR_GITHUB_API_COMMITS_HEADERS_ACCEPT",
                         type=str,
                         default="application/vnd.github-commitcomment.full+json")
    }
}
CONFIG_CI_FILE = getenv("LOKTAR_CONFIG_CI_FILE", type=str, default="config.json")

ROOT_PATH = {
    "jenkins": getenv("LOKTAR_ROOT_PATH_JENKINS", type=str, default="/var/lib/jenkins"),
    "container": getenv("LOKTAR_ROOT_PATH_CONTAINER", type=str, default=None),
    "build": getenv("LOKTAR_ROOT_PATH_BUILD", type=str, default=None)
}

JENKINS = {
    "host": getenv("LOKTAR_JENKINS_HOST", type=str, default=None),
    "user": getenv("LOKTAR_JENKINS_USER", type=str, default=None),
    "password": getenv("LOKTAR_JENKINS_PASSWORD", type=str, default=None)
}

SLAVE_ENVIRONMENT = {
    "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:{0}/.local/bin"
            .format(ROOT_PATH["container"]),
    "env_file": getenv("LOKTAR_SLAVE_ENVIRONMENT_ENV_FILE", type=str, default=None),
    "ssh_image": getenv("LOKTAR_SLAVE_ENVIRONMENT_SSH_IMAGE", type=str, default=None),
}

AWS = {
    "REGION": getenv("LOKTAR_AWS_REGION", type=str, default=None),
    "BUCKET": getenv("LOKTAR_AWS_BUCKET", type=str, default=None)
}

PLUGINS_INFO = {
    "locations": getenv("LOKTAR_PLUGINS_LOCATIONS", type=list, default=[]),
    "workspace": getenv("LOKTAR_PLUGINS_WORKSPACE", type=str, default=None),
    "clean_exit_code": getenv("LOKTAR_PLUGINS_CLEAN_EXIT_CODE", type=bool, default=None)
}

SLACK = {
    "token": getenv("LOKTAR_SLACK_TOKEN", type=str, default=None),
    "channel": getenv("LOKTAR_SLACK_CHANNEL", type=str, default=None)
}

QUAY = {
    "limit": getenv("LOKTAR_QUAY_LIMIT", type=int, default=100)
}

RETRY = {
    "multiplier": getenv("LOKTAR_RETRY_MULTIPLIER", type=float, default=1.5),
    "interval": getenv("LOKTAR_RETRY_INTERVAL", type=float, default=0.5),
    "randomization_factor": getenv("LOKTAR_RETRY_RANDOMIZATION_FACTOR", type=float, default=0.5),
    "max_sleep_time": getenv("LOKTAR_RETRY_MAX_SLEEP_TIME", type=float, default=180)
}

STORAGE_PROXY = {
    "host": getenv("LOKTAR_STORAGE_PROXY_HOST", type=str, default=None),
    "port": getenv("LOKTAR_STORAGE_PROXY_PORT", type=str, default=None)
}

CI = {
    "external_fqdn": getenv("LOKTAR_CI_EXTERNAL_FQDN", type=str, default=None)
}


DEPENDENDY_GRAPH = {
    "repo": getenv("LOKTAR_CI_DEPENDENCY_GRAPH_REPO", type=str, default="/tmp")
}

DETECT_PR_COLLISION = getenv("LOKTAR_DETECT_PR_COLLISION", type=bool, default=False)

GUAY = {
    "host": getenv("LOKTAR_GUAY_HOST", type=str, default=None),
    "timeout": getenv("LOKTAR_GUAY_TIMEOUT", type=int, default=1800)
}
