# Building an E-learning Platform

### To run locally

- pipenv install
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- Please install memcached have and have it run locally
- python manage.py runserver

<p>
By using model inheritance, I created a versatile system to manage different types of content for the course modules. I implemented a custom model field to order objects. I also used class-based views and mixins. I worked with groups and permissions to restrict access to my views. Finally, I used formsets to manage course modules, and I built a drag-and-drop functionality with jQuery UI to reorder modules and their contents.
</p>

<p>
I implemented the public views for the course catalog. I also built a system for students to register and enroll on courses aswell as created the functionality to render different types of content for the course modules. Finally, I learned how to use the Django cache framework and I installed and monitored the Memcached cache backend.
</p>
<p>
I used the Django REST framework to build a RESTful API for my project. I created serializers and views for models, and I built custom API views. I also added authentication to my API and restricted access to API views using permissions. Next, I created custom permissions, and implemented viewsets and routers. Finally, I used the Requests library to consume the API from an external Python script.
</p>

<p>
I created a chat server using Channels, implemented a WebSocket consumer and client.I also enabled communication between consumers using a channel layer with Redis and modified the consumer to be fully asynchronous.
</p>
