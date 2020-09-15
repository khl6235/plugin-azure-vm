from schematics import Model
from schematics.types import StringType


class OS(Model):
    os_distro = StringType()
    os_arch = StringType(default='x86')
    os_details = StringType()