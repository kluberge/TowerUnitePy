from pytower.selection import Selection
from pytower.suitebro import Suitebro, TowerObject
from pytower.tools import set_url
from pytower.tool_lib import ToolParameterInfo, ParameterDict

TOOL_NAME = 'ReplaceURL'
VERSION = '1.0'
AUTHOR = 'Physics System'
URL = 'https://github.com/rainbowphysics/PyTower/blob/main/tools/replace_url.py'
INFO = '''Replaces URL on canvas objects in the given selection.'''
PARAMETERS = {'url': ToolParameterInfo(dtype=str, description='URL to set'),
              'replace': ToolParameterInfo(dtype=str, description='URL to replace')}


def should_replace(obj: TowerObject, url: str) -> bool:
    if not obj.is_canvas():
        return False

    return obj.is_canvas() and obj.properties['properties']['URL']['Str']['value'] == url


def main(save: Suitebro, selection: Selection, params: ParameterDict):
    selection = Selection({obj for obj in selection if should_replace(obj, params.replace)})
    set_url.main(save, selection, params)
