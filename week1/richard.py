# height score

print ('what is your height in centimetres?')
height=input('my height is: ')

if 170 <= height <= 180:
    print('you are a little too tall for me')
    height = 1
elif height > 180:
    print('sorry you far too tall for me')
    height = 0
elif 160 <= height <= 169:
    print('you are the perfect height!')
    height = 2
else:
    print ('you are a little short for me ')
    height = 1

print('your score so far is %s out of 2') % height

# what activity do you like most?

print ('Which of the following would you like to do most? 1) watching sport , 2) go to the movies, 3) party or 4) write python code?')
activity=raw_input('the activity I like most is: ')

if activity == 'watching sport':
    print('good choice, not quite my favorite though...')
    activity = 2
elif activity=='go to the movies':
    print('sorry the movies is far from my favorite activity')
    activity = 1
elif activity=='party':
    print('yes I like to party too, not quite my favorite though')
    activity = 2
elif activity=='write python code':
    print('I love to code too, top marks from me!!!')
    activity = 3
else:
    print ('sorry 0 points, you cannot follow simple instructions')
    activity = 0
second_score=height+activity

print('your score so far is %s out of 5') % second_score
