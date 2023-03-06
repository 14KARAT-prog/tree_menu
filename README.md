# tree_menu
Tree menu in django
# Приложения для отрисовки меню с помощью tags  
Простое Django приложения для отрисовки древовидного меню. Меню и его элементы создаются и редактируются в админ понели Django (Для создания меню в поле parent необходимо ничего не выбирать, в противном случае элемент привяжется к меню и будет выводится как его дочерний элемент).
## **Requirements**:
*asgiref==3.6.0
*Django==4.1.7
*Pillow==9.4.0
*sqlparse==0.4.3
## **Сборка и запуск**:
Для отображения меню при запуске следует сначала создать его и добавить дочерние элементы меню в админ понели Django, Для этого после сборки и запуска приложения необходимо перейти по пути http://127.0.0.1:8000/admin. Сам проект будет находится по ссылке http://127.0.0.1:8000/tree_menu

<html>
<body>
<p>git clone https://github.com/14KARAT-prog/tree_menu.git</p>
<p>cd tree_menu</p>
<p>pip install virtualenv</p>
<p>python -m venv venv</p>
<p>cd venv/Scripts/activate</p>
<p>pip install -r requirements.txt</p>
<p>cd app</p>
<p>python manage.py makemigrations</p>
<p>python manage.py migrate</p>
<p>python manage.py createsuperuser</p>
<p>python manage.py runserver</p>
</body>
</html>

## License
This project is licensed under the terms of the MIT license