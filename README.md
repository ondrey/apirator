# apirator
Проект на flask - Реализован интерфейс для создания api.

Данный интерфейс создан для личного удобства, дает возможность быстро регистрировать новые АПИ. 
Для перспективных проектов рекомендуется использовать библиотеки вроде flaskRESTful (https://flask-restful.readthedocs.io/en/latest/) и т.п..

## Порядок регистрации новой функции апи:
1. Создание файла в папке LibAPI
2. Наследуемся от базового класса ObjectAPI
3. Создаем метод с префиксом api_ - данный далее будет доступен по ссылке host.com/<Название вашего класса>/<Наименование метода>
4. Регистрируем новый объект в файле apirator/LibAPI/__init__.py


## todo:
1. Добавить декоратор для обработки ошибок
2. Декоратор для разграничения доступа по ключу