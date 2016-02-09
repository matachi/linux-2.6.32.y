# How to get fix proposals in xconfig

    $ git clone --depth 1 --branch scala-2.9 git@github.com:matachi/rangeFix.git
    $ cd rangeFix
    $ less README.md # Follow the instructions
    $ cd ..

    $ git clone git@github.com:matachi/linux-2.6.32.y.git
    $ cd linux-2.6.32.y
    $ export RANGEFIX=`readlink -f ../rangeFix`
    $ make xconfig

In xconfig, select a tristate option whose value you want to change and press
either `n`, `m` or `y` on your keyboard. If the choice causes a conflict with
the configuration, it will execute RangeFix in the background. After some
seconds when RangeFix is done, it will output fixes in the terminal and in the
conflicts view. Open the conflicts view by clicking on the C in the toolbar.

A demonstration of the workflow can be seen on
<https://www.youtube.com/watch?v=G8vBa8js3Jo>.

