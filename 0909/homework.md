# Compiled Bootstrap

 CSS, JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일로 추가하시오. 부트스트랩이 적용되기 위해 작성해야 할 코드를 제출하시오.

```python
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="{% static 'bootstrap.min.css' %}"
  </head>
<body>
  <div class="container">

    {% block content %}
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
  
    {% endblock content %}

  </div>
  <link rel="stylesheet" href="{% static 'bootstrap.bundle.min.js' %}">
  </body>
</html>
```



