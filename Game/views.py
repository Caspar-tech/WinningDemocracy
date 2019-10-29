from django.shortcuts import render, redirect
from .forms import UserRegisterForm 
from .models import Counties, Representatives, Parties, General, Topics, Deals
from django.views.generic import ListView, DetailView
from .logic import (
    Reset, 
    Hold_elections,
    Hold_vote,
    Non_user_candidate_selection,
    Save_user_vote,
    Save_user_candidates,
    Save_government_declaration,
    Proposed_declaration_reaction,
    Save_user_declaration_reaction,
    Appoint_declaration_maker,
    Non_user_declaration_proposal,
    Select_three_new_proposals,
    Non_user_vote_selections,
    Propose_deal,
    Deal_check,
    Test,
    Next_action,
    Force_next_action,
)

#Main-page viewclass
class MainView(ListView):
    model = Counties
    template_name = 'Game/main.html'
    context_object_name = 'Counties'
    ordering = ['Name']

    # Overwrite standard "get_context" to add extra context (the Counties-model)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in QuerySets of extra context
        context['Parties'] = Parties.objects.all()
        context['Representatives'] = Representatives.objects.all()
        context['General'] = General.objects.get(Name="Game1")
        return context
    
    #Overwrite the post-method to execute functions when 
    #buttons are pushed with a post-method
    def post(self, request, *args, **kwargs):
        if request.POST.get('Reset') == 'Reset':
            Reset()
        if request.POST.get('Test') == 'Test':
            Test()
        if request.POST.get('Next_action') == 'Next_action':
            Next_action(request.POST)
        if request.POST.get('Force_next_action') == 'Force_next_action':
            Force_next_action()
        return super().get(request, *args, **kwargs)
        
#Register-page render function
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserRegisterForm()
    return render(request, 'Game/register.html', {'form': form})

#Counties-page viewclass
class ElectionsView(ListView):
    model = Counties
    template_name = 'Game/elections.html'
    context_object_name = 'Counties'
    ordering = ['Name']

    #Overwrite the post-method to execute functions when 
    #buttons are pushed with a post-method
    def post(self, request, *args, **kwargs):
        if request.POST.get('Hold elections') == 'Hold elections':
            Next_action(request.POST)
        if request.POST.get('Non_user_candidate_selection') == 'Non_user_candidate_selection':
            Non_user_candidate_selection()
        if request.POST.get('Save') == 'Save':
            Save_user_candidates(request.POST)
            Next_action(request.POST)
        return super().get(request, *args, **kwargs)

    # Overwrite standard "get_context" to add extra context (the Counties-model)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in QuerySets of extra context
        context['Parties'] = Parties.objects.all()
        context['User_parties'] = Parties.objects.exclude(User=None)
        context['Non_user_parties'] = Parties.objects.filter(User=None)
        context['Representatives'] = Representatives.objects.all()
        context['General'] = General.objects.get(Name="Game1")
        return context

#Page you can use to zoom into one county
class DetailCountiesView(DetailView):
    model = Counties
    template_name = 'Game/detail_counties.html'
    context_object_name = 'Counties'

    # Overwrite standard "get_context" to add extra context (the Repr-model)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in QuerySets of extra context
        context['Representatives'] = Representatives.objects.all()
        context['General'] = General.objects.get(Name="Game1")
        context['Parties'] = Parties.objects.all()
        return context

#Page you can use to zoom into one representative
class RepresentativesDetailView(DetailView):
    model = Representatives
    template_name = 'Game/detail_representatives.html'
    context_object_name = 'Representatives'

    # Overwrite standard "get_context" to add extra context (the Counties-model)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of extra context
        context['General'] = General.objects.get(Name="Game1")
        context['Counties'] = Counties.objects.all()
        context['Parties'] = Parties.objects.all()
        return context

#Page you can use to zoom into one party
class PartiesDetailView(DetailView):
    model = Parties
    template_name = 'Game/detail_parties.html'
    context_object_name = 'PartiesDetail'

    # Overwrite standard "get_context" to add extra context (the Repr-model)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of extra context
        context['Representatives'] = Representatives.objects.all()
        context['General'] = General.objects.get(Name="Game1")
        context['Parties'] = Parties.objects.all()
        return context

#Parliament-page viewclass, with Party-model
class ParliamentView(ListView):
    model = Parties
    template_name = 'Game/parliament.html'
    context_object_name = 'Parties'

    # Overwrite standard "get_context" to add extra context (the Repr-model)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of extra context
        context['Topics'] = Topics.objects.all()
        context['General'] = General.objects.get(Name="Game1")
        context['Current_proposals'] = Topics.objects.exclude(Current_proposal_number=None).order_by("Current_proposal_number")
        context['Deals'] = Deals.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('Non_user_vote_selections') == 'Non_user_vote_selections':
            Non_user_vote_selections()
        elif request.POST.get('Save') == 'Save':
            Save_user_vote(request.POST)
            Next_action(request.POST)
        elif request.POST.get('Select_three_new_proposals') == 'Select_three_new_proposals':
            Select_three_new_proposals()
        elif request.POST.get('Propose deal') == 'Propose deal':
            Propose_deal(request.POST)
        elif request.POST.get('Deal_check') == 'Deal_check':
            Deal_check() 
        elif request.POST.get('Continue') == 'Continue':
            Next_action(request.POST) 
        return super().get(request, *args, **kwargs)

#Government-page viewclass, with Party-model
class GovernmentView(ListView):
    model = Parties
    template_name = 'Game/government.html'
    context_object_name = 'Parties'
    ordering = ['Name']

    # Overwrite standard "get_context" to add extra context (the Repr-model)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of extra context
        context['General'] = General.objects.get(Name="Game1")
        return context
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('Propose declaration') == 'Propose declaration':
            Save_government_declaration(request.POST)
            Next_action(request.POST)
        if request.POST.get('Proposed_declaration_reaction') == 'Proposed_declaration_reaction':
            Proposed_declaration_reaction()
        if request.POST.get('Save') == 'Save':
            Save_user_declaration_reaction(request.POST)
            Next_action(request.POST)        
        if request.POST.get('Appoint_declaration_maker') == 'Appoint_declaration_maker':
            Appoint_declaration_maker()
        if request.POST.get('Continue') == 'Continue':
            Non_user_declaration_proposal()
            Next_action(request.POST)
        return super().get(request, *args, **kwargs)
        