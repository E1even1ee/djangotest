## 18/06/2018
### Summary
### LinkedIn API
```python
from linkedin import linkedin
API_KEY = "863k3zflrmrr0s"
API_SECRET = "kmSPuEasunuumHMC"
RETURN_URL = "http://localhost:8000"

TOKEN = "AQVnH8IItEgIf95GYfM3wUInxtitFkn8V3UCyG6yZ9OR7u5W-cqmXcVepB61_bcENT5q3sWZPwLjMhxBxbprMKhSA20UTpKJbTM9hhiv7Xu-I45Po3pvhz95UU2llhEV8SvNITQ21OKeDmOtWIjScfLtXTm0tUeGiqktT5qXy9MMGj2XxbYMDLjrqjNbFv78SnFyjiQNrZoxjspdS7sSJiEbcGDEu_8xgxc0eU1WIu8NrYoXAVXwsXmYYSY7qwUtw4hOsHIFKPeLFbLyaX2ghc1MSsz_uzdsaV8jZomCF0gU1sF-rxhxPrf03-Hs0kd74y6E6BXYkzTpDbIJ6X9MOaBFXgF0Eg"
APPLICATION = linkedin.LinkedInApplication(token=TOKEN)
```
### Get Profile
```python
APPLICATION.get_profile()
```
```python
{u'headline': u'Developer | Consultant at EY Quantitative Services', u'lastName': u'Li', u'siteStandardProfileRequest': {u'url': u'https://www.linkedin.com/profile/view?id=AAoAAB62WnsBgsJqAU4rlFiG2qctt9C_dQozEh0&authType=name&authToken=yvKG&trk=api*a5603906*s5799096*'}, u'id': u'iHNVBII7Df', u'firstName': u'Zheng(Elevn)'}
```
```python
APPLICATION.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
```
```json
{u'distance': 0, u'numConnections': 257, u'firstName': u'Zheng(Elevn)', u'lastName': u'Li', u'location': {u'country': {u'code': u'au'}, u'name': u'Sydney, Australia'}, u'id': u'iHNVBII7Df'}
```
Profile Fields Description
https://developer.linkedin.com/docs/fields
### Search Company
```python
search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})
```
```json
{u'companies': {u'_total': 2523, u'_count': 10, u'_start': 0, u'values': [{u'websiteUrl': u'http://thinkbiglearnsmart.com', u'universalName': u'think-big-learn-smart', u'name': u'ThinkB!G.LearnSmart - Adobe, Apple, & Microsoft Authorized Training Center'}, {u'websiteUrl': u'www.i4ict.com', u'universalName': u'i4ict', u'name': u'I4ICT - Apple, Microsoft & Google Apps Specialist'}, {u'websiteUrl': u'www.alliancedata.com', u'universalName': u'alliance-data', u'name': u'Alliance Data'}, {u'websiteUrl': u'http://business.nasdaq.com', u'universalName': u'nasdaq', u'name': u'Nasdaq'}, {u'websiteUrl': u'http://www.idaireland.com', u'universalName': u'ida-ireland', u'name': u'IDA Ireland'}, {u'websiteUrl': u'Olacabs.com', u'universalName': u'olacabs-com', u'name': u'Ola (ANI Technologies Pvt. Ltd)'}, {u'websiteUrl': u'www.netcomlearning.com', u'universalName': u'netcom-learning', u'name': u'NetCom Learning'}, {u'websiteUrl': u'www.nhls.com', u'universalName': u'nh-learning-solutions', u'name': u'NH Learning Solutions Corporation'}, {u'websiteUrl': u'http://www.ccbtechnology.com', u'universalName': u'ccb', u'name': u'CCB Technology'}, {u'websiteUrl': u'www.techrepublic.com', u'universalName': u'techrepublic', u'name': u'TechRepublic'}]}}
```
### Network API
```python
from linkedin.linkedin import NETWORK_UPDATES
print NETWORK_UPDATES.enums
{'APPLICATION': 'APPS',
 'CHANGED_PROFILE': 'PRFU',
 'COMPANY': 'CMPY',
 'CONNECTION': 'CONN',
 'EXTENDED_PROFILE': 'PRFX',
 'GROUP': 'JGRP',
 'JOB': 'JOBS',
 'PICTURE': 'PICT',
 'SHARED': 'SHAR',
 'VIRAL': 'VIRL'}
```
### ~~Services that need a partner account~~
~~Get connection~~
```python
APPLICATION.get_connections()
```
~~Search Profile~~
```python
APPLICATION.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})
```
~~Search Jobs~~
```python
APPLICATION.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'python', 'count': 2})
```
~~Group API~~
```python
APPLICATION.get_group(41001)
{u'id': u'41001', u'name': u'Object Oriented Programming'}

APPLICATION.get_memberships(params={'count': 20})
{u'_total': 1,
 u'values': [{u'_key': u'25827',
   u'group': {u'id': u'25827', u'name': u'Python Community'},
   u'membershipState': {u'code': u'member'}}]}

APPLICATION.get_posts(41001)

APPLICATION.get_post_comments(
    %POST_ID%,
    selectors=[
        {"creator": ["first-name", "last-name"]},
        "creation-timestamp",
        "text"
    ],
    params={"start": 0, "count": 20}
)

title = 'Scala for the Impatient'
summary = 'A new book has been published'
submitted_url = 'http://horstmann.com/scala/'
submitted_image_url = 'http://horstmann.com/scala/images/cover.png'
description = 'It is a great book for the keen beginners. Check it out!'

APPLICATION.submit_group_post(41001, title, summary, submitted_url, submitted_image_url, description)
```
~~Company API~~
```python
APPLICATION.get_company_updates(1035, params={'count': 2})
```
```json
# Get the latest updates about Microsoft
application.get_company_updates(1035, params={'count': 2})
{u'_count': 2,
 u'_start': 0,
 u'_total': 58,
 u'values': [{u'isCommentable': True,
   u'isLikable': True,
   u'isLiked': False,
   u'numLikes': 0,
   u'timestamp': 1363855486620,
   u'updateComments': {u'_total': 0},
   u'updateContent': {u'company': {u'id': 1035, u'name': u'Microsoft'},
    u'companyJobUpdate': {u'action': {u'code': u'created'},
     u'job': {u'company': {u'id': 1035, u'name': u'Microsoft'},
      u'description': u'Job Category: SalesLocation: Sacramento, CA, USJob ID: 812346-106756Division: Retail StoresStore...',
      u'id': 5173319,
      u'locationDescription': u'Sacramento, CA, US',
      u'position': {u'title': u'Store Manager, Specialty Store'},
      u'siteJobRequest': {u'url': u'http://www.linkedin.com/jobs?viewJob=&jobId=5173319'}}}},
   u'updateKey': u'UNIU-c1035-5720424522989961216-FOLLOW_CMPY',
   u'updateType': u'CMPY'},
  {u'isCommentable': True,
   u'isLikable': True,
   u'isLiked': False,
   u'numLikes': 0,
   u'timestamp': 1363855486617,
   u'updateComments': {u'_total': 0},
   u'updateContent': {u'company': {u'id': 1035, u'name': u'Microsoft'},
    u'companyJobUpdate': {u'action': {u'code': u'created'},
     u'job': {u'company': {u'id': 1035, u'name': u'Microsoft'},
      u'description': u'Job Category: Software Engineering: TestLocation: Redmond, WA, USJob ID: 794953-81760Division:...',
      u'id': 5173313,
      u'locationDescription': u'Redmond, WA, US',
      u'position': {u'title': u'Software Development Engineer in Test, Senior-IEB-MSCIS (794953)'},
      u'siteJobRequest': {u'url': u'http://www.linkedin.com/jobs?viewJob=&jobId=5173313'}}}},
   u'updateKey': u'UNIU-c1035-5720424522977378304-FOLLOW_CMPY',
   u'updateType': u'CMPY'}]}
```
~~Job API~~
```python
APPLICATION.get_job(job_id=5174636)
```
```json
{u'active': True,
 u'company': {u'id': 2329, u'name': u'Schneider Electric'},
 u'descriptionSnippet': u"The Industrial Accounts Sales Manager is a quota carrying senior sales position principally responsible for generating new sales and growing company's share of wallet within the industrial business, contracting business and consulting engineering business. The primary objective is to build and establish strong and lasting relationships with technical teams and at executive level within specific in",
 u'id': 5174636,
 u'position': {u'title': u'Industrial Accounts Sales Manager'},
 u'postingTimestamp': 1363860033000}
```
