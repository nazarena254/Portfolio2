# Portfolio

## Description
Django web application that allows admin to add or edit her skills and projects.

## Author
Nazarena Wambura.</br>
[Github Account](https://github.com/nazarena254)

## Setup/Installation Requirements
1. Create a folder and cd to it.
2. Clone the repository below with the command `git clone <https option url> .`  <br>
    https://github.com/nazarena254/Portfolio2  
3. Install dependencies in the requirements.txt file `pip install -r requirements.txt` .
4.  Type code . or atom . based on the text editor you have & work on it.   

## Database
1. Set up Database(postgresql) and put your username and password in the code
2. Make migrations
    `python3 manage.py makemigrations`
3. Migrate
   `python3 manage.py migrate`

## Running the Application
1. Run main aplication locally on http://127.0.0.1:8000/ local host<br>    
   * `python3.9 manage.py runserver` <br>
    Note: python version will vary in future

## Creating Admins
1. Creating Admin Locally<br>
     `python manage.py createsuperuser`  Then set username, email & password.

2. Creating Heroku Admin   
     `heroku run python manage.py createsuperuser` Then set username, email & password.

### Homepage
![Homepage](./folio/static/images/portfolio.png) 

## Technologies Used
* Python3.9.2 - as backend language
* Django4.0.5 - as a Framework
* Bootstrap4 - for responsiveness & styling
* Cloudinary - as cloud-based image storage server 
* PostgreSQL - as database
* Heroku - for deploying app

## Support & Contact Information
For any further inquiries, bugs, contributions or comments, reach me at:<br>
Email:<nancyngunjiri1@gmail.com> <br>
[LinkedIn](https://www.linkedin.com/in/nazarena-wambura)

## License
[MIT License](https://github.com/nazarena254/Portfolio2/blob/master/LICENSE)<br>
Copyright (c) 2022 **Nazarena Wambura**
