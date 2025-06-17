import sqlite3
import pandas as pd
from main import *

def test_filtering():
    assert(df_no_moons.shape[0] == 2)
    assert(df_no_moons.iloc[0]['rings'] == 0)
    assert(df_name_seven.shape == (3, 2))
    assert(list(df_name_seven['name']) == ['Mercury', 'Jupiter', 'Neptune'])

def test_advanced_filtering():
    assert(df_mass.shape == (4, 2))
    assert(list(df_mass['name']) == ['Mercury', 'Venus', 'Earth', 'Mars'])
    assert(df_mass_moon.shape == (1, 6))
    assert(df_mass_moon['name'][0] == 'Mars')
    assert(df_blue.shape == (3, 2))
    assert(list(df_blue['name']) == ['Earth', 'Uranus', 'Neptune'])

def test_ordering_and_limiting():
    assert(list(df_hungry['name']) == ['Snoopy', 'Clifford', None, 'Scooby', 'Lassie', 'Pickles'])
    assert(df_hungry.iloc[0]['name'] == 'Snoopy')
    assert(list(df_hungry_ages['age']) == [4, 4, 7, 6, 3])
    assert(df_hungry_ages.iloc[-1]['name'] == 'Snoopy')
    # assert(list(df_4_oldest['name']) == ['Pickles', 'McGruff', 'Snowy', 'Lassie'])
    assert(list(df_4_oldest['name']) == ['Pickles', 'McGruff', 'Lassie', 'Snowy'])

    assert(df_4_oldest.iloc[0]['name'] == 'Pickles')

def test_aggregation():
    assert(df_ruth_years.values[0][0] == 22)
    assert(df_hr_total.values[0][0] == 714)

def test_grouping_and_aggregation():
    assert(list(df_teams_years['team']) == ['BOS', 'NY'])
    assert(list(df_teams_years['number_years']) == [7, 15])
    assert(round(df_at_bats['average_at_bats'][0]) == 481)
    assert(df_at_bats['team'][0] == 'NY')