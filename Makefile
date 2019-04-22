install_requirements:
	pip install -r requirements.txt

test:
	python -m unittest discover ./ -v
