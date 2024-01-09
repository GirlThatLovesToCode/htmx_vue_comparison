# Django Rest Framework and Vue versus Django and HTMX


## Introduction

Building a great single-page app (SPA) that became a standard in recent years, requires both, a robust back-end and a well-designed front-end.
To a Pythonista, off course, creating a robust back-end doesn't pose a big problem.
Using either a time-honoured Django or up-and-coming FastAPI, you can't miss.
But if your forte is Python, you may have a problem deciding what to use for front-end.
The intent of this article is to compare Django Rest Framework/Vue with Django/HTMX so you can better decide which combination better suits you needs.


## Django Rest Framework and Vue

[Django Rest Framework](https://www.django-rest-framework.org/) (DRF) is built on top of Django, maintaining most of it's functionality.
The main difference is DRF instead of serving a human-readable site serves an API endpoint that is meant as a point of entry for another program.

Usage of DRF for a website requires a front-end framework.
Vue, while trailing behind Angular and React in popularity as highlighted by the [StackOverflow Developer Survey](https://survey.stackoverflow.co/2023/#most-popular-technologies-webframe), compared to the former two, doesn't have a steep learning curve and can be easier to integrate in existing project.
[Vue.js](https://vuejs.org/) considers itself "*approachable, performant and versatile*".

Compared to HTMX, it's well seasoned (since 2014).

TODO: make a diagram of how vue talks to DRF (two separate entities that communicate with each other).

### Example

## Django and HTMX

HTMX got a reputation of a "JavaScript framework for people who hate JavaScript". 
It's [rapidly gaining popularity](https://risingstars.js.org/2023/en#section-framework).

If you used any FE framework before, it has an entirely different feeling to it - for starters, it's not a stand-alone.
It's like HTML on steroids.


TODO: make a diagram of how HTMX talks to Django (specks of HTMX inside of Django - intertwined).

### Example


## DRF/Vue vs. Django/HTMX

While this article aims at explaining the differences between DRF-Vue and Django-HTMX combos, you have to understand that directly comparing Vue and HTMX is like comparing apples and oranges.

The choice between Vue.js with Django Rest Framework and HTMX with Django depends on the specific requirements and goals of your project, as well as the expertise of your development team. 
Vue.js is often chosen for applications requiring rich client-side interactions and complex state management, while HTMX is preferred for simpler applications where server-side rendering is adequate and less client-side complexity is desired.

## Conclusion

In this article, you got some basic idea about using Django/HTMX and DRF/Vue combos.
Depending on your needs and preferences you can now make a more informed decision on which one to use.

While HTMX is light and simple to use, Vue is probably a better choice for more complex projects - but it can be a lot of overhead.

> **Did HTMX impress you?**
> Check out the [Full-stack Django with HTMX and Tailwind Course](https://testdriven.io/courses/django-htmx/).

> **Do you prefer Django Rest Framework and Vue?**
> We've got you covered:
> 1. [Developing RESTful APIs with Django REST Framework](https://testdriven.io/courses/django-rest-framework/)
> 2. [Learn Vue by Building and Deploying a CRUD App Course](https://testdriven.io/courses/learn-vue/)
