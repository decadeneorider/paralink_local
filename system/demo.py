from dateutil import  rrule
from datetime import datetime
from system.db.contract_db import Contractdb

contract_infor = Contractdb().display_contract_1()
end_date = contract_infor[0][10]
print(end_date)
start_date = datetime.now()
# end_date =datetime.now()
weeks = rrule.rrule(rrule.DAILY, dtstart=end_date, until=start_date)
print(weeks.count())