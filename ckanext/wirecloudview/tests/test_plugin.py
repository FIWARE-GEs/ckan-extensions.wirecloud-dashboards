# -*- coding: utf-8 -*-

# Copyright (c) 2017 Future Internet Consulting and Development Solutions S.L.

# This file is part of CKAN WireCloud View Extension.

# CKAN WireCloud View Extension is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN WireCloud View Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN WireCloud View Extension. If not, see <http://www.gnu.org/licenses/>.
# This file is part of CKAN Data Requests Extension.

import unittest

from mock import MagicMock, patch

import ckanext.wirecloudview.plugin as plugin


class DataRequestPluginTest(unittest.TestCase):

    def test_process_dashboardid_should_strip(self):

        self.assertEqual(plugin.process_dashboardid(self, "  owner/name ", context), "onwer/name")

    def test_process_dashboardid_should_leave_untouched_valid_dashboard_ids(self):

        self.assertEqual(plugin.process_dashboardid(self, "owner/name", context), "onwer/name")
