run:
	python -W ignore main.py

clean:
	> txt/mi_headlines.txt
	> txt/decibel.txt

test:
	> txt/mi_headlines.txt
	> txt/decibel.txt
	python -W ignore main.py
