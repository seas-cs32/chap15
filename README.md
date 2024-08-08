This directory contains everything needed for
**Chapter 15 (Embrace Runtime Debugging)** in
[*Computational Thinking and Problem Solving (CTPS)*](https://profsmith89.github.io/ctps/ctps.html)
by Michael D. Smith.

`pdb0.py`: Starter script that differs from `pdb1.py`, which is
in the CTPS book, in allowing the reader or an instructor to
write all the code in the function `my_pdb`. Since the
implementation of `my_pdb` violates its interface definition,
`pdb0.py` will fail if you run it.

`pdb1.py`: Script that sets us up for inserting a breakpoint in
a script-to-be-debugged. It prints out the input script. It is
also capable of writing out the input script under the
input filename with a `-db` suffix appended.

`pdb2.py`: Extends `pdb1.py` by inserting the
breakpoint and writes out the edited script.

`pdb3.py`: Extends `pdb2.py` to launch the edited
script with a breakpoint in it.

`pin32.py`: Turns `pdb3.py` into an instrumentation program.

`repl32.py`: Turns `pin32.py` into a script that inserts a
read-execute-print loop at the breakpoint location.

`guess32.py`: A slightly modified version of the script from
Chapter 5, which we use as the input for our debuggers and
instrumentation scripts.
