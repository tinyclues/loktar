import os
import re


def docker_deps(basepath):
    """Get docker image dependencies.

    Args:
        basepath (str): Path to the package

    Returns:
        set: Dependencies names.
    """
    docker_file = os.path.join(basepath, "Dockerfile")
    if os.path.exists(docker_file):
        with open(docker_file, "r") as f:
            dockerfile = f.read()
        re_dockerfile = re.compile("FROM (.+)")
        docker_from_list = re_dockerfile.findall(dockerfile)

        if docker_from_list:
            def map_docker_image(docker_from):
                docker_image_name_tag = docker_from.rsplit("/", 1)[-1]
                return docker_image_name_tag.split(":", 1)[0]

            return {map_docker_image(docker_from) for docker_from in docker_from_list}
    return set()


Plugin = docker_deps
