Introduction
============

Use collective.geo.flexitopic to easily build interactive maps out of plone
collections. It combines Plone maps (collective.geo_) with collective.flexitopic_.


collective.flexitopic
=====================

Flexitopic integrates the easy use of Plone collections with a Flexigrid_
AJAX view. The criteria from the topic are taken to construct a simple
query form to narrow down a search inside a collection.
For old style collections subtopics are displayed inside tabs of the collection.

* Flexitopic does not install a new content type but just adds an
  additional view to the collection type.
* it degrades for non Javascript browsers to a simple table - (almost)
  same usability, no information loss.
* it requires JQuery only (built into Plone 4) no JQueryUI
* lightweight JS
      * Flexigrid_: 24 KB packed
      * JSlider_: 15 KB packed

Usage
-----

Add a collection. The Criteria of the collection will be used to build
a form to narrow down your search inside the collection.
If the criterion (the index in portal_catalog) is sortable you can sort
this column. Not all criteria types can be used as input for
Flexi collection so beware.

* Search Text: full text search inside the collections. If you leave
  the criterion value empty users can search for content containing
  that text, if the value is not empty it will search for this text
  plus the text the user supplied.
* Title: search or sort by title (see above)
* Description: search description only (search see above, no sorting here!)
* Dates (effective, created, ...):  will be converted to  date ranges
  and can be selected with the JQuery JSlider_ Plugin)
* Location (path index): will not be displayed in the search form
  and always be applied to the query
* Keyword Indexes (like tags): a drop down list will be generated to
  narrow the search down

      * if the criterion operator is AND the list will contain all
        unique values of the index minus the ones you selected,
        the query will search for all terms that match your criteria
        plus the user input (this only applies to old style collections)
      * if the criterion is OR the terms you selected will be display
        in the selection list. The search will be for the user supplied
        input only. This is the only available behavior for new style
        collections

The output is always a table with the fields you supplied in the
'Table Columns' of the collection, no matter if 'Display as Table'
is checked or not.

Subtopics (old style Collections only):
---------------------------------------

Flexitopic will display subtopics as tabs on top of the page. The first
tab is the description of the topic, subtopics will occupy the following
tabs. Subtopics will always be displayed as (plain html) tables defined
by the criteria,  'Table Columns' and the 'Number of Items' of the subtopic.


Documentation
=============

Full documentation for end users can be found in the "docs" folder.
It is also available online at https://collectivegeo.readthedocs.io/


Translations
============

This product has been translated into

- Spanish.

You can contribute for any message missing or other new languages, join us at 
`Plone Collective Team <https://www.transifex.com/plone/plone-collective/>`_ 
into *Transifex.net* service with all world Plone translators community.


Installation
============
This addon can be installed has any other addons, please follow official
documentation_.


Add to buildout's configuration

::

    [buildout]
    ...
    eggs =
        collective.geo.flexitopic

Re-run buildout, e.g. with

::

    $ ./bin/buildout

Restart Plone and activate the product in Plone's Add-on configuration
section.


Tests status
============

This add-on is tested using Travis CI. The current status of the add-on is:

.. image:: https://img.shields.io/travis/collective/collective.geo.flexitopic/master.svg
    :target: https://travis-ci.org/collective/collective.geo.flexitopic

.. image:: http://img.shields.io/pypi/v/collective.geo.flexitopic.svg
   :target: https://pypi.org/project/collective.geo.flexitopic


Contribute
==========

Have an idea? Found a bug? Let us know by `opening a ticket`_.

- Code repository: https://github.com/collective/collective.geo.flexitopic/
- Questions and comments to http://www.coactivate.org/projects/collectivegeo/lists/collectivegeo-discussion/
- Report bugs at https://github.com/collective/collective.geo.flexitopic/issues
- Documentation: https://collectivegeo.readthedocs.io/


License
=======

The project is licensed under the GPLv2.


.. _Flexigrid: https://github.com/paulopmx/Flexigrid
.. _JSlider: http://egorkhmelev.github.com/jslider/
.. _documentation: https://docs.plone.org/manage/installing/installing_addons.html
.. _collective.flexitopic: https://pypi.org/project/collective.flexitopic/
.. _collective.geo.index: https://pypi.org/project/collective.geo.index/
.. _collective.geo: https://pypi.org/project/collective.geo.bundle/
.. _`opening a ticket`: https://github.com/collective/collective.geo.bundle/issues
