import os
from elffile import ELFFile

if os.name == "posix":
    ELF_PATH = "/Users/th/source/dy_re/libcms_crack/libcms.so"
else:
    ELF_PATH = "D:\\s\\dy_re\\cms_crack\\libcms.so"


ELFFile(ELF_PATH).getELF().pp_strs_content()