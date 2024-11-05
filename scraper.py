import requests

def get_courses():
    params = {
        "institution": "UVA01",
        "term": "1248",  
        "subject": "CS",
        "page": "1"
    }

    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1'


    response = requests.get(url, params=params)
    courses = response.json()

    # Print each course in a readable format
    for course in courses:
        print(f"\nCourse: {course['subject']} {course['catalog_nbr']}-{course['class_section']}")
        print(f"Title: {course['descr']}")
        print(f"Instructor: {course.get('instructors', 'TBA')}")
        print(f"Enrollment: {course['enrollment_available']}/{course['class_capacity']}")
        print(f"Schedule: {course.get('schedule')}")
        print("-" * 50)
    
if __name__ == "__main__":
    get_courses()