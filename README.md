# Event API in DRF

**Developer: Stuart Wall**

💻 [Live link]()

This repository contains the API set up using Django REST Framework for the Tick It front-end application ([repository here]() and [live website here]())

## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Credits](#credits)

## User Stories

The back-end section of the project focuses on its administration side and covers a single user story:
- As admin, I want to be able to create, edit and delete users, events, comments, likes, attendance and followers; so that I can have complete control over the content of the application.  If necessary, I can remove any inappropriate content and add my own directly.


## Database

The following models were created to represent the database model structure of the application:


#### User Model




#### Event Model



#### Comment Model



#### Attending Model



#### Like Model



#### Follower Model



#### Profile Model


##### Back to [top](#table-of-contents)


## Technologies Used

### Languages & Frameworks

- Python
- Django

### Libraries & Tools

- [Cloudinary](https://cloudinary.com/)
- [Graphviz](https://dreampuf.github.io/GraphvizOnline/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Gitpod](https://gitpod.io/workspaces)
- [Heroku](https://heroku.com)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html)
- [Psycopg2](https://www.psycopg.org/docs/)
- [ElephantSQL](https://www.elephantsql.com/)

##### Back to [top](#table-of-contents)


## Validation

### Python Validation

PEP8 was unavailable at the time of creating this project so [Pycodestyle](https://pypi.org/project/pycodestyle/) was used instead to continually check all Python code for errors and warnings.


## Testing

The following tests were carried out on the app:
1. Manual testing of user stories
2. Automated testing

### Manual testing of user stories

- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------


In addition: events, comments and likes can be created by logged-in users only. Users can only update or delete the content which was created by themselves.

<details><summary>Screenshots - USER</summary>
    <details><summary>Create user</summary>

    </details>
</details>



### Automated testing

Automated testing was done using the Django Rest Framework APITestCase.

- Tests summary

<details><summary>Individual app report</summary>

</details>

<details><summary>Combined report</summary>

</details>


##### Back to [top](#table-of-contents)


## Credits


### Code

This project was created based on the Code Institute's Django REST API walkthrough project ['Moments'](https://github.com/Code-Institute-Solutions/drf-api).

##### Back to [top](#table-of-contents)