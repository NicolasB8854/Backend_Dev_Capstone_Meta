# Backend_Dev_Capstone_Meta

## Introduction
<p> This project serves as a Full-Stack Web Application for the Little Lemon Restaurant. </p>
<p> It's key functionalities are: </p>
<li> Menu</li>
<li> Reservation</li>
<li> API</li>
<img src="/littlelemon_start.jpg"></img>
## Setup 

<p> As a package manager, PDM was used. You can download it via pip and then type </p>
```
pdm install 
```
<p> Into the command line to activate the virtual environment. </p>
<br>
<p> To run the application, type: </p>
```
python manage.py runserver
```

## Testing 

<p> For API Testing, you will need to create a user. This can be done via: </p>
<p> 127.0.0.1:8000/auth/users <p>

The APIs can be tested at: <br>
<li> 127.0.0.1:8000/menu-api/ </li>
<li> 127.0.0.1:8000/menu-api/3 </li>
<li> 127.0.0.1:8000/booking-api/ </li>
<br>
<p> To test the application, type: <p>
```
python manage.py test
```
