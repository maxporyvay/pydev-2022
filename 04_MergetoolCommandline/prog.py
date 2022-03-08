import readline
import shlex
import cmd
from pynames.generators import *
from pynames.generators.elven import *
from pynames.generators.iron_kingdoms import *
from pynames import GENDER, LANGUAGE


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
gens = {**simple_generators, **elven_generators, **iron_kingdoms_generators}


class Repl(cmd.Cmd):
    
    prompt = '>'

    current_language = LANGUAGE.NATIVE

    def do_language(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        if len(args) == 1:
            if args[0] in ['ru', 'RU']:
                self.current_language = LANGUAGE.RU
            elif args[0] in ['en', 'EN']:
                self.current_language = LANGUAGE.EN
            elif args[0] in ['native', 'NATIVE']:
                self.current_language = LANGUAGE.NATIVE
            else:
                return
        else:
            return

    def gengen(self, args):
        if args[0] in simple_generators:
                gen = simple_generators[args[0]]
                if len(args) == 1:
                    print(gen().get_name_simple(GENDER.MALE, self.current_language))
                elif len(args) == 2:
                    if args[1] == 'male':
                        print(gen().get_name_simple(GENDER.MALE, self.current_language))
                    elif args[1] == 'female':
                        print(gen().get_name_simple(GENDER.FEMALE, self.current_language))
                    else:
                        return
                else: return
        elif args[0] == 'elven':
            if len(args) == 1:
                print(elven_generators['warhammer']().get_name_simple(GENDER.MALE, self.current_language))
            elif len(args) == 2:
                if args[1] in ['male', 'female']:
                    if args[1] == 'male':
                        print(elven_generators['warhammer']().get_name_simple(GENDER.MALE, self.current_language))
                    elif args[1] == 'female':
                        print(elven_generators['warhammer']().get_name_simple(GENDER.FEMALE, self.current_language))
                elif args[1] in elven_generators:
                    gen = elven_generators[args[1]]
                    print(gen().get_name_simple(GENDER.MALE, self.current_language))
                else:
                    return
            elif len(args) == 3:
                if args[1] in elven_generators and args[2] in ['male', 'female']:
                    gen = elven_generators[args[1]]
                    if args[2] == 'male':
                        print(gen().get_name_simple(GENDER.MALE, self.current_language))
                    elif args[2] == 'female':
                        print(gen().get_name_simple(GENDER.FEMALE, self.current_language))
                else:
                    return
            else:
                return
        elif args[0] == 'iron_kingdoms':
            if len(args) == 1:
                print(iron_kingdoms_generators['caspian_midlunder_sulese']().get_name_simple(GENDER.MALE, self.current_language))
            elif len(args) == 2:
                if args[1] in ['male', 'female']:
                    if args[1] == 'male':
                        print(iron_kingdoms_generators['caspian_midlunder_sulese']().get_name_simple(GENDER.MALE, self.current_language))
                    elif args[1] == 'female':
                        print(iron_kingdoms_generators['caspian_midlunder_sulese']().get_name_simple(GENDER.FEMALE, self.current_language))
                elif args[1] in iron_kingdoms_generators:
                    gen = iron_kingdoms_generators[args[1]]
                    print(gen().get_name_simple(GENDER.MALE, self.current_language))
                else:
                    return
            elif len(args) == 3:
                if args[1] in iron_kingdoms_generators and args[2] in ['male', 'female']:
                    gen = iron_kingdoms_generators[args[1]]
                    if args[2] == 'male':
                        print(gen().get_name_simple(GENDER.MALE, self.current_language))
                    elif args[2] == 'female':
                        print(gen().get_name_simple(GENDER.FEMALE, self.current_language))
                else:
                    return
            else:
                return
        else:
            return

    def do_generate(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        try:
            self.gengen(args)
        except KeyError:
            temp = self.current_language
            self.current_language = LANGUAGE.NATIVE
            self.gengen(args)
            self.current_language = temp

    def do_info(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        if len(args) == 1:
            if args[0] in gens:
                gen = gens[args[0]]
                print(gen().get_names_number())
            else:
                return
        elif len(args) == 2:
            if args[0] in gens:
                gen = gens[args[0]]
                if args[1] == 'male':
                    print(gen().get_names_number(GENDER.MALE))
                elif args[1] == 'female':
                    print(gen().get_names_number(GENDER.FEMALE))
                elif args[1] == 'language':
                    trs = gen().get_name().translations
                    dct = {}
                    for k, v in trs.items():
                        dct = v
                        break
                    print(*dct)
                else:
                    return
            else:
                return
        else:
            return

    def complete_info(self, text, line, begidx, endidx):
        if line.count(' ') == 1:
            return [s for s in gens if s.startswith(text)]
        elif line.count(' ') == 2:
            if line.split()[1] in gens:
                return [s for s in ['male', 'female', 'language'] if s.startswith(text)]
            else:
                return []
        else:
            return []

    def complete_generate(self, text, line, begidx, endidx):
        if line.count(' ') == 1:
            return [s for s in list(simple_generators.keys()) + ['elven', 'iron_kingdoms'] if s.startswith(text)]
        elif line.count(' ') == 2:
            if line.split()[1] in simple_generators:
                return [s for s in ['male', 'female'] if s.startswith(text)]
            elif line.split()[1] == 'elven':
                return [s for s in list(elven_generators.keys()) + ['male', 'female'] if s.startswith(text)]
            elif line.split()[1] == 'iron_kingdoms':
                return [s for s in list(iron_kingdoms_generators.keys()) + ['male', 'female'] if s.startswith(text)]
            else:
                return []
        elif line.count(' ') == 3:
            if line.split()[1] == 'elven' and line.split()[2] in elven_generators or line.split()[1] == 'iron_kingdoms' and line.split()[2] in iron_kingdoms_generators:
                return [s for s in ['male', 'female'] if s.startswith(text)]
            else:
                return []
        else:
            return []

    def complete_language(self, text, line, begidx, endidx):
        if line.count(' ') == 1:
            return [s for s in ['ru', 'RU', 'en', 'EN', 'native', 'NATIVE'] if s.startswith(text)]
        else:
            return []
        
    def do_exit(self, arg):
        return True


Repl().cmdloop()
