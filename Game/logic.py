from .models import (
    Counties, 
    Representatives, 
    Parties,
    General,
    Topics,
    Deals
)
from django.contrib.auth.models import User
from operator import itemgetter
import random

# This function resets all Models / Databases
def Reset():
    Parties.objects.all().delete()
    Parties.objects.bulk_create([
        Parties(Name='Progress party', Next_action=0, Turn="Now", CP=100, LR=0, User=User.objects.get(username="User1"), Seats=3, Vote="Yes", Vote_proposal_1="Yes", Vote_proposal_2="No", Vote_proposal_3="No", Expected_vote_proposal_1=None, Expected_vote_proposal_2=None, Expected_vote_proposal_3=None, Made_deal="No", Deal_breaker=False, Prime_minister=False, Government=False, Declaration_maker="No", Declaration_reaction="Rejects"),
        Parties(Name='Conservative union', Next_action=0, Turn="Not yet", CP=-100, LR=0, User=User.objects.get(username="User2"), Seats=2, Vote="Yes", Vote_proposal_1="Yes", Vote_proposal_2="No", Vote_proposal_3="No", Expected_vote_proposal_1=None, Expected_vote_proposal_2=None, Expected_vote_proposal_3=None, Made_deal="No", Deal_breaker=False, Prime_minister=False, Government=False, Declaration_maker="No", Declaration_reaction="Rejects"),
        Parties(Name='Ultra Left', Next_action=0, Turn=None, CP=0, LR=-100, User=None, Seats=2, Vote="Yes", Vote_proposal_1="No", Vote_proposal_2="No", Vote_proposal_3="No", Expected_vote_proposal_1=None, Expected_vote_proposal_2=None, Expected_vote_proposal_3=None, Made_deal="No", Deal_breaker=False, Prime_minister=False, Government=False, Declaration_maker="No", Declaration_reaction="Rejects"),
        Parties(Name='Right Point', Next_action=0, Turn=None, CP=0, LR=100, User=None, Seats=2, Vote="Yes", Vote_proposal_1="No", Vote_proposal_2="No", Vote_proposal_3="No", Expected_vote_proposal_1=None, Expected_vote_proposal_2=None, Expected_vote_proposal_3=None, Made_deal="No", Deal_breaker=False, Prime_minister=False, Government=False, Declaration_maker="No", Declaration_reaction="Rejects"),
        Parties(Name='Independent', Next_action=0, Turn=None, CP=0, LR=0, User=None, Seats=0, Vote="Yes", Vote_proposal_1="No", Vote_proposal_2="No", Vote_proposal_3="No", Expected_vote_proposal_1=None, Expected_vote_proposal_2=None, Expected_vote_proposal_3=None, Made_deal="No", Deal_breaker=False, Prime_minister=False, Government=False, Declaration_maker="No", Declaration_reaction="Rejects"),
    ])

    Representatives.objects.all().delete()
    Representatives.objects.bulk_create([
        Representatives(Name='Merita', CP=100, LR=0, Party=Parties.objects.get(Name="Progress party"), County_election="", Percentage=0),
        Representatives(Name='Awiti', CP=90, LR=15, Party=Parties.objects.get(Name="Progress party"), County_election="", Percentage=0),
        Representatives(Name='Jez', CP=80, LR=-20, Party=Parties.objects.get(Name="Progress party"), County_election="", Percentage=0),
        Representatives(Name='Raya', CP=70, LR=25, Party=Parties.objects.get(Name="Progress party"), County_election="", Percentage=0),

        Representatives(Name='Gallus', CP=-100, LR=0, Party=Parties.objects.get(Name="Conservative union"), County_election="", Percentage=0),
        Representatives(Name='Almudena', CP=-90, LR=-25, Party=Parties.objects.get(Name="Conservative union"), County_election="", Percentage=0),
        Representatives(Name='Brynmor', CP=-80, LR=20, Party=Parties.objects.get(Name="Conservative union"), County_election="", Percentage=0),
        Representatives(Name='Patricia', CP=-70, LR=-15, Party=Parties.objects.get(Name="Conservative union"), County_election="", Percentage=0),

        Representatives(Name='Eka', CP=0, LR=-100, Party=Parties.objects.get(Name="Ultra Left"), County_election="", Percentage=0),
        Representatives(Name='Caren', CP=15, LR=-90, Party=Parties.objects.get(Name="Ultra Left"), County_election="", Percentage=0),
        Representatives(Name='Signe', CP=-20, LR=-80, Party=Parties.objects.get(Name="Ultra Left"), County_election="", Percentage=0),
        Representatives(Name='Jannicke', CP=25, LR=-70, Party=Parties.objects.get(Name="Ultra Left"), County_election="", Percentage=0),

        Representatives(Name='Iver', CP=0, LR=100, Party=Parties.objects.get(Name="Right Point"), County_election="", Percentage=0),
        Representatives(Name='Zetenty', CP=-25, LR=90, Party=Parties.objects.get(Name="Right Point"), County_election="", Percentage=0),
        Representatives(Name='Lise', CP=20, LR=80, Party=Parties.objects.get(Name="Right Point"), County_election="", Percentage=0),
        Representatives(Name='Saara', CP=-15, LR=70, Party=Parties.objects.get(Name="Right Point"), County_election="", Percentage=0),
    ])

    Counties.objects.all().delete()
    Counties.objects.bulk_create([
        Counties(Name='University City County', CP=80, LR=0, Spread=5, Representative=Representatives.objects.get(Name="Merita")),
        Counties(Name='Biblebelt County', CP=-80, LR=0, Spread=5, Representative=Representatives.objects.get(Name="Gallus")),
        Counties(Name='Union County', CP=0, LR=-80, Spread=5, Representative=Representatives.objects.get(Name="Eka")),
        Counties(Name='Rich People County', CP=0, LR=80, Spread=5, Representative=Representatives.objects.get(Name="Iver")),

        Counties(Name='Big City County', CP=25, LR=-25, Spread=5, Representative=Representatives.objects.get(Name="Raya")),
        Counties(Name='Pretty Place County', CP=25, LR=25, Spread=5, Representative=Representatives.objects.get(Name="Patricia")),
        Counties(Name='Farm County', CP=-25, LR=25, Spread=5, Representative=Representatives.objects.get(Name="Jannicke")),
        Counties(Name='Factory County', CP=-25, LR=-25, Spread=5, Representative=Representatives.objects.get(Name="Saara")),

        Counties(Name='In The Middle County', CP=0, LR=0, Spread=5, Representative=Representatives.objects.get(Name="Zetenty")),
    ])

    General.objects.all().delete()
    General.objects.bulk_create([
        General(
            Name="Game1", 
            Next_action="Submit candidates",
            Year=1,
            Test=True, 
            Message_elections_page="Please submit your ballot list",
            Message_outcome_proposal_1="",
            Message_outcome_proposal_2="",
            Message_outcome_proposal_3="",
            Worldview=0,
            Nature=0,
            Ethics=0,
            Taxation=0,
            Social_protection=0,
            Immigration=0,
            LR = 0,
            CP = 0,
            Worldview_bar = 50,
            Nature_bar = 50,
            Ethics_bar = 50,
            Taxation_bar = 50,
            Social_protection_bar = 50,
            Immigration_bar = 50,
            LR_bar = 50,
            CP_bar = 50,
            Worldview_govt = "",
            Nature_govt = "",
            Ethics_govt = "",
            Taxation_govt = "",
            Social_protection_govt = "",
            Immigration_govt = "",
            Votes_for_declaration = 0,
            Votes_against_declaration= 0,
            Status_forming_government= "Attempting",
            )
    ])

    Topics.objects.all().delete()
    Topics.objects.bulk_create([
        Topics(Proposal="Invest more in United Nations", Parent="Worldview", Shift=10, New=True, Current_proposal=False, Current_proposal_number=1),
        Topics(Proposal="Participate in international peace keeping mission", Parent="Worldview", Shift=10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Redrawl from international cooperation platform", Parent="Worldview", Shift=-10, New=False, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Instate measures to protect national industry", Parent="Worldview", Shift=-10, New=False, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Create 3 extra nature reserves", Parent="Nature", Shift=-10, New=False, Current_proposal=False, Current_proposal_number=2),
        Topics(Proposal="Extend endangered species list", Parent="Nature", Shift=-10, New=False, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Cut rainforest to create space for agriculture", Parent="Nature", Shift=10, New=False, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Mark environmmental activists as terrorists", Parent="Nature", Shift=10, New=False, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Stimulate a national LHBTI pride day", Parent="Ethics", Shift=10, New=True, Current_proposal=False, Current_proposal_number=3),
        Topics(Proposal="Allow abortions further on in pregnancy", Parent="Ethics", Shift=10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Reduce same sex adoption possibilities", Parent="Ethics", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Extend traditional values in the constitution", Parent="Ethics", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Extra tax on the highest earners", Parent="Taxation", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="More tax deductabilities for the poor", Parent="Taxation", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Lower taxes for all residents", Parent="Taxation", Shift=10, New=False, Current_proposal=True, Current_proposal_number=None),
        Topics(Proposal="Decrease taxes on second homes", Parent="Taxation", Shift=10, New=False, Current_proposal=True, Current_proposal_number=None),
        Topics(Proposal="Enforce mandatory health care insurance", Parent="Social_protection", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Increase minium wage", Parent="Social_protection", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Increase personal responsibility for pension savings", Parent="Social_protection", Shift=10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Increase commercial stimulants in health care", Parent="Social_protection", Shift=10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Close the borders for most immigrants", Parent="Immigration", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Organize a social media anti immigration campaign", Parent="Immigration", Shift=-10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Less strict access rules for political asylum seekers", Parent="Immigration", Shift=10, New=True, Current_proposal=False, Current_proposal_number=None),
        Topics(Proposal="Let more family members of asylumseeker enter the country", Parent="Immigration", Shift=10, New=True, Current_proposal=False, Current_proposal_number=None),
        
    ])

    Deals.objects.all().delete()

    # when we start the game we let all non_user parties select their candidates
    Non_user_candidate_selection()

# This functions lets the logged in user save his candidates per county to participate in that county election
def Save_user_candidates(FormInput):
    Counties_model = Counties.objects.all()

    Double_candidate = False
    Used_representatives = []
    # We loop trough all counties
    for county in Counties_model:
        Candidate = FormInput.get(county.Name)
        
        # We check whether a candidate was filled in for this county
        if Candidate != "":
            # We check whether a candidate is not used in multiple counties
            if Candidate not in Used_representatives:
                Candidate_object = Representatives.objects.get(Name=Candidate)
                Candidate_object.County_election = county.Name
                Candidate_object.save()
                Used_representatives.append(Candidate)
            else:
                # If the candidate is used double we don't save him and give a warning message
                Game1 = General.objects.get(Name="Game1")
                Game1.Message_elections_page = "You cannot select 1 representative for multiple counties"
                Game1.save()
                Double_candidate = True

    # If no candidates were used double we give a succes message
    if Double_candidate == False:
            Game1 = General.objects.get(Name="Game1")
            Game1.Message_elections_page = "You succesfully saved your candidate list"
            Game1.save()

# This functions selects for non-user parties which repr.'s will take part in which county elections
def Non_user_candidate_selection():
    # We reset the County_election-attribute for all representatives to "" 
    Representatives_model = Representatives.objects.all()
    for representative in Representatives_model:
        representative.County_election = ""
        representative.save()

    # This function is only for candidate selection for non-user Parties (/computer / A.I.)
    Non_user_parties = Parties.objects.filter(User=None)
    Counties_model = Counties.objects.all()

    # per non_user_party we make a list of the distance between the party(LR,CP) and all country(LR,CP)
    for party in Non_user_parties:
        Party_county_distance_list = []
        for county in Counties_model:
            unit = []
            unit.append(county.Name)
            unit.append(Coordinate_distance(party.LR, party.CP, county.LR, county.CP))
            Party_county_distance_list.append(unit)
        # we sort the list in such a way that the county that has the closest distance with the party
        # is first in the list.
        Party_county_distance_list = sorted(Party_county_distance_list, key=itemgetter(1))
        
        # Per county we look which representative of that party is closest to the political-coordinate 
        # of that county. This representative will be candidate for this party in that county. We use the
        # the sorted list to first fill candidate positions in counties that are close to the party.
        for unit in Party_county_distance_list:
            county = Counties.objects.get(Name=unit[0])
            # Best_candidate is a working list that represents the best scoring candidate for this loop
            Best_candidate = ["", 300]
            # we filter the repr on the base whether they are member of the party that we are looping
            # trough right now.
            RepresentativeSubModel = Representatives.objects.filter(Party=party)
            for representative in RepresentativeSubModel:
                # only repr who havn't been selected as candidate yet are taken in consideration
                if representative.County_election == "":
                    Repr_county_distance = Coordinate_distance(representative.LR, representative.CP, county.LR, county.CP)
                    # we check whether this repr scores better than previous checked repr
                    if Repr_county_distance < Best_candidate[1]:
                        # if this is true we make that candidate the Best_candidate for now
                        Best_candidate[0] = representative.Name
                        Best_candidate[1] = Repr_county_distance
            # If a candidate is selected from the representatives we save this to the Representatie database
            # this excludes this repr to be candidate in any other election
            if Best_candidate[0] != "":
                Candidate = Representatives.objects.get(Name=Best_candidate[0])
                Candidate.County_election = county.Name
                Candidate.save()

    print("Non user candidates are selected")

# This function returns the distance between two coordinates (LR1, CP1) and (LR2, CP2)
def Coordinate_distance(LR1, CP1, LR2, CP2):
    # Distance between two LR-points
    LR_distance = LR1 - LR2
    # Distance between two CP-points
    CP_distance =  CP1 - CP2
    # Use pythagoras to get the absolute distance
    Absolute_distance = (CP_distance**2 + LR_distance**2)**0.5
    return Absolute_distance

# This functions counts how many seats every party has
def Count_seats():
    # we reset all party-seats to 0
    Parties_model = Parties.objects.all()
    for party in Parties_model:
        party.Seats = 0
        party.save()

    # per county we check which party holds the seat and add a seat to the total
    # of that party
    Counties_model = Counties.objects.all()
    for county in Counties_model:
        county.Representative.Party.Seats +=1
        county.Representative.Party.save()

# This function starts elections between submitted candidates
def Hold_elections():
    # we reset the outcome of the last election
    Candidates = Representatives.objects.all()
    for candidate in Candidates:
        candidate.Percentage = 0
        candidate.save()

    CountiesModel = Counties.objects.all()
    for county in CountiesModel:
        county.Representative = None
        county.save()

    # We delete any independents from the last election, else they
    # actively particpiate.
    Representatives.objects.filter(Party=Parties.objects.get(Name="Independent")).delete()

    # loop trough all the counties to hold elections in all counties:
    Counties_model = Counties.objects.all()
    for county in Counties_model:
        print(county.Name)
        
        # Use the Coordinates_around_point-function to get a list of
        # coordinates surounding the LR-CP point of the specific county
        # these point represent all the voters in the county.
        Coordinates_list = Coordinates_around_point(county.LR, county.CP, county.Spread)

        Candidates = Representatives.objects.filter(County_election=county.Name)

        # Now we loop trough all the coordinates and check per coordinate
        # which representative is the closes and wins that vote
        for coordinate in Coordinates_list:
            # We reset the coordinate winner
            Coordinate_winner = ["Name", 300]

            # per coordinate we loop trough all the candidates and get the absolute
            # distance between the coordinate and the representative LR-PC
            for candidate in Candidates:
                # Distance between two LR-points
                LR_distance = coordinate[0] - candidate.LR
                # Distance between two CP-points
                CP_distance =  coordinate[1] - candidate.CP
                # Use pythagoras to get the absolute distance
                Absolute_distance = (CP_distance**2 + LR_distance**2)**0.5
                
                # if this candidate has the lowest absolute_distance so far
                # he is made coordinate_winner. Either he stays winner or
                # another candidate surpasses him with an even lower distance.
                if Absolute_distance < Coordinate_winner[1]:
                    Coordinate_winner[0] = candidate.Name
                    Coordinate_winner[1] = Absolute_distance

            # The candidate who wins gets +(100/97%) of the votes this is added
            # to the percentage of votes he already had    
            for candidate in Candidates:
                if candidate.Name == Coordinate_winner[0]:
                    percentage = candidate.Percentage
                    percentage += (100 / 37)
                    candidate.Percentage = percentage
                    candidate.save()
        
        # We check which candidate that participated in this county has the highest
        # percentage of votes. That candidates becomes the representative of this county.
        Candidates = Representatives.objects.filter(County_election=county.Name)
        Percentage = 0
        for candidate in Candidates:
            print(candidate.Name)
            print(candidate.Percentage)
            if candidate.Percentage > Percentage:
                Percentage = candidate.Percentage
                county.Representative = candidate
                county.save()

        # In case there are no candidates submitted for the elections in a
        # county a backup-independent candidate is created
        if county.Representative == None:
            back_up_repr = Representatives(Name='Backup', CP=0, LR=0, Party=Parties.objects.get(Name="Independent"), County_election=county.Name, Percentage=100)
            back_up_repr.save()
            county.Representative = back_up_repr
            county.save()
        print("The winner is: " + county.Representative.Name)

    # We count how many seats every party has now and put that in the databases
    Count_seats()

    # We reset the declaration makers from the last time a government declaration was made
    Parties_model = Parties.objects.all()
    for party in Parties_model:
        party.Declaration_maker = "No"
        party.save()

# When provided with one point on the political spectrum (LR and CP) and 
# provided with the space between points (cluster / spread) this function
# gives a list of 97 coordinatos surounding that point in a more or less
# circle shape.
def Coordinates_around_point(LR, CP, Spread):
    LR = LR
    CP = CP
    # spread stand for how clustered the coordinates around the main
    # point should be. Larger spread is a larger cluster with more space
    # between the individual coordinates.
    spread = Spread

    # we get the outer most coordinates (97 points version)
    #LR_min = LR - (4 * spread)
    #LR_max = LR + (5 * spread)
    #CP_min = CP - (4 * spread)
    #CP_max = CP + (5 * spread)

    # we get the outer most coordinates (37 point version)
    LR_min = LR - (2 * spread)
    LR_max = LR + (3 * spread)
    CP_min = CP - (2 * spread)
    CP_max = CP + (3 * spread)

    # We use the outer most coordinates to loop trough all possible
    # coordinate between those and add them to the list of coordinates
    CoordinateList = []
    for h in range(LR_min, LR_max, spread):
        for l in range(CP_min, CP_max, spread):
            Coordinate = [h, l]
            CoordinateList.append(Coordinate)
    
    # No we have a "square" of  81 coordinates, we now add 12 extra coordinates
    # to have it look more like a circle. (97 points version)
    #for x in range(-1, 2):
        #Coordinate = [(LR + (5 * spread)), (CP + (x * spread))]
        #CoordinateList.append(Coordinate)
        #Coordinate = [(LR - (5 * spread)), (CP + (x * spread))]
        #CoordinateList.append(Coordinate)
        #Coordinate = [(LR + (x * spread)), (CP + (5 * spread))]
        #CoordinateList.append(Coordinate)
        #Coordinate = [(LR + (x * spread)), (CP - (5 * spread))]
        #CoordinateList.append(Coordinate)

    # No we have a "square" of  25 coordinates, we now add 12 extra coordinates
    # to have it look more like a circle. (37 points version)
    for x in range(-1, 2):
        Coordinate = [(LR + (3 * spread)), (CP + (x * spread))]
        CoordinateList.append(Coordinate)
        Coordinate = [(LR - (3 * spread)), (CP + (x * spread))]
        CoordinateList.append(Coordinate)
        Coordinate = [(LR + (x * spread)), (CP + (3 * spread))]
        CoordinateList.append(Coordinate)
        Coordinate = [(LR + (x * spread)), (CP - (3 * spread))]
        CoordinateList.append(Coordinate)

    # Lastly we add 4 more coordinates who complete the "circle" shape of the
    # cloud of coordinates. (97 points version)
    #Coordinate = [LR, CP + (6 * spread)]
    #CoordinateList.append(Coordinate)
    #Coordinate = [LR, CP - (6 * spread)]
    #CoordinateList.append(Coordinate)
    #Coordinate = [LR + (6 * spread), CP]
    #CoordinateList.append(Coordinate)
    #Coordinate = [LR - (6 * spread), CP]
    #CoordinateList.append(Coordinate)
    
    return CoordinateList

# This function selects three new proposal for in parliament
def Select_three_new_proposals():
    print(Topics.objects.filter(New=True).count())

    # If there are less than 3 New proposals left, than we reset all proposals to new
    # excluding the proposals from last round to avoid voting over the same proposal
    # twice in a row.
    if Topics.objects.filter(New=True).count() < 3:
        print("Refresh")
        Non_current_proposals = Topics.objects.filter(Current_proposal_number=None)

        for proposal in Non_current_proposals:
            proposal.New = True
            proposal.save()

    # Trough a 3-time-loop 3 new proposals are selected
    for i in range(1,4):
        print(i)
        
        Old_proposal = Topics.objects.get(Current_proposal_number=i)
        Old_proposal.Current_proposal_number = None
        Old_proposal.save()
        
        New_proposal = Topics.objects.filter(New=True).order_by('?').first()
        New_proposal.New = False
        New_proposal.Current_proposal_number = i
        New_proposal.save()
        print(New_proposal)

# This functions determines how non_user_parties vote on the current proposals
def Non_user_vote_selections():
    General_model = General.objects.get(Name="Game1")

    # we get the current LRCP, we reference all proposals for all parties against this
    LR = General_model.LR
    CP = General_model.CP
    print("The current LR is: " + str(LR))
    print("The current CP is: " + str(CP))
    print("")

    # We loop trough the 3 proposals
    for i in range(1,4):
        proposal = Topics.objects.get(Current_proposal_number=i)
        print("Proposal #" + str(i) + ": "+ str(proposal))
        print("The parent topic is: " + str(proposal.Parent))

        Current_parent_score = getattr(General_model, proposal.Parent)
        print("The current score on this topic is: " + str(Current_parent_score))

        Parent_score_if_yes = Current_parent_score + proposal.Shift
        Parent_score_if_no = Current_parent_score
        print("The score on this topic if accepted would be: " + str(Parent_score_if_yes))

        # We temporarily set the Topic-score as if the proposal was voted yes
        setattr(General_model, proposal.Parent, Parent_score_if_yes)

        # Now we calculate the LRCP if the proposal was voted yes
        LR_new = (
            General_model.Worldview +
            General_model.Nature +
            General_model.Taxation +
            General_model.Social_protection
        ) / 4

        CP_new = (
            General_model.Worldview +
            General_model.Ethics +
            General_model.Immigration -
            General_model.Nature
        ) / 4

        print("LR if proposal would be accepted: " + str(LR_new))
        print("CP if proposal would be accepted: " + str(CP_new))

        # Now we loop trough all the non_user_parties
        Parties_model = Parties.objects.all()
        for party in Parties_model:
            print("---" + party.Name + "---")
            # We calculate the LRCP distance between the parties ideology against the situation if the proposal
            # is voted yes and voted no
            Distance_if_yes_vote = Coordinate_distance(party.LR, party.CP, LR_new, CP_new)
            Distance_if_no_vote = Coordinate_distance(party.LR, party.CP, LR, CP)
            print("Distance if vote yes: " + str(Distance_if_yes_vote))
            print("Distance if vote no: " + str(Distance_if_no_vote))
            
            # We combine a string with the current "i" to get a variable that we can use for settattr in the
            # upcmoming if-then
            Vote_proposal = ("Vote_proposal_" + str(i))
            # The expected vote proposal is only for user-parties. We guess what users are going to vote so
            # if users suggest a policy deal, non-user parties can calculate whether its a good deal
            Expected_vote_proposal = ("Expected_vote_proposal_" + str(i))

            # Depending on which has the shortest distance the party is set to vote yes or no
            if Distance_if_yes_vote < Distance_if_no_vote:
                print("Vote Yes")
                if party.User == None:
                    setattr(party, Vote_proposal, "Yes")
                else:
                    setattr(party, Expected_vote_proposal, "Yes")
                party.save()
            else:
                print("Vote No")
                if party.User == None:
                    setattr(party, Vote_proposal, "No")
                else:
                    setattr(party, Expected_vote_proposal, "No")
                party.save()
        
        # In case 2 or 3 of three proposals have the same Parent topic we need to reset the parent score
        # if not, the next loop will add up the proposal score to the already adjusted parent score
        setattr(General_model, proposal.Parent, Parent_score_if_no)
        print("")

# This function determines whether a non-user party accepts a poltical deal from a user party
def Propose_deal(FormInput):
    User_party = Parties.objects.get(Name=FormInput.get("party_name"))
    print("The current user party is: " + str(User_party))
    Other_party = Parties.objects.get(Name=FormInput.get("other_party"))
    print("The other party is: " + str(Other_party))

    # First we check if the non-user party has not already made a deal, it cannot make more than one deal
    if Other_party.Made_deal == "Yes":
        print("This party already made a deal")
        User_party.Message_proposal_deal = (str(Other_party) + " already made a deal on these proposals")
    else:
        # Second we check whether the user party is known for breaking deals.
        if User_party.Deal_breaker == True:
            print("The deal proposing party is know for breaking deals, so no deal possible")
            User_party.Message_proposal_deal = ("You are known for breaking deals, " + str(Other_party) + " doesn't trust you.")
        else:
            # We calculate the the total number of votes (yes or no * number of seats) that are favorable for the
            # non user party if there is no deal. We use the "expected vote" for the user parties. we calculated
            # earlier what we expect users to vote.
            Without_deal_in_favor = 0
            if User_party.Expected_vote_proposal_1 == Other_party.Vote_proposal_1:
                Without_deal_in_favor += User_party.Seats
            if User_party.Expected_vote_proposal_2 == Other_party.Vote_proposal_2:
                Without_deal_in_favor += User_party.Seats
            if User_party.Expected_vote_proposal_3 == Other_party.Vote_proposal_3:
                Without_deal_in_favor += User_party.Seats
            Without_deal_in_favor += (Other_party.Seats*3)
            print("Without deal <" + str(Without_deal_in_favor) + "> expected votes favor the other party")
            
            # Now we calculate the number of votes if the deal is accepted by the non user party
            With_deal_in_favor = 0
            if FormInput.get("Deal_proposal_1_user") == Other_party.Vote_proposal_1:
                With_deal_in_favor += User_party.Seats
            if FormInput.get("Deal_proposal_2_user") == Other_party.Vote_proposal_2:
                With_deal_in_favor += User_party.Seats
            if FormInput.get("Deal_proposal_3_user") == Other_party.Vote_proposal_3:
                With_deal_in_favor += User_party.Seats
            if FormInput.get("Deal_proposal_1_other") == Other_party.Vote_proposal_1:
                With_deal_in_favor += Other_party.Seats
            if FormInput.get("Deal_proposal_2_other") == Other_party.Vote_proposal_2:
                With_deal_in_favor += Other_party.Seats
            if FormInput.get("Deal_proposal_3_other") == Other_party.Vote_proposal_3:
                With_deal_in_favor += Other_party.Seats
            print("With deal <" + str(With_deal_in_favor) + "> votes favor the other party") 

            # If the deal increases the favorable votes it is accepted
            if With_deal_in_favor <= Without_deal_in_favor:
                print("No deal")
                User_party.Message_proposal_deal = (str(Other_party) + " doesn't think is a fair deal")
            else:
                print("Deal")
                # we create an entry for the Deal-model which we use later to check whether the user party
                # kept his part of the deal
                Deals.objects.create(    
                    Current = True,
                    User = User_party.User,
                    User_party = User_party,
                    Other_party = Other_party.Name,
                    Promised_vote_proposal_1 = FormInput.get("Deal_proposal_1_user"),
                    Promised_vote_proposal_2 = FormInput.get("Deal_proposal_2_user"),
                    Promised_vote_proposal_3 = FormInput.get("Deal_proposal_3_user")
                )
                # We save the deal for the non user party, this way we ensure the non user party will keep his part
                Other_party.Vote_proposal_1 = FormInput.get("Deal_proposal_1_other")
                Other_party.Vote_proposal_2 = FormInput.get("Deal_proposal_2_other")
                Other_party.Vote_proposal_3 = FormInput.get("Deal_proposal_3_other")
                Other_party.Made_deal = "Yes"
                Other_party.save()

    User_party.save()

# This functions lets a logged in user save his voting choice
def Save_user_vote(FormInput):
    User_party = Parties.objects.get(Name=FormInput.get("Party_name"))
    User_party.Vote_proposal_1 = FormInput.get("Vote_proposal_1")
    User_party.Vote_proposal_2 = FormInput.get("Vote_proposal_2")
    User_party.Vote_proposal_3 = FormInput.get("Vote_proposal_3")
    User_party.save()

# This function holds a vote and counts the votes for each proposal 
def Hold_vote():
    Parties_model = Parties.objects.all()

    for i in range(1,4):
        General_model = General.objects.get(Name="Game1")
        Yes_vote = 0
        No_vote = 0
        Vote_proposal = ("Vote_proposal_" + str(i))
        print(Vote_proposal)

        for party in Parties_model:
            Vote = getattr(party, Vote_proposal)
            print(str(party.Name) + ": " + str(Vote))

            Vote_value = party.Seats
            if Vote == "Yes":
                Yes_vote += Vote_value
            else:
                No_vote += Vote_value
        
        print("Yes votes: " + str(Yes_vote))
        print("No votes: " + str(No_vote))

        if Yes_vote > No_vote:
            print("A majority votes Yes")

            proposal = Topics.objects.get(Current_proposal_number = i)
            print("The topic of the proposal is: " + str(proposal.Parent))

            Topic_score = getattr(General_model, proposal.Parent)
            print("Old score is: " + str(Topic_score))
            Topic_score += proposal.Shift
            # The theme_score can not get larger than 100
            if Topic_score > 100:
                Topic_score = 100
            if Topic_score < -100:
                Topic_score = -100
            print("New score is: " + str(Topic_score))
            setattr(General_model, proposal.Parent, Topic_score)
            # Because the progress bars in the countrymenu need a 0-100 score instead of a -100 to 100 score 
            # we converse the Theme_score to a Theme_score_bar. This is for display/html purposes.
            Topic_score_bar = (Topic_score + 100) / 2
            setattr(General_model, (proposal.Parent + "_bar"), Topic_score_bar)

            print(getattr(General_model, ("Message_outcome_proposal_" + str(i))))
            print("Message_outcome_proposal_" + str(i))
            print("Accepted: " + str(Yes_vote) + " against " + str(No_vote))
            setattr(General_model, ("Message_outcome_proposal_" + str(i)), ("Accepted: " + str(Yes_vote) + " against " + str(No_vote)))
            print(getattr(General_model, ("Message_outcome_proposal_" + str(i))))

        else:
            print("No majority, the proposal is not accepted")
            setattr(General_model, ("Message_outcome_proposal_" + str(i)), ("Rejected: " + str(Yes_vote) + " against " + str(No_vote)))

        print("")
        General_model.save()
    
    # This functions calculates the LR-CP ratio of the country based on the score on all themes
    Calculate_general_lrcp()

# This functions checks after votes are held whether non user parties kept their deals
def Deal_check():
    print("")
    print("--- Dealcheck ---")
    Current_deals = Deals.objects.filter(Current=True)

    # For deals that are current we check whether promise matches actual voting behaviour
    for deal in Current_deals:
        print(str(deal.User_party) + " promised " + str(deal.Promised_vote_proposal_1) + str(deal.Promised_vote_proposal_2) + str(deal.Promised_vote_proposal_3))
        print(str(deal.User_party) + " voted " + str(deal.User_party.Vote_proposal_1) + str(deal.User_party.Vote_proposal_2) + str(deal.User_party.Vote_proposal_3))
        if (
            deal.Promised_vote_proposal_1 != deal.User_party.Vote_proposal_1 or
            deal.Promised_vote_proposal_2 != deal.User_party.Vote_proposal_2 or
            deal.Promised_vote_proposal_3 != deal.User_party.Vote_proposal_3
        ):
            deal.User_party.Deal_breaker = True
            deal.User_party.save()
            print("Deal breaker")
        else:
            print("Deal keeper")
        
        # we set the current deal to false
        deal.Current = False
        deal.save()
    
    Parties_model = Parties.objects.all()
    for party in Parties_model:
        party.Made_deal = "No"
        party.save()

# This function calculates the LR-CP ratio of the country after a vote (submit_votes)
def Calculate_general_lrcp():
    General_model = General.objects.get(Name="Game1")
    LR = (
        General_model.Worldview +
        General_model.Nature +
        General_model.Taxation +
        General_model.Social_protection
    ) / 4

    CP = (
        General_model.Worldview +
        General_model.Ethics +
        General_model.Immigration -
        General_model.Nature
    ) / 4

    General_model.LR = LR
    General_model.CP = CP
    General_model.LR_bar = (LR + 100) / 2
    General_model.CP_bar = 100 - ((CP + 100) / 2)
    General_model.save()

# <Testmodus> This function changes the Next_action by force
def Force_next_action():
    General_model = General.objects.get(Name="Game1")
    Next_action = General_model.Next_action
    Year = General_model.Year
        
    if Next_action == "Submit candidates":
        Next_action = "Hold elections"
    elif Next_action == "Hold elections":
        Next_action = "Propose declaration"
    elif Next_action == "Propose declaration":
        Next_action = "Form government"
    elif Next_action == "Form government":
        Next_action = "Discuss proposals"
    elif Next_action == "Discuss proposals":
        Next_action = "Study outcome"
    elif Next_action == "Study outcome" and Year < 4:
        Next_action = "Discuss proposals"
        Year += 1
    elif Next_action == "Study outcome":
        Next_action = "Submit candidates"
        Year = 1
        
    print(Next_action)
    print("The year is: " + str(Year))

    General_model.Year = Year
    General_model.Next_action = Next_action
    General_model.save()

    Parties_model = Parties.objects.all()
    for party in Parties_model:
        party.Next_action = 0
        party.save()

# This function changes the Next_action (incl textboxes and disabling buttons)
def Next_action(FormInput):
    Former_turn_party = Parties.objects.get(Turn="Now")
    print("The party that had the turn: " + str(Former_turn_party))
    Former_turn_party.Turn = "Done"
    Former_turn_party.save()
   
    Number_of_users = Parties.objects.exclude(User=None).count()
    print("Number of user: " + str(Number_of_users))
    Number_of_users_done = Parties.objects.filter(Turn="Done").count()
    print("Number of users had their turn: " + str(Number_of_users_done))

    Next_action_ready = "No"
    if Number_of_users == Number_of_users_done:
        print("Time for the next action")
        Next_action_ready = "Yes"
        User_parties = Parties.objects.exclude(User=None)
        for party in User_parties:
            party.Turn = "Not yet"
            party.save()

    Current_turn_party = Parties.objects.filter(Turn="Not yet").order_by("Seats").first()
    print("The turn goes to " + str(Current_turn_party.Name))
    Current_turn_party.Turn = "Now"
    Current_turn_party.save()
    
    if Next_action_ready == "Yes":
        General_model = General.objects.get(Name="Game1")
        Next_action = General_model.Next_action

        Year = General_model.Year
            
        if Next_action == "Submit candidates":
            Next_action = "Hold elections"
        elif Next_action == "Hold elections":
            Hold_elections()
            Next_action = "Propose declaration"
            Appoint_declaration_maker()
        elif Next_action == "Propose declaration":
            Next_action = "Form government"
        elif Next_action == "Form government":
            Proposed_declaration_reaction()
            General_model = General.objects.get(Name="Game1")
            if General_model.Status_forming_government == "Succes" or General_model.Status_forming_government == "Failed":
                Next_action = "Discuss proposals"
                Non_user_vote_selections()
            else:
                Next_action = "Propose declaration"
                Appoint_declaration_maker()
        elif Next_action == "Discuss proposals":
            Deal_check()
            Hold_vote()
            General_model = General.objects.get(Name="Game1")
            Next_action = "Study outcome"
        elif Next_action == "Study outcome" and Year < 4:
            Select_three_new_proposals()
            Next_action = "Discuss proposals"
            Year += 1
        elif Next_action == "Study outcome":
            Next_action = "Submit candidates"
            Non_user_candidate_selection()
            Year = 1
            
        print(Next_action)
        print("The year is: " + str(Year))

        General_model.Year = Year
        General_model.Next_action = Next_action
        General_model.save()

# This function saves a proposed government declaration so other parties can see it
def Save_government_declaration(FormInput):
    General_model = General.objects.get(Name="Game1")

    General_model.Worldview_govt = FormInput.get("Worldview")
    General_model.Nature_govt = FormInput.get("Nature")
    General_model.Ethics_govt = FormInput.get("Ethics")
    General_model.Taxation_govt = FormInput.get("Taxation")
    General_model.Social_protection_govt = FormInput.get("Social_protection")
    General_model.Immigration_govt = FormInput.get("Immigration")
    General_model.save()

# This functions calculates the effect of the proposed govt declaration on lrcp
def Calculate_lrcp_effect_government_declaration(Succes):
    General_model = General.objects.get(Name="Game1")

    # It takes all the variables that are put in the declaration and provide a score
    print(General_model.Worldview_govt)
    if General_model.Worldview_govt == "More national":
        General_model.Worldview += -10
        print("-10")
    else:
        General_model.Worldview += 10
        print("10")

    print(General_model.Nature_govt)
    if General_model.Nature_govt == "More preservation":
        General_model.Nature += -10
        print("-10")
    else:
        General_model.Nature += 10
        print("10")

    print(General_model.Ethics_govt)
    if General_model.Ethics_govt == "More conservative":
        General_model.Ethics += -10
        print("-10")
    else:
        General_model.Ethics += 10
        print("10")

    print(General_model.Taxation_govt)
    if General_model.Taxation_govt == "Higher taxes":
        General_model.Taxation += -10
        print("-10")
    else:
        General_model.Taxation += 10
        print("10")

    print(General_model.Social_protection_govt)
    if General_model.Social_protection_govt == "More government":
        General_model.Social_protection += -10
        print("-10")
    else:
        General_model.Social_protection += 10
        print("10")

    print(General_model.Immigration_govt)
    if General_model.Immigration_govt == "More closed borders":
        General_model.Immigration += -10
        print("-10")
    else:
        General_model.Immigration += 10
        print("10")

    # It calculates the effect on LR and CP
    LR = (
        General_model.Worldview +
        General_model.Nature +
        General_model.Taxation +
        General_model.Social_protection
    ) / 4

    CP = (
        General_model.Worldview +
        General_model.Ethics +
        General_model.Immigration -
        General_model.Nature
    ) / 4

    print("LR if decl. accepted: " + str(LR))
    print("CP if decl. accepted: " + str(CP))

    # This funtion can be called after a majority accepted governement declaration
    # in that case all above actions are saved. Else they are not saved but only a LR, CP
    # output is generated
    if Succes == "Yes":
        General_model.Worldview_bar = (General_model.Worldview + 100 ) /2
        General_model.Nature_bar = (General_model.Nature + 100 ) /2
        General_model.Ethics_bar = (General_model.Ethics + 100 ) /2
        General_model.Taxation_bar = (General_model.Taxation + 100 ) /2
        General_model.Social_protection_bar = (General_model.Social_protection + 100 ) /2
        General_model.Immigration_bar = (General_model.Immigration + 100 ) /2
        General_model.CP_bar = 100 - (CP + 100) / 2
        General_model.LR_bar = (LR + 100) / 2
        General_model.CP = CP
        General_model.LR = LR
        General_model.save()
    else:
        # It returns the LR and CP so other functions can use this to either make AI-players decide
        # whether they accept the declaration.
        return(LR, CP)

# This function calculates whether non-user parties agree with the proposed declaration
# and whether the declaration has majority support
def Proposed_declaration_reaction():
    Non_user_parties = Parties.objects.filter(User=None)
    General_model = General.objects.get(Name="Game1")

    # We calculate the new LR and CP if the proposed government declaration would be accepted
    LR_new, CP_new = Calculate_lrcp_effect_government_declaration("No")
    LR_current = General_model.LR
    CP_current = General_model.CP
    
    print("LR current: " + str(LR_current))
    print("CP current: " + str(CP_current))

    # Now we check for every nonn_user party whether the new CP-LR would be an improvement
    # if yes, the party accepts the proposed declaration
    for party in Non_user_parties:
        Party_LR = party.LR
        Party_CP = party.CP

        Current_distance = Coordinate_distance(Party_LR, Party_CP, LR_current, CP_current)
        print(party.Name + " current distance: " + str(Current_distance))

        New_distance = Coordinate_distance(Party_LR, Party_CP, LR_new, CP_new)
        print(party.Name + " new distance: " + str(New_distance))

        if New_distance < Current_distance or party.Declaration_maker == "Yes":
            party.Declaration_reaction = "Accepts"
        else:
            party.Declaration_reaction = "Rejects"
        party.save()
        print(party.Declaration_reaction)
    
    # We calculate whether the proposed declaration has received majority support
    Parties_model = Parties.objects.all()
    
    Accept = 0
    Reject = 0
    for party in Parties_model:
        Reaction = party.Declaration_reaction
        # we take into consideration the value (eg. Seats) of the vote of a party
        Reaction_value = party.Seats
        if Reaction == "Accepts":
            Accept += Reaction_value
        else:
            Reject += Reaction_value
    
    print("Seats accepting declaration: " + str(Accept))
    print("Seats rejecting declaration: " + str(Reject))

    General_model = General.objects.get(Name="Game1")
    General_model.Votes_for_declaration = Accept
    General_model.Votes_against_declaration = Reject

    if Accept > Reject:
        General_model.Status_forming_government = "Succes"
        General_model.save()
        Calculate_lrcp_effect_government_declaration("Yes")
    else:
        Current_declaration_maker = Parties.objects.all().get(Declaration_maker="Yes")
        Current_declaration_maker.Declaration_maker = "Failed"
        Current_declaration_maker.save()
        General_model.Status_forming_government = "Attempting"

        Parties_model = Parties.objects.all().filter(Declaration_maker="No")
        if Parties_model.count() == 0:
            General_model.Status_forming_government = "Failed"
        General_model.save()

# This functions lets a logged in user save his voting choice
def Save_user_declaration_reaction(FormInput):
    User_party = Parties.objects.get(Name=FormInput.get("party_name"))
    User_party.Declaration_reaction = FormInput.get("Declaration_reaction")
    User_party.save()

# This functions checks which party may propose a government declaration
def Appoint_declaration_maker():
    # We take all parties that have not tried/failed yet to propose a government declaration from the database
    # and order them by number of seats, the biggest one first.
    Parties_model = Parties.objects.all().filter(Declaration_maker="No").order_by("-Seats")
    print(Parties_model)

    # We check whether there are multiple parties who have the samen number of most seats
    Most_seats  = Parties_model.first().Seats
    print("Most seats = " + str(Most_seats))

    Largest_party = Parties_model.filter(Seats=Most_seats)
    print(Largest_party)

    # In case multiple parties are biggest together we pick one random to be declaration maker
    # if there is only party the largeste, that party will be declaration maker.
    if Largest_party.count() > 1:
        Winner = Largest_party.order_by("?").first()
        Winner.Declaration_maker = "Yes"
        print("Declaration maker (after draw) = " + str(Winner.Name))
    else:
        Winner = Largest_party.first()
        print("Declaration maker = " + str(Winner.Name))
        Winner.Declaration_maker = "Yes"
    Winner.save()

# This function creates a declaration proposal for a non-user party
def Non_user_declaration_proposal():
    #First we check whether there is a declaration maker
    # if so, the function continues, else it stops.
    try:
        Current_declaration_maker = Parties.objects.all().get(Declaration_maker="Yes")
        print("The declaration_maker = " + str(Current_declaration_maker))
    except:
        print("There is no current declaration maker")
        return

    # Second we check whether the declaration maker is a non_user party
    # if so, the function continues, else it stops.
    if Current_declaration_maker.User == None:
        print("Declaration maker is a computer")

        # In the next part a random declaration proposal will be made. After that we
        # check whether the proposal is beneficial for the proposal maker. If not the loop
        # starts again. This continues until a random proposal is positive or we made
        # 10 loops. In that case the last random proposal is presented to the other parties.
        Good_proposal = 0
        Count = 0
        while Count < 10 and  Good_proposal == 0:
            General_model = General.objects.get(Name="Game1")

            # For every topic we randomly select one of the two options
            # also we incorporate the numerical effect it has on this topic
            Dice = random.randint(0,1)       
            if Dice == 0:
                General_model.Worldview_govt = "More national"
                Worldview = General_model.Worldview -10
            else:
                General_model.Worldview_govt = "More global"
                Worldview = General_model.Worldview + 10
            print(General_model.Worldview_govt)
            print(Worldview)

            Dice = random.randint(0,1)       
            if Dice == 0:
                General_model.Nature_govt = "More preservation"
                Nature = General_model.Nature  -10
            else:
                General_model.Nature_govt = "More exploitation"
                Nature = General_model.Nature + 10
            print(General_model.Nature_govt)
            print(Nature)

            Dice = random.randint(0,1)
            if Dice == 0:
                General_model.Ethics_govt = "More conservative"
                Ethics = General_model.Ethics -10
            else:
                General_model.Ethics_govt = "More liberal"
                Ethics = General_model.Ethics + 10
            print(General_model.Ethics_govt)
            print(Ethics)

            Dice = random.randint(0,1)     
            if Dice == 0:
                General_model.Taxation_govt = "Higher taxes"
                Taxation = General_model.Taxation -10
            else:
                General_model.Taxation_govt = "Lower taxes"
                Taxation = General_model.Taxation + 10
            print(General_model.Taxation_govt)
            print(Taxation)

            Dice = random.randint(0,1)
            if Dice == 0:
                General_model.Social_protection_govt = "More government"
                Social_protection = General_model.Social_protection -10
            else:
                General_model.Social_protection_govt = "More free market"
                Social_protection = General_model.Social_protection + 10
            print(General_model.Social_protection_govt)
            print(Social_protection)

            Dice = random.randint(0,1)
            if Dice == 0:
                General_model.Immigration_govt = "More closed borders"
                Immigration = General_model.Immigration -10
            else:
                General_model.Immigration_govt = "More shelter"
                Immigration = General_model.Immigration + 10
            print(General_model.Immigration_govt)
            print(Immigration)

            # Now we calculate the the effect the random proposal would have on the
            # LR and CP of the game.
            LR_new = (
                Worldview +
                Nature +
                Taxation +
                Social_protection
            ) / 4

            CP_new = (
                Worldview +
                Ethics +
                Immigration -
                Nature
            ) / 4

            print("LR if decl. accepted: " + str(LR_new))
            print("CP if decl. accepted: " + str(CP_new))

            # Here we check whether the random proposal LRCP is better or worse for the
            # declaration maker compared to the current LRCP
            Party_LR = Current_declaration_maker.LR
            Party_CP = Current_declaration_maker.CP
            LR_current = General_model.LR
            CP_current = General_model.CP

            Current_distance = Coordinate_distance(Party_LR, Party_CP, LR_current, CP_current)
            print(Current_declaration_maker.Name + " current distance: " + str(Current_distance))

            New_distance = Coordinate_distance(Party_LR, Party_CP, LR_new, CP_new)
            print(Current_declaration_maker.Name + " new distance: " + str(New_distance))

            # If the random proposal is beneficial for the declaration maker we exit the loop
            # if not we re-enter the loop for a new random proposal.
            if New_distance < Current_distance:
                print("Good proposal")
                Good_proposal = 1
            else:
                print("Bad proposal")
                Count += 1

        # The last random proposal is saved to the model / database
        print("Loops needed: " + str(Count))
        General_model.save()

    else:
        print("Declaration maker is a user")
        return

def Test():
    General_model = General.objects.get(Name="Game1")

    if General_model.Test == False:
        General_model.Test = True
        General_model.save()
        print("Test modus activated")
    else:
        General_model.Test = False
        General_model.save()
        print("Test modus deactivated")