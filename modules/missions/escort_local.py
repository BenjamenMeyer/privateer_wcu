from go_somewhere_significant import *
from go_to_adjacent_systems import *
import Briefing
import Director
import VS
import debug
import faction_ships
import launch
import quest
import unit
import universe
import vsrandom


class escort_local (Director.Mission):

    def __init__(self, factionname, numsystemsaway, enemyquantity,  waves, distance_from_base, creds, incoming, protectivefactionname='', jumps=(), var_to_set='', dynamic_attack_fg='', dynamic_type='', dynamic_defend_fg='', dynamic_defend_type='', greetingText=['Escort: give up while you still can...', 'If you let us ravage our target then we grant you passage today.']):
        Director.Mission.__init__(self)
        self.greetingText = greetingText
        self.dedicatedattack = vsrandom.randrange(0, 2)*vsrandom.randrange(0, 2)
        if (VS.GetRelation(factionname, protectivefactionname) >= 0.0):
            self.dedicatedattack = 1
        self.arrived = 0
        self.launchedfriend = 0
        self.protectivefaction = protectivefactionname
        self.var_to_set = var_to_set
        self.quantity = 0
        self.mplay = "all"
        self.gametime = VS.GetGameTime()
        self.waves = waves
        self.incoming = incoming
        self.dynatkfg = dynamic_attack_fg
        self.dynatktype = dynamic_type
        self.dyndeffg = dynamic_defend_fg
        self.dyndeftype = dynamic_defend_type
        self.attackers = []
        self.objective = 0
        self.targetiter = 0
        self.ship_check_count = 0
        self.faction = factionname
        self.jp = VS.Unit()
        self.cred = creds
        self.quantity = enemyquantity
        self.savedquantity = enemyquantity
        self.distance_from_base = distance_from_base
        self.defendee = VS.Unit()
        self.difficulty = 1
        self.you = VS.getPlayer()
        self.respawn = 0
        name = self.you.getName()
        self.successdelay = 0
        self.mplay = universe.getMessagePlayer(self.you)
        self.adjsys = go_to_adjacent_systems(self.you, numsystemsaway, jumps)
        VS.IOmessage(0, "escort mission", self.mplay, 
                    "Good Day, %s. Your mission is as follows:" % name)
        self.adjsys.Print("You are in the %s system,", 
                        "Proceed swiftly to %s.", 
                        "Your arrival point is %s.", 
                        "escort mission", 1)

    def SetVarValue(self, value):
        if (self.var_to_set != ''):
            quest.removeQuest(self.you.isPlayerStarship(), self.var_to_set, value)

    def SuccessMission(self):
        self.defendee.setFgDirective('b')
        self.defendee.setFlightgroupLeader(self.defendee)
        if (self.incoming):
            un = unit.getSignificant(vsrandom.randrange(0, 20), 1, 0)
            if (un.getName() == self.defendee.getName()):
                un = unit.getSignificant(vsrandom.randrange(0, 30), 1, 0)
            if (un.getName() == self.defendee.getName()):
                un = unit.getSignificant(vsrandom.randrange(0, 40), 1, 0)
            if (un.getName() == self.defendee.getName()):
                un = unit.getSignificant(vsrandom.randrange(0, 30), 1, 0)
            if (un.getName() == self.defendee.getName()):
                un = unit.getSignificant(vsrandom.randrange(0, 40), 1, 0)
            if (un.getName() != self.defendee.getName()):
                self.defendee.performDockingOperations(un, 0)
                debug.info("docking with "+un.getName())
        else:
            self.defendee.ActivateJumpDrive(0)
            self.defendee.SetTarget(self.adjsys.SignificantUnit())
        self.successdelay = VS.GetGameTime()+1

    def PayMission(self):
        VS.AdjustRelation(self.you.getFactionName(), self.faction, .03, 1)
        self.SetVarValue(1)
        if (self.cred > 0):
            self.you.addCredits(self.cred)
            VS.IOmessage(0, "escort mission", self.mplay, 
                    "Excellent work pilot! Your effort has thwarted the foe!")
            VS.IOmessage(0, "escort mission", self.mplay,
                    "You have been rewarded for your effort as agreed.")
        VS.terminateMission(1)

    def FailMission(self):
        self.you.addCredits(-self.cred)
        VS.AdjustRelation(self.you.getFactionName(), self.faction, -.02, 1)
        self.SetVarValue(-1)
        VS.IOmessage(0, "escort mission", self.mplay,
                "You Allowed the base you were to protect to be destroyed.")
        VS.IOmessage(0, "escort mission", self.mplay,
                "You are a failure to your race!")
        VS.IOmessage(1, "escort mission", self.mplay,
                "We have contacted your bank and informed them of your failure to deliver on credit."
                " They have removed a number of your credits for this inconvenience."
                " Let this serve as a lesson.")
        VS.terminateMission(0)

    def NoEnemiesInArea(self, jp):
        if (self.adjsys.DestinationSystem() != VS.getSystemFile()):
            return 0
        if (self.ship_check_count >= len(self.attackers)):
            VS.setCompleteness(self.objective, 1.0)
            return 1
        un = self.attackers[self.ship_check_count]
        self.ship_check_count += 1
        if (un.isNull() or (un.GetHullPercent() < .7 and self.defendee.getDistance(un) > 7000)):
            return 0
        else:
            VS.setObjective(self.objective, "Destroy the %s"%un.getName())
            self.ship_check_count = 0
        return 0

    def GenerateEnemies(self, jp, you):
        count = 0
        VS.addObjective("Protect %s from %s" % (jp.getName(), self.faction))
        self.objective = VS.addObjective(
            "Destroy All %s Hostiles" % self.faction)
        VS.setCompleteness(self.objective, 0.0)
        debug.info("quantity "+str(self.quantity))
        while (count < self.quantity):
            L = launch.Launch()
            if self.dynatkfg == "":
                atkfg = "Shadow"
            else:
                atkfg = self.dynatkfg
            L.fg = atkfg
            L.dynfg = ""
            if count == 0:
                L.fgappend = ""
            else:
                L.fgappend = "_"+str(count)
            if (self.dynatktype == ''):
                L.type = faction_ships.getRandomFighter(self.faction)
            else:
                L.type = self.dynatktype
            L.ai = "default"
            L.num = 1
            L.minradius = 20000.0
            L.maxradius = 25000.0
            try:
                L.minradius *= faction_ships.launch_distance_factor
                L.maxradius *= faction_ships.launch_distance_factor
            except:
                pass
            L.faction = self.faction
            launched = L.launch(you)
            if (count == 0):
                self.you.SetTarget(launched)

            if (1):
                launched.SetTarget(jp)
            else:
                launched.SetTarget(you)
            if (self.dedicatedattack):
                launched.setFgDirective('B')
            self.attackers += [launched]
            count += 1
        if (self.respawn == 0 and len(self.attackers) > 0):
            self.respawn = 1
            import universe
            universe.greet(
                self.greetingText, self.attackers[0], you, self.dyndeffg)
        else:
            VS.IOmessage(0, "escort mission", self.mplay,
                         "Eliminate all %s ships here" % self.faction)
            VS.IOmessage(0, "escort mission", self.mplay,
                         "You must protect %s." % jp.getName())
        self.quantity = 0

    def GenerateDefendee(self):
        import escort_mission
        escort_mission.escort_num += 1
        L = launch.Launch()
        if self.dyndeffg == "":
            deffg = "Escort"
            L.fgappend = "_"+str(escort_mission.escort_num)
        else:
            deffg = self.dyndeffg
            L.fgappend = ""
        L.fg = deffg
        L.dynfg = ""
        L.faction = self.protectivefaction
        if (self.dyndeffg == '' and self.dyndeftype == ''):
            L.type = faction_ships.getRandomFighter(self.protectivefaction)
        else:
            L.type = self.dyndeftype
        L.ai = "default"
        L.num = 1
        L.minradius = 2.0*self.you.rSize()
        L.maxradius = 3.0*self.you.rSize()
        L.forcetype = True
        escortee = L.launch(self.you)
        escortee.upgrade("jump_drive", 0, 0, 0, 1)
        escortee.setFlightgroupLeader(self.you)
        escortee.setFgDirective('F')
        return escortee

    def Execute(self):
        if (self.successdelay):
            if (self.defendee.getUnitSystemFile() != self.you.getUnitSystemFile() or VS.GetGameTime()-self.successdelay > 120):
                if (self.defendee):
                    self.PayMission()
                else:
                    self.FailMission()
            return  # nothing more happens inside this control
        if (self.you.isNull() or (self.launchedfriend and self.defendee.isNull())):
            VS.IOmessage(0, "escort mission", self.mplay,
                    "#ff0000You were unable to arrive in time to help. Mission failed.")
            self.SetVarValue(-1)
            VS.terminateMission(0)
            return
        if (not self.adjsys.Execute()):
            return
        if (not self.arrived):
            self.arrived = 1
            if (self.launchedfriend == 0 and not self.incoming):
                self.defendee = self.GenerateDefendee()
                self.launchedfriend = 1
            self.adjsys = go_somewhere_significant(
                self.you, 0, self.distance_from_base, 0)
            self.adjsys.Print("You must visit the %s",
                              "escort mission", "docked around the %s", 0)
            self.jp = self.adjsys.SignificantUnit()
        else:
            if (self.launchedfriend == 0):
                self.defendee = self.GenerateDefendee()
                self.launchedfriend = 1
            if (self.defendee.isNull()):
                self.FailMission(you)
                return
            else:
                self.defendee.setFlightgroupLeader(self.you)
                if (VS.GetGameTime()-self.gametime > 10):
                    self.defendee.setFgDirective('F')
                if (self.quantity > 0):
                    self.GenerateEnemies(self.defendee, self.you)
                if (self.ship_check_count == 0 and self.dedicatedattack):
                    if (self.targetiter >= len(self.attackers)):
                        self.targetiter = 0
                    else:
                        un = self.attackers[self.targetiter]
                        if (not un.isNull()):
                            un.SetTarget(self.defendee)
                        self.targetiter = self.targetiter+1
                if (self.NoEnemiesInArea(self.defendee)):
                    if (self.waves > 0):
                        self.quantity = self.savedquantity
                        self.waves -= 1
                    else:
                        self.SuccessMission()

    def initbriefing(self):
        debug.info("init briefing")

    def loopbriefing(self):
        debug.info("loop briefing")
        Briefing.terminate()

    def endbriefing(self):
        debug.info("ending briefing")
