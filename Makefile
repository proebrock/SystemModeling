TEX = pdflatex -shell-escape


.PHONY: all
all: systemmodeling.pdf

systemmodeling.pdf: systemmodeling.tex
	$(TEX) systemmodeling.tex
	$(TEX) systemmodeling.tex
	$(TEX) systemmodeling.tex

.PHONY: clean
clean:
	rm -f *.aux *.log *.out

.PHONY: distclean
distclean:
	rm -f *.aux *.log *.out systemmodeling.pdf
