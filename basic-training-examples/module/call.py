import cmd
from cmd import cmd_exec as execute

print("\n*** Module using example ***\n")

cmd.cmd_exec("echo one way of calling module function")
execute("echo other way of calling module function")
execute("bla-bla-bla", "there are no such command 'bla-bla-bla'")

