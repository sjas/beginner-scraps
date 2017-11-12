import random

### This file contains both the real values to place within the variables,
###  as well as the function to actually replace the variables within the
###  tasks that are passed to the function.

# takes task presented from tasks.py (via start.py) and puts actual values
def random_replace(task,answer):

    # Placing new function calls within this function is how new random
    #  values are selected for each new task, otherwise the same 'random'
    #  variable is selected over and over again. Sadly it took me many
    #  hours to work this out :-) These next few lines cause a new random
    #  element to be selected from the appropriate list when called.
    rndser1 = rand_ser1()
    rndser2 = rand_ser2()
    rndser3 = rand_ser3()
    rndser4 = rand_ser4()
    rndeth1 = rand_eth1()
    rndeth2 = rand_eth2()
    rndeth3 = rand_eth3()
    rndeth4 = rand_eth4()
    rndeth5 = rand_eth5()
    rndeth6 = rand_eth6()
    rndeth7 = rand_eth7()
    rndeth8 = rand_eth8()
    rnduser = rand_user()
    rndpass = rand_pass()
    rndhost1 = rand_host1()
    rndhost2 = rand_host2()
    rndhost3 = rand_host3()
    rndhost4 = rand_host4()
    rndhost5 = rand_host5()
    rndhost6 = rand_host6()
    rndhost7 = rand_host7()
    rndhost8 = rand_host8()
    rndhost9 = rand_host9()
    rndhost10 = rand_host10()
    # Maybe I went a little overboard on hostnames? :-) 10x50

    # This is where the placeholder from the task/answer is actually replaced
    #  with a real value
    task = task.replace('SINT1', rndser1)
    task = task.replace('SINT2', rndser2)
    task = task.replace('SINT3', rndser3)
    task = task.replace('SINT4', rndser4)
    task = task.replace('EINT1', rndeth1)
    task = task.replace('EINT2', rndeth2)
    task = task.replace('EINT3', rndeth3)
    task = task.replace('EINT4', rndeth4)
    task = task.replace('EINT5', rndeth5)
    task = task.replace('EINT6', rndeth6)
    task = task.replace('EINT7', rndeth7)
    task = task.replace('EINT8', rndeth8)
    task = task.replace('USERNAME', rnduser)
    task = task.replace('PASSWORD', rndpass)
    task = task.replace('HOSTNAME1', rndhost1)
    task = task.replace('HOSTNAME2', rndhost2)
    task = task.replace('HOSTNAME3', rndhost3)
    task = task.replace('HOSTNAME4', rndhost4)
    task = task.replace('HOSTNAME5', rndhost5)
    task = task.replace('HOSTNAME6', rndhost6)
    task = task.replace('HOSTNAME7', rndhost7)
    task = task.replace('HOSTNAME8', rndhost8)
    task = task.replace('HOSTNAME9', rndhost9)
    task = task.replace('HOSTNAME10', rndhost10)

    answer = answer.replace('SINT1', rndser1)
    answer = answer.replace('SINT2', rndser2)
    answer = answer.replace('SINT3', rndser3)
    answer = answer.replace('SINT4', rndser4)
    answer = answer.replace('EINT1', rndeth1)
    answer = answer.replace('EINT2', rndeth2)
    answer = answer.replace('EINT3', rndeth3)
    answer = answer.replace('EINT4', rndeth4)
    answer = answer.replace('EINT5', rndeth5)
    answer = answer.replace('EINT6', rndeth6)
    answer = answer.replace('EINT7', rndeth7)
    answer = answer.replace('EINT8', rndeth8)
    answer = answer.replace('USERNAME', rnduser)
    answer = answer.replace('PASSWORD', rndpass)
    answer = answer.replace('HOSTNAME1', rndhost1)
    answer = answer.replace('HOSTNAME2', rndhost2)
    answer = answer.replace('HOSTNAME3', rndhost3)
    answer = answer.replace('HOSTNAME4', rndhost4)
    answer = answer.replace('HOSTNAME5', rndhost5)
    answer = answer.replace('HOSTNAME6', rndhost6)
    answer = answer.replace('HOSTNAME7', rndhost7)
    answer = answer.replace('HOSTNAME8', rndhost8)
    answer = answer.replace('HOSTNAME9', rndhost9)
    answer = answer.replace('HOSTNAME10', rndhost10)
    # I'm sure there's a better way to do this, but oh well

    #print(task,answer)  #debug
    return task,answer

### Random Variables

def rand_ser1():
    rndser1 = random.choice(['s0/0','s0/1','s0/2','s0/3','s1/0','s1/1','s1/2','s1/3',
                            's2/0','s2/1','s2/2','s2/3','s3/0','s3/1','s3/2','s3/3'])
    return rndser1

def rand_ser2():
    rndser2 = random.choice(['s0/0','s0/1','s0/2','s0/3','s1/0','s1/1','s1/2','s1/3',
                            's2/0','s2/1','s2/2','s2/3','s3/0','s3/1','s3/2','s3/3'])
    return rndser2

def rand_ser3():
    rndser3 = random.choice(['s0/0','s0/1','s0/2','s0/3','s1/0','s1/1','s1/2','s1/3',
                            's2/0','s2/1','s2/2','s2/3','s3/0','s3/1','s3/2','s3/3'])
    return rndser3

def rand_ser4():
    rndser4 = random.choice(['s0/0','s0/1','s0/2','s0/3','s1/0','s1/1','s1/2','s1/3',
                            's2/0','s2/1','s2/2','s2/3','s3/0','s3/1','s3/2','s3/3'])
    return rndser4

def rand_eth1():
    rndeth1 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth1

def rand_eth2():
    rndeth2 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth2

def rand_eth3():
    rndeth3 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth3

def rand_eth4():
    rndeth4 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth4

def rand_eth5():
    rndeth5 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth5

def rand_eth6():
    rndeth6 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth6

def rand_eth7():
    rndeth7 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth7

def rand_eth8():
    rndeth8 = random.choice(['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
                            'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3'])
    return rndeth8

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

def rand_host1():
    # from http://soybomb.com/tricks/words/
    rndhost1 = random.choice(['surecred','coatemently','cognetism','patrud',
        'agonalted','tormating','comicker','shuttels','sasking','posible',
        'scophiteness','ferring','harisket','comilled','flocry','linetiones',
        'gaunlity','oducianis','broirs','antensollsy','thologicant','marred',
        'queath','aborging','capturonicale','rulexityrator','faities','condrively',
        'presseol','posignet','paraturnelasy','carillion','daligel','supertuggly',
        'bloclanch','sudatinization','boroseld','gustator','viatiosyned','coffix',
        'aferiums','cauthetinel','disgrudiscayer','sicompost','etuadom',
        'hellindistaths','cannibed','baggedoming','carrition','glintending'])
    return rndhost1

def rand_host2():
    rndhost2 = random.choice(['examized','adjunce','claspeeleck','vaudity',
        'curvise','oduchibeers','adructions','leraterly','wassempods','truidled',
        'ganson','rollaheitele','saffers','turist','linoducted','barnstanizined',
        'navilizes','egarita','niannuish','forcomasizater','trings','sailostricath',
        'illsard','sclarlor','chnized','wettreving','bumpute','stinflaud',
        'saneliattently','catary','chainvey','petenny','baselled','jametaills',
        'acheal','wrappot','oligide','embefinaviner','beance','synouste',
        'bedrophitling','ementinger','heaviallism','pioneight','prever','hibility',
        'tracquises','couriner','reconven','eldevoy'])
    return rndhost2

def rand_host3():
    rndhost3 = random.choice(['instiviting','kimoundiciphys','chaminglauther',
        'mounct','cornial','consing','adversers','partak','phying','dernated',
        'pliotably','footintrutes','standma','orthress','gramploy','rersessieg',
        'cheouser','chutole','saulattating','wirepers','lighwarding','fraurayized',
        'gartain','latick','scapter','shindonmenrink','parashant','expervoutwar',
        'luftovisp','wingalnes','bisquesqueged','mannerlopmenes','unimman','laxiel',
        'mastickens','gramals','hangerlance','oblity','granal','worksh',
        'nessnesshazes','delity','cought','procump','posupping','burgents',
        'bowmentionized','chewerated','chartiess','descess'])
    return rndhost3

def rand_host4():
    rndhost4 = random.choice(['potefunna','medimisecrify','gradjan','catadeleves',
        'protocation','sculay','obeling','ficilliaseces','parcuring','ausconly',
        'libelarphipse','imanges','rategroide','bonderewithen','reples','diaggion',
        'eathms','bleare','streguidah','loweretersiffs','surestandes',
        'arpnesslewive','cauces','mcfaretramp','glopled','excepty','palinked',
        'jeantify','arizers','gaspiry','spirremnly','oblinatoing','fectedics',
        'coltical','stuyers','latickle','fausly','possemptorned','aggled',
        'payalivergive','mcconctuarne','supears','blenly','atioleved','disgrawbers',
        'adounctic','standyliverted','cutles','scafforthrons','acedgaternad'])
    return rndhost4

def rand_host5():
    rndhost5 = random.choice(['defere','sweavelly','impromated','enturbely',
        'anations','haillicaly','misundided','forman','devors','extrous',
        'clochumousiver','mentics','stationsion','conjark','faularmobsum','allogy',
        'spanguiden','dowarex','overeliating','rouggling','stincoweasons','thertin',
        'moized','amplies','bation','acocry','gablan','soremyrocker','derson',
        'kingess','pacious','ilosely','visablons','foranow','worminvoyant',
        'perplawn','ingened','gelaring','barthweights','patherians',
        'refurrecterict','oveneshobbles','dantairs','lograms','endireburge',
        'mortighted','aphirobeds','abjuric','fudging','mounde'])
    return rndhost5

def rand_host6():
    rndhost6 = random.choice(['tutitution','sembertaving','ferequainsole',
        'charremeg','throuts','oichee','contraze','confrong','rasorgeoscres',
        'livasquishoes','nosting','uratemenes','poledge','assignal','inating',
        'paripped','matects','subrington','prepar','venumbusnetrue','bossors',
        'agmatelockers','pinessur','exquennu','tahoolation','bastlessed','morammed',
        'regaton','proption','hiridises','rogenefable','crypor','safection',
        'mediff','shesseculp','reproffs','anbetraphy','dianizess','monshize',
        'unitiquit','modeouble','shdome','fleerinstria','tabovising','polina',
        'shoptorroric','gripulosive','primagic','overragger','lusible'])
    return rndhost6

def rand_host7():
    rndhost7 = random.choice(['examinequetion','glitized','brassigned','tradams',
        'midley','desmalbayder','paused','somenesed','thinteril','brevitewayingf',
        'piterague','dogened','synctudete','mcbruity','tholiatorited','recognes',
        'stresomergan','garding','scendize','tionsketer','repric','prosoproquate',
        'radicaughts','chatioms','inklestal','hymelighte','rimery','mensegypt',
        'paremong','sionium','officksting','bastrily','primperper','hereve',
        'arctart','reorie','dancting','buchirrection','adraiming','caucate',
        'inizes','innond','disticithfuli','swantlinteness','sebaked','ostella',
        'porticanstine','affred','patrysics','formuteser'])
    return rndhost7

def rand_host8():
    rndhost8 = random.choice(['trayantem','scotypes','fluenterrooted','unfirmico',
        'keneuted','amouncturbon','snuffsholer','sturriflece','famelowers',
        'leecterepuble','irresele','dreabound','boarcharitory','safeation','valrus',
        'maninged','compreled','shakowls','gurkinventing','exight','forchapplents',
        'honersalcoate','resencor','compet','regratomp','ronessagmens','belizes',
        'reintece','asturk','wickencevisift','notachned','bowsonal','planne',
        'drumbite','litiverns','flowinst','nicistic','thinintersest','fadiging',
        'descuffighly','redewdle','oveggs','arraten','flairingly','catter',
        'bellboottess','cogrances','derling','addeted','aldrod'])
    return rndhost8

def rand_host9():
    rndhost9 = random.choice(['bowlets','fridgelizer','fewenholdson','grapprostly',
        'arescal','aboloutbition','holistraphot','triestion','trations','shadowled',
        'befruseharth','downstic','queeps','obseler','piecht','parationized',
        'autors','buttlen','sulton','scotisoffres','cushanize','pipereses',
        'focunds','gioverts','ficiese','havisignated','compeiscover','maninogard',
        'moduplifix','wagoured','shocers','putachape','shessimilly','catutall',
        'corrands','sociprehis','horric','sillanimagons','remoducer','surged',
        'dolphized','procle','dilounting','unctly','unemen','odiatio','humbrant',
        'clintrudes','lestoclar','comped'])
    return rndhost9

def rand_host10():
    rndhost10 = random.choice(['nefigyroadest','irbalder','savoten','eudows',
        'apparang','baskethaverty','torious','formuting','rebourizes','calatte',
        'manuism','bottiersions','maciner','stulting','prottion','faunush',
        'discletend','cabiddy','presquility','webbon','berrots','bechindisams',
        'beessighted','anintruts','gartairding','pervists','micribily','orphilite',
        'furrecies','robuddentran','rantuingly','rooments','voyalikers','lousher',
        'bulbring','ionsibusly','reston','mither','diddadors','exconninat',
        'immelly','libeltimpectan','detructon','cheolong','darnity','mikong',
        'libesee','crypser','macheded','aimediscard'])
    return rndhost10
