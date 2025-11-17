# Python Flask static files & bootstrap
static files, bootstrap setup and use

<br />
<br />
 
**Define static files path**
```python
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
```
```diff
+ /static/img
+ /static/css
+ /static/js
```

**Use of static files**
```html
index.html

<img src="/img/checker-board.png" alt="checker board">

<p class="special">Text with css class</p>

<script src="/js/hello.js"></script>
```
```html
base.html

<link rel="stylesheet" href="/css/style.css">
```
```html
static/css/style.css

.special {
  color: red;
  font-size: 22px;
}
```
```js
static/js/hello.js

window.onload = function(){
    this.setTimeout(function() {
        alert('Hello World!')
    }, 5000)
};
```
**Bootstrap**
1. Go to bootstrap official website
2. Download Compiled CSS and JS
3. Extract CSS and put in static/css, extract JS and put in static/js folders
4. link css and js script in base html template
5. Now you can use bootstrap with flask
```html
index.html

<a href="#" class="btn btn-primary">Button text</a>
```
```html
base.html

<link rel="stylesheet" href="/css/bootstrap.css">

<script src="/js/bootstrap.js"></script>
```
