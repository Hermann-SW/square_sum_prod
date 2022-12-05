""" square_sum_prod executable needs to be copied to a $PATH directory, eg. by:

git clone https://github.com/Hermann-SW/square_sum_prod.git
cd suqare_sum_prod
make
cp suqare_sum_prod ~/.local/bin
make clean

Then [ for 221 = 13*17 = (3²+2²)*(4²+1²) ]:

$ python Popen.py 221
#3,2,4,1#
$

Any factor 2 or "=3 (mod 4)" will assert in square_sum_prod and abort Python.
"""
import subprocess
import sys

def square_sum_prod(n):
    cmd = "square_sum_prod " + str(n) + " py"

    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = proc.communicate()

    if proc.returncode != 0:
        return None

    print("#"+str(out[0].decode())+"#")


square_sum_prod(sys.argv[1] if len(sys.argv) > 1 else 1105)
