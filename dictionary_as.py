"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student1 = {"student_name": 'Joey',
                "age": 20,
                "roll_no": 67,
                "section": 'E',
                "college_name": 'JB Science College'
           }
print(student1)

"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
student_info = {'Student_1': {'student_name': 'Amruta',
                             'age': 21,
                             'roll_no': 81,
                             'class': 'B.E. IIIrd Year',
                             'section': 'Electrical B',
                             'percentage': 79.77,
                             'university_name': 'Nagpur University'
                             },
                'Student_2': {'student_name': 'Rahul',
                             'age': '20',
                             'roll_no': 42,
                             'class': 'B.E. IInd Year',
                             'section': 'CS A',
                             'percentage': 81.04,
                             'university_name': 'Bhopal University'
                             },
                'Student_3': {'student_name': 'Simran',
                             'age': '19',
                             'roll_no': 33,
                             'class': 'B.E. IInd Year',
                             'section': 'Electronics A',
                             'percentage': 77.48,
                             'university_name': 'Mumbai University'
                             }
}
print(student_info)

"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employees = {'emp1': {'emp_name': 'Sakshi',
                      'salary/month': 25000,
                      'designation': 'Semiconductor Validation Engineer'
                     },
             'emp2': {'emp_name': 'Pranav',
                      'salary/month': 30000,
                      'designation': 'IT Engineer'
                     },
             'emp3': {'emp_name': 'Anupriya',
                      'salary/month': 35000,
                      'designation': 'Data Analyst'
                     },
             'emp4': {'emp_name': 'Tushar',
                      'salary/month': 40000,
                      'designation': 'Quality Assurance Engineer'
                     }
}
print(employees['emp3']['designation'])