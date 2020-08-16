from section import Section
import section_type

class Sections():
    def __init__(self, elf, shoff, shnum, shentsize):
        super().__init__()
        self.elf = elf
        self.shoff = shoff
        self.shnum = shnum
        self.shentsize = shentsize
        self.sections = []
        for i in range(0, shnum):
            start = shoff + i * shentsize
            self.sections.append(Section(self.elf, start))
        self.s_str = [s for s in self.sections if section_type.s_strtab.value == s.type]

    def pp(self):
        pass