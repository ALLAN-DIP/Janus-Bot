__author__ = "Konstantine Kahadze"
__email__ = "konstantinekahadze@gmail.com"

from typing import Tuple
from daidepp.grammar import create_daide_grammar
from daidepp.node_visitor import daide_visitor
import random

ADJACENCY = {'ADR': ['ALB', 'APU', 'ION', 'TRI', 'VEN'], 'AEG': ['BUL/SC', 'CON', 'EAS', 'GRE', 'ION', 'SMY'], 'ALB': ['ADR', 'GRE', 'ION', 'SER', 'TRI'], 'ANK': ['ARM', 'BLA', 'CON', 'SMY'], 'APU': ['ADR', 'ION', 'NAP', 'ROM', 'VEN'], 'ARM': ['ANK', 'BLA', 'SEV', 'SMY', 'SYR'], 'BAL': ['BER', 'BOT', 'DEN', 'LVN', 'KIE', 'PRU', 'SWE'], 'BAR': ['NWY', 'NWG', 'STP/NC'], 'BEL': ['BUR', 'ENG', 'HOL', 'NTH', 'PIC', 'RUH'], 'BER': ['BAL', 'KIE', 'MUN', 'PRU', 'SIL'], 'BLA': ['ANK', 'ARM', 'BUL/EC', 'CON', 'RUM', 'SEV'], 'BOH': ['GAL', 'MUN', 'SIL', 'TYR', 'VIE'], 'BOT': ['BAL', 'FIN', 'LVN', 'STP/SC', 'SWE'], 'BRE': ['ENG', 'GAS', 'MAO', 'PAR', 'PIC'], 'BUD': ['GAL', 'RUM', 'SER', 'TRI', 'VIE'], 'BUL/EC': ['BLA', 'CON', 'RUM'], 'BUL/SC': ['AEG', 'CON', 'GRE'], 'BUL': ['AEG', 'BLA', 'CON', 'GRE', 'RUM', 'SER'], 'BUR': ['BEL', 'GAS', 'RUH', 'MAR', 'MUN', 'PAR', 'PIC', 'SWI'], 'CLY': ['EDI', 'LVP', 'NAO', 'NWG'], 'CON': ['AEG', 'BUL/EC', 'BUL/SC', 'BLA', 'ANK', 'SMY'], 'DEN': ['BAL', 'HEL', 'KIE', 'NTH', 'SKA', 'SWE'], 'EAS': ['AEG', 'ION', 'SMY', 'SYR'], 'EDI': ['CLY', 'LVP', 'NTH', 'NWG', 'YOR'], 'ENG': ['BEL', 'BRE', 'IRI', 'LON', 'MAO', 'NTH', 'PIC', 'WAL'], 'FIN': ['BOT', 'NWY', 'STP/SC', 'SWE'], 'GAL': ['BOH', 'BUD', 'RUM', 'SIL', 'UKR', 'VIE', 'WAR'], 'GAS': ['BUR', 'BRE', 'MAO', 'MAR', 'PAR', 'SPA/NC'], 'GRE': ['AEG', 'ALB', 'BUL/SC', 'ION', 'SER'], 'HEL': ['DEN', 'HOL', 'KIE', 'NTH'], 'HOL': ['BEL', 'HEL', 'KIE', 'NTH', 'RUH'], 'ION': ['ADR', 'AEG', 'ALB', 'APU', 'EAS', 'GRE', 'NAP', 'TUN', 'TYS'], 'IRI': ['ENG', 'LVP', 'MAO', 'NAO', 'WAL'], 'KIE': ['BAL', 'BER', 'DEN', 'HEL', 'HOL', 'MUN', 'RUH'], 'LON': ['ENG', 'NTH', 'YOR', 'WAL'], 'LVN': ['BAL', 'BOT', 'MOS', 'PRU', 'STP/SC', 'WAR'], 'LVP': ['CLY', 'EDI', 'IRI', 'NAO', 'WAL', 'YOR'], 'LYO': ['MAR', 'PIE', 'SPA/SC', 'TUS', 'TYS', 'WES'], 'MAO': ['BRE', 'ENG', 'GAS', 'IRI', 'NAF', 'NAO', 'POR', 'SPA/NC', 'SPA/SC', 'WES'], 'MAR': ['BUR', 'GAS', 'LYO', 'PIE', 'SPA/SC', 'SWI'], 'MOS': ['LVN', 'SEV', 'STP', 'UKR', 'WAR'], 'MUN': ['BER', 'BOH', 'BUR', 'KIE', 'RUH', 'SIL', 'TYR', 'SWI'], 'NAF': ['MAO', 'TUN', 'WES'], 'NAO': ['CLY', 'IRI', 'LVP', 'MAO', 'NWG'], 'NAP': ['APU', 'ION', 'ROM', 'TYS'], 'NWY': ['BAR', 'FIN', 'NTH', 'NWG', 'SKA', 'STP/NC', 'SWE'], 'NTH': ['BEL', 'DEN', 'EDI', 'ENG', 'LON', 'HEL', 'HOL', 'NWY', 'NWG', 'SKA', 'YOR'], 'NWG': ['BAR', 'CLY', 'EDI', 'NAO', 'NWY', 'NTH'], 'PAR': ['BUR', 'BRE', 'GAS', 'PIC'], 'PIC': ['BEL', 'BRE', 'BUR', 'ENG', 'PAR'], 'PIE': ['LYO', 'MAR', 'TUS', 'TYR', 'VEN', 'SWI'], 'POR': ['MAO', 'SPA/NC', 'SPA/SC'], 'PRU': ['BAL', 'BER', 'LVN', 'SIL', 'WAR'], 'ROM': ['APU', 'NAP', 'TUS', 'TYS', 'VEN'], 'RUH': ['BEL', 'BUR', 'HOL', 'KIE', 'MUN'], 'RUM': ['BLA', 'BUD', 'BUL/EC', 'GAL', 'SER', 'SEV', 'UKR'], 'SER': ['ALB', 'BUD', 'BUL', 'GRE', 'RUM', 'TRI'], 'SEV': ['ARM', 'BLA', 'MOS', 'RUM', 'UKR'], 'SIL': ['BER', 'BOH', 'GAL', 'MUN', 'PRU', 'WAR'], 'SKA': ['DEN', 'NWY', 'NTH', 'SWE'], 'SMY': ['AEG', 'ANK', 'ARM', 'CON', 'EAS', 'SYR'], 'SPA/NC': ['GAS', 'MAO', 'POR'], 'SPA/SC': ['LYO', 'MAO', 'MAR', 'POR', 'WES'], 'SPA': ['GAS', 'LYO', 'MAO', 'MAR', 'POR', 'WES'], 'STP/NC': ['BAR', 'NWY'], 'STP/SC': ['BOT', 'FIN', 'LVN'], 'STP': ['BAR', 'BOT', 'FIN', 'LVN', 'MOS', 'NWY'], 'SWE': ['BAL', 'BOT', 'DEN', 'FIN', 'NWY', 'SKA'], 'SYR': ['ARM', 'EAS', 'SMY'], 'TRI': ['ADR', 'ALB', 'BUD', 'SER', 'TYR', 'VEN', 'VIE'], 'TUN': ['ION', 'NAF', 'TYS', 'WES'], 'TUS': ['LYO', 'PIE', 'ROM', 'TYS', 'VEN'], 'TYR': ['BOH', 'MUN', 'PIE', 'TRI', 'VEN', 'VIE', 'SWI'], 'TYS': ['ION', 'LYO', 'ROM', 'NAP', 'TUN', 'TUS', 'WES'], 'UKR': ['GAL', 'MOS', 'RUM', 'SEV', 'WAR'], 'VEN': ['ADR', 'APU', 'PIE', 'ROM', 'TRI', 'TUS', 'TYR'], 'VIE': ['BOH', 'BUD', 'GAL', 'TRI', 'TYR'], 'WAL': ['ENG', 'IRI', 'LON', 'LVP', 'YOR'], 'WAR': ['GAL', 'LVN', 'MOS', 'PRU', 'SIL', 'UKR'], 'WES': ['MAO', 'LYO', 'NAF', 'SPA/SC', 'TUN', 'TYS'], 'YOR': ['EDI', 'LON', 'LVP', 'NTH', 'WAL'], 'SWI': ['MAR', 'BUR', 'MUN', 'TYR', 'PIE']}
TYPES = {'ADR': 'WATER', 'AEG': 'WATER', 'ALB': 'COAST', 'ANK': 'COAST', 'APU': 'COAST', 'ARM': 'COAST', 'BAL': 'WATER', 'BAR': 'WATER', 'BEL': 'COAST', 'BER': 'COAST', 'BLA': 'WATER', 'BOH': 'LAND', 'BOT': 'WATER', 'BRE': 'COAST', 'BUD': 'LAND', 'BUL/EC': 'COAST', 'BUL/SC': 'COAST', 'bul': 'COAST', 'BUR': 'LAND', 'CLY': 'COAST', 'CON': 'COAST', 'DEN': 'COAST', 'EAS': 'WATER', 'EDI': 'COAST', 'ENG': 'WATER', 'FIN': 'COAST', 'GAL': 'LAND', 'GAS': 'COAST', 'GRE': 'COAST', 'HEL': 'WATER', 'HOL': 'COAST', 'ION': 'WATER', 'IRI': 'WATER', 'KIE': 'COAST', 'LON': 'COAST', 'LVN': 'COAST', 'LVP': 'COAST', 'LYO': 'WATER', 'MAO': 'WATER', 'MAR': 'COAST', 'MOS': 'LAND', 'MUN': 'LAND', 'NAF': 'COAST', 'NAO': 'WATER', 'NAP': 'COAST', 'NWY': 'COAST', 'NTH': 'WATER', 'NWG': 'WATER', 'PAR': 'LAND', 'PIC': 'COAST', 'PIE': 'COAST', 'POR': 'COAST', 'PRU': 'COAST', 'ROM': 'COAST', 'RUH': 'LAND', 'RUM': 'COAST', 'SER': 'LAND', 'SEV': 'COAST', 'SIL': 'LAND', 'SKA': 'WATER', 'SMY': 'COAST', 'SPA/NC': 'COAST', 'SPA/SC': 'COAST', 'spa': 'COAST', 'STP/NC': 'COAST', 'STP/SC': 'COAST', 'stp': 'COAST', 'SWE': 'COAST', 'SYR': 'COAST', 'TRI': 'COAST', 'TUN': 'COAST', 'TUS': 'COAST', 'TYR': 'LAND', 'TYS': 'WATER', 'UKR': 'LAND', 'VEN': 'COAST', 'VIE': 'LAND', 'WAL': 'COAST', 'WAR': 'LAND', 'WES': 'WATER', 'YOR': 'COAST', 'SWI': 'SHUT'}
COMBOS = {
    "FLT" : {"FLT": {"WATER", "COAST"}, "AMY": {"LAND", "COAST"}},
    "AMY" : {"FLT": {"COAST"}, "AMY": {"LAND", "COAST"}}
}


st = [(('FRA', 'AMY', 'PAR'), 'MTO', 'PIC') , (('FRA', 'AMY', 'PAR') ,'MTO', 'BUR') ,(('GER', 'AMY', 'MUN') ,'MTO', 'BUR')]

def random_orders(orders : list):
    '''
    Takes in a list of orders and returns similar but randomly deviant orders.
    '''
    assert contains_only_moves(orders)
    print("Orders:", orders)
    map(lambda order: randomize(order), orders)
    print(orders)

def randomize(order: tuple) -> tuple:
    '''
        Takes in an order and returns a randomly deviant verson of it.
    '''
    tag = order[1]
    tag_to_func = {
        "WVE": {lambda: order},
        "BLD": random_deviant(order), "REM": random_deviant(order), "DSB": random_deviant(order), 
        "MTO": random_movement(tag, order), "RTO": random_movement(tag, order), 
        "HLD": random_hold(order),
        "SUP": random_support(tag, order),
        "CVY": random_convoy(tag, order),
        "CTO": random_convoy_to(order)
    }
    return tag_to_func[tag]
    
def random_convoy_to(order):
    '''
    This takes a convoy order and returns the longest alternate convoy,
    '''
    (_, _, amy_loc), _, province, _, (sea_provinces) = order
    sea_provinces.reverse()
    for i, sea in enumerate(sea_provinces):
        valid = [loc for loc in ADJACENCY[sea] if TYPES[loc] == "COAST" and loc != [province] and loc not in ADJACENCY[amy_loc]]
        if valid:
            route = sea_provinces[i:]
            route.reverse()
            return (order[0], "CTO", random.choice(valid), "VIA", route)
    return order


def random_convoy(tag, order):
    '''
    This takes in the order and produces a convoy to a different destination if it is possible
    and believable. An unbelievable convoy would be one that convoys a unit to a province the
    unit can move to by itself.
    '''
    (amy_country, amy_type, amy_loc), _, (flt_country, flt_type, flt_loc), _, province = order
    assert amy_type == "AMY" and flt_type == "FLT"
    adj = [loc for loc in ADJACENCY[flt_loc] if TYPES[loc] == "COAST" and loc not in ADJACENCY[amy_loc] and loc != province]
    if adj:
        return (order[0], tag, order[2], "CTO", random.choice(adj))
    else:
        return order

def random_support(tag, order):
    if len(order) <= 3: # if it is supporting to hold
        (_, supporter_type, supporter_loc), _, (_, supported_type, supported_loc) = order
        supporter_adjacent, supported_adjacent = ADJACENCY[supporter_loc], ADJACENCY[supported_loc]
        adj_to_both = [adjacency for adjacency in supporter_adjacent if adjacency in supported_adjacent and (not dest_choices or TYPES[adjacency] in dest_choices)]
        chance_of_move = 0.5
        dest_choices = COMBOS[supporter_type][supported_type]
        if adj_to_both and random.random() < chance_of_move:
            return (order[0], "SUP", order[2], "MTO", random.choice(adj_to_both))
        else:
            return (order[0], tag, order[2])
    else: # if it is supporting to move
        (sup_country, sup_type, sup_loc), _, (rec_country, rec_type, rec_loc), _, province = order
        sup_adjacent, rec_adjacent = ADJACENCY[sup_loc], ADJACENCY[rec_loc]
        dest_choices = COMBOS[sup_type][rec_type]
        adj_to_both = [adjacency for adjacency in sup_adjacent if adjacency in rec_adjacent and adjacency != province and TYPES[adjacency]]
        if adj_to_both:
            return (order[0], tag, order[2], "MTO", random.choice(adj_to_both))
        else:
            return order
        

def random_movement(tag, order, chance_of_move=0.5):
    if random.random() < chance_of_move or tag == "RTO":
        (country, unit_type, loc), _,  dest  = order
        all_adjacent = ADJACENCY[loc]
        all_adjacent.remove(dest)
        new_dest = random.choice(all_adjacent)
        return ((country, unit_type, loc), tag, new_dest)
    else:
        return ((country, unit_type, loc), "HLD")
    
def random_hold(order, chance_of_move=0.5):
    if random.random() < chance_of_move:
        ((country, unit_type, loc), _) = order[0][2]
        move_loc = random.choice(ADJACENCY[loc])
        return ((country, unit_type, loc), "MTO", move_loc)
    else:
        return order

def random_deviant(real_choice, available=None):
    '''
        Takes in the real intended build location and an optional list
        of available places to build and returns a random deviant or
        the original value if there are no alternatives.
    '''
    if len(available) > 1:
        available.remove(real_choice)
        return random.choice(available)
    else:
        return real_choice

        
def contains_only_moves(list_in : list) -> bool:
    order_words = {"MTO", "SUP", "CVY", "HLD", "CTO", "RTO", "DSB", "BLD", "REM", "WVE"}
    for item in list_in:
        if (not isinstance(item, tuple)) or item[1] not in order_words:
            return False
    return True 
            
# print(random_build("PIC", available=["PIC", "PAR","BUR"]))
print(ADJACENCY["BUR"])