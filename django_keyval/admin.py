'''
django_keyval/tests

Copyright (C) 2013 Edwin van Opstal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see `<http://www.gnu.org/licenses/>`.
'''

from __future__ import division
from __future__ import absolute_import

from django.contrib import admin
from django_keyval.models import _KvStore


class KvStoreAdmin(admin.ModelAdmin):
    list_display = ('prop_name', 'prop_key', 'prop_value',)
    search_fields = ('prop_key',)
    list_filter = ('prop_name',)
    ordering = ('prop_name', 'prop_key')

admin.site.register(_KvStore, KvStoreAdmin)
