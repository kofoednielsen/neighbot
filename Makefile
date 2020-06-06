# ░█▀▄░█▀▀░█░█
# ░█░█░█▀▀░▀▄▀
# ░▀▀░░▀▀▀░░▀░
venv:
	pipenv install

clean:
	pipenv --rm


# ░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀▄
# ░█░█░█░█░█░░░█▀▄░█▀▀░█▀▄
# ░▀▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀

docker-build:
	docker build . -t neighbot

docker-run: docker-build
	docker run --rm -i -t \
		-p 8080:80\
		--name="neighbot"\
		--env-file ./.env\
		neighbot
