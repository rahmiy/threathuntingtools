#!/usr/bin/env python
# coding: utf-8
# pylint: disable=unused-wildcard-import, import-error

import sys
sys.path.append(r'..\elasticsearch_hunting')
import datetime
import powershell

start_datetime = datetime.datetime.strptime('2019-05-01 19:40:00.0', '%Y-%m-%d %H:%M:%S.%f')
end_datetime = datetime.datetime.strptime('2019-07-29 19:50:00.0', '%Y-%m-%d %H:%M:%S.%f')

powershell_telemetry = powershell.Telemetry(start_datetime = start_datetime, end_datetime = end_datetime, scan = True)
powershell_telemetry.analyze()
powershell_telemetry.dump_script_blocks()