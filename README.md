# todo_django - http://todo-dj.herokuapp.com/todo/ 
**Instructions:** https://github.com/noah-dev/todo_django/blob/master/instructions.png

![Demo](https://github.com/noah-dev/todo_django/blob/master/login/static/login/demo.gif)
# Intro:
My name is Noah - I'm an aspiring developer and this is one of my side projects. This readme document will cover the why, how, and the what. **Why I built this, How I built this, and What I accomplished.**

# Why build a TODO app?
Although the business logic is pretty straight forward, I saw it as a great opportunity to learn front-end skills. This includes:
* Building a responsive(-ish) site using Bootstrap.
* Designing clean, stylish designs using CSS & Bootstrap
* Creating a user interface that enables users to select and display an item
* Adding animations via CSS Transitions & jQuery code

Although at the outset I didn't know much of the above, I did know there were a ton of resources to help me in implementing the features & feel I wanted. Django, HTML/CSS/JS & jQuery all have big communities, enabling me to learn and build quicker. 

# How does it work?
**UML Diagram**
In broad strokes, the three most key players are the user (the person), the front end (html/css/js) and the back end (django/postgres).

![UML](uml_diagram.png)

As shown in the diagram, there are four ways a user can interact with the app. I will briefly cover how this looks; if you are interested in more granualarity, check the appendix. 

**1: Login** 

Each user has their own list of items. In order to access the list, the user must first login. This is accomplished by using Django's built-in user authentication system. After typing in and submitting the login form, Django will authenticate the credentials against a table in postgres. If successful, Django will log the user in and redirect to the todo page, which shows the list of items. 

**2: Select An Item From The Right**

As seen in the demo, the todo page is split into main sections (excluding the navbar). The left-hand side shows one item in detail while the right-hand side shows all items with fewer details. To change which item the left-hand side shows, the user clicks on an item from the right-hand side. An item will go pale upon hover over, and once clicked an AJAX request will fetch that item's details from postgres. Once retrived from postgres, the front end will update the DOM elements of the left-hand side to show the selected item. 

**3: Toggle completion status of Item**

On the left-hand side, (execluding the navbar) the item's details are shown. At the bottom is a checkbox to indicate whether or not an item is complete. If the item is complete, the checkbox will already be checked. If the user clicks on the checkbox and toggles the state, an AJAX request is sent to Django. Django will update the appropriate record in postgres and return. From there the front end will update the DOM elements of both the left-hand side (for the checkbox) and the right-hand side (for the completion status)

**4: Add New Item**

By clicking on the plus sign, the user may add a new item. Once complete and submitted, Django will recieve the POST request and add a new record to postgres. Once complete, Django will provide a new HTML page to the front end. This new HTML page will contains the newly added item and will be visible to the user. 

# What did I accomplish & learn?

**1: I Met My Goals (And Then Some)**

I knew I wanted to build a TODO app with great design. I used inkscape to create a mockup to establish not only the look and feel, but also imagine how the user might interact. The colol palette, three column design (navbar, left-side & right-side) were established. I imagined the entire list of items shown on the right-side, with the user selecting a item to to be displayed in detail on the left-side. The navbar on the left would be able to collapse/expand and would show links to add new items or go to the repo. 

![mockup](mockup.png)

The end result looks a bit different, but in spirit it accomplishes everything the mockup envisioned. And then some. I did not intend to build a Login feature; but as I thought about how users experience, having the ability to login would make the app much better. If I shared this with multiple people, the list could become unrely and confusing. 

Though it would increase the scope of the project, I did some research to estimate the cost. I found a series of step-by-step youtube videos that covered the feature, showing how to use Django's built-in login module. Instead of spending weeks working through official docs and trial and error, with these videos, I realized I could implement this quickly at minimal time cost. After 2 days, the feature was implemented and deployed.

I am very satisfied with the end result. It takes a simple concept, and expands on it by adding slick design, nice user interface and a login page. I learned new tools, become proficient with them, and executed to create something I am proud of.

**2: jQuery, AJAX & Login**

At first, I didn't know jQuery: I had only used it for Bootstrap. A key part of my user interface was selecting items from the right-side and having it show on the left-side. To that end, I learned jQuery to execute code upon clicking certain elements. 

To show the selected item on the left-side, I planned on Django serving new HTML files. That would require a page refresh, and wondered if there was a better way. Googling led me to AJAX requests. After some learning, trying and failing, I implemented a basic AJAX request to retrive the appropriate record from postgres. I then learned to use jQuery to populate the text of DOM elements. AJAX requests are also used in updating the completion status of an item. 

As previously mentioned, having a login feature would improve the user experience. This would be the first time I'd implement such a feature, and I was grateful for the great Django community. The series of youtube videos were super helpful; it taught me enough to implement a login page. From there I added a new field to the model for username, so that the right items could be shown to the right users. The code was updated to account for the username field and would now require user login. Once complete, the end result worked as I had hoped. 

**3: I'm A Better Web Dev**

Tying into the previous three, accomplishing a project like this has shown me a lot of new ways to solve challenges. Having gone through database managment, UI design, login authentication and deployment for a simple project like this gives me new appreciation for the many web applications that I rely on. The fact that I accomplished this feels me with determination to learn new things and move on to tackle new, bigger, better projects.

# Resources & References
**Other people's code**
* Date picker: https://github.com/dbushell/Pikaday

**Tutorials which cover the basics of setting up Django**
* Offical tutorial: https://docs.djangoproject.com/en/1.11/intro/tutorial01/
* Excellent tutorial: https://tutorial.djangogirls.org/en/

**Youtube tutorials**
* User login/authentication: https://www.youtube.com/watch?v=BIgVhBBm6zI

**Official Documentation**
* Django: https://docs.djangoproject.com/en/1.11/
* jQuery: https://api.jquery.com/
* Bootstrap: https://v4-alpha.getbootstrap.com/getting-started/introduction/

**Unofficial Documentation**
* All around resource: https://www.w3schools.com/

**Blogs, Stackoverflow, and other misc sites for specific issues**

# Appendix

**WIP**
