install_prod_deps:
	pipenv install

installs_dev_deps:
	pipenv install --dev

install_deps: install_prod_deps installs_dev_deps