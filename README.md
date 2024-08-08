# Backend Dev Capstone Meta
<img src="/littlelemon_start.jpg"></img>
<p> This project serves as a Full-Stack Web Application for the Little Lemon Restaurant. </p>
<p> It's key functionalities are: </p>
<li> Observing the menu that the Little Lemon restaurant provides</li>
<li> Booking a Table</li>
<li> Viewing the Reservations that are already present in the database </li>
<li> For authenticated user, an API is provided to add items to the menu list</li>

## Table of Contents
- [Backend Dev Capstone Meta](#backend-dev-capstone-meta)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Contributing](#contributing)


## Setup 

<p> As a package manager, PDM was used. You can download it via pip and then type: </p>

```
pdm install 
```

<p> Into the command line to activate the virtual environment. </p>
<p> Also, make sure that you have MySQL installed on your computer to access the database.
<p> You can download it here: <a href="https://www.mysql.com/downloads/">Download MySQL</a></p>

## Usage 

<p> To run the application, type: </p>

``` 
python manage.py runserver
```

<p> If you make any changes to the models contained in the project, make sure to migrate them correctly by typing:

``` 
python manage.py makemigrations
python manage.py migrate
```

## Testing 

<p> For API Testing, you will need to create a user. This can be done via accessing the following link while the server runs: </p>
<p> 127.0.0.1:8000/auth/users <p>

The APIs can be tested at: <br>
<li> 127.0.0.1:8000/menu-api/ </li>
<li> 127.0.0.1:8000/menu-api/3 </li>
<li> 127.0.0.1:8000/booking-api/ </li>
<br>
<p> To test the application, type: </p>

```
python manage.py test
```

## Contributing

<p> If you would like to become part of the project, please follow these steps: <p>
<ol>
<li> Fork the repository. </li>
<li> Create a new branch: `git checkout -b feature-name`. </li>
<li> Make your changes. </li>
<li> Push your branch: `git push origin feature-name`. </li>
<li> Create a pull request. </li>
</ol>
