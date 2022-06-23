import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 15th Aug']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['srinu', 'tarunu','mallesh', 'swamy', 'pavan']
residence = ['Georgia','Russia', 'Armenia', 'USA', 'Germany']
went = ['cinema', 'university','seminar', 'school', 'park']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))