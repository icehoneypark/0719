# 1. 기본 그리드 레이아웃

```
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice1</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 1</h1>
      </div>
    </div>

    <!-- 1. -->
    <!-- padding이 24px로 돼있어서 0으로 없앰 -->
    <div class="row p-0">
      <div class="item">
        <p>1</p>
      </div>
      <div class="item">
        <p>2</p>
      </div>
      <div class="item">
        <p>3</p>
      </div>
    </div>

    <!-- 2. -->
    <!-- padding이 24px로 돼있어서 0으로 없앰 -->
    <div class="row p-0">
      <div class="item col">
        <p>1</p>
      </div>
      <div class="item col">
        <p>2</p>
      </div>   
    </div>

    <!-- 3. -->
    <!-- 12column을 3 6 3으로 나눠서 지정 -->
    <div class="row">
      <div class="item col-3">
        <p>1</p>
      </div>  
      <div class="item col-6">
        <p>2</p>
      </div>
      <div class="item col-3">
        <p>3</p>
      </div>
    </div> 
    
    <!-- 4. -->
    <!-- 12column을 2 7 3으로 나눠서 지정 -->
    <div class="row">
      <div class="item col-2">
        <p>1</p>
      </div>
      <div class="item col-7">
        <p>2</p>
      </div>
      <div class="item col-3">
        <p>3</p>
      </div> 
    </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>
```

# 2. 반응형 그리드

```
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice2</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 2</h1>
      </div>
    </div>

    
    <!-- 1. -->
    <div class="row">
      <!-- 텍스트에 적힌대로 지정 -->
      <div class="item col-4 col-sm-2">
        <p>576px 미만 4 <br> 576px 이상 2</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
    </div>


    <!-- 2. -->
    <div class="row">
      <!-- 텍스트에 적힌대로 지정 -->
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-3">
        <p>768px 미만 3 <br> 768px 이상 3</p>
      </div>
      <div class="item col-4 col-md-3">
        <p>768px 미만 4 <br> 768px 이상 3</p>
      </div>
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-2">
        <p>768px 미만 3 <br> 768px 이상 2</p>
      </div>
    </div>


    <!-- 3. -->
    <div class="row">
      <!-- 텍스트에 적힌대로 지정 -->
      <div class="item col-4 col-sm-3 col-md-6">
        <p>576px 미만 4 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-6 col-sm-3 col-md-6">
        <p>576px 미만 6 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-2 col-sm-6 col-md-12">
        <p>576px 미만 2 <br> 768px 미만 6 <br> 768px 이상 12</p>
      </div>
    </div>


    <!-- 4. -->
    <div class="row">
      <!-- 텍스트에 적힌대로 지정 -->
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-12">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 12</p>
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>
</html>
```

# 3. 그리드 심화

```
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice3</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 3</h1>
      </div>
    </div>

    <!-- 1. -->
    <div class="row">
      <!-- 텍스트에 적힌대로 지정 -->
      <div class="item col-4 col-md-4">
        <p>item1</p>
      </div>
      <!-- 텍스트에 적힌대로 지정(offset으로 공백 자리 채움) -->
      <div class="item col-8 col-md-4 offset-md-4">
        <p>item2</p>
      </div>
    </div>


    <!-- 2. -->
    <div class="row">
      <!-- 텍스트에 적힌대로 지정(offset으로 공백 자리 채움) -->
      <div class="item col-4 / col-md-4 offset-md-4 / col-lg-7 offset-lg-5"> 
        <p>item1</p>
      </div>
      <!-- 텍스트에 적힌대로 지정(offset으로 공백 자리 채움) -->
      <div class="item col-4 offset-4 / col-md-4 offset-md-0 / col-lg-8 offset-lg-2">
        <p>item2</p>
      </div>
    </div>
    

    <!-- 3. -->
    <div class="row">
      <!-- 텍스트에 적힌대로 지정 -->
      <div class="item col-12 col-md-3">
        item1
      </div>
      <!-- 텍스트에 적힌대로 지정 -->
      <div class="item col-md-9">
        <div class="row">
          <!-- 텍스트에 적힌대로 지정(Nesting) -->
          <div class="item col-6 col-lg-3">item2</div>
          <div class="item col-6 col-lg-3">item3</div>
          <div class="item col-6 col-lg-3">item4</div>
          <div class="item col-6 col-lg-3">item5</div>
        </div>
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>
</html>
```

