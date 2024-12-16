# Title: dae-validator
# Version: 1.0.0
# Publisher: NFDI4Culture
# Publication date: December 5, 2024
# Author: Joerg Heseler
# License: CC BY-SA 4.0

from __future__ import print_function
import json
import subprocess
import sys
from lxml import etree

SUCCESS_CODE = 0
ERROR_CODE = 1
DAE_SCHEMES_PATH = '/usr/share/schemes/dae' 

class DAEValidatorException(Exception):
    pass

def format_event_outcome_detail_note(format, version, result):
    note = 'format="{}";'.format(format)
    if version is not None:
        note = note + ' version="{}";'.format(version)
    if result is not None:
        note = note + ' result="{}"'.format(result)

    return note

def get_schemes_path_from_arguments():
    global DAE_SCHEMES_PATH
    for arg in sys.argv:
        if arg.lower().startswith("--schemes-path="):
            return arg.split("=", 1)[1].rstrip('/\\')
    return DAE_SCHEMES_PATH

def validate_dae_file(target):
    try:
        try:
            target_xml_tree = etree.parse(target, parser=etree.XMLParser(huge_tree=True))
        except etree.XMLSyntaxError as e:
            raise DAEValidatorException(e)
        target_xml_root = target_xml_tree.getroot()
        format = 'DAE (COLLADA Digital Asset Exchange)'
        version = target_xml_root.attrib.get('version')
        xsd_path = get_schemes_path_from_arguments()
        # xsd_path = './schemes/dae/'
        # according to the official specification only 1.5.0 and not 1.5 is valid here
        if version == '1.5.0':
            xsd_path += '/collada_schema_1_5_0.xsd'
        else:
            xsd_path += '/collada_schema_1_4_1.xsd'
        try:
            xsd_schema = etree.XMLSchema(etree.parse(xsd_path))
        except OSError:
            raise Exception("DAE schemes path not found. Use --schemes-path= to specify its path.")
#        except etree.XMLSchemaParseError as e:
            # raise DAEValidatorException(e)
        validation_successful = xsd_schema.validate(target_xml_tree)
        if not validation_successful:
            error_log = '\n'.join([str(error) for error in xsd_schema.error_log])
            raise DAEValidatorException(error_log)
        
        note = format_event_outcome_detail_note(format, version, '') #error_log

        print(
            json.dumps(
                {
                    "eventOutcomeInformation": "pass",
                    "eventOutcomeDetailNote": note,
                    "stdout": target + " validates.",
                }
            )
        )

        return SUCCESS_CODE
    except DAEValidatorException as e:
        print(
            json.dumps(
                {
                    "eventOutcomeInformation": "fail",
                    "eventOutcomeDetailNote": str(e),
                    "stdout": None,
                }
            ),
            file=sys.stderr,
        )
        return ERROR_CODE
    except Exception as e:
        print(e, file=sys.stderr)
        return ERROR_CODE

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'DAE Validator, version 1.0.0')
        print()
        print(f'This script validates DAE files against schemas provided by https://www.khronos.org/api/collada.')
        print()
        print(f'Usage: python dae-validator.py <DAE file> [options]')
        print()        
        print(f'--schemes-path=<path to DAE schemes>    path to DAE schemes, default={DAE_SCHEMES_PATH}')
        sys.exit(0)

    target = sys.argv[1]
    sys.exit(validate_dae_file(target))
