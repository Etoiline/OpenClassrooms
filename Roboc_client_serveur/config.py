#-*- coding:utf-8 -*-

import re

#Variables générales

hote = ''
port = 65000
dossier_cartes = "cartes"
regex_deplacement = re.compile (r"^([nsweNSWE])(\d*)$")
regex_action = re.compile (r"^([MPmp])([nsweNSWE])$")
