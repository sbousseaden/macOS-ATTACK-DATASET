import pytest
import glob
import json
from schema import Schema, And, Use, Optional, SchemaError

def get_files():
    files = glob.glob("./**/*.json")
    return files

@pytest.mark.parametrize("file", get_files())
def test_json_format(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
        assert json.loads(data)

@pytest.mark.parametrize("file", get_files())
def test_documents_exist(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
    rule = json.loads(data)
    schema = Schema({'tactic': str, 'techniques': [str], 'documents': [dict]}, ignore_extra_keys=True)
    assert schema.validate(rule)
