import helper

def test_hubble():
  output = helper.execute_cmd(["/usr/bin/hubble","--version"])
  assert '3.0.7' in output
