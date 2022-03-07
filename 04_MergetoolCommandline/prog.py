import readline
import shlex
import cmd
from pynames.generators import *
from pynames.generators.elven import *
from pynames.generators.iron_kingdoms import *
from pynames import GENDER, LANGUAGE


current_language = LANGUAGE.NATIVE

simple_generators = {'scandinavian': scandinavian.ScandinavianNamesGenerator,
                     'russian': russian.PaganNamesGenerator,
                     'mongolian': mongolian.MongolianNamesGenerator,
                     'korean': korean.KoreanNamesGenerator,
                     'goblins': goblin.GoblinGenerator,
                     'orcs': orc.OrcNamesGenerator}
elven_generators = {'warhammer': WarhammerNamesGenerator,
                    'dnd': DnDNamesGenerator}
iron_kingdoms_generators = {'caspian_midlunder_sulese': CaspianMidlunderSuleseFullnameGenerator,
                            'dwarf': DwarfFullnameGenerator,
                            'gobber': GobberFullnameGenerator,
                            'iossan_nyss': IossanNyssFullnameGenerator,
                            'khadoran': KhadoranFullnameGenerator,
                            'orgun': OgrunFullnameGenerator,
                            'ryn': RynFullnameGenerator,
                            'thurian_morridane': ThurianMorridaneFullnameGenerator,
                            'tordoran': TordoranFullnameGenerator,
                            'trollkin': TrollkinFullnameGenerator}


class Repl(cmd.Cmd):
    
    prompt = '>'

    def do_generate(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        if args[0] in simple_generators:
            gen = simple_generators[args[0]]
            if len(args) == 1:
                print(gen().get_name_simple(GENDER.MALE, current_language))
            elif len(args) == 2:
                if args[1] == 'male':
                    print(gen().get_name_simple(GENDER.MALE, current_language))
                elif args[1] == 'female':
                    print(gen().get_name_simple(GENDER.FEMALE, current_language))
                else:
                    return
            else: return
        elif args[0] == 'elven':
            if len(args) == 1:
                print(elven_generators['warhammer']().get_name_simple(GENDER.MALE, current_language))
            elif len(args) == 2:
                if args[1] in ['male', 'female']:
                    if args[1] == 'male':
                        print(elven_generators['warhammer']().get_name_simple(GENDER.MALE, current_language))
                    elif args[1] == 'female':
                        print(elven_generators['warhammer']().get_name_simple(GENDER.FEMALE, current_language))
                elif args[1] in elven_generators:
                    gen = elven_generators[args[1]]
                    print(gen().get_name_simple(GENDER.MALE, current_language))
                else:
                    return
            elif len(args) == 3:
                if args[1] in elven_generators and args[2] in ['male', 'female']:
                    gen = elven_generators[args[1]]
                    if args[2] == 'male':
                        print(gen().get_name_simple(GENDER.MALE, current_language))
                    elif args[2] == 'female':
                        print(gen().get_name_simple(GENDER.FEMALE, current_language))
                else:
                    return
            else:
                return
        elif args[0] == 'iron_kingdoms':
            if len(args) == 1:
                print(iron_kingdoms_generators['caspian_midlunder_sulese']().get_name_simple(GENDER.MALE, current_language))
            elif len(args) == 2:
                if args[1] in ['male', 'female']:
                    if args[1] == 'male':
                        print(iron_kingdoms_generators['caspian_midlunder_sulese']().get_name_simple(GENDER.MALE, current_language))
                    elif args[1] == 'female':
                        print(iron_kingdoms_generators['caspian_midlunder_sulese']().get_name_simple(GENDER.FEMALE, current_language))
                elif args[1] in iron_kingdoms_generators:
                    gen = iron_kingdoms_generators[args[1]]
                    print(gen().get_name_simple(GENDER.MALE, current_language))
                else:
                    return
            elif len(args) == 3:
                if args[1] in iron_kingdoms_generators and args[2] in ['male', 'female']:
                    gen = iron_kingdoms_generators[args[1]]
                    if args[2] == 'male':
                        print(gen().get_name_simple(GENDER.MALE, current_language))
                    elif args[2] == 'female':
                        print(gen().get_name_simple(GENDER.FEMALE, current_language))
                else:
                    return
            else:
                return
        else:
            return
                
    def do_exit(self, arg):
        return True


Repl().cmdloop()
