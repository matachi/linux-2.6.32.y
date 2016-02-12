# How to get fix proposals in xconfig

You first must have Java JRE installed. Then run `make xconfig`.

In xconfig, select a tristate option whose value you want to change and press
either `n`, `m` or `y` on your keyboard. If the choice causes a conflict with
the configuration, it will execute RangeFix in the background. After some
seconds when RangeFix is done, it will output fixes in the terminal and in the
conflicts view. Open the conflicts view by clicking on the C in the toolbar.

A demonstration of the workflow can be seen on
<https://www.youtube.com/watch?v=G8vBa8js3Jo>.

