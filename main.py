#!/usr/bin/env python3
from keys import misp_url, misp_key
from event import create_event_dict
from misp import init, add_event, publish_event, get_all_events, delete_event
import json


# Connect to the MISP instance
misp = init(misp_url, misp_key)

# Delete all the existing events
for event in get_all_events(misp):
    delete_event(misp, event)

# Create event json strings
print('####### Creating CVE events #######')
cve_events_data = json.load(open('input_raw_events/cve_events_data.json', 'r'))
cve_events_dicts = []
for cve_event_data in cve_events_data:
    cve_event_dict = create_event_dict(cve_event_data)
    cve_misp_event = add_event(misp, cve_event_dict)
    publish_event(misp, cve_misp_event)
    cve_events_dicts.append(cve_event_dict)
json.dump(cve_events_dicts, open('output_misp_events/cve_events_list.json', 'w'))

print('####### Creating ICSMA events #######')
icsma_events_data = json.load(
    open('input_raw_events/icsma_events_data.json', 'r'))
icsma_events_dicts = []
for icsma_event_data in icsma_events_data:
    icsma_event_dict = create_event_dict(icsma_event_data)
    icsma_misp_event = add_event(misp, icsma_event_dict)
    publish_event(misp, icsma_misp_event)
    icsma_events_dicts.append(icsma_event_dict)
json.dump(icsma_events_dicts, open(
    'output_misp_events/icsma_events_list.json', 'w'))

print('####### Creating MedicalDevice events #######')
medical_device_events_data = json.load(
    open('input_raw_events/medical_device_events_data.json', 'r'))
medical_device_events_dicts = []
for medical_device_event_data in medical_device_events_data:
    medical_device_event_dict = create_event_dict(medical_device_event_data)
    medical_device_misp_event = add_event(misp, medical_device_event_dict)
    publish_event(misp, medical_device_misp_event)
    medical_device_events_dicts.append(medical_device_event_dict)
json.dump(medical_device_events_dicts, open(
    'output_misp_events/medical_device_events_list.json', 'w'))
