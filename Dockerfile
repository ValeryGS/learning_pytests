# Указываем с какого имаджа нужно собрать контейнер
FROM python:3.8-alpine

# Переменные окружения. Помните, что ARG доступен только когда мы собираем наш контейнер
# когда мы будем его запускать, то доступ к этой переменной получить уже не сможем.
ARG run_env=development
ENV env $run_env

# С помощью этих штук, вы можете оставить какую-то информацию о себе
LABEL "обучение"="Запуск тестов в docker"
LABEL "взято из"="SolveMe community"

# Указываем директорию в которой мы будем работать внутри докера
WORKDIR ./usr/Docker_autotests_yandex

# Создаём вольюм, для того чтобы иметь возможность получить данные после того, как контейнер закончит свою работу
VOLUME /allure_tmp

# Этой командой обновляем наш базовый образ
RUN apk update && apk upgrade && apk add bash

# Копируем отдельно наш файл с зависимостями
COPY requirements.txt .

# Инстайлим наши зависимости внутри контейнера
RUN pip3 install -r requirements.txt

# Копируем наши файлики внутрь контейнера
COPY . .

# Ну и наконец-то запускаем наши тесты
CMD pytest -m "$env" -s -v tests
# --alluredir=allure_tmp


#Эту команду мы запускаем чтобы собрать наш контейнер
#docker build --build-arg env=development -t auto_tests_yandex .

#Эта команда нужна чтобы запустить наш созданый контейнер
#docker run auto_tests_yandex

#Эти 2 команды нам нужны чтобы скопировать данные из контейнера и чтобы сгенерировать из результата репорт
#docker cp $(docker ps -a -q | head -1):/usr/Docker_autotests_yandex/allure_tmp .
#allure serve allure_tmp/
#Две команды ниже, помогут вам в экспериментах, чтобы после них почистить свой компьютер
#docker rm $(docker ps -a -q)
#docker kill $(docker ps -q)