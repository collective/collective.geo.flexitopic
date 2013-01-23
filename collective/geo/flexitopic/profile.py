from zope.interface import implements

from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as INonQ
from collective.geo.flexitopic import DEPENDENCIES


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        _dependencies = ['%s:default' % item for item in DEPENDENCIES]
        return _dependencies


class HiddenProducts(object):
    implements(INonQ)

    def getNonInstallableProducts(self):
        return DEPENDENCIES
