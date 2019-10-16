# -*- coding: utf-8 -*-
# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# Hack to force urllib3 to reference greened ssl library, rather than the built-in one
import sys

sys.modules['requests.packages.urllib3.contrib.pyopenssl'] = __import__(
    'eventlet.green.ssl')  # noqa

import eventlet

eventlet.monkey_patch(psycopg=True)
# noinspection PyUnresolvedReferences, PyPep8
import requests  # noqa
# noinspection PyUnresolvedReferences, PyPep8
import requests.packages.urllib3

import datetime  # noqa: I100
# noinspection PyPep8
import json
# noinspection PyPep8
import logging
# noinspection PyPep8
import time
# noinspection PyPep8
import traceback

# noinspection PyPep8
from plexxiconnect import defines, events_api_client, object_types, utils
# noinspection PyPep8
from plexxiconnect import event as event_definitions
# noinspection PyPep8
from plexxiconnect.cx import event_protocol
# noinspection PyPep8
from plexxiconnect.db import tags
# noinspection PyPep8
from plexxiconnect.db.model import meta
# noinspection PyPep8
from plexxiconnect.debug import eventlet_debug
# noinspection PyPep8
import pytz
# noinspection PyPep8
from st2reactor.sensor.base import PollingSensor


__all__ = [
    'PlexxiEventSensor'
]

class PlexxiEventSensorException(Exception):
    """Plexxi Sensor received an unknown event type."""
    pass

class PlexxiEventSensor(PollingSensor):
    """Sensor which monitors events on the Plexxi fabric.

    A 'Passive' Sensor in StackStorm terminology, which registers an event listener with the
    Connect API Event Feed for changes on the fabric, and dispatches triggers to st2 rabbitmq bus
    in order to trigger event-based workflows.

    """

    def __init__(self, sensor_service, config=None, poll_interval=None):
        super(PlexxiEventSensor, self).__init__(sensor_service=sensor_service,
                                                  config=config,
                                                  poll_interval=poll_interval)
        self._trigger_ref = 'hpecfm.new-plexxi-event'
        self._logger = self._sensor_service.get_logger(__name__)

    def setup(self):
        self._client = PlexxiSearch(
            ipaddress=self._config['ipaddress'],
            username=self._config['username'],
            password=self._config['password']
        )
        self._last_id = None

    def poll(self):
        try:
            events = self._client.events_api_client()

        except Exception as e:
            self._logger.exception('Polling Plexxi failed: %s' % (str(e)))
            return

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def _get_last_id(self):
        pass

    def _set_last_id(self, last_id):
        pass

    def _dispatch_trigger_from_plexxi(self, event):
        trigger = self._trigger_ref

        payload = {
            'test': events
        }
        self._sensor_service.dispatch(trigger=trigger, payload=payload)
