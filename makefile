run:
	python -W ignore main.py

clean:
	> txt/mi_headlines.txt
	> txt/mi_releases.txt
	> txt/decibel.txt

test:
	> txt/mi_headlines.txt
	> txt/mi_releases.txt
	> txt/decibel.txt
	python -W ignore main.py
