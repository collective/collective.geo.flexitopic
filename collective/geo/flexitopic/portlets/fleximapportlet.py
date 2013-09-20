from zope.interface import Interface
from zope.interface import implements

from collective.flexitopic.portlets import flexitopicportlet as base
#from plone.portlets.interfaces import IPortletDataProvider

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from collective.geo.flexitopic import flexitopicMessageFactory as _

from zope.i18nmessageid import MessageFactory
__ = MessageFactory("plone")

class IFlexiMapPortlet(base.IFlexiTopicPortlet):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    show_table = schema.Bool(title=_(u"Show table"),
                description=_(u"Uncheck if you want to hide the resultstable"),
                required=False,
                default=True,
                )
    show_form = schema.Bool(title=_("Show search form"),
                description=_(u"Uncheck if you want to hide the searchform"),
                required=False,
                default=True,
                )

class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IFlexiMapPortlet)
    show_table = True
    show_form = True

    def __init__(self, header=u"", target_collection=None, limit=None,
                 show_more=True, omit_border=False,
                 flexitopic_width=None, flexitopic_height=None,
                 show_table = True, show_form = True):
        super(Assignment, self).__init__(header=u"",
                target_collection=None, limit=None,
                show_more=True, omit_border=False,
                flexitopic_width=None, flexitopic_height=None)
        self.show_table = show_table
        self.show_form = show_form

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return __(u"Flexitopic map portlet")


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IFlexiMapPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget

    label = _(u"Add Flexitopic Portlet")
    description = _(u""" You can search the collection and the map
                    with the fields you provided in the topic criteria.
                    """)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IFlexiMapPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget

    label=_(u"Edit FlexiTopic Map Portlet")
    description = _(u""" You can search the collection and the map
                    with the fields you provided in the topic criteria.
                    """)
