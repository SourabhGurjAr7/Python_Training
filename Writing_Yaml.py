#Writing a yaml file
import yaml
person_data={
    "Name":"Mike Williams",
    "E-mail": "mikehomie34@gmail.com",
    "DOB":"18-4-1998",
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
        "Zip Code": 23754,

    },
    "Languages":["Python","C","C++","Scala","Java"],
    "Sex": "Male",
    "Hobbies": ["Playing Volley Ball","Basket Ball","Dancing","Travelling"],
    "Current Device":{
        "Mobile":{
            "Apple":{
                "I-Phone 14":['146.7 x 71.5 x 7.8' ,'256GB 6GB RAM','iOS 16']
            }
        },
        "Laptop":{
            "HP":{
                "HP-Spectre x360 16 (2022)":['13.30-inch','256GB 8GB RAM','Core i7']

            }
        }
    }
}
with open("Demo.yml", 'w') as f:
    yaml.dump(person_data,f,default_flow_style=False)

'''

#Reading Yaml file
import yaml

with open('Demo.yml','r') as file:
    data=yaml.safe_load(file)
print(data)

'''