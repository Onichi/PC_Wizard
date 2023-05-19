from app import db, create_app
from app.models import CPU

app = create_app()
app.app_context().push()

def fill_db(info):
    info = info
    name = info[0]
    Core = info[1]
    Number_of_Cores = info[2]
    Number_of_threads = info[3]
    Process_technology = info[4]
    Connector = info[5]
    Frequency = info[6]
    multiplier = info[7]
    HTT_Bclk = info[8]
    Memory_type = info[9]
    L1_cache = info[10]
    L2_cache = info[11]
    L3_cache = info[12]
    Supply_voltage = info[13]
    TDP = info[14]
    Number_of_transistors = info[15]
    Crystal_area = info[16]
    Limit_temperature = info[17]
    Instruction = info[18]
    try:
        Other_Features = info[19]
    except: Other_Features = "?"
    try :
        Date_of_issue = info[20]
    except: Date_of_issue = "?"
    try:
        Cost = info[20]
    except: Cost = "?"

    insertion_query = CPU(name=name, Core=Core, Number_of_Cores=Number_of_Cores,
                          Number_of_threads=Number_of_threads,
                          Process_technology=Process_technology,
                          Connector=Connector, Frequency=Frequency, Multiplier=multiplier,
                          HTT_Bclk=HTT_Bclk,
                          Memory_type=Memory_type, L1_cache=L1_cache, L2_cache=L2_cache,
                          L3_cache=L3_cache,
                          Supply_voltage=Supply_voltage, TDP=TDP,
                          Number_of_transistors=Number_of_transistors,
                          Crystal_area=Crystal_area, Limit_temperature=Limit_temperature,
                          Instruction_set=Instruction,
                          Other_Features=Other_Features, Date_of_issue=Date_of_issue, Cost=Cost
                          )
    db.session.add(insertion_query)
    db.session.commit()