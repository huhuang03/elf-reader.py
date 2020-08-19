import os
from elf import ELF

if os.name == "posix":
    ELF_PATH = "/Users/th/source/dy_re/libcms_crack/libcms.so"
else:
    ELF_PATH = "D:\\s\\dy_re\\cms_crack\\libcms.so"


ELF(ELF_PATH).pp()