#!/usr/bin/env python3
import os
nch = "srcn"
pch = "srcp"

blocks = [
    "CHDL",
    "CHDLA",
    "CHDLCM",
    "CHL",
    "CHLA",
    "CHLCM"
]

ss = """
description: |
  ---
  layout: post
  title: ID char
  categories: sim
  ---

simulations:

"""



def genspi(fname,sub,repl):

    foname = fname.replace("src","") + repl.lower()
    with open(fname + ".spi") as fi:
        with open(foname + ".spi","w") as fo:
            for l in fi:
                l = l.replace(sub,repl)
                fo.write(l)
    os.system(f"ln -s {fname}.yaml {foname}.yaml")
    os.system(f"ln -s {fname}.meas {foname}.meas")

    ss = f"""
  {foname}:
    name: {foname.upper()}
    description:
    data:
      - name: Sch_tfs
        src: results/{foname}_tfs
        method: minmax

"""

    #os.system(f"git add {foname}.py {foname}.spi")
    return ss



for b in blocks:
    ss += genspi(nch,"CHDL",b) + " "
    ss += genspi(pch,"CHDL",b) + " "

with open("summary.yaml","w") as fo:
    fo.write(ss)
