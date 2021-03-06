# TODO:
# Read in the csv
# Total amount of gun deaths in each state
# Total amount of negative tweets in each state
# Save each of these in two arrays
# Write a new CSV with these numbers

# Load the Pandas libraries with alias 'pd'
import csv
import pandas as pd

# Initialize the arrays
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
          'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
state_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
               'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
state_populations = [4887871, 737438, 7171646,
                     3013825, 39557045, 5695564, 3572665, 967171, 21299325, 10519475, 1420491, 1754208, 12741080, 6691878, 3156145, 2911505, 4468402, 4659978, 1338404, 6042718, 6902149, 9995915, 5611179, 2986530, 6126452, 1062305, 1929268, 3034392, 1356458, 8908520, 2095428, 19542209, 10383620, 760077, 11689442, 3943079, 
                     4190713, 12807060, 1057315, 5084127, 882235, 6770010, 28701845, 3161105, 626299, 8517685, 7535591, 1805832, 5813568, 577737]
state_backgrounds = [474294, 78761, 377838, 248439, 1297132, 524770, 177690, 47723, 1203145, 549532, 14088, 207320, 2831447, 896148, 189159, 172047, 4912441, 307192, 93360, 151470, 211295, 489957, 604078, 247278, 469184, 117607, 74477, 127434, 120889, 93124, 156853, 358614, 529916, 62334, 717475, 332291, 359682, 1021943, 25030, 280749, 90693, 694101, 1571632, 295858, 41550, 476760, 627301, 241678, 452520, 60150]
state_votes = [62.1, 51.3, 48.1, 60.6, 31.5, 43.3, 40.9, 41.7, 48.6, 50.4, 30.0, 59.2, 38.4, 56.5, 51.1, 56.2, 62.5, 58.1, 44.9, 33.9, 32.8, 47.3, 44.9, 57.9, 56.4, 55.6, 58.7, 45.5, 46.5, 41.0, 40.0, 36.5, 49.8, 63.0, 51.3, 65.3, 39.1, 48.2, 38.9, 54.9, 61.5, 60.7, 52.2, 45.1, 30.3, 44.4, 36.8, 67.9, 47.2, 68.2]
state_incomes = [46257,76440,53558,44334,67739,65685,73433,61757,50860,53559,74511,51807,60960,52314,56247,54935,46659,45146,53079,78945,75297,52492,65599,41754,51746,50027,56927,55180,70936,76126,46748,62909,50584,60656,52334,49176,57532,56907,60596,49501,54467,48547,56565,65977,57677,68114,67106,43385,56811,59882]
state_deaths = [0] * 50
state_injured = [0] * 50
state_incidents = [0] * 50
state_registered = [0] * 50 

# Read data from file 'data.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
def ingest():
    data = pd.read_csv('data.csv')
    data.drop(['incident_id', 'city_or_county', 'address', 'incident_url', 'source_url', 'incident_url_fields_missing', 'congressional_district', 'gun_stolen', 'gun_type', 'incident_characteristics', 'latitude', 'location_description', 'longitude', 'n_guns_involved', 'notes', 'participant_age', 'participant_age_group', 'participant_gender', 'participant_name', 'participant_relationship', 'participant_status', 'participant_type', 'sources', 'state_house_district', 'state_senate_district'], axis=1, inplace=True)
    print('dataset loaded with shape', data.shape)
    print(data)
    return data


def ingestFirearms():
    data = pd.read_csv('firearms.csv')
    print('dataset loaded with shape', data.shape)
    print(data)
    return data


data = ingest()
total_injured = 0 
total_deaths = 0
total_incidents = 0


def preprocess(data):
    for row in data.itertuples():
        global total_injured
        total_injured += row.n_injured
        global total_deaths
        total_deaths += row.n_killed
        global total_incidents
        total_incidents += 1
        for i in range(50):
            if states[i] == row.state:
                state_deaths[i] += row.n_killed
                state_injured[i] += row.n_injured
                state_incidents[i] += 1


def processFirearms(data):
    for row in data.itertuples():
        for i in range(50):
            if states[i] == row.state:
                print(row)
                state_registered[i] += row.total

preprocess(data)
print("Total Injured: ", total_injured)
print("Total Killed: ", total_deaths)
print(state_deaths)
print(state_injured)
print(state_incidents)
print(total_incidents)
print(sum(state_incidents))

firearms = ingestFirearms()
processFirearms(firearms)
print(state_registered)


myFile = open('processed.csv', 'w')
with myFile:
   writer = csv.writer(myFile)
   writer.writerow(['state', 'code', 'injured', 'killed', 'incidents', 'death_rate', 'n_registered', 'registration_rate', 'background_checks', 'background_rate', 'trump', 'income'])
   for i in range(50):
       death_rate = ( state_deaths[i] / state_populations[i] ) * 100000
       registration_rate = ( state_registered[i] / state_populations[i] ) * 100000
       background_rate = ( state_backgrounds[i] / state_populations[i] ) * 100000
       row = [states[i], state_codes[i], state_injured[i], state_deaths[i], state_incidents[i], death_rate, state_registered[i], registration_rate, state_backgrounds[i], background_rate, state_votes[i], state_incomes[i]]
       print(row)
       writer.writerow(row)
