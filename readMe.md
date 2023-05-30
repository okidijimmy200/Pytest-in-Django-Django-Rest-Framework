[![Python application](https://github.com/okidijimmy200/Pytest-in-Django-Django-Rest-Framework/actions/workflows/build.yaml/badge.svg)](https://github.com/okidijimmy200/Pytest-in-Django-Django-Rest-Framework/actions/workflows/build.yaml)
This application aims to dig into the inner workings of django and django-restframework using pytest.

We build a school application that features classrooms with individual student attributes, including performance metrics. We developed a classroom and student models with relevant attributes and conducting unittests for the models inttest.py file. We create unittests for students, testing student grades.


We create an API folder that houses views, routes, and serializers. This folder serves as a centralized location for organizing and managing the components necessary for building an efficient and reliable API.


We develop a serializer class specifically designed for students, enabling the transformation of data for storage in the database and facilitating efficient querying. This serializer class plays a pivotal role in ensuring seamless communication between the application and the database, allowing for smooth data handling and retrieval operations.
We utilize generic views to streamline the creation, listing, updating, and deletion of students within the students model. By leveraging these pre-built views, we can efficiently handle common CRUD (Create, Read, Update, Delete) operations, simplifying the development process and ensuring consistency.

Furthermore, we prioritize thorough testing of the different views to verify their functionality and robustness. We  perform unit tests specifically tailored to each view, validating their behavior under various scenarios. This rigorous testing approach guarantees that the views function as intended, providing a reliable and error-free experience for managing student data.

We develop views for classrooms, implementing authentication and authorization mechanisms using the default Django Rest Framework (DRF) authentication. By leveraging DRF's built-in authentication features, we ensure secure access and control over the classroom-related functionalities.

In addition, we meticulously craft unit tests specifically focused on creating classrooms. These tests rigorously assess the behavior and accuracy of the classroom creation process, ensuring that it functions as expected. By thoroughly testing this functionality, we can identify and address any potential issues, guaranteeing a reliable and error-free classroom creation experience.

To run the Project:
> pip install requirements.txt

>python manage.py makemigrations

>python manage.py migrate

>python manage.py runserver