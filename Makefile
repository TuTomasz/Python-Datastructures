install:
	@echo 🧰 Installing  Dependencies 
	poetry install

build:
	@echo 🏗️ Initializing New Build
	make -k clean 
	make test
	make lint
	@echo 🔧 Building Packages
	poetry build

install-build:
	@echo 💿 Install build 
	pip install dist/*.tar.gz

clean:
	@echo 🧹 cleanup
	rm -rf dist/ 

test:
	@echo 🧪 Running Tests
	poetry run pytest tests/

lint:
	@echo ♻️ Reformatting Code
	poetry run black .