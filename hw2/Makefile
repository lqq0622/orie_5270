cover:
	make lint
	make cover_tests

lint:
	flake8 --max-line-length=120 tree tests

cover_tests:
	py.test -s --tb short --cov-config .coveragerc --cov tree --cov-report term-missing --cov-report xml \
	--cov-report html \
	--junitxml junit.xml \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	tests

