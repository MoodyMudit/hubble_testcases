import helper
import json

def test_hubble():
  output = helper.execute_cmd(["/usr/bin/hubble","--version"])
  assert '3.0.7' in output

def test_hubble_compliance():
  output = helper.execute_cmd(["/usr/bin/hubble","hubble.audit","--json"])
  object = json.loads(output)
  compliance = object["Compliance"]
  assert compliance != ''

def test_hubble_grains_get():
  output = helper.execute_cmd(["/usr/bin/hubble","grains.get", "host", "--json"])
  object = json.loads(output)
  assert object != ''
