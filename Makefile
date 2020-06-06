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
	docker build . -t sms-noise-bot

docker-run: docker-build
	docker run --rm -i -t \
		-p 8080:80\
		--name="sms-noise-bot"\
		--env-file ./.env\
		sms-noise-bot
