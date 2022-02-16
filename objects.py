import enum 

class label:
    triage_accepted = 1
    needs_triage = 2 
    DNM_hold = 3
    DNM_wip = 4 
    DNM_needs_release_note = 5
    needs_rebase = 6
    priority = 7
    kind = 8
    lgtm = 9

class Card:
    def __init__(self, label, card_id): 
        self.label = label
        self.id = card_id

