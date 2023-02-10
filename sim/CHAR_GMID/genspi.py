#!/usr/bin/env python3
import os
nch = "srcn"
pch = "srcp"

blocks = [
    "CHDL"
    "CHDLA",
    "CHDLCM",
    "CHL",
    "CHLA",
    "CHLCM"
]

def genspi(fname,sub,repl):
    foname = fname.replace("src") + repl.lower()
    with open(fname + ".spi") as fi:
        with open(foname + ".spi","w") as fo:
            for l in fi:
                l = l.replace(sub,repl)
                fo.write(l)
    os.system("ln -s {srcn}.yaml {foname}.yaml")
    os.system("ln -s {srcn}.meas {foname}.meas")
    #os.system(f"git add {foname}.py {foname}.spi")
    return foname

names = ""
for b in blocks:
    names += genspi(nch,"CHDL",b) + " "
    names += genspi(pch,"CHDL",b) + " "
print(names)
