## 28/05/2018
### Summary
I set up the Github and create a folder keeping track of my work dairy and learning log. I watched half of the Django online courses on Udemy, focusing on data model creation, data migration and MTV pattern of Django, and put down some key notes. I also set up all the required environment on Pycharm, with Python 2.7.15, Django 1.8 and PostgreSQL 10.4.
### Github setup
```
git status
git add -A
git commit -m "some comments"
git pull origin branch
git push -u origin branch

git branch
git checkout master
git remote set-url git@github.com:E1even1ee/djangotest.git
```
### PostgreSQL
Start the server
```
C:\Users\lizh1\Documents\workspace\resource\pgsql\bin
> pg_ctl -D ^"C^:^\Users^\lizh1^\Documents^\workspace^\resource^\pgsql^\data^" -l logfile start
```
Stop the server
```
> pg_ctl stop -D ^"C^:^\Users^\lizh1^\Documents^\workspace^\resource^\pgsql^\data^"
```
#### PostgreSQL
**Username:**
postgres
**Password:**
ey
#### Django superuser
**Username:**
admin
**Password:**
ey
