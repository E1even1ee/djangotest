## JQuery Catchup
### Basics
The jQuery syntax is tailor-made for  **selecting**  HTML elements and performing some  **action**  on the element(s).

Basic syntax is:  **$(_selector_)._action_()**

-   A $ sign to define/access jQuery
-   A (_selector_) to "query (or find)" HTML elements
-   A jQuery  _action_() to be performed on the element(s)

Examples:

$(this).hide() - hides the current element.

$("p").hide() - hides all paragraph elements.

$(".test").hide() - hides all elements with class="test".

$("#test").hide() - hides the element with id="test".
```javascript
$(document).ready(function(){  
	// jQuery methods go here...
});
```
This is to prevent any jQuery code from running before the document is finished loading (is ready)!
```javascript
$(function(){  
	// jQuery methods go here...   
});
```
```javascript
$(document).ready(function(){  
	$("button").click(function(){  
		$("#test").hide();  
	});  
});
```
```javascript
$("*")
$(this)
$("p.intro")
$("p:first")
$("ul li:first")
$("ul li:first-child")
$("[href]")
$("a[target='_blank']")
$("a[target!='_blank']")
$(":button")
$("tr:even")
$("tr:odd")
```
#### Events
Mouse Events
- click
- dblclick
- monseenter
- mouseleave
- hover (mouseenter + mouseleave) 
- mousedown
- mouseup

Keyboard Events
- keypress
- keydown
- keyup

Form Events
- submit
- change
- focus <-> blur

Document/Window Events
- load
- resize
- scroll
- unload

### Effects
```javascript
$("button").click(function(){  
$("p").hide(1000);  
});
```
```javascript
$("button").click(function(){  
$("p").toggle();  
});
```
**fade methods**:

-   fadeIn()
-   fadeOut()
-   fadeToggle()
-   fadeTo()

**slide methods**:

-   slideDown()
-   slideUp()
-   slideToggle()

**animate**:
```javascript
$("button").click(function(){  
	var div = $("div");  
	div.animate({left: '100px'}, "slow");  
	div.animate({fontSize: '3em'}, "slow");  
});
```
**stop**:
```javascript
$("#stop").click(function(){  
	$("#panel").stop();  
});
```
**$(_selector_).hide(_speed,callback_);**
```javascript
$("button").click(function(){  
	$("p").hide("slow", function(){  
		alert("The paragraph is now hidden");  
	});  
});
```
### DOM
Three simple, but useful, jQuery methods for DOM manipulation are:

-   text() - Sets or returns the **text content** of selected elements
-   html() - Sets or returns the content of selected elements (**including HTML markup**)
-   val() - Sets or returns the **value of form fields**
-   attr() - Gets attribute values.

Set with callback, which can be run for infinite times
```javascript
$(document).ready(function(){
    $("button").click(function(){
        $("#w3s").attr("href", function(i, origValue){
            return origValue + "/jquery/"; 
        });
    }); 
});
```
**append and prepend**
```javascript
$("p").append("Some appended text.");
$("p").prepend("Some prepended text.");
```
**remove and empty**
remove() method removes the selected element(s) and its child elements.
empty() method removes the child elements of the selected element(s).
```javascript
$("#div1").remove();
$("#div1").empty();
$("p").remove(".test, .demo");
```
**add class to interact with css**
```css
.important {  
font-weight:  bold;  
font-size:  xx-large;  
}  
  
.blue {  
color:  blue;  
}
```
```javascript
$("button").click(function(){  
	$("h1, h2, p").addClass("blue");  
	$("div").addClass("important");  
});

$("button").click(function(){  
	$("h1, h2, p").removeClass("blue");  
});

$("button").click(function(){  
	$("h1, h2, p").toggleClass("blue");  
});
```
```javascript
$("p").css("background-color", "yellow");
$("p").css({"background-color": "yellow", "font-size": "200%"});
```
![alt text](https://www.w3schools.com/Jquery/img_jquerydim.gif )
```javascript
$("button").click(function(){  
	var txt = "";  
	txt += "Inner width: " + $("#div1").innerWidth() + "</br>";  
	txt += "Inner height: " + $("#div1").innerHeight();  
	$("#div1").html(txt);  
});
```
### Traverse
```javascript
$(document).ready(function(){  
	$("span").parent();  
});

$(document).ready(function(){  
	$("div").children("p.first");  
});

$(document).ready(function(){
    $("div").find("*").css({"color": "red", "border": "2px solid red"});
});
```
Three useful jQuery methods for traversing up the DOM tree are:

-   parent()
-   parents()
-   parentsUntil()

Two useful jQuery methods for traversing down the DOM tree are:

-   children()
-   find()

There are many useful jQuery methods for traversing sideways in the DOM tree:

-   siblings()
-   next()
-   nextAll()
-   nextUntil()
-   prev()
-   prevAll()
-   prevUntil()

The most basic filtering methods are **first()**, **last()** and **eq()**, which allow you to select a specific element based on its position in a group of elements.

Other filtering methods, like **filter()** and **not()** allow you to select elements that match, or do not match, a certain criteria.
### Ajax
```javascript
$("#div1").load("demo_test.txt #p1");
```
```javascript
$.get(_URL,callback_);

$("button").click(function(){  
	$.get("demo_test.asp", function(data, status){  
		alert("Data: " + data + "\nStatus: " + status);  
	});  
});

$.post(_URL,data,callback_);

$(document).ready(function(){
    $("button").click(function(){
        $.post("demo_test_post.asp",
        {
          name: "Donald Duck",
          city: "Duckburg"
        },
        function(data,status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    });
});
```
### Misc
To identify JQuery because the other frameworks are also using $ sign
```javascript
$.noConflict();  
jQuery(document).ready(function(){  
	jQuery("button").click(function(){  
		jQuery("p").text("jQuery is still working!");  
	});  
});
```
```javascript
var jq = $.noConflict();  
	jq(document).ready(function(){  
		jq("button").click(function(){  
			jq("p").text("jQuery is still working!");  
		});  
});
```
#### Filterable Table
```javascript
$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
```
