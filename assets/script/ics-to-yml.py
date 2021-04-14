#!/usr/bin/env python3
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

# Built-in modules
from datetime import date
from datetime import time

# Third-party modules
from ics import Calendar
import requests
import yaml

upcoming_events_url = 'https://www.openmainframeproject.org/events/category/zowe?ical=1&tribe_display=photo'
past_events_url = 'https://www.openmainframeproject.org/events/category/zowe?action=tribe_photo&tribe_paged=1&tribe_event_display=past&ical=1&tribe_display=past'

upcoming = Calendar(requests.get(upcoming_events_url).text)
past = Calendar(requests.get(past_events_url).text)

eventlist = []
for i in range(2):
    if i == 0:
        x = upcoming.events
    else:
        x = past.events
    for event in list(x):
        eventinstance = {}
        eventinstance['event'] = event.name

        start_time_stamp = event.begin.format() #'2021-04-21 08:30:00+08:00'
        end_time_stamp = event.end.format()

        # start_time_stamp.split()[0] = 2021-04-21

        start_date = date.fromisoformat(start_time_stamp.split()[0]).strftime('%B %d') #4 April
        end_date = date.fromisoformat(end_time_stamp.split()[0]).strftime('%B %d')

        if start_date == end_date:
            eventinstance['schedule'] = start_date + ' @ ' + time.fromisoformat((event.begin.format()).split()[1]).strftime('%I:%M %p') + ' - ' + time.fromisoformat((event.end.format()).split()[1]).strftime('%I:%M %p') 
            #April 21 @ 08:30 AM - 09:30 PM
        else:
            eventinstance['schedule'] = start_date + ' - ' + end_date #March 15 - March 20
        
        description_list = event.description.split()[:40]
        description = ""
        for words in description_list:
            description = description + words + " "

        eventinstance['description'] = description.strip() + "..."
        eventinstance['url'] = event.url
        eventlist.append(eventinstance)

with open(r'../_data/upcoming_events.yml', 'w') as yamlfile:
    yaml.dump(eventlist, yamlfile, sort_keys=False)