from subprocess import Popen,PIPE

def execute_cmd(cmd):
   print("Executing command:")
   print(" ".join(cmd))
   proc = Popen(cmd, stdout=PIPE)
   output = proc.communicate()
   output = output[0].decode('ascii').rstrip('\n')
   return output
