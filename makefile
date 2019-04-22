run:
	python main.py

clean:
	> metalinjection.txt
	> decibel.txt
	> metalstorm.txt

test:
	> metalinjection.txt
	> decibel.txt
	python main.py
