## HTML Catch-up
```html
<p>Yes, that really <em>is</em> exciting. <strong>Warning:</strong> level of excitement may cause head to explode.</p>
```
Paragraph element makes each content into a **separate line**

### ***p*** vs ***br***

It could be tempting to over-use line breaks and [`br`](http://htmldog.com/references/html/tags/br/) shouldn’t be used if two blocks of text are intended to be separate from one another (because if that’s what you want to do you probably want the [`p`](http://htmldog.com/references/html/tags/p/) tag).
### Headings
```html
<!DOCTYPE html>

<html>

<head>
    <title>My first web page</title>
</head>

<body>
    <h1>My first web page</h1>

    <h2>What this is</h2>
    <p>A simple page put together using HTML</p>

    <h2>Why this is</h2>
    <p>To learn HTML</p>
</body>

</html>
```

### ***ol*** vs ***ul***
**ol** comes with default sequence
### Image
```html
<img src="http://www.htmldog.com/badge1.gif" width="120" height="90" alt="HTML Dog">
```
### Form
```html
<form action="contactus.php" method="post">

    <p>Name:</p>
    <p><input type="text" name="name" value="Your name"></p>

    <p>Species:</p>
    <p><input name="species"></p>
    <!-- remember: 'type="text"' isn't actually necessary -->

    <p>Comments: </p>
    <p><textarea name="comments" rows="5" cols="20">Your comments</textarea></p>

    <p>Are you:</p>
    <p><input type="radio" name="areyou" value="male"> Male</p>
    <p><input type="radio" name="areyou" value="female"> Female</p>
    <p><input type="radio" name="areyou" value="hermaphrodite"> An hermaphrodite</p>
    <p><input type="radio" name="areyou" value="asexual"> Asexual</p>

    <p><input type="submit"></p>

</form>
```
### ***span*** vs ***div***
They are used to group together a chunk of HTML and hook some information onto that chunk, most commonly with the attributes `class`and `id` to associate the element with a [class or id CSS selector](http://htmldog.com/guides/css/intermediate/classid/).

The difference between [`span`](http://htmldog.com/references/html/tags/span/) and [`div`](http://htmldog.com/references/html/tags/div/) is that a [`span`](http://htmldog.com/references/html/tags/span/) element is **in-line** and usually used for a small chunk of HTML inside a line (such as inside a paragraph) whereas a [`div`](http://htmldog.com/references/html/tags/div/) (division) element is **block-line** (which is basically equivalent to having a line-break before and after it) and used to group larger chunks of code.

### Table
colspan and rowspan
```html
<table>
    <tr>
        <th>Column 1 heading</th>
        <th>Column 2 heading</th>
        <th>Column 3 heading</th>
    </tr>
    <tr>
        <td>Row 2, cell 1</td>
        <td colspan="2">Row 2, cell 2, also spanning Row 2, cell 3</td>
    </tr>
    <tr>
        <td rowspan="2">Row 3, cell 1, also spanning Row 4, cell 1</td>
        <td>Row 3, cell 2</td>
        <td>Row 3, cell 3</td>
    </tr>
    <tr>
        <td>Row 4, cell 2</td>
        <td>Row 4, cell 3</td>
    </tr>
</table>
```
### Select
```html
<form action="dogselecta.php">
    <select name="dog">
        <option>Arctic Fox</option>
        <option>Maned Wolf</option>
        <option>Grey Wolf</option>
        <option>Red Fox</option>
        <option>Fennec</option>
        <option selected>Domestic Dog</option>
    </select>
    <input type="submit">
</form>
```
