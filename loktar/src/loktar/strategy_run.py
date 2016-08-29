from loktar.environment import PLUGINS_INFO
from loktar.exceptions import CIBuildPackageFail
from loktar.exceptions import CITestFail
from loktar.exceptions import ImportPluginError
from loktar.log import Log
from loktar.plugin import find_plugin

ACCEPT_RUN_TYPE = ["test", "artifact", ]


def strategy_runner(package, run_type, remote=False):
    """Run the packaging functions

        Args:
            package (dict): package_config
            run_type (str): Represent the strategy to run on a package (test or artifact)
            remote (bool): Represent if the plugin is executed in remote or not, default value: False

        Raises:
            CITestFail: some error occurred during the test
            CITestUnknown: wrong value for config['test_type']
            CIBuildPackageFail: some error occurred during a packaging
            ImportPluginError: Fail to find / import a plugin
    """

    logger = Log()

    if run_type not in ACCEPT_RUN_TYPE:
        raise ValueError("run_type must be equal to 'test' or 'artifact', actual value: {0}".format(run_type))

    elif run_type == "test" and package["test_type"] == "no-test":
        logger.info("Tag no-test detected, skip test")
        return {}
    else:
        params = {"type": "test_type", "exception": CITestFail}\
            if run_type == "test" else {"type": "pkg_type", "exception": CIBuildPackageFail}

        plugins_location = PLUGINS_INFO["locations"].split(",") \
            if type(PLUGINS_INFO["locations"]) is str else PLUGINS_INFO["locations"]

        try:
            runner = find_plugin(package[params["type"]], run_type, plugins_location, PLUGINS_INFO["workspace"])
            logger.info("The plugin {} is loaded".format(package[params["type"]]))
        except ImportPluginError:
            raise

        logger.info("Starting {} plugin ...".format(package[params["type"]]))

        try:
            return runner.run(package, remote)
        except Exception as e:
            logger.error(str(e))
            raise params["exception"](str(e))
