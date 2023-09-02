from template_event_struct import *
import copy
import uuid


attribute_fieldname = 'Attribute'
object_fieldname = 'Object'
tag_fieldname='Tag'

def create_tag_dict(tag_data):
    tag_dict = copy.deepcopy(template_tag_dict)
    for key in list(tag_data.keys()):
        if tag_data[key] and key in tag_dict.keys():
            tag_dict[key] = tag_data[key]
    return tag_dict

def create_object_dict(obj_data, attributes_count):
    obj_dict = copy.deepcopy(template_object_dict)
    if attribute_fieldname in obj_data.keys():
        attribute_field = obj_data[attribute_fieldname]
        for attribute in attribute_field:
            attribute_dict = create_attribute_dict(attribute)
            obj_dict[attribute_fieldname].append(attribute_dict)
            attributes_count = attributes_count + 1
    obj_dict['uuid'] = str(uuid.uuid4())
    return obj_dict, attributes_count


def create_attribute_dict(attr_data):
    attr_dict = copy.deepcopy(template_attribute_dict)
    for key in list(attr_data.keys()):
        if attr_data[key] and key in attr_dict.keys():
            attr_dict[key] = attr_data[key]
    attr_dict['uuid'] = str(uuid.uuid4())
    return attr_dict


def create_event_dict(data):
    attributes_count = 0
    event_dict = copy.deepcopy(template_event_dict)
    attribute_field = []
    object_field = []
    tag_field = []
    event_fields = list(data.keys())
    # Extract attributes
    if attribute_fieldname in event_fields:
        attribute_field = data[attribute_fieldname]
        event_fields.remove(attribute_fieldname)
    # Extract objects
    if object_fieldname in event_fields:
        object_field = data[object_fieldname]
        event_fields.remove(object_fieldname)
    #Extract tags
    if tag_fieldname in event_fields:
        tag_field = data[tag_fieldname]
        event_fields.remove(tag_fieldname)
    # Set event field
    for key in event_fields:
        if data[key] and key in event_dict['Event'].keys():
            event_dict['Event'][key] = data[key]
    event_dict['Event']['uuid'] = str(uuid.uuid4())
    # Add attributes to the event
    for attribute in attribute_field:
        attribute_dict = create_attribute_dict(attribute)
        event_dict['Event'][attribute_fieldname].append(attribute_dict)
        attributes_count = attributes_count + 1
    # Add objects to the event
    for obj in object_field:
        object_dict, attributes_count = create_object_dict(obj, attributes_count)
        event_dict['Event'][object_fieldname].append(object_dict)
    event_dict['Event']['attribute_count'] = attributes_count
    #Add tags to the event
    for tag in tag_field:
        tag_dict = create_tag_dict(tag)
        event_dict['Event'][tag_fieldname].append(tag_dict)
    return event_dict
    
       
