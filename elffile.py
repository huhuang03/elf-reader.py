import os
from elf import ELF

_MAGIC_HEADR = bytearray([0x7f, 0x45, 0x4c, 0x46])

class ELFFile:
    def __init__(self, path):
        super().__init__()
        assert os.path.exists(path)
        self.content = open(path, 'rb').read()
        # self._magic = self.content[0: len(_MAGIC_HEADR)]
        # assert self._magic == _MAGIC_HEADR
        self.elf = ELF(self.content)


    def getELF(self) -> ELF:
        return self.elf
