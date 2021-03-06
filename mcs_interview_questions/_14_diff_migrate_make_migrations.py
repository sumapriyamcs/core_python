'''

14. difference between migrate and make migrations:

makemigrate:

It will generate the SQL command to create the table corresponding to each class you
made in the models.py file.

migrate:

It will create the table in the database using the commands which have been generated by makemigrations.


The corresponding SQL command after creating your class models in models.py and using makemigrations will be

migrate, which is responsible for applying migrations, as well as unapplying
and listing their status. makemigrations, which is responsible for creating new
migrations based on the changes you have made to your models.


Makemigration:- if you do any changes in you app models, makemigration will identify
those changes and will create migration with those changes in migration folder of app.

Migrate:- this command will apply your changes on your database and also create an entry
in django_migration table. Migrate check what are migration not present in db migration
table and run only for db changes.


python manage.py makemigrations : Create the migrations (generate the SQL commands).
python manage.py migrate: Run the migrations (execute the SQL commands).



makemigrations is responsible for packaging up your model changes into individual
migration files - analogous to commits - and migrate is responsible for applying
those to your database.


'''