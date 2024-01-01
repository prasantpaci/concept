#!/usr/bin/python3

# To run simple command which should raise on failure
a = subprocess.run(['ls'], check=True)
# a will have dict {'args': ['ls'], 'returncode': 0, 'stdout': None, 'stderr': None}
# on successful execution

# TimeoutExpired for Processes That Take Too Long
a = subprocess.run(['ls'], check=True, timeout=1)

#FileNotFoundError for Programs That Don’t Exist
a = subprocess.run(['you there'])
# Will return FileNotFoundError: [Errno 2] No such file or directory: 'you there'

#An Example of Exception Handling
try:
    subprocess.run(
        ["You there"], timeout=10, check=True
    )
except FileNotFoundError as exc:
    print(f"Process failed because the executable could not be found.\n{exc}")
except subprocess.CalledProcessError as exc:
    print(
        f"Process failed because did not return a successful return code. "
        f"Returned {exc.returncode}\n{exc}"
    )
except subprocess.TimeoutExpired as exc:
    print(f"Process timed out.\n{exc}")

# To capture command output which will return byte object
lso = subprocess.run(["sh", "-c", "ls ~/prasant/technical/python"], capture_output=True)
# lso.stdout will return b'general\nmodules\n'

# To capture command output in encoded form
lso = subprocess.run(["sh", "-c", "ls ~/prasant/technical/python"], capture_output=True,
encoding=True)
# lso.stdout will return 'general\nmodules\n'

# To capture command output in temporary file
from tempfile import TemporaryFile
with TemporaryFile() as f:
    ls_process = subprocess.run(["sh", "-c", "ls ~/prasant/technical/python"], stdout=f)
    f.seek(0)
    print(f.read().decode("utf-8"))
# The output would be '0\ngeneral\nmodules\n' where '0\n' is because of f.seek(0)

# Pipe Simulation With run()
ls_process = subprocess.run(["ls ~/prasant/technical/python"], stdout=subprocess.PIPE,
shell=True)
grep_process = subprocess.run(["grep", "modules"], input=ls_process.stdout,
stdout=subprocess.PIPE)
print(grep_process.stdout.decode("utf-8"))
# The output would be 'modules'
# It’s important that 'ls_process.stdout’ set to input rather than stdin. This is because
# the .stdout attribute isn’t a file-like object. It’s a bytes object, so it can’t be used
# as an argument to stdin.

# Alternatively using file as input for Pipe Simulation With run()
from tempfile import TemporaryFile
with TemporaryFile() as f:
    ls_process = subprocess.run(["ls ~/prasant/technical/python"], stdout=f, shell=True)
    f.seek(0)
    grep_process = subprocess.run(
        ["grep", "modules"], stdin=f, stdout=subprocess.PIPE
    )
# 0 from f.seek(0)
print(grep_process.stdout.decode("utf-8"))
# The output would be '0\nmodules\n' where '0\n' is because of f.seek(0)
