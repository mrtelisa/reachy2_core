#!/usr/bin/env python
"""Setup config file."""
from glob import glob
from os import path

from setuptools import find_packages, setup

package_name = "reachy_config"

data_files = [
    ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
    ("share/" + package_name, ["package.xml"]),
    ("share/" + package_name + "/config/default", glob("config/default/*.yaml")),
    ("share/" + package_name + "/config/fake", glob("config/fake/*.yaml")),
    ("share/" + package_name + "/config/schema", glob("config/schema/*.yaml")),
]

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=data_files,
    install_requires=[
        "PyYAML",
    ],
    extras_require={
        "doc": ["sphinx"],
    },
    entry_points={  # setup entrypoint config cheker to launch reachy_config.py
        "console_scripts": [
            "reachy_config = reachy_config.reachy_config:config_check",
        ],
    },
    maintainer="Pollen Robotics",
    maintainer_email="contact@pollen-robotics.com",
    description="Config parser for Reachy2.",
    license="Apache-2.0",
)
