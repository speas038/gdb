#Allow loading of .gdbinit files in debug directory
add-auto-load-safe-path .

set print pretty on
set confirm off
set verbose off

set history save on
set history size 500

# append or overwrite?
set logging overwrite on
set logging on
show logging

# These make gdb never pause in its output
set height 0
set width 0


