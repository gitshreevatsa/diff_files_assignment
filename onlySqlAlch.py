from flask import jsonify
from app import db, meta, company_table


def create(body):
  company_ID=int(body['company_ID'])
  Company_Name=str(body['company_Name'])
  Sector=str(body['Sector'])
  website = str(body['Website'])
  email = str(body['Email'])
  result = db.engine.execute(company_table.insert(),[{'company_ID': company_ID, 'company_Name' : Company_Name, 'Sector' : Sector,
                                          'Website' : website, 'Email' : email}])
  return "added successfully"

def read():
    dataview = company_table.select()
    result = db.engine.execute(dataview)
    row_list = [] 
    for row in result.fetchall():
        row_list.append(dict(row))
    return jsonify(row_list)


def update(body):
    dict_input = dict(body)
    match = dict_input['company_ID']
    for key, value in dict_input.items():
        updated = company_table.update().where(company_table.c.company_ID==match).values({key:value})
        result = db.engine.execute(updated)

def delete(body):
    option = body['company_ID']
    deleted = company_table.delete().where(company_table.c.company_ID == option)
    result = db.engine.execute(deleted)
    





"""
{
    "company_ID" : 1,
    "company_Name" : "Sony",
    "Sector" : "Private",
    "Website" : "sony.com",
    "Email" : "sony@gmail.com"
}

{
    "company_ID" : 2,
    "company_Name" : "Dell",
    "Sector" : "Private",
    "Website" : "Dell.com",
    "Email" : "Dell@gmail.com"
}

{
    "company_ID" : 3,
    "company_Name" : "ONGC",
    "Sector" : "Government",
    "Website" : "ONGC.in",
    "Email" : "ONGC@gmail.com"
}

{
    "company_ID" : 4,
    "company_Name" : "Pyse",
    "Sector" : "Private",
    "Website" : "pyse.in",
    "Email" : "pyse.co.in"
}

"""