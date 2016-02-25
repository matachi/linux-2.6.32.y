# How to get fix proposals in xconfig

You first must have Java JRE and Z3 installed. RangeFix will look for Z3 at
`/usr/bin/z3`. Then run `make xconfig`. During the first startup it will
download [RangeFix.jar](https://github.com/matachi/rangeFix/releases/).

A demonstration of the workflow can be seen on <https://youtu.be/vxop46vQpsk>.

## Knowns issues

1. You must ensure that you have a .config file. The reason being that it's
   sent as an input to RangeFix in the background.

2. It's only possible to edit tristate options. RangeFix does not currently
   support other Kconfig inputs.

3. The selected options are part of the fixes, which make them a bit harder to
   comprehend.

