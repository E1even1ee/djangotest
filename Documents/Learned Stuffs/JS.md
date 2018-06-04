## JavaScript Catch-up
### Function
```javascript
var add = function (a, b) {
    return a + b;
};
```
```javascript
var result = add(1, 2);
```
### Object
```javascript
var jedi = {
    name: "Yoda",
    age: 899,
    talk: function () { alert("another... Sky... walk..."); }
};
```
```javascript
var person = {
    age: 122
};

person.name = {
    first: "Jeanne",
    last: "Calment"
};
```
### Array iteration
```javascript
var helloFrom = function (personName) {
    return "Hello from " + personName;
}

var people = ['Tom', 'Yoda', 'Ron'];

people.push('Bob');
people.push('Dr Evil');

people.pop();

for (var i=0; i < people.length; i++) {
    var greeting = helloFrom(people[i]);
    alert(greeting);
}
```
### DOM
**By ID**
```javascript
var pageHeader = document.getElementById('page-header');
```
**By Tag Name**
document.getElementsByTagName
**By Class Name**
document.getElementsByClassName
**By CSS Selector**
```javascript
var pageHeader = document.querySelector('#header');
var buttons = document.querySelectorAll(.btn);
```
### Events and Callback
addEventListener can be applied on any elements
```javascript
var handleClick = function (event) {
    // do something!
};
var button = document.querySelector('#big-button');
button.addEventListener('click', handleClick);
```
### AJAX
_Asynchronous JavaScript and XML_
```javascript
$.get('/data.json', function (data) {
    console.log(data);
}).fail(function () {
    // Uh oh, something went wrong
});
```
```javascript
$.post('/save', { username: 'tom' }, function (data) {
    console.log(data);
}).fail(function () {
    // Uh oh, something went wrong
});
```
With the most control
```javascript
$.ajax({
    url: '/save',
    method: 'POST',
    data: { username: 'tom' },
    success: function (data) {
        console.log(data);
    }),
    error: function () {
        // Uh oh, something went wrong
    }
});
```
### JQuery
```javascript
$('.btn').click(function () {
    // do something
});
```
```javascript
var doSomething = function (event) { . . . };
window.addEventListener('DOMContentLoaded', doSomething);
```

But we can do it more easily with jQuery, and it will work cross-browser:

```javascript
$(window).ready(doSomething);
```

This can be shortened further to:

```javascript
$(doSomething);
```
To do this without jQuery, listen for the load event on the window:

```javascript
window.addEventListener('load', doSomething);
```

But it’s even easier with jQuery:

```javascript
$(window).load(doSomething);
```
**Check**
```javascript
$.isPlainObject({ name: 'Tom' });
```
```javascript
$.isFunction(function () { });
```
```javascript
$.isArray([1, 2, 3]);
```
### OOP and prototype inherit
```javascript
var Person = function (name) {
    this.name = name;
};
```
```javascript
Person.prototype.say = function (words) {
    alert(this.name + ' says "' + words + '"');
};
```
```javascript
var tom = new Person("tom");
tom.say("Hello");
```
### Create DOM with JS
```javascript
var div = document.createElement('div');
div.textContent = "Sup, y'all?";
div.setAttribute('class', 'note');
document.body.appendChild(div);
```
Remove an element
```javascript
div.parentNode.removeChild(div);
```
Creating with **jQuery**
```javascript
var div = $('<div/>').text("Sup, y'all?").appendTo(document.body);
$('<span/>').text('Hello!').appendTo(div);
```
### Regular expression
```javascript
var regex = /^[a-z\s]+$/;
var lowerCaseString = 'some characters';

if (lowerCaseString.match(regex)) {
    alert('Yes, all lowercase');
}
```
```javascript
var text = "There is everything and nothing.";

text = text.replace(/(every|no)thing/g, 'something');
```
### NodeJS example
Node comes with a core set of modules, one of which is “_http_”, used to set up a web server. Here’s a simple HTTP server example that serves one page to all requests:

```javascript

var http = require('http');

var server = http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World\n');
})

server.listen(1337, '127.0.0.1');

console.log('Server running at http://127.0.0.1:1337/');

```

We grab the “http” module then create a server with a single callback function that serves all requests and then set it up to listen on localhost port 1337.

### AngularJS
An open-source client-side JavaScript framework that uses **HTML** as its templating language.
**MODEL**
Just HTML
```html
<input ng-model="name">

<h1>Hello {{ name }}</h1>
```
**FUNCTION**
Just JS
```javascript
var AppCtrl = function ($scope) {
    $scope.name = "Yoda";
};
```
**CONTROLLER**
A controller has a _scope_, which is an area of DOM it has access to. Giving a controller a scope looks like this:
```html
<div ng-controller="AppCtrl">
    <input ng-model="name">
     <h1>Hello {{ name }}</h1>
</div>
```
