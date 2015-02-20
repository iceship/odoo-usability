# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: David BEAL
#    Copyright 2015 Akretion
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sale Display For Dev',
    'version': '0.2',
    'author': 'Akretion',
    'maintainer': 'Akretion',
    'category': '',
    'description': """
Add new display to system admin group to avoid to check these checkbox:
- uom
- pricelist
- delivery/invoice address
    """,
    'depends': [
        'sale',
    ],
    'website': 'http://www.akretion.com/',
    'data': [
        'group.xml',
    ],
    'tests': [],
    'installable': True,
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': [],
    },
    'auto_install': True,
}