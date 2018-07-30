#!/usr/bin/env python
'''1. Use Jinja2 to generate the following configuration: 

--------
router ospf 40
 network 10.220.88.0 0.0.0.255 area 0
--------

The process ID, network, wildcard mask, and area should all be variables in the Jinja2 template.

Use a template directly embedded in your Python script.'''
import jinja2
ospf_config="""
router ospf {{process_id}}
  network {{network}} {{wildcard_mask}} area {{area_number}}
"""
ospf_vars = {
    'process_id': '40',
    'network': '10.220.88.0',
    'wildcard_mask': '0.0.0.255',
    'area_number': '0'
}
template = jinja2.Template(ospf_config)
output = template.render(**ospf_vars)
print(output)

