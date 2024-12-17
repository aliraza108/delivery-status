import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import offline as po

file = pd.read_excel("file.xlsx")
Status = file['Status']



# Pie Chart Gettin Total Returns 
# Count Return
return_total = 0
for i in Status:
    if(i=="Returned to shipper"):
        return_total=return_total+1



# Count Delivered
Delivered_total = 0
for i in Status:
    if(i=="Delivered"):
        Delivered_total=Delivered_total+1

# Count Pending
pending_Status = 0
for i in Status:
    if(i=="Pending"):
        pending_Status=pending_Status+1


# Count Pickup
pickupRQ_Status = 0
for i in Status:
    if(i=="Pickup Request Sent"):
        pickupRQ_Status=pickupRQ_Status+1


# Count Cancelled
Cancelled_Status = 0
for i in Status:
    if(i=="Cancelled"):
        Cancelled_Status=Cancelled_Status+1

# Count Pickup Request not Send
NotPickUpRQ_Status = 0
for i in Status:
    if(i=="Pickup Request not Send"):
        NotPickUpRQ_Status=NotPickUpRQ_Status+1

# Count Being Return
BeingRT_Status = 0
for i in Status:
    if(i=="Being Return"):
        BeingRT_Status=BeingRT_Status+1


total = [Delivered_total,return_total,pending_Status,pickupRQ_Status,Cancelled_Status,NotPickUpRQ_Status,BeingRT_Status]
label_x = ["Delivered", "Return","Pending","Pickup Request Send", "Cencelled","Pick Request not send", "Being Return"]


pt = px.pie(values=total,names=label_x,title='Leopards Delivery Report AUG - SEP 2024 ',color=label_x,labels=label_x)



po.plot(pt,"file.html")