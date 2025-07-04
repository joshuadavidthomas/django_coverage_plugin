# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/django_coverage_plugin/blob/master/NOTICE.txt

"""Django Template Coverage Plugin"""

__version__ = "3.1.1"

from .plugin import DjangoTemplatePluginException  # noqa
from .plugin import DjangoTemplatePlugin


def coverage_init(reg, options):
    plugin = DjangoTemplatePlugin(options)
    reg.add_file_tracer(plugin)
    reg.add_configurer(plugin)
