Installation process:

### Django-htmx notes:

### Vue-DRF notes:

you need to install cors in order to use it loccaly (https://dzone.com/articles/how-to-fix-django-cors-error)

### Comparison:

#### Vue vs HTMX:
ChatGPT output:
It's important to note that the choice between Vue.js with Django Rest Framework and HTMX with Django depends on the
specific requirements and goals of your project, as well as the expertise of your development team. Vue.js is often
chosen for applications requiring rich client-side interactions and complex state management, while HTMX is preferred
for simpler applications where server-side rendering is adequate and less client-side complexity is desired.


| Aspect                         | Vue.js with Django Rest Framework                                  | HTMX with Django                                   |
|--------------------------------|--------------------------------------------------------------------|----------------------------------------------------|
| **Complexity**                 | Higher complexity. Vue.js is a full-fledged frontend framework requiring knowledge of JavaScript, Vue.js concepts, and integration with Django Rest Framework for API calls. | Simpler. HTMX is an extension to HTML and works seamlessly with standard Django templates, requiring less setup and no additional language. |
| **Development Approach**       | SPA (Single Page Application) approach or integrating Vue components into Django templates. Requires a separate REST API. | Traditional multi-page application approach. Enhances Django templates with AJAX capabilities. |
| **Interactivity**              | High level of interactivity. Ideal for dynamic and complex user interfaces with real-time data updates. | Moderate interactivity. Suitable for adding dynamic behavior to pages without the complexity of a JavaScript framework. |
| **Learning Curve**             | Steeper learning curve due to the need to understand both Vue.js and Django Rest Framework. | Lower learning curve, especially for developers already familiar with Django. |
| **Performance**                | Can offer better client-side performance for complex applications, but requires careful management of state and API interactions. | Server-rendered pages with partial updates, reducing the need for client-side processing. |
| **Scalability**                | Better suited for large-scale, complex applications where a rich client-side experience is essential. | More suitable for smaller to medium-scale applications where full-scale SPA complexity is not required. |
| **Data Handling**              | Frontend (Vue.js) communicates with the backend (Django) via API calls, handling data in JSON format. | Data handling is managed server-side. HTMX can request HTML fragments or JSON for updates. |
| **SEO Optimization**           | Requires additional considerations for SEO, as SPAs are not inherently SEO-friendly. | Better SEO out of the box since content is server-rendered. |
| **Development Speed**          | Potentially slower initial development due to setup and complexity, but can be faster for updates in long-term projects. | Quicker to develop initially, especially for developers experienced with Django. Ideal for rapid development. |
| **Testing**                    | Requires separate testing strategies for frontend (Vue.js) and backend (Django Rest Framework). | Testing can be primarily focused on the Django side, with standard Django testing tools. |

#### Vue-DRF vs Django-HTMX

ChatGPT output:

| Aspect                        | DRF with Vue.js                                       | Django with HTMX                                  |
|-------------------------------|------------------------------------------------------|---------------------------------------------------|
| **Architecture**              | Decoupled frontend (Vue.js) and backend (DRF).       | Coupled, with HTMX enhancing server-rendered HTML.|
| **Complexity**                | Higher due to separate frontend and backend concerns.| Lower, with most logic handled server-side.       |
| **Interactivity**             | High, with dynamic and reactive UI components.       | Moderate, with AJAX-driven interactivity.         |
| **Learning Curve**            | Steeper, requiring knowledge of DRF, Vue.js, and their integration. | Gentler, particularly for those already familiar with Django. |
| **Performance**               | Can be optimized for client-side, but depends on efficient API design and usage. | Reliant on server performance, with less client-side processing. |
| **Development Speed**         | Potentially slower due to complexity and separate frontend/backend development. | Faster for simple applications, especially if familiar with Django. |
| **Data Handling**             | Frontend (Vue.js) communicates with backend (DRF) via RESTful API calls. | Server-side data handling with HTML responses augmented by HTMX. |
| **Scalability**               | Good for large-scale, complex applications needing a rich UI. | More suitable for smaller to medium-scale applications. |
| **SEO**                       | Requires additional setup for SEO with SPAs.         | Better for SEO due to server-rendered content.    |
| **Testing**                   | Requires separate frontend and backend testing strategies. | Simplified testing primarily focused on the Django side. |
| **Use Case**                  | Ideal for complex, interactive web applications.     | Best for applications where simplicity and rapid development are key. |



### Other articles

1. Django/Vue vs. Django/HTMX