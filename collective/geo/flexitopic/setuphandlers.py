import logging
from Products.CMFCore.utils import getToolByName
# The profile id of your package:
PROFILE_ID = 'profile-collective.geo.flexitopic:default'


def do_nothing(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('collective.geo.flexitopic')
        logger.info("Empty upgrade step")

def add_ng_collection(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('collective.geo.flexitopic')
    logger.info("Add typeinfo for new style collections")
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'typeinfo')


def import_various(context):
    """Import step for configuration that is not handled in xml files.
    """
    # Only run step if a flag file is present
    if context.readDataFile('collective.geo.flexitopic-default.txt') is None:
        return
    logger = context.getLogger('collective.geo.flexitopic')
    site = context.getSite()
    pass
