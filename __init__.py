import os
import six

from logging import warning, info
from codecs import open

from pelican import signals, contents

METADATA_KEY = 'oldurl'


def get_generators(generators):
    return HtaccessGenerator


def register():
    signals.get_generators.connect(get_generators)


class HtaccessGenerator(object):

    def __init__(self, context, settings, path, theme, output_path, *null):
        self.output_path = output_path
        self.context = context
        self.siteurl = settings.get('SITEURL')


    def generate_output(self, writer):
        path = os.path.join(self.output_path, '.htaccess')

        info('writing {0}'.format(path))

        with open(path, 'w', encoding='utf-8') as fd:

            for article in self.context['articles']:
                if METADATA_KEY in article.metadata:
                    oldurl = six.b(article.metadata[METADATA_KEY])
                    newurl = '{0}/{1}'.format( self.siteurl, article.url )
                    info('Emitting rewrite rule for {0} to {1}'.format(oldurl,newurl))
#                    fd.write('Redirect permanent {0} {1}\n'.format(oldurl,newurl))
                    fd.write('rewrite {0} {1} permanent;\n'.format(oldurl,newurl))
