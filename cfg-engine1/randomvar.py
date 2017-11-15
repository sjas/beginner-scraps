import random
from netaddr import *

# This file requires the netaddr library  pip3 install netaddr

### This file contains both the real values to place within the variables,
###  as well as the function to actually replace the variables within the
###  tasks that are passed to the function.


'''
netaddr primer:

rndip1 = rand_ip()   # my function to generate a random unicast IP (1 - 223, -127)

rndnet1 = IPNetwork(rndip1 + '/' + str(random.randint(8,30)))
rndnet1 is rndnet1.network     # is it the network address?
rndnet1 is rndnet1.broadcast   # is it the broadcast address?

rndnet1.ip                # ip address without CIDR notation
str(rndnet1)              # ip address with CIDR notation
rndnet1.network           # network address
rndnet1.broadcast         # broadcast address
rndnet1.netmask           # subnet mask
rndnet1.hostmask          # wildcard
rndnet1.prefixlen = 20    # change / assign different prefix length later
rndnet1.ip.bits()         # binary octets of IP address
rndnet1.network.bits()    # binary octets of network address
rndnet1.netmask.bits()    # binary octets of subnet mask
rndnet1.broadcast.bits()  # binary octets of broadcast address

list1 = list(rndnet1)     # creates a list of every IPAddress('x.x.x.x') in the range
len(list1)                # how many IPs are in the range
str(list1[1])             # access individual addresses in the range
str(random.choice(list1)) # random IP from range, includes net/bcast

for ip in rndnet1:        # print all IPs in range
    print(ip)

for ip in rndnet1.iter_hosts():  # print all host IPs in range (ex net/bcast)
    print(ip)

range1 = IPRange('start-ip', 'end-ip')  # creates arbitrary range

for ip in range1:   # print all IPs in arbitrary range
    print(ip)

# You can also compare IPAddress and IPNetwork in == < > <= >- != manner

'''


# takes task presented from tasks.py (via start.py) and puts actual values
def random_replace(task,answer):

    # Placing new function calls within this function is how new random
    #  values are selected for each new task, otherwise the same 'random'
    #  variable is selected over and over again. Sadly it took me many
    #  hours to work this out :-)


    # The following lines instantiate new randomized variables from other
    #  functions within this file

    rndser1 = rand_serial()    # returns single random sX/X interface
    rndser2 = rand_serial()
    rndser3 = rand_serial()
    rndser4 = rand_serial()

    # Make sure each is unique
    while rndser1 == rndser2 or rndser1 == rndser3 or rndser1 == rndser4:
        rndser1 = rand_serial()
    while rndser2 == rndser1 or rndser2 == rndser3 or rndser2 == rndser4:
        rndser2 = rand_serial()
    while rndser3 == rndser1 or rndser3 == rndser2 or rndser3 == rndser4:
        rndser3 = rand_serial()
    while rndser4 == rndser1 or rndser4 == rndser2 or rndser4 == rndser3:
        rndser4 = rand_serial()


    rndeth1 = rand_ethernet()  # returns single random eX/X interface
    rndeth2 = rand_ethernet()
    rndeth3 = rand_ethernet()
    rndeth4 = rand_ethernet()

    # Make sure each is unique
    while rndeth1 == rndeth2 or rndeth1 == rndeth3 or rndeth1 == rndeth4:
        rndeth1 = rand_ethernet()
    while rndeth2 == rndeth1 or rndeth2 == rndeth3 or rndeth2 == rndeth4:
        rndeth2 = rand_ethernet()
    while rndeth3 == rndeth1 or rndeth3 == rndeth2 or rndeth3 == rndeth4:
        rndeth3 = rand_ethernet()
    while rndeth4 == rndeth1 or rndeth4 == rndeth2 or rndeth4 == rndeth3:
        rndeth4 = rand_ethernet()


    rnduser = rand_user()       # random username from list
    rndpass = rand_pass()       # random password from list

    rndname1 = rand_name()      # random name from list of 500
    rndname2 = rand_name()
    rndname3 = rand_name()
    rndname4 = rand_name()

    # Make sure each name is unique
    while rndname1 == rndname2 or rndname1 == rndname3 or rndname1 == rndname4:
        rndname1 = rand_name()
    while rndname2 == rndname1 or rndname2 == rndname3 or rndname2 == rndname4:
        rndname2 = rand_name()
    while rndname3 == rndname1 or rndname3 == rndname2 or rndname3 == rndname4:
        rndname3 = rand_name()
    while rndname4 == rndname1 or rndname4 == rndname2 or rndname4 == rndname3:
        rndname4 = rand_name()


    rndpercent = rand_percent()  # random value between 0 - 100

    rnd100x1 = rand_100()   # 1 - 100
    rnd100x2 = rand_100()   # 1 - 100
    rnd100x3 = rand_100()   # 1 - 100
    rnd100x4 = rand_100()   # 1 - 100

    # Make sure each is unique
    while rnd100x1 == rnd100x2 or rnd100x1 == rnd100x3 or rnd100x1 == rnd100x4:
        rnd100x1 = rand_100()
    while rnd100x2 == rnd100x1 or rnd100x2 == rnd100x3 or rnd100x2 == rnd100x4:
        rnd100x2 = rand_100()
    while rnd100x3 == rnd100x1 or rnd100x3 == rnd100x2 or rnd100x3 == rnd100x4:
        rnd100x3 = rand_100()
    while rnd100x4 == rnd100x1 or rnd100x4 == rnd100x2 or rnd100x4 == rnd100x3:
        rnd100x4 = rand_100()

    rnd1000 = rand_1000() # 1 - 1000
    rnd4094 = rand_4094() # 1 - 4094 excluding 1002 - 1005
    rnd24 = rand_2_4()    # 2, 3 or 4


    # Generate single random unicast IP addresses
    rndip1 = rand_ip()
    rndip2 = rand_ip()
    rndip3 = rand_ip()
    rndip4 = rand_ip()

    # Place the random unicast IP addresses into a random /8 - /30
    rndnet1 = IPNetwork(rndip1 + '/' + str(random.randint(8,30)))
    rndnet2 = IPNetwork(rndip2 + '/' + str(random.randint(8,30)))
    rndnet3 = IPNetwork(rndip3 + '/' + str(random.randint(8,30)))
    rndnet4 = IPNetwork(rndip4 + '/' + str(random.randint(8,30)))

    # Choose a different random IP address and prefix if = net/bcast address
    while rndnet1.ip is rndnet1.network or rndnet1.ip is rndnet1.broadcast:
        rndip1 = rand_ip()
        rndnet1 = IPNetwork(rndip1 + '/' + str(random.randint(8,30)))
    while rndnet2.ip is rndnet2.network or rndnet2.ip is rndnet2.broadcast:
        rndip2 = rand_ip()
        rndnet2 = IPNetwork(rndip2 + '/' + str(random.randint(8,30)))
    while rndnet3.ip is rndnet3.network or rndnet3.ip is rndnet3.broadcast:
        rndip3 = rand_ip()
        rndnet3 = IPNetwork(rndip3 + '/' + str(random.randint(8,30)))
    while rndnet4.ip is rndnet4.network or rndnet4.ip is rndnet4.broadcast:
        rndip4 = rand_ip()
        rndnet4 = IPNetwork(rndip4 + '/' + str(random.randint(8,30)))

    # This function's IPs are completely isolated and separate from the above
    rndiprange1 = rand_iprange()  # returns /24 range, start ip, end ip
    rndiprange2 = rand_iprange()  #  as list elements 0,1,2
    rndiprange3 = rand_iprange()  #  useful for small IP pools
    rndiprange4 = rand_iprange()




    # This is where the placeholders from the task/answer are actually replaced
    #  with real values. All verification logic must be worked out above
    #  before reaching this point.

    task = task.replace('SINT1', rndser1)
    task = task.replace('SINT2', rndser2)
    task = task.replace('SINT3', rndser3)
    task = task.replace('SINT4', rndser4)

    task = task.replace('EINT1', rndeth1)
    task = task.replace('EINT2', rndeth2)
    task = task.replace('EINT3', rndeth3)
    task = task.replace('EINT4', rndeth4)

    task = task.replace('USERNAME', rnduser)
    task = task.replace('PASSWORD', rndpass)

    task = task.replace('NAME1', rndname1)
    task = task.replace('NAME2', rndname2)
    task = task.replace('NAME3', rndname3)
    task = task.replace('NAME4', rndname4)

    task = task.replace('PERCENT', str(rndpercent))
    task = task.replace('REVPCNT', str(100 - rndpercent))


    task = task.replace('RNDNET1IP', str(rndnet1.ip))        # IP
    task = task.replace('RNDNET1PFX', str(rndnet1.prefixlen))# the x in /x
    task = task.replace('RNDNET1CIDR', str(rndnet1))         # x.x.x.x/x
    task = task.replace('RNDNET1NET', str(rndnet1.network))  # network address
    task = task.replace('RNDNET1BC', str(rndnet1.broadcast)) # bcast address
    task = task.replace('RNDNET1MSK', str(rndnet1.netmask))  # subnet mask
    task = task.replace('RNDNET1WC', str(rndnet1.hostmask))  # wildcard mask

    task = task.replace('RNDNET2IP', str(rndnet2.ip))        # IP
    task = task.replace('RNDNET2PFX', str(rndnet2.prefixlen))# the x in /x
    task = task.replace('RNDNET2CIDR', str(rndnet2))         # x.x.x.x/x
    task = task.replace('RNDNET2NET', str(rndnet2.network))  # network address
    task = task.replace('RNDNET2BC', str(rndnet2.broadcast)) # bcast address
    task = task.replace('RNDNET2MSK', str(rndnet2.netmask))  # subnet mask
    task = task.replace('RNDNET2WC', str(rndnet2.hostmask))  # wildcard mask

    task = task.replace('RNDNET3IP', str(rndnet3.ip))        # IP
    task = task.replace('RNDNET3PFX', str(rndnet3.prefixlen))# the x in /x
    task = task.replace('RNDNET3CIDR', str(rndnet3))         # x.x.x.x/x
    task = task.replace('RNDNET3NET', str(rndnet3.network))  # network address
    task = task.replace('RNDNET3BC', str(rndnet3.broadcast)) # bcast address
    task = task.replace('RNDNET3MSK', str(rndnet3.netmask))  # subnet mask
    task = task.replace('RNDNET3WC', str(rndnet3.hostmask))  # wildcard mask

    task = task.replace('RNDNET4IP', str(rndnet4.ip))        # IP
    task = task.replace('RNDNET4PFX', str(rndnet4.prefixlen))# the x in /x
    task = task.replace('RNDNET4CIDR', str(rndnet4))         # x.x.x.x/x
    task = task.replace('RNDNET4NET', str(rndnet4.network))  # network address
    task = task.replace('RNDNET4BC', str(rndnet4.broadcast)) # bcast address
    task = task.replace('RNDNET4MSK', str(rndnet4.netmask))  # subnet mask
    task = task.replace('RNDNET4WC', str(rndnet4.hostmask))  # wildcard mask


    task = task.replace('RNDIPRANGE1', rndiprange1[0])   #x.x.x.x - y
    task = task.replace('RNDIPRANGEst1', rndiprange1[1]) #x.x.x.x
    task = task.replace('RNDIPRANGEen1', rndiprange1[2]) #x.x.x.y
    task = task.replace('RNDIPRANGE2', rndiprange2[0])
    task = task.replace('RNDIPRANGEst2', rndiprange2[1])
    task = task.replace('RNDIPRANGEen2', rndiprange2[2])
    task = task.replace('RNDIPRANGE3', rndiprange3[0])
    task = task.replace('RNDIPRANGEst3', rndiprange3[1])
    task = task.replace('RNDIPRANGEen3', rndiprange3[2])
    task = task.replace('RNDIPRANGE4', rndiprange4[0])
    task = task.replace('RNDIPRANGEst4', rndiprange4[1])
    task = task.replace('RNDIPRANGEen4', rndiprange4[2])

    task = task.replace('RND100x1', str(rnd100x1))
    task = task.replace('RND100x2', str(rnd100x2))
    task = task.replace('RND100x3', str(rnd100x3))
    task = task.replace('RND100x4', str(rnd100x4))
    task = task.replace('RND1K', str(rnd1000))
    task = task.replace('RND4094', str(rnd4094))
    task = task.replace('RND24', str(rnd24))





    answer = answer.replace('SINT1', rndser1)
    answer = answer.replace('SINT2', rndser2)
    answer = answer.replace('SINT3', rndser3)
    answer = answer.replace('SINT4', rndser4)
    answer = answer.replace('EINT1', rndeth1)
    answer = answer.replace('EINT2', rndeth2)
    answer = answer.replace('EINT3', rndeth3)
    answer = answer.replace('EINT4', rndeth4)

    answer = answer.replace('USERNAME', rnduser)
    answer = answer.replace('PASSWORD', rndpass)

    answer = answer.replace('NAME1', rndname1)
    answer = answer.replace('NAME2', rndname2)
    answer = answer.replace('NAME3', rndname3)
    answer = answer.replace('NAME4', rndname4)

    answer = answer.replace('PERCENT', str(rndpercent))
    answer = answer.replace('REVPCNT', str(100 - rndpercent))


    answer = answer.replace('RNDNET1IP', str(rndnet1.ip))        # IP
    answer = answer.replace('RNDNET1PFX', str(rndnet1.prefixlen))# the x in /x
    answer = answer.replace('RNDNET1CIDR', str(rndnet1))         # x.x.x.x/x
    answer = answer.replace('RNDNET1NET', str(rndnet1.network))  # network address
    answer = answer.replace('RNDNET1BC', str(rndnet1.broadcast)) # bcast address
    answer = answer.replace('RNDNET1MSK', str(rndnet1.netmask))  # subnet mask
    answer = answer.replace('RNDNET1WC', str(rndnet1.hostmask))  # wildcard mask

    answer = answer.replace('RNDNET2IP', str(rndnet2.ip))        # IP
    answer = answer.replace('RNDNET2PFX', str(rndnet2.prefixlen))# the x in /x
    answer = answer.replace('RNDNET2CIDR', str(rndnet2))         # x.x.x.x/x
    answer = answer.replace('RNDNET2NET', str(rndnet2.network))  # network address
    answer = answer.replace('RNDNET2BC', str(rndnet2.broadcast)) # bcast address
    answer = answer.replace('RNDNET2MSK', str(rndnet2.netmask))  # subnet mask
    answer = answer.replace('RNDNET2WC', str(rndnet2.hostmask))  # wildcard mask

    answer = answer.replace('RNDNET3IP', str(rndnet3.ip))        # IP
    answer = answer.replace('RNDNET3PFX', str(rndnet3.prefixlen))# the x in /x
    answer = answer.replace('RNDNET3CIDR', str(rndnet3))         # x.x.x.x/x
    answer = answer.replace('RNDNET3NET', str(rndnet3.network))  # network address
    answer = answer.replace('RNDNET3BC', str(rndnet3.broadcast)) # bcast address
    answer = answer.replace('RNDNET3MSK', str(rndnet3.netmask))  # subnet mask
    answer = answer.replace('RNDNET3WC', str(rndnet3.hostmask))  # wildcard mask

    answer = answer.replace('RNDNET4IP', str(rndnet4.ip))        # IP
    answer = answer.replace('RNDNET4PFX', str(rndnet4.prefixlen))# the x in /x
    answer = answer.replace('RNDNET4CIDR', str(rndnet4))         # x.x.x.x/x
    answer = answer.replace('RNDNET4NET', str(rndnet4.network))  # network address
    answer = answer.replace('RNDNET4BC', str(rndnet4.broadcast)) # bcast address
    answer = answer.replace('RNDNET4MSK', str(rndnet4.netmask))  # subnet mask
    answer = answer.replace('RNDNET4WC', str(rndnet4.hostmask))  # wildcard mask


    answer = answer.replace('RNDIPRANGE1', rndiprange1[0])   #x.x.x.x - y
    answer = answer.replace('RNDIPRANGEst1', rndiprange1[1]) #x.x.x.x
    answer = answer.replace('RNDIPRANGEen1', rndiprange1[2]) #x.x.x.y
    answer = answer.replace('RNDIPRANGE2', rndiprange2[0])
    answer = answer.replace('RNDIPRANGEst2', rndiprange2[1])
    answer = answer.replace('RNDIPRANGEen2', rndiprange2[2])
    answer = answer.replace('RNDIPRANGE3', rndiprange3[0])
    answer = answer.replace('RNDIPRANGEst3', rndiprange3[1])
    answer = answer.replace('RNDIPRANGEen3', rndiprange3[2])
    answer = answer.replace('RNDIPRANGE4', rndiprange4[0])
    answer = answer.replace('RNDIPRANGEst4', rndiprange4[1])
    answer = answer.replace('RNDIPRANGEen4', rndiprange4[2])


    answer = answer.replace('RND100x1', str(rnd100x1))
    answer = answer.replace('RND100x2', str(rnd100x2))
    answer = answer.replace('RND100x3', str(rnd100x3))
    answer = answer.replace('RND100x4', str(rnd100x4))
    answer = answer.replace('RND1K', str(rnd1000))
    answer = answer.replace('RND4094', str(rnd4094))
    answer = answer.replace('RND24', str(rnd24))



    # I'm sure there's a better way to do this, but oh well

    #print(task,answer)  #debug
    return task,answer

### Random Variables

def rand_serial():
    rndser1 = random.choice(['s0/0','s0/1','s0/2','s0/3','s1/0','s1/1','s1/2','s1/3',
                             's2/0','s2/1','s2/2','s2/3','s3/0','s3/1','s3/2','s3/3'])
    return rndser1

def rand_ethernet():
    rndeth1 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                             'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth1

def rand_user():
    # from http://jimpix.co.uk/words/random-username-generator.asp
    rnduser = random.choice(['skedaddleengineer','noddleresearcher','snoutannouncer',
        'bumfmillwright','dutygrammarian','idiopathiconlooker','gubbinsmourner',
        'folliclepodiatrist','doodleplayer','yahoogeologist','ladidaastronomer',
        'ciliadon','blubberbroker','masticatesinger','rigmarolemortician',
        'shenanigansoldier','shrubberytechnician','sassafrastailor','oblongphysicist',
        'poppycockdesigner','cougarshoemaker','turdiformbishop','spatulaminstrel',
        'gauzetherapist','doozypilot'])
    return rnduser

def rand_pass():
    # from http://www.dinopass.com/
    rndpass = random.choice(['@ngryRule41','hotS@lmon50','niceox99','wi$eLiquid28',
        '$caryParrot61','brownTh!ng51','lou)Ray12','uglyEn)15','fl@tJaguar57',
        'whi+eButton12','t!nyMoon99','f!rstGorilla15','sweetRa(coon89','longWorm97',
        '@ngryWave48','j@deMask42','oldL!quid19','heavyS!lk98','blac<Iron98',
        '<eenLead58','brownW!sh20','3mptyHelp19','!voryRing65',']adeLlama64',
        'm!styBrain92'])
    return rndpass

def rand_name():
    # from http://soybomb.com/tricks/words/
    rndname = random.choice(['surecred','coatemently','cognetism','patrud',
        'agonalted','tormating','comicker','shuttels','sasking','posible',
        'scophiteness','ferring','harisket','comilled','flocry','linetiones',
        'gaunlity','oducianis','broirs','antensollsy','thologicant','marred',
        'queath','aborging','capturonicale','rulexityrator','faities','condrively',
        'presseol','posignet','paraturnelasy','carillion','daligel','supertuggly',
        'bloclanch','sudatinization','boroseld','gustator','viatiosyned','coffix',
        'aferiums','cauthetinel','disgrudiscayer','sicompost','etuadom',
        'hellindistaths','cannibed','baggedoming','carrition','glintending',
        'examized','adjunce','claspeeleck','vaudity',
        'curvise','oduchibeers','adructions','leraterly','wassempods','truidled',
        'ganson','rollaheitele','saffers','turist','linoducted','barnstanizined',
        'navilizes','egarita','niannuish','forcomasizater','trings','sailostricath',
        'illsard','sclarlor','chnized','wettreving','bumpute','stinflaud',
        'saneliattently','catary','chainvey','petenny','baselled','jametaills',
        'acheal','wrappot','oligide','embefinaviner','beance','synouste',
        'bedrophitling','ementinger','heaviallism','pioneight','prever','hibility',
        'tracquises','couriner','reconven','eldevoy',
        'instiviting','kimoundiciphys','chaminglauther',
        'mounct','cornial','consing','adversers','partak','phying','dernated',
        'pliotably','footintrutes','standma','orthress','gramploy','rersessieg',
        'cheouser','chutole','saulattating','wirepers','lighwarding','fraurayized',
        'gartain','latick','scapter','shindonmenrink','parashant','expervoutwar',
        'luftovisp','wingalnes','bisquesqueged','mannerlopmenes','unimman','laxiel',
        'mastickens','gramals','hangerlance','oblity','granal','worksh',
        'nessnesshazes','delity','cought','procump','posupping','burgents',
        'bowmentionized','chewerated','chartiess','descess',
        'potefunna','medimisecrify','gradjan','catadeleves',
        'protocation','sculay','obeling','ficilliaseces','parcuring','ausconly',
        'libelarphipse','imanges','rategroide','bonderewithen','reples','diaggion',
        'eathms','bleare','streguidah','loweretersiffs','surestandes',
        'arpnesslewive','cauces','mcfaretramp','glopled','excepty','palinked',
        'jeantify','arizers','gaspiry','spirremnly','oblinatoing','fectedics',
        'coltical','stuyers','latickle','fausly','possemptorned','aggled',
        'payalivergive','mcconctuarne','supears','blenly','atioleved','disgrawbers',
        'adounctic','standyliverted','cutles','scafforthrons','acedgaternad',
        'defere','sweavelly','impromated','enturbely',
        'anations','haillicaly','misundided','forman','devors','extrous',
        'clochumousiver','mentics','stationsion','conjark','faularmobsum','allogy',
        'spanguiden','dowarex','overeliating','rouggling','stincoweasons','thertin',
        'moized','amplies','bation','acocry','gablan','soremyrocker','derson',
        'kingess','pacious','ilosely','visablons','foranow','worminvoyant',
        'perplawn','ingened','gelaring','barthweights','patherians',
        'refurrecterict','oveneshobbles','dantairs','lograms','endireburge',
        'mortighted','aphirobeds','abjuric','fudging','mounde',
        'tutitution','sembertaving','ferequainsole',
        'charremeg','throuts','oichee','contraze','confrong','rasorgeoscres',
        'livasquishoes','nosting','uratemenes','poledge','assignal','inating',
        'paripped','matects','subrington','prepar','venumbusnetrue','bossors',
        'agmatelockers','pinessur','exquennu','tahoolation','bastlessed','morammed',
        'regaton','proption','hiridises','rogenefable','crypor','safection',
        'mediff','shesseculp','reproffs','anbetraphy','dianizess','monshize',
        'unitiquit','modeouble','shdome','fleerinstria','tabovising','polina',
        'shoptorroric','gripulosive','primagic','overragger','lusible',
        'examinequetion','glitized','brassigned','tradams',
        'midley','desmalbayder','paused','somenesed','thinteril','brevitewayingf',
        'piterague','dogened','synctudete','mcbruity','tholiatorited','recognes',
        'stresomergan','garding','scendize','tionsketer','repric','prosoproquate',
        'radicaughts','chatioms','inklestal','hymelighte','rimery','mensegypt',
        'paremong','sionium','officksting','bastrily','primperper','hereve',
        'arctart','reorie','dancting','buchirrection','adraiming','caucate',
        'inizes','innond','disticithfuli','swantlinteness','sebaked','ostella',
        'porticanstine','affred','patrysics','formuteser',
        'trayantem','scotypes','fluenterrooted','unfirmico',
        'keneuted','amouncturbon','snuffsholer','sturriflece','famelowers',
        'leecterepuble','irresele','dreabound','boarcharitory','safeation','valrus',
        'maninged','compreled','shakowls','gurkinventing','exight','forchapplents',
        'honersalcoate','resencor','compet','regratomp','ronessagmens','belizes',
        'reintece','asturk','wickencevisift','notachned','bowsonal','planne',
        'drumbite','litiverns','flowinst','nicistic','thinintersest','fadiging',
        'descuffighly','redewdle','oveggs','arraten','flairingly','catter',
        'bellboottess','cogrances','derling','addeted','aldrod',
        'bowlets','fridgelizer','fewenholdson','grapprostly',
        'arescal','aboloutbition','holistraphot','triestion','trations','shadowled',
        'befruseharth','downstic','queeps','obseler','piecht','parationized',
        'autors','buttlen','sulton','scotisoffres','cushanize','pipereses',
        'focunds','gioverts','ficiese','havisignated','compeiscover','maninogard',
        'moduplifix','wagoured','shocers','putachape','shessimilly','catutall',
        'corrands','sociprehis','horric','sillanimagons','remoducer','surged',
        'dolphized','procle','dilounting','unctly','unemen','odiatio','humbrant',
        'clintrudes','lestoclar','comped',
        'nefigyroadest','irbalder','savoten','eudows',
        'apparang','baskethaverty','torious','formuting','rebourizes','calatte',
        'manuism','bottiersions','maciner','stulting','prottion','faunush',
        'discletend','cabiddy','presquility','webbon','berrots','bechindisams',
        'beessighted','anintruts','gartairding','pervists','micribily','orphilite',
        'furrecies','robuddentran','rantuingly','rooments','voyalikers','lousher',
        'bulbring','ionsibusly','reston','mither','diddadors','exconninat',
        'immelly','libeltimpectan','detructon','cheolong','darnity','mikong',
        'libesee','crypser','macheded','aimediscard'])
    return rndname

def rand_percent():
    rndpercent = random.randint(0,100)
    return rndpercent

def rand_ip():   # single random unicast IP address
    oct1 = random.randint(1,223)    # unicast range
    oct2 = random.randint(1,254)
    oct3 = random.randint(1,254)
    oct4 = random.randint(1,254)

    while oct1 == 127:   # choose a different value if 127
        oct1 = random.randint(1,223)

    rndip = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.' + str(oct4)

    return rndip


def rand_iprange():   # single unicast IP range within /24
    oct1 = random.randint(1,223)
    oct2 = random.randint(1,254)
    oct3 = random.randint(1,254)
    oct4 = random.randint(1,253)     #one less than max since it's a range
    endrange = random.randint(1,254)

    while oct1 == 127:   # choose a different value if 127
        oct1 = random.randint(1,223)

    while endrange < oct4:  # make sure the end is greater than the beginning
        endrange = random.randint(1,254)

    rndiprange = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.'\
                  + str(oct4) + " - " + str(endrange)

    rangestart = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.'\
                  + str(oct4)

    rangeend = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.'\
                  + str(endrange)

    return rndiprange,rangestart,rangeend


def rand_100():
    rnd100 = random.randint(1,100)
    return rnd100

def rand_1000():
    rnd1000 = random.randint(1,1000)
    return rnd1000

def rand_4094():  # intended for random VLAN selection
    rnd4094 = random.randint(1,4094)

    while rnd4094 == 1002 or rnd4094 == 1003 or\
          rnd4094 == 1004 or rnd4094 == 1005:    # exclude disallowed VLANs
        rnd4094 = random.randint(1,4094)

    return rnd4094

def rand_2_4():
    rnd24 = random.choice([2,3,4])
    return rnd24
