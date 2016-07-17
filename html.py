from HTMLParser import HTMLParser
import re

debug = False

resources = []

def combine_r(inp):
    return '('+')|('.join(inp)+')'

class HTML_parser(HTMLParser):
    css_attrs = ['style']
    js_attrs  = ['onclick']
    js_srcs  = [r'^javascript:']
    src_attrs = ['src','href','url']
    invalid_srcs = ['#' , '^[\s]*$']

    def handle_starttag(self, tag, attrs):
        if debug: print "Encountered a start tag:", tag

        for (attrname, attrval) in attrs:
            if debug: print "       attr: ", attr
            if attrname in self.src_attrs:
                # Skip invalid resources
                if re.match(combine_r(self.invalid_srcs), attrval):
                    continue
                if re.match(combine_r(self.js_srcs), attrval):
                    # Handle javascript code here
                    pass
                else:
                    print "Found resource in tag %s - %s - %s" % (tag, attrname, attrval)
                    resources.append(attrval)
            if attrval in self.css_attrs:
                pass
            if attrname in self.js_attrs:
                pass

    def handle_endtag(self, tag):
        pass
        # print "Encountered an end tag :", tag
        
    def handle_data(self, data):
        pass
        # print "Encountered some data  :", data

sample_file = "samples/camelot-platform/django/elastico_dashboard/dashboard/static/dashboard/production/general_elements.html"

sfile = open(sample_file).read()

parser = HTML_parser()
parser.feed(sfile)

# ('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")
# ^\s*(?!\/\/|\/\*).*('(?:[^'\\]|\\.)*')
# ^(?!//|/\*).*\[cC\]:\\\\
# comment regex - (\/\*(?:.|\n)*?\*\/|\/\/.*$)
# string regex - ('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")
# remove comments in strings (replace them for a little bit) - (?:"(\/\/).*"|'(\/\/).*')