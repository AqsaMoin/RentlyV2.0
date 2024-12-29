# Yo!
### You guys just have to change the frontend codes in the templates folder backend is ready

# Luminari
### Illuminating your Views

### This project aims to provide the people on some unknown good places in the world by illuminating them on our website.As we believe it improves the Eco-toursim of the place and also helps in building an bond to the local people by understanding it's culture

The project provides the endusers to upload the places of their of what they think which are places for the people to visit to them as well

* You can upload the places
* You can upload an site
* And etc..,

### How to install this program on your end

* Firstly clone this repo by using this link<br>
git clone repo link

* Next step is to have an virtual env in your folder of the same as the folder cloned and run this cmd
python -m venv sam

* After creating an venv it should be in your parent folder where you have the clone repo folder now run this cmd
sam/Scripts/activate

* after no errors it should be like (sam) in your terminal
(sam)your_terminal_path

* Now change directory to the luminari by this
cd luminari

* Now install the django latest version by this
pip install django django-autoslug

* With this you now can make the migrations
python manage.py makemigrations

* This should show no changes detected or some green signs but no errors

* After this done use this
python manage.py migrate

* After the project is migrated and no error occurs
 ### Firstly congrats for keeping this up now we are in the last command

 * The last command is
 python manage.py runserver 3108

* If everything is perfect the server will run register yourself and say what things you need to change:)

#### Read the limitations file

