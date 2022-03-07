import readline
import shlex
import cmd


class Repl(cmd.Cmd):
    prompt = '>'

    def do_exit(self, arg):
        return True


Repl().cmdloop()
