
# Welcome to TaskManager!

This is my **Django project**. **TaskManager** is a web page where as a user you can register, log in and manage your tasks whereas page admins can create tasks and assign them to you.

Here's **why I chose Django** for this project:

There are many **third-party applications** that come with Django. These applications can be integrated depending on project requirements. Django consists of many applications — such as for authorization — that can easily be plugged into a system.

With Django you get **Admin panel by default**. A Django admin panel helps you manage your application. It is generated automatically from Python code so it saves you a lot of time on that. There’s also lots of room for customization in the Django admin panel thanks to third-party applications.

Django is valued for its object-relational mapper that helps developers **interact with databases**. An object-relational mapper (ORM) is a library that automatically transfers data stored in databases such as PostgreSQL and MySQL into objects commonly used in application code.

## Functionalities

TaskManager Django Project **functionalities** are:
-   Three types of users exist: **superuser**, **admin user (task manager)** and **normal user**. 

- Admins can  log in to default **Django Admin Page** and where they have limited access to manage tasks and task assignments. Normal users can log in to **TaskManager web page** and manage their tasks.
-  **Superusers** have all Admin Page permissions like **create, view, update or delete users, groups, tasks and assigned tasks, also grant permissions**.  Admin user can be created by a superuser by giving normal user a staff status and assigning him to a group "Admin".
-   **Admins** can **visit Django Admin page and create tasks, assign them to users, view, update or delete tasks** (they can only see and change those tasks and assigned tasks that they created or assigned)
-  **Users** can log in to TaskManager web page and **view tasks assigned to them only, read descriptions and mark tasks as completed**

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"
