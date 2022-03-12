#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import json
import requests
from pprint import pprint

__author__ = "Milla Jauhiainen"
__copyright__ = "Copyright 2019, Tampere University"
__email__ = "milla.jauhiainen@tuni.fi"


class SimpleFHIRClient(object):
    def __init__(self, server_url, server_user, server_password, debug=False):
        self.debug = debug
        self.server_url = server_url
        self.server_user = server_user
        self.server_password = server_password

    def get_all_patients(self):
        requesturl = self.server_url + "/Patient?_format=json"
        entries = self._get_json(requesturl)["entry"]
        return [entry["resource"] for entry in entries]

    def get_all_data_for_patient(self, patient_id):
        requesturl = self.server_url + "/Patient/" + \
            patient_id + "$everything?_format=json"
        return self._get_json(requesturl)["entry"]

    def _get_json(self, requesturl):
        response = requests.get(requesturl,
                                auth=(self.server_user, self.server_password))
        response.raise_for_status()
        result = response.json()
        if self.debug:
            pprint(result)
        return result