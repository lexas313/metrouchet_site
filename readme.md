# Сайт для компаний занимающихся обслуживанием счетчиков воды

Приложение на Django для управления заявками

## Содержание

- [Описание](#описание)
- [Требования](#требования)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Использование](#использование)
- [Контакты](#контакты)

## Описание

Информационный сайт для заказа услуг

## Требования

- Docker
- Docker Compose
- Python 3.X

## Установка
1. Клонируйте репозиторий:
```bash
git clone git@github.com:lexas313/metrouchet_site.git
```
2. Перейдите в папку с проектом:
```bash
cd metrouchet_site
```
3. Убедитесь, что у вас установлен Docker и Docker Compose.

## Запуск проекта

1. Постройте и запустите контейнеры:
```bash
docker compose up --build
```
2. Откройте браузер и перейдите по адресу `http://localhost:80` для доступа к приложению.

## Использование

При запуске контейнеров суперпользователь создастся автоматически с логином: root и паролем: root.

## Контакты
- Email: lexas313@gmail.com
- GitHub: [lexas313](https://github.com/lexas313)