# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TreeMapping
                                 A QGIS plugin
 A plugin to generate trees from satellite images
                             -------------------
        begin                : 2014-11-27
        copyright            : (C) 2014 by ICRAF
        email                : e.omwandho@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TreeMapping class from file TreeMapping.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tree_mapping import TreeMapping
    return TreeMapping(iface)
