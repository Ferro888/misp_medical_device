from pymisp import PyMISP, MISPEvent
from keys import misp_verifycert


def init(url, key):
    return PyMISP(url, key, misp_verifycert, 'json')


def add_event(misp_instance=None, event_json_str=None):
    if misp_instance and event_json_str:
        misp_event = MISPEvent()
        misp_event.from_dict(kwargs=event_json_str)
        # print(misp_event.info)
        return misp_instance.add_event(misp_event)


def publish_event(misp_instance=None, misp_event=None):
    if misp_instance and misp_event:
        misp_instance.publish(misp_event)
        return True
    return False


def get_all_events(misp_instance=None):
    if misp_instance:
        return misp_instance.events()
    return None


def delete_event(misp_instance=None, misp_event=None):
    if misp_instance and misp_event:
        misp_instance.delete_event(misp_event)
        misp_instance.delete_event_blocklist(misp_event)
