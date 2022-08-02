"""Ansible Galaxy dependencies for lists of collections."""
import logging
import os

from molecule import util
from molecule.dependency.ansible_galaxy.base import AnsibleGalaxyBase

LOG = logging.getLogger(__name__)


class Collections(AnsibleGalaxyBase):
    """Collection-specific Ansible Galaxy dependency handling."""

    FILTER_OPTS = ("role-file", "roles-path")  # type: ignore
    COMMANDS = ("collection", "install")

    @property
    def default_options(self):
        general = super(Collections, self).default_options
        return util.merge_dicts(
            general,
            {
                "requirements-file": os.path.join(
                    self._config.scenario.directory, "collections.yml"
                ),
                "collections-path": os.path.join(
                    self._config.scenario.ephemeral_directory, "collections"
                ),
            },
        )

    @property
    def default_env(self):
        general = super(Collections, self).default_env
        return util.merge_dicts(
            general, {self._config.ansible_collections_path: self.install_path}
        )

    @property
    def install_path(self):
        return self.options["collections-path"]

    @property
    def requirements_file(self):
        return self.options["requirements-file"]
