from elf_header import ElfHeader
from sections import Sections

# the entier elf
class ELF:
    def __init__(self, content):
        super().__init__()
        self.content = content
        self.len = len(self.content)
        self.elf_header = ElfHeader(self)
        self.sections = Sections(self, self.elf_header.shoff, self.elf_header.shnum, self.elf_header.shentsize)

    def extra(self, index: int, size: int) -> int:
        return self.content[index: index + size]

    def pp(self):
        desc = self.elf_header.pp()\
            + f"\n{self.sections.s_str}"
        print(desc)

    def is_64(self):
        return self.elf_header.is_64()

    def part(self, start, size, start_64 = -1, size_64 = -1):
        return self.elf_header.part(start, size, start_64, size_64)