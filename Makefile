slow:
	venv/bin/nosetests tests.test_slow --with-timer

fair:
	venv/bin/nosetests tests.test_fair --with-timer

fast:
	venv/bin/nosetests tests.test_fast --with-timer

.PHONY: slow, fair, fast
