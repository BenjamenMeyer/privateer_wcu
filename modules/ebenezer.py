import campaign_lib
from campaign_lib import *

ebenezerspeech1={"intro":[("Ebenezer","My name is Ebenezer, I'm Commander of the local Shepperd Militia."),
                            ("Burrows","The local what?"),
                            ("Ebenezer","The Shepperd Militia. Our team aims at replacing the more and more corrupt or absent militia forces around this area which we call the 'Grey Zone'."),
                            ("Burrows","I don't understand a single word."),
                            ("Ebenezer","The 'Grey Zone' is the area around New Caledonia, known for its immense pirate activity. Both the Militia and the Confederation don't show up too often around here, so our bases are being flooded with Brilliance and our merchants are under constant attack."),
                            ("Burrows","I see. So you're a bunch of little boys climbing into ships and playing police."),
                            ("Ebenezer","Basically yes, this is our problem at the moment. We're armed badly, and we have few good pilots, not to talk of leaders. But we're going to change that, with the help of Privateers like you."),
                            ("Burrows","Go on."),
                            ("Ebenezer","I need you for a little training flight with one of our pilots. Collect him and show him how a real ace deals with the enemy in an outnumbered situation. You and your Talon wingman are going to attack 3 pirate Talons. I'll pay 5000 for this little lesson.")],
                "reject1":[("Burrows","I'm no teacher. Forget it."),
                            ("Ebenezer","Well, I'll find someone else.")],
                "reconsider":[("Burrows","I've reconsidered."),
                            ("Ebenezer","Okay then. For 5000, show your wingman how to wipe out 3 pirate Talons.")],
                "reject2":[("Burrows","Nah.")],
                "accept":[("Burrows","Just make sure that my student won't forget his sandwich, I'll take care of the rest."),
                            ("Ebenezer","I'll also give him a bottle of milk if that suits you.")],
                "accept2":[("Ebenezer","Good.")],
                "reminder":[("Ebenezer","What's the delay?"),
                            ("Burrows","I'm still planning my lesson."),
                            ("Ebenezer","Your wingman is already in space. I don't want to see him vaporized, man."),
                            ("Burrows","Don't worry.")],
                "failure":[("Ebenezer","Well, I didn't hire you for observing an execution. We need every ship we can get... except of yours.")]
                }

ebenezerspeech2={"intro":[("Burrows","Okay, let's hope your pilot is smarter now."),
                            ("Ebenezer","That was quite a good show. Interested in participating in more missions, Mr..."),
                            ("Burrows","Burrows. Grayson Burrows. Probably, but not as a teacher."),
                            ("Ebenezer","That'd be a waste of your skills, Mr. Burrows. We're awaiting a freighter with weapon parts. We're going to construct a new kind of gun."),
                            ("Burrows","What kind of gun are you talking about?"),
                            ("Ebenezer","Since our pilots are not exactly aces, we need a gun with a low fire delay so they have a better chance to hit. The Turbo Laser should suit our needs."),
                            ("Burrows","Okay then, you want me to bring this freighter in?"),
                            ("Ebenezer","Yes. I'll pay 10000 credits. Be aware that the pirates will most likely try to prevent this. You'll get two Talon wingmen.")],
                "reject1":[("Burrows","I don't know what's frightening me more - the pirates or your wingmen.")],
                "reconsider":[("Burrows","Maybe we can come to an agreement."),
                            ("Ebenezer","That's nice - for 10000, bring in my freighter. You'll get two Talon wingmen, if you like it or not.")],
                "reject2":[("Burrows","No chance.")],
                "accept":[("Burrows","I'll do it.")],
                "accept2":[("Ebenezer","Good.")],
                "reminder":[("Ebenezer","The freighter is already in the system."),
                            ("Burrows","Yeah, I thought I'd check for pirate activity by looking through this large window..."),
                            ("Ebenezer","Don't try to fool me. Move out or I'll arrest you.")],
                "failure":[("Ebenezer","The freighter is lost. Our business ends here.")]
                }

ebenezerspeech3={"intro":[("UNLOCKED: Turbo Laser."),
                            ("Burrows","Your freighter is in, and the pirate force is wiped out."),
                            ("Ebenezer","Very nice. I now have a delicate mission for you. The Confederation has learnt about our efforts to build up a new militia."),
                            ("Burrows","Yeah, what's wrong with that?"),
                            ("Ebenezer","We don't have the congress permission to do so - so we got the status of a paramilitary organization. A Broadsword has entered New Caledonia, most likely for negotiations. Meet it and escort it in."),
                            ("Burrows","What's the wages?"),
                            ("Ebenezer","5000.")],
                "reject1":[("Burrows","Playing Babysitter for the feds? Why not force me to enlist?"),
                            ("Ebenezer","C'mon, that's easy money.")],
                "reconsider":[("Burrows","Again, what do you want me to do?"),
                            ("Ebenezer","For 5000, escort in a confed Broadsword.")],
                "reject2":[("Burrows","Forget it.")],
                "accept":[("Burrows","Okay.")],
                "accept2":[("Burrows","Okay.")],
                "reminder":[("Ebenezer","Move out and escort that Broadsword.")],
                "failure":[("Ebenezer","What did you do out there? Where's the Broadsword? You've let the meeting pass by! You're fired!")]
                }

ebenezerspeech4={"intro":[("Burrows","We need to talk."),
                            ("Ebenezer","Sure, later... where's the crew of that Broadsword."),
                            ("Burrows","They're dead."),
                            ("Ebenezer","DEAD?"),
                            ("Burrows","Yes. They weren't here to negotiate. They were here to arrest you. I've managed to prevent this."),
                            ("Ebenezer","Oh my god... we killed a confed ship. I'm going to court for this."),
                            ("Burrows","Well, let's fly to Perry and apologize then."),
                            ("Ebenezer","To PERRY? Are you crazy? They'd put me into jail right away! No, let me think... I have a friend on Macabee who could deliver the message for me. He's neutral. No risk for me, no risk for you."),
                            ("Burrows","Fine for me."),
                            ("Ebenezer","Okay then... here's the message pad. I'll pay 10000 credits for its instant delivery to Macabee in Nexus. My friend is informed, he'll be collecting it on the landing pad.")],
                "reject1":[("Burrows","10000?... I know you can pay more, in this bad situation of yours.")],
                "reconsider":[("Burrows","Say, 15000?"),
                            ("Ebenezer","It's 10000 for we're both in this trouble. Bring the pad to Macabee.")],
                "reject2":[("Burrows","No.")],
                "accept":[("Burrows","I'm on my way."),
                            ("Ebenezer","Hurry up.")],
                "accept2":[("Ebenezer","Thank you. Make haste!")],
                "reminder":[("Ebenezer","Back already?"),
                            ("Burrows","I haven't left yet, actually."),
                            ("Ebenezer","Man, the feds will send reinforcements. Move your ass!")],
                "failure":[("Ebenezer","A confederate transport has docked at Edinburgh. I'll be arrested in a few minutes. Thanks to your incompetency.")]
                }

ebenezerspeech5={"intro":[("Burrows","Okay, I delivered the message to Macabee. No thanks to the confed ambush."),
                            ("Ebenezer","Thanks. My friend already clarified that little misunderstanding. Obviously the Broadsword pilot wasn't sane enough to obey his orders."),
                            ("Burrows","So everything's fine now?"),
                            ("Ebenezer","Yes. The Confederation accepted the implementation of the Shepperd faction."),
                            ("Burrows","Good. Any more missions?"),
                            ("Ebenezer","Yes. I've hired additional Privateers for the education of our pilots, but I have a final mission for you. We're going to introduce a new fighter, the Sparrowhawk."),
                            ("Burrows","That's the successor of the Talon, isn't it?"),
                            ("Ebenezer","It is. We've sent out all of our forces to mess around with the pirates. They're currently attacking an empty Drayman, escorted by our forces. You're to escort the real freighter."),
                            ("Burrows","So no wingmen for me."),
                            ("Ebenezer","But also no opposition to expect. I'll pay 50000 for escorting my Drayman CVL safely in.")],
                "reject1":[("Burrows","You wouldn't pay that much if there wasn't a high risk. I'm not stupid.")],
                "reconsider":[("Burrows","Please tell me about the mission again."),
                            ("Ebenezer","For 50000, escort a Drayman CVL in.")],
                "reject2":[("Burrows","No. The not obvious hazards are usually the most hazardous hazards.")],
                "accept":[("Burrows","Nice money. Of course I'll do it."),
                            ("Ebenezer","Excellent. Move out.")],
                "accept2":[("Ebenezer","No risk, no fun.")],
                "reminder":[("Ebenezer","I'm not sure how long the pirates will swallow the pill. They might as well turn around and head back to New Caledonia. Better move out now.")],
                "failure":[("Ebenezer","That freighter was of great importance to us. Most of our funds were invested in those new ships. Thanks to you, the Shepperds no longer exist.")]
                }

ebenezersuccess=[("UNLOCKED: Sparrowhawk."),
            ("Burrows","Your freighter has docked. I was ambushed by ships of kilrathi origin, piloted by retros."),
            ("Ebenezer","That was most likely coincidence, but the Confederation might be interested to learn about a possible cooperation between Retros and Kilrathis, so I sent them a message. Well now, million thanks! I've made sure that you can also grab one of those Sparrowhawks, if you like!"),
            ("Burrows","Thanks. Good luck with the Shepperds. I hope you can stabilize the Grey Zone now. Goodbye.")]

def LoadEbenezerCampaign():
    EBENEZER_SPRITE  = ("informant.spr","Talk_to_Ebenezer","bases/heads/dilloh.spr") #sprite file for the fixer
    ebenezermission1 = CampaignClickNode() # Initialize each node
    ebenezermission2 = CampaignClickNode() # Initialize each node
    ebenezermission3 = CampaignClickNode() # Initialize each node
    ebenezermission4 = CampaignClickNode() # Initialize each node
    ebenezermission5 = CampaignClickNode() # Initialize each node
    ebenezerfinish = CampaignNode()

    priv=Campaign("ebenezer_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(ebenezermission1) # the first node.

    MakeMission(priv,
        EBENEZER_SPRITE,
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        ClearFactionRecord('militia',1.0,PushRelation('militia')),
        LaunchWingmen("militia__","talon",1),
        'defend',('pirates_',0,1,5000,123456.789,0,False,True,'merchant__',(),priv.name+"_mission",'','talon','',3), # Mission arguments.
        priv.name+"_mission",
        ebenezerspeech1,
        None,
        CampaignEndNode(priv),
        ebenezermission2,
        ebenezermission1)

    MakeMission(priv,
        EBENEZER_SPRITE,
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        AddCredits(5000),
        LaunchWingmen("militia__","talon",2),
        'escort_local',('pirates_',0,6,1,3000,0,True,'merchant__',(),priv.name+"_mission",'','talon','','drayman'), # Mission arguments.
        priv.name+"_mission",
        ebenezerspeech2,
        None,
        CampaignEndNode(priv),
        ebenezermission3,
        ebenezermission2)

    MakeMission(priv,
        EBENEZER_SPRITE,
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        AddCredits(10000,AddTechnology("turbolas")),
        None,
        'bounty_leader',(0,0,0,False,0,'merchant_',(),priv.name+"_mission",'','broadsword',False,'',["You won't prevent us from arresting Ebenezer! Die!"]), # Mission arguments.
        priv.name+"_mission",
        ebenezerspeech3,
        None,
        CampaignEndNode(priv),
        ebenezermission4,
        ebenezermission3)

    MakeCargoMission(priv,
        EBENEZER_SPRITE,
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        [InSystemCondition("Gemini/Nexus","Macabee")],
        AddCredits(5000),
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/Nexus",),0,'confed_',4,'','',[("All shepperd affiliates are hereby sentenced to death!")],['Gemini/Crab-12', 'Gemini/Capella', 'Gemini/Nexus'], 'Macabee')),
        ("Message",1),
        priv.name+"_mission",
        ebenezerspeech4,
        None,
        CampaignEndNode(priv),
        ebenezermission5,
        ebenezermission4)

    MakeMission(priv,
        EBENEZER_SPRITE,
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
        AddCredits(10000),
        None,
        'escort_local',('retro_',0,5,1,3000,0,True,'merchant__',(),priv.name+"_mission",'','krant','','draymanCVL'), # Mission arguments.
        priv.name+"_mission",
        ebenezerspeech5,
        None,
        CampaignEndNode(priv),
        ebenezerfinish,
        ebenezermission5)

    ebenezerfinish.Init(priv,
        [],
        None,
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/New_Caledonia","Edinburgh")],
            ebenezersuccess,
            EBENEZER_SPRITE,
            TrueSubnode(AddCredits(50000,AddTechnology("sparrow"))),
            None,
            [CampaignEndNode(priv)])])
    return priv
