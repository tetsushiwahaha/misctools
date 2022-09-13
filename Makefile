#TARGET = docsample
TARGET = slidesample

$(TARGET): 
	latexmk $(TARGET)
	
v:
	vim $(TARGET).tex

clean:
	latexmk -C

prev:
	open -a preview $(HOME)/Desktop/$(TARGET).pdf 

t:
	touch $(TARGET).tex
