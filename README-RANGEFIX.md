# How to get fix proposals in xconfig

You first must have Java JRE installed. Then run `make xconfig`.

A demonstration of the workflow can be seen on <https://youtu.be/vxop46vQpsk>.

## Knowns issues

1. You must ensure that you have a .config file. The reason being that it's
   sent as an input to RangeFix in the background.

2. RangeFix will crash if the .config file contains too large values. For
   instance, if you have a value like `0xdead000000000000` you need to change
   it to something smaller like `0xdead0000`.

3. It's only possible to edit tristate options. RangeFix does not currently
   support other Kconfig inputs.

4. The selected options are part of the fixes, which make them a bit harder to
   comprehend.

