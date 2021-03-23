import glob
import json
import os
import sys

from bioblend.galaxy import GalaxyInstance
from bioblend.galaxy.workflows import WorkflowClient

try:
    gi = GalaxyInstance(url=sys.argv[1], key=sys.argv[2])
except Exception as e:
    print(f'Failed to connect to the Galaxy instance, check URL and API keys. {e}')

publish = True
input_path = sys.argv[3]
wf_list = []
if os.path.isdir(input_path):
    for wf in glob.glob(input_path + "/*.ga"):
        wf_list.append(wf)
if os.path.isfile(input_path):
    wf_list.append(input_path)

for wf_path in wf_list:
    # extract Workflow name from .ga
    wf_dict = json.load(open(wf_path))
    if 'tags' in wf_dict.keys():
        if 'GTN' not in wf_dict['tags']:
            wf_dict['tags'].append('GTN')
    else:
        wf_dict['tags'] = ['GTN']
    wf_name = wf_dict.get('name', None)
    print(f'Processing wf {wf_name}')
    wf_id = None
    if wf_name:
        # find workflow with name
        wf_id = gi.workflows.get_workflows(name=wf_name)
        if len(wf_id) > 0:
            # if found then update
            try:
                update_details = gi.workflows.update_workflow(wf_id[0]['id'], workflow=wf_dict, published=publish)
            except Exception as e:
                print(f'Error updating workflow named {wf_name}: {e}')
            # print(f'The workflow named {wf_name} was updated with details: {update_details}')
        else:
            wf_id = None
    if not wf_id:
        # otherwise upload 
        import_details= gi.workflows.import_workflow_dict(workflow_dict=wf_dict,publish=publish) 
        # print(f'A new workflow was created with details: {import_details}')
