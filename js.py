# ('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")
# ^\s*(?!\/\/|\/\*).*('(?:[^'\\]|\\.)*')
# ^(?!//|/\*).*\[cC\]:\\\\
# comment regex - (\/\*(?:.|\n)*?\*\/|\/\/.*$)
# string regex - ('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")
# remove comments in strings (replace them for a little bit) - (?:"(\/\/).*"|'(\/\/).*')

import re

comment_regex = r"(\/\*(?:.|\n)*?\*\/|\/\/.*$)"
replace_comment_string_regex = r"(?:\"(\/\/).*\"|'(\/\/).*')"
string_regex =  r"(\'(?:[^'\\]|\\.)*\'|\"(?:[^\"\\]|\\.)*\")"

sample_file = 'samples/camelot-platform/django/elastico_dashboard/dashboard/static/dashboard/vendors/jquery/src/ajax.js'