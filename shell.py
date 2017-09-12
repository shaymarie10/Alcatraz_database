import core, time, sys
typing_speed = 24


def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


slow_type('You have entered present day of the 1940s.')
print('Alcatraz Prison Database.')
time.sleep(1)

prison = core.Prison([
    core.Prisoner(
        'Alphonse Gabriel "Al" Capone', '2536', 'Scarface', 41, '1/18/1899',
        'New York', 'tax invasion',
        'Capones mental state is the capacity of a 12 year old boy. He hillucinates and becomes dilusional often.'
    ),
    core.Prisoner(
        'George Kelly', '6732', 'Machine Gun Kelly', 55, '7/18/1885',
        'Tennessee', 'kidnap, armed robbery',
        'Kelly was mocked for his nickname as he was called pop gun kelly. He was not seen as a threat but more of a joke of mockery.'
    ),
    core.Prisoner('Robert Stoud', '1520', 'Birdman of Alcatraz', 52,
                  '1/28/1890', 'Washington', 'manslaughter',
                  'Psychopathic personality of Superior Intelligence. IQ 112'),
    core.Prisoner(
        'Henri Young', '5392', 'unknown', 29, '6/20/1911', 'Missouri',
        'manslaughter, bank robbery',
        'Young sleepwalks and has dual personality, irresistible impulse and dissociation of ideas, strange psycho-physiological states in which the body acts while the mind sleeps'
    ),
    core.Prisoner(
        'Mickey Cohen', '3134', 'King of Los Angeles', 27, '9/4/1913',
        'New York', 'mafia ties',
        'No mental disorders discovered even though Mickey was hemoraging from the head due to the bludgeon of a fellow inmate in Mickeys sleep'
    ),
    core.Prisoner(
        'Basal Banghart', '1441', 'The Owl', 39, '9/11/1901', 'Michigan',
        'kidnap',
        'Banghart is a prison escape artist. His work is diligent and precise. His mental state is intact with reality, Banghart is remarkably intelligient but chooses to fight against the law.'
    ),
    core.Prisoner(
        'Bernard Coy', '8256', 'Barney', 40, '2/13/1900', 'Kentucky',
        'bank robbery',
        'Coy is a very precise and observant mind. He prays on the weak and is an expert manipulator. He is impulsive and his motives are dangerous.'
    ),
    core.Prisoner(
        'Rufus Franklin', '3352', 'Whitey', 24, '1/15/1916', 'Alabama',
        'murder, grand theft auto',
        'Methodical thinker, Franklin finds thrill in the challenge of the law'
    ),
    core.Prisoner(
        'Herbert Farmer', '2763', 'Deafy', 49, '3/9/1891', 'Missouri',
        'participation of conspiracy escape',
        'Farmer owned an underworld fugitive safe house. Besides conspiracy of participation, he was known for larceny and swindling. His motives to help felons is unknown.'
    ),
])

print("""

                    __            ================================
         ALCATRAZ  /__\            ||     ||<(.)>||<(.)>||     || 
       ____________|  |            ||    _||     ||     ||_    || 
       |_|_|_|_|_|_|  |            ||   (__D     ||     C__)   || 
       |_|_|_|_|_|_|__|            ||   (__D     ||     C__)   ||
      A@\|_|_|_|_|_|/@@Aa          ||   (__D     ||     C__)   ||
   aaA@@@@@@@@@@@@@@@@@@@aaaA      ||   (__D     ||     C__)   ||
  A@@@@@@@@@@@DWB@@@@@@@@@@@@A     ||     ||     ||     ||  dwb||
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ================================""")

authority = ['shay shuffield', 'jane smith', 'jay cox']
name = input('Authorized only. Please enter your name').strip().lower()

'int int->  int'
if name in authority:
    print('Welcome ' + name)

    code = input('To proceed please enter your certified ID number').strip()
    if code == '102944':
        print('confirmed')
    else:
        print('access denied.')
else:
    print('This name is not authorized.')

'str str -> str'
confirmation = input(
    'I hereby solemenly swear I am who I say I am. Enter your first & last name for confirmation'
).strip()

if name in authority:
    print('You have enter the database of Alcatraz.')

    print(
        '''\t1 Alphonse Capone\tid number-2536\n\t2 George Kelly\tid number-6732\n\t3 Robert Stoud\tid number-1520\n\t4 Henri Young\tid number-5392\n\t5 Mickey Cohen\tid number-3134\n\t6 Basel Bangnart\tid number-1441\n\t7 Bernard Coy\tid number-8256\n\t8 Rufus Franklin\tid number-3352\n\t9 Herbert Farmer\tid number-2763\n'''
    )
    while True:
        search_inmate = input(
            'Key in the id number of the inmate you wish to see.').strip()

        x = prison.find_by_id(search_inmate)
        print(x)
        background = input(
            'Key in xxx for additional information on a particular inmate. Press n for no.'
        )
        if background == 'xxx':
            print(x.background)
        if background == 'n':
            print('Your request has been noted.')

else:
    print('Your confirmation was denied.')
