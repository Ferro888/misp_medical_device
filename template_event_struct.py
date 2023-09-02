template_event_dict = {
    'Event': {
        'id': '4335',
        'orgc_id': '1',
        'org_id': '1',
        'date': '2023-06-07',
        'threat_level_id': '1',
        'info': 'Test Event',
        'published': False,
        'uuid': '78cc4740-0038-44a1-85ab-0c185208a5b4',
        'attribute_count': '12',
        'analysis': '0',
        'timestamp': '1685525783',
        'distribution': '1',
        'proposal_email_lock': False,
        'locked': False,
        'publish_timestamp': '0',
        'sharing_group_id': '0',
        'disable_correlation': False,
        'extends_uuid': '',
        'protected': None,
        'event_creator_email': 'fer.alessio25@gmail.com',
        'Org': {
            'id': '1',
            'name': 'TOR-VERGATA',
            'uuid': '43d474ed-ab66-4ea2-a533-79ee8ab97357',
            'local': True
        },
        'Orgc': {
            'id': '1',
            'name': 'TOR-VERGATA',
            'uuid': '43d474ed-ab66-4ea2-a533-79ee8ab97357',
            'local': True
        },
        'Attribute': [],
        'ShadowAttribute': [],
        'RelatedEvent': [],
        'Galaxy': [],
        'Object': [],
        'EventReport': [],
        'CryptographicKey': [],
        'Tag':[]
    }
}

template_object_dict = {
    'id': '3681635',
    'name': 'vulnerability',
    'meta-category': 'vulnerability',
    'description': 'Vulnerability object describing a common vulnerability enumeration which can describe published, unpublished, under review or embargo vulnerability for software, equipments or hardware.',
    'template_uuid': '81650945-f186-437b-8945-9f31715d32da',
    'template_version': '8',
    'event_id': '4335',
    'uuid': '6b048216-6bce-404e-ba4e-84f965c8632a',
    'timestamp': '1685525783',
    'distribution': '5',
    'sharing_group_id': '0',
    'comment': '',
    'deleted': False,
    'first_seen': None,
    'last_seen': None,
    'ObjectReference': [],
    'Attribute': []
}

template_attribute_dict = {
    'id': '26825196',
    'type': 'text',
    'category': 'Other',
    'to_ids': False,
    'uuid': '720999f7-ccc6-49a6-8650-1b9efb8ce28a',
    'event_id': '4335',
    'distribution': '5',
    'timestamp': '1685525783',
    'comment': '',
    'sharing_group_id': '0',
    'deleted': False,
    'disable_correlation': False,
    'object_id': '3681635',
    'object_relation': 'cvss-score',
    'first_seen': None,
    'last_seen': None,
    'value': '9',
    'Galaxy': [],
    'ShadowAttribute': []
}

template_tag_dict = {
"id":"475",
"name":"\tmalware_classification:malware-category=\"Botnet\"",
"colour":"#22681c",
"exportable":True,
"user_id":"0",
"hide_tag":False,
"numerical_value":None,
"is_galaxy":False,
"is_custom_galaxy":False,
"local_only":False,
"local":0,
"relationship_type":None
}