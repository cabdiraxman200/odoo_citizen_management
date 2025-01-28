{
"name":"Hospital_Management",
"author":"Abdirahman Hassan",
"version":"17.0.1.1",
"category":"Hospital",
"summmary":"Hospital Management System",
"description":"""Hospital Management System""",
"sequence":-100,
"depends":['mail','product','account'],
"data":[
    "security/security.xml",
    "security/ir.model.access.csv",
    'data/patient_tag_data.xml',
    "wizard/cancel_appointment.xml",
    "views/patients_view.xml",
    "views/appointment_view.xml",
     'views/female_patient_view.xml',
     'views/patient_view_tag.xml',
      'views/account_move_view.xml',
      "views/menu.xml"
],
    "demo":[],
    "application":True,
    "auto-install":False,
    "license":"LGPL-3",

}
