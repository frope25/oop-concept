"""
coding principle
DRY - DON'T REPEAT YOURSELF

Normal code 

        E-Learning Website

    Student:        Instructor:                    
    -Register       -Register
    -Login          -Login
    -Enroll         -Create Courses
    -Checkout       -Check Earnings

DRY Code:-

                User:                                      Father:
            -Register                                   -Black Hair
            -Login

    Student:        Instructor:                     You:                Brother/Sister:
    -Enroll         -Create Course                  -Black Hair         -Brown Hair
    -Checkout       -Check Earnings                 -Dark Skin Color    -White Skin Color

Biggest benefit of Inheritance
CODE REUSABILITY
Always goes in Bottom-UP approach


        Parent Class        - Data Member (Variable in Class)
            ^               - Member function/Class Method
        Child Class         - Class Constructors

    ** Private Members are not Inherited of Parent Class in Child Class
"""