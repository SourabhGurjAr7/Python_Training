
import yaml
person_data={
    "Name":"Mike",
    "E-mail": "mikehomie34@gmail.com",
    "DOB":18-4-1998,
    "Age":24,
    "Education":{
        "School":{
            "NYC High School,US":{
                "Grade":"A+"
            }
        },
        "College":{
            "Sanford College New York":{
                "Grade":"B"
            }
        }
    },
    "Address":{
        "Street":"A-21 Benjamin Street",
        "City":"New York",
        "Country":"United States of America",
        "Zip Code":"23754",

    },
    "Languages":["Python","C","C++","Scala","Java"],
    "Sex": "Male",
    "Hobbies": ["Playing Volley Ball","Basket Ball","Dancing","Travelling"],
    "Current Device":{
        "Mobile":{
            "Apple":{
                "I-Phone 14":"256 GB"
            }
        },
        "Laptop":{
            "HP":{
                "HP-Spectre x360 16 (2022)":"16 GB DDR4-3200 MHz RAM"

            }
        }
    }
}
with open("Demo.yml",'w') as f:
    yaml.dump(person_data,f,default_flow_style=False)

'''
import yaml
with open("Demo.yml","r") as f:
    data=yaml.safe_load(f)
print(data)
'''