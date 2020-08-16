from elffile import ELFFile

ELF_PATH = "D:\\s\\dy_re\\cms_crack\\libcms.so"


ELFFile(ELF_PATH).getELF().pp()