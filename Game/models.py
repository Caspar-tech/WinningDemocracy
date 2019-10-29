from django.db import models
from django.contrib.auth.models import User

class General(models.Model):
    Name = models.TextField()
    Next_action = models.TextField(default="Submit candidates")
    Year = models.IntegerField(default=1)
    Test = models.BooleanField(default=False)
    Message_elections_page = models.TextField()
    Message_government_page = models.TextField()
    Message_outcome_proposal_1 = models.TextField(default="")
    Message_outcome_proposal_2 = models.TextField(default="")
    Message_outcome_proposal_3 = models.TextField(default="")
    Worldview = models.IntegerField(default=0)
    Nature = models.IntegerField(default=0)
    Ethics = models.IntegerField(default=0)
    Taxation = models.IntegerField(default=0)
    Social_protection = models.IntegerField(default=0)
    Immigration = models.IntegerField(default=0)
    LR = models.IntegerField(default=0)
    CP = models.IntegerField(default=0)
    Worldview_bar = models.IntegerField(default=0)
    Nature_bar = models.IntegerField(default=0)
    Ethics_bar = models.IntegerField(default=0)
    Taxation_bar = models.IntegerField(default=0)
    Social_protection_bar = models.IntegerField(default=0)
    Immigration_bar = models.IntegerField(default=0)
    LR_bar = models.IntegerField(default=0)
    CP_bar = models.IntegerField(default=0)
    Worldview_govt = models.TextField(default="")
    Nature_govt = models.TextField(default="")
    Ethics_govt = models.TextField(default="")
    Taxation_govt = models.TextField(default="")
    Social_protection_govt = models.TextField(default="")
    Immigration_govt = models.TextField(default="")
    Votes_for_declaration = models.IntegerField(default=0)
    Votes_against_declaration = models.IntegerField(default=0)
    Status_forming_government = models.TextField(default="")
    
    def __str__(self):
        return self.Name

class Parties(models.Model):
    Name = models.TextField()
    Next_action = models.IntegerField(default=0)
    Turn = models.TextField(null=True, default=None)
    CP = models.IntegerField()
    LR = models.IntegerField()
    User = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, default=None)
    Seats = models.IntegerField()
    Vote = models.TextField()
    Vote_proposal_1 = models.TextField(default="No")
    Vote_proposal_2 = models.TextField(default="No")
    Vote_proposal_3 = models.TextField(default="No")
    Expected_vote_proposal_1 = models.TextField(null=True, default=None)
    Expected_vote_proposal_2 = models.TextField(null=True, default=None)
    Expected_vote_proposal_3 = models.TextField(null=True, default=None)
    Made_deal = models.TextField(default="No")
    Message_proposal_deal =  models.TextField(default="")
    Deal_breaker = models.BooleanField(default=False)
    Prime_minister = models.BooleanField(default=False)
    Government = models.BooleanField(default=False)
    Declaration_maker = models.TextField(default="No")
    Declaration_reaction = models.TextField(default="Rejects")

    def __str__(self):
        return self.Name

class Representatives(models.Model):
    Name = models.TextField()
    CP = models.IntegerField()
    LR = models.IntegerField()
    Party = models.ForeignKey(Parties, on_delete=models.SET_NULL, null=True)
    County_election = models.TextField(default="")
    Percentage = models.FloatField(default=0)

    def __str__(self):
        return self.Name

# Every county has only 1 representative --> OnetoOneField
# On_delete the value becomes Null instead of the countty being deleted (models.CASCADE)
# But fur Null to be possible we have to set null=True
class Counties(models.Model):
    Name = models.TextField()
    CP = models.IntegerField()
    LR = models.IntegerField()
    Spread = models.IntegerField(default=2)
    Representative = models.OneToOneField(Representatives, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name

class Topics(models.Model):
    Proposal = models.TextField()
    Parent = models.TextField()
    Shift = models.IntegerField(default=10)
    New = models.BooleanField(default=True)
    Current_proposal = models.BooleanField(default=True)
    Current_proposal_number = models.IntegerField(null=True, default=None)

    def __str__(self):
        return self.Proposal

class Deals(models.Model):
    Current = models.BooleanField(default=True)
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    User_party = models.ForeignKey(Parties, on_delete=models.SET_NULL, null=True)
    Other_party = models.TextField(default="")
    Promised_vote_proposal_1 = models.TextField()
    Promised_vote_proposal_2 = models.TextField()
    Promised_vote_proposal_3 = models.TextField()
