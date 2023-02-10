
TB=idgm
#VIEW=Sch
VIEW=Sch
#VIEW=Ver

OPT=

TBS=idgm_nchdla idgm_pchdla idgm_nchdlcm idgm_pchdlcm idgm_nchl idgm_pchl idgm_nchla idgm_pchla idgm_nchlcm idgm_pchlcm

CORNER=tfs

all:
	${foreach f,${TBS}, make ${CORNER} TB=${f};}

genspi:
	python3 genspi.py

typical:
	cicsim run --name typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

slow:
	cicsim run --name slow ${TB} ${OPT} ${VIEW} Gt Kss "Th,Tl" Vl

fast:
	cicsim run --name fast ${TB} ${OPT} ${VIEW} Gt Kff "Th,Tl" Vh

tfs:
	cicsim run --name tfs ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff"  "Tt,Th,Tl" Vt

ttffss:
	cicsim run --name ttffss ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt" Vt

temp:
	cicsim run --name temp ${TB} ${OPT} ${VIEW} Gt "Ktt" "Tt,Th,Tl" Vt

tfsp:
	python3 plot_idgm.py ${TB}_${VIEW}GtAttAssAffTtThTlVt.run ${OPT}

test:
	${MAKE} tfs tfsp

summary:
	cicsim summary --output "README.md"
	pandoc -s README.md -o README.html

clean:
	-rm -rf output_*
	-rm -rf __pycache__
	-rm *.run
	-rm *.pdf
	-rm *.csv
