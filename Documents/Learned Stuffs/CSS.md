## CSS Catch-up
```css
#top {
    background-color: #ccc;
    padding: 20px
}

.intro {
    color: red;
    font-weight: bold;
}
```
**#** is for ID selector and **.** is for Class selector

HTML selectors don't need special prefix

The difference between an ID and a class is that an **ID** can be used to identify **one element**, whereas a **class** can be used to identify **more than one**.

But if you are using special selectors inside HTML element, you can identify it with **body.jam**

Grouping
```css
h2, .thisOtherClass, .yetAnotherClass {
    color: red;
}
```
Nesting
```html
<div id="top">
    <h1>Chocolate curry</h1>
    <p>This is my recipe for making curry purely with chocolate</p>
    <p>Mmm mm mmmmm</p>
</div>
```
```css
#top {
    background-color: #ccc;
    padding: 1em
}

#top h1 {
    color: #ff0;
}

#top p {
    color: red;
    font-weight: bold;
}
```
Shorthand properties
```css
p {
    margin-top: 1px;
    margin-right: 5px;
    margin-bottom: 10px;
    margin-left: 20px;
}
```
Can be summed up following pattern top-right-bottom-left:
```css
p {
    margin: 1px 5px 10px 20px;
}
```
```css
p {
    border-width: 1px;
    border-color: red;
    border-style: solid;
}
```
Can be simplified as:
```css
p {
    border: 1px red solid;
}
```
padding means 30px for **top and bottom**; 10px for **right and left**
```css
p {
    font: 14px/1.5 "Times New Roman", times, serif;
    padding: 30px 10px;
    border: 1px black solid;
    border-width: 1px 5px 5px 1px;
    border-color: red green blue yellow;
    margin: 10px 50px;
}
```
background image
```css
body {
    background: white url(http://www.htmldog.com/images/bg.gif) no-repeat top right;
}
```
background-color
background-image
background-repeat: repeat, repeat-y, repeat-x, no-repeat
background-position: top, center, bottom, left, right

### Specificity
If the selectors are the same then the ***last*** one will always take precedence.
The ***more specific*** a selector, the more preference it will be given when it comes to conflicting styles.

Calculation of specificity:
The actual specificity of a group of nested selectors takes some calculating. You can give every **ID selector**(“#whatever”) a value of **100**, every **class selector** (“.whatever”) a value of **10** and every **HTML selector**(“whatever”) a value of **1**. When you add them all up, hey presto, you have a specificity value.

```css
li { display: inline }
```
![alt text](http://htmldog.com/figures/displayInline.png "Inline")

```css
#navigation a {
    display: block;
    padding: 20px 10px;
}
```
![alt text](http://htmldog.com/figures/displayBlock.png "block")
```css
#navigation, #related_links { display: none }
```
### Rounded border
[`border-top-left-radius`](http://htmldog.com/references/css/properties/border-top-left-radius/), [`border-top-right-radius`](http://htmldog.com/references/css/properties/border-top-right-radius/), [`border-bottom-right-radius`](http://htmldog.com/references/css/properties/border-bottom-right-radius/), and [`border-bottom-left-radius`](http://htmldog.com/references/css/properties/border-bottom-left-radius/)
```css
#monroe {
    background: #fff;
    width: 100px;
    height: 100px;
    border-radius: 6px 12px 18px 24px;
}
```
### Special Selectors
#### Universal selectors
Using a standalone universal selector is commonly used to “reset” many of a browser’s default styles. Setting a margin to zero, for example, will kill all spacing around the likes of paragraphs, headings and blockquotes.
```css
* {
    margin: 0;
    padding: 0;
}

#contact * {
    display: block;
}
```
#### Child selectors
```html
<ul id="genus_examples">
    <li>Cats
        <ul>
            <li>Panthera</li>
            <li>Felis</li>
            <li>Neofelis</li>
        </ul>
    </li>
    <li>Apes
        <ul>
            <li>Pongo</li>
            <li>Pan</li>
            <li>Homo</li>
        </ul>
    </li>
</ul>
```
CSS:
```css
#genus_examples > li { border: 1px solid red }
```
#### Adjacent selectors
```html
<h1>Clouded leopards</h1>
<p>Clouded leopards are cats that belong to the genus Neofelis.</p>
<p>There are two extant species: Neofelis nebulosa and Neofelis diardi.</p>
```
```css
h1 + p { font-weight: bold }
```
Only the first paragraph, that following the heading, will be made bold.
```css
h1 ~ p { font-weight: bold }
```
All siblings at the same level.
#### Colors
```css
h1 {
    padding: 50px;
    background-image: url(snazzy.jpg);
    color: rgba(0,0,0,0.8);
}
```
rgba(0,0,0,0.8) is saying red=“0”, green=“0”, blue=“0”, alpha=“0.8”, which, all together, makes it 80% black.
```css
#smut { color: hsl(36, 100%, 50%) }
```
```css
#rabbit { background: hsla(0, 75%, 75%, 0.5) }
```
### Animation and Transition
-   [`transition-property`](http://htmldog.com/references/css/properties/transition-property/): which property (or properties) will transition.
-   [`transition-duration`](http://htmldog.com/references/css/properties/transition-duration/): how long the transition takes.
-   [`transition-timing-function`](http://htmldog.com/references/css/properties/transition-timing-function/): if the transition takes place at a constant speed or if it accelerates and decelerates.
-   [`transition-delay`](http://htmldog.com/references/css/properties/transition-delay/): how long to wait until the transition takes place.
```css
a:link {
    transition: all .5s linear 0;
    color: hsl(36,50%,50%);
}
a:hover {
    color: hsl(36,100%,50%);
}
```
### Transformation
![alt text](http://htmldog.com/figures/transform.png "block")
```css
.note {
    width: 300px;
    height: 300px;
    background: hsl(36,100%,50%);
}
```
```css
transform: rotate(-10deg);
```
```css
transform: skew(20deg,10deg);
```
```css
transform: scale(1,2);
```
```css
transform: translate(100px,200px);
```
Combining
```css
transform: rotate(-10deg) scale(2);
```
### Gradients
```css
background: linear-gradient(to bottom right, orange, red);
```
```css
background: radial-gradient(circle, yellow, green);
```
