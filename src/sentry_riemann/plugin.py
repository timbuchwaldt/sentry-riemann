# coding: utf-8
"""
sentry_riemann.plugin
"""
import riemann_client.client
from riemann_client.transport import UDPTransport

from sentry.plugins import Plugin

import sentry_riemann
from sentry_riemann.forms import RiemannOptionsForm


class RiemannPlugin(Plugin):
    """
    Sentry plugin to send errors stats to StatsD.
    """
    author = 'Tim Buchwaldt'
    author_url = 'https://github.com/timbuchwaldt/sentry-riemann'
    version = sentry_riemann.VERSION
    description = 'Send errors stats to Riemann.'
    slug = 'riemann'
    title = 'Riemann'
    conf_key = slug
    conf_title = title
    resource_links = [
        ('Source', 'https://github.com/timbuchwaldt/sentry-riemann'),
        ('Bug Tracker', 'https://github.com/timbuchwaldt/sentry-riemann/issues'),
        ('README', 'https://github.com/timbuchwaldt/sentry-riemann/blob/master/README.rst'),
    ]
    project_conf_form = RiemannOptionsForm

    def is_configured(self, project, **kwargs):
        """
        Check if plugin is configured.
        """
        params = self.get_option
        return bool(params('host', project) and params('port', project))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        host = self.get_option('host', group.project)
        port = self.get_option('port', group.project)
        prefix = self.get_option('prefix', group.project)
        track_only_new = self.get_option('track_only_new', group.project)

        metric = []
        metric.append(group.project.slug.replace('-', '_'))
        metric.append(group.get_level_display())


        with riemann_client.client.Client(UDPTransport(host, port)) as client:
            if not track_only_new or (is_new and track_only_new):
                client.event(service='_'.join(metric), state='error', host=event.server_name)
