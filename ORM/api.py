from flask import Flask, jsonify, request
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy import insert, select, func, join
from sqlalchemy.orm import sessionmaker
import MySQLdb
import json

app = Flask(__name__)

# Q1. Users should be able to create programs, add semesters in programs, add courses in each semester, add sections,
#     add students in semester programs, and add instructors in programs.

# 1. Create Program (Insert new record in program table)
@app.route('/create/program', methods=['POST'])
def create_program():
    body = request.get_json()

    #create an engine that connects to the ORM database
    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')

    #make connection to the database using connect()
    connection = engine.connect()

    #create a MetaData object: metadata
    metadata = MetaData(bind=engine)

    #reflect MetaData object
    MetaData.reflect(metadata)

    #Reflect program table from the engine
    program = Table('program', metadata, autoload=True, autoload_with=engine)

    #build an insert statement without any values
    stmt = insert(program)

    try:
        connection.execute(stmt, body)

        return jsonify({
            'status': 200,
            'message': 'Program has been successfully created',
            'data': {
                'number_of_programs_inserted': len(body),
                'records_inserted': body
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Program not created!",
            'data': {}
        })


# 2. Insert semester in program

@app.route('/insert/semester', methods=['POST'])
def insert_semester():
    body = request.get_json()

    #create an engine that connects to the ORM database
    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')

    #make connection to the database using connect()
    connection = engine.connect()

    #create a MetaData object: metadata
    metadata = MetaData(bind=engine)

    #reflect MetaData object
    MetaData.reflect(metadata)

    #Reflect program table from the engine
    semester = Table('semester', metadata, autoload=True, autoload_with=engine)

    #build an insert statement without any values
    stmt = insert(semester)

    try:
        results = connection.execute(stmt, body)
        print(results)

        return jsonify({
            'status': 200,
            'message': 'Semester has been successfully inserted',
            'data': {
                'number_of_rows_inserted': results.rowcount,
                'records_inserted': body
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Semester couldn't be inserted!",
            'data': {}
        })


# 2. Insert department in program

@app.route('/insert/department', methods=['POST'])
def insert_department():
    body = request.get_json()


    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    department = Table('department', metadata, autoload=True, autoload_with=engine)

    stmt = insert(department)

    try:
        results = connection.execute(stmt, body)
        print(results)

        return jsonify({
            'status': 200,
            'message': 'Department has been successfully inserted',
            'data': {
                'number_of_rows_inserted': results.rowcount,
                'records_inserted': body
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Department couldn't be inserted!",
            'data': {}
        })

# 4. Insert courses in each semester

@app.route('/insert/course', methods=['POST'])
def insert_course():
    body = request.get_json()

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    course = Table('course', metadata, autoload=True, autoload_with=engine)

    stmt = insert(course)

    try:
        results = connection.execute(stmt, body)
        print(results)

        return jsonify({
            'status': 200,
            'message': 'Course has been successfully inserted',
            'data': {
                'number_of_rows_inserted': results.rowcount,
                'records_inserted': body
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Course couldn't be inserted!",
            'data': {}
        })

# 5. Insert sections in each semester

@app.route('/insert/section', methods=['POST'])
def insert_section():
    body = request.get_json()

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    section = Table('section', metadata, autoload=True, autoload_with=engine)

    stmt = insert(section)

    try:
        results = connection.execute(stmt, body)
        print(results)

        return jsonify({
            'status': 200,
            'message': 'Section has been successfully inserted',
            'data': {
                'number_of_rows_inserted': results.rowcount,
                'records_inserted': body
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Section couldn't be inserted!",
            'data': {}
        })


# 6. Insert students in each section

@app.route('/insert/student', methods=['POST'])
def insert_student():
    body = request.get_json()

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    student = Table('student', metadata, autoload=True, autoload_with=engine)

    stmt = insert(student)

    try:
        results = connection.execute(stmt, body)
        print(results)

        return jsonify({
            'status': 200,
            'message': 'Student record has been successfully inserted',
            'data': {
                'number_of_rows_inserted': results.rowcount,
                'records_inserted': body
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Failed to insert student record!",
            'data': {}
        })


# 7. Insert instructors in each department
# Each program has many departments and each department has several instructors

@app.route('/insert/instructor', methods=['POST'])
def insert_instructor():
    body = request.get_json()

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    instructor = Table('instructor', metadata, autoload=True, autoload_with=engine)

    stmt = insert(instructor)

    try:
        results = connection.execute(stmt, body)
        print(results)

        return jsonify({
            'status': 200,
            'message': 'Successfully inserted Instructor record',
            'data': {
                'number_of_rows_inserted': results.rowcount,
                'records_inserted': body
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Failed to insert Instructor record!",
            'data': {}
        })

#-------------------------------------------------------------------------------------------------------------------------------------

# Q2. Users should be able to view the total students and  instructor list, Number of students in [each semester,
#     each program, each section.]

# 8. Get a list of total students
@app.route('/get/students', methods=['GET', 'POST'])
def get_students():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    student = Table('student', metadata, autoload=True, autoload_with=engine)

    # build a select statement
    stmt = select([student])
    student_list = []                   #empty list to append dictionaries containing student details

    try:
        results = connection.execute(stmt).fetchall()

        for result in results:
            dict_student = dict()
            dict_student['student_id'] = result.student_id
            dict_student['student_name'] = result.student_name
            dict_student['student_gender'] = result.student_gender
            dict_student['student_dob'] = result.student_dob
            dict_student['permanent_address'] = result.permanent_address
            dict_student['current_address'] = result.current_address
            dict_student['student_contact_no'] = result.student_contact_no
            dict_student['sec_num'] = result.sec_num

            student_list.append(dict_student)
        return student_list

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Failed to retrieve student list"})


# 8. Get a list of total instructors

@app.route('/get/instructors', methods=['GET'])
def get_instructors():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    instructor = Table('instructor', metadata, autoload=True, autoload_with=engine)

    # build a select statement
    stmt = select([instructor])
    instructor_list = []                   #empty list to append dictionaries containing instructor details

    try:
        results = connection.execute(stmt).fetchall()

        for result in results:
            dict_instructor = dict()
            dict_instructor['Instructor id'] = result.ins_id
            dict_instructor['Name'] = result.ins_name
            dict_instructor['Address'] = result.ins_address
            dict_instructor['Contact Number'] = result.ins_contact_no
            dict_instructor['Gender'] = result.ins_gender
            dict_instructor['Position'] = result.ins_post
            dict_instructor['Full Time?'] = result.is_full_time
            dict_instructor['Department'] = result.dept_id

            instructor_list.append(dict_instructor)
        return instructor_list

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Failed to retrieve Instructor list"})

# 9. Get the number of students in each section

@app.route('/section/count-student', methods=['GET'])
def section_count_student():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    section = Table('section', metadata, autolaod=True, autoload_with=engine)
    student = Table('student', metadata, autoload=True, autoload_with=engine)

    stmt = select([section.columns.sec_num, func.count(student.columns.student_id).label('Number_of_Students')])
    stmt = stmt.select_from((section.join(student, section.columns.sec_num == student.columns.sec_num)))

    stmt = stmt.group_by(section.columns.sec_num)

    results = connection.execute(stmt).fetchall()
    results_list = []
    for result in results:
        count_dict = dict()
        count_dict['Section'] = result.sec_num
        count_dict['Number of Students'] = result.Number_of_Students
        results_list.append(count_dict)

    return jsonify({
        'status': 200,
        'message': 'Successfully retrieved the number of students in each section',
        'data': {
            'number_of_rows_returned': len(results),
            'records': results_list
        }
    })



# 10. Get the number of students in each semester

@app.route('/semester/count-student', methods=['GET'])
def sem_count_student():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    semester = Table('semester', metadata, autoload=True, autoload_with=engine)
    section = Table('section', metadata, autolaod=True, autoload_with=engine)
    student = Table('student', metadata, autoload=True, autoload_with=engine)

    stmt = select([semester.columns.sem_id, semester.columns.sem_number, func.count(student.columns.student_id).label('Number_of_Students')])
    stmt = stmt.select_from((semester
                             .join(section, semester.columns.sem_id == section.columns.sem_id)) \
                            .join(student, section.columns.sec_num == student.columns.sec_num))
    stmt = stmt.group_by(semester.columns.sem_id,
                         semester.columns.sem_number)

    results = connection.execute(stmt).fetchall()
    results_list = []
    for result in results:
        count_dict = dict()
        count_dict['Semester ID'] = result.sem_id
        count_dict['Semester No.'] = result.sem_number
        count_dict['Number of Students'] = result.Number_of_Students
        results_list.append(count_dict)

    return jsonify({
        'status': 200,
        'message': 'Successfully retrieved the number of students in each semester',
        'data': {
            'number_of_rows_returned': len(results),
            'records': results_list
        }
    })

# 11. Get the number of students in each program

@app.route('/program/count-student', methods=['GET'])
def program_count_student():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    program = Table('program', metadata, autoload=True, autoload_with=engine)
    semester = Table('semester', metadata, autoload=True, autoload_with=engine)
    section = Table('section', metadata, autolaod=True, autoload_with=engine)
    student = Table('student', metadata, autoload=True, autoload_with=engine)

    stmt = select([program.columns.program_id, program.columns.program_abbreviation, program.columns.program_name,
                   func.count(student.columns.student_id).label('Number_of_Students')])
    stmt = stmt.select_from((program.join(semester, program.columns.program_id == semester.columns.program_id))\
                             .join(section, semester.columns.sem_id == section.columns.sem_id))\
                            .join(student, section.columns.sec_num == student.columns.sec_num)
    stmt = stmt.group_by(program.columns.program_id,
                         program.columns.program_abbreviation,
                         program.columns.program_name)

    results = connection.execute(stmt).fetchall()
    results_list = []
    for result in results:
        count_dict = dict()
        count_dict['Program ID'] = result.program_id
        count_dict['Program(abbreviation)'] = result.program_abbreviation
        count_dict['Full Name'] = result.program_name
        count_dict['Number of Students'] = result.Number_of_Students
        results_list.append(count_dict)

    return jsonify({
        'status': 200,
        'message': 'Successfully retrieved the number of students in each program',
        'data': {
            'number_of_rows_returned': len(results),
            'records': results_list
        }
    })


#-------------------------------------------------------------------------------------------------------------------------------------

# Q3. Users should be able to view courses that are taught each semester and show sections of each semester,
#     show instructors of each semester.

# # 12. List of courses in each semester
@app.route('/semester/course-list', methods=['GET', 'POST'])
def semester_course_list():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    semester = Table('semester', metadata, autoload=True, autoload_with=engine)
    course = Table('course', metadata, autoload=True, autoload_with=engine)

    # build a select statement
    stmt = select([semester.columns.sem_id, semester.columns.sem_number, course])
    stmt = stmt.select_from(semester.join(course, semester.columns.sem_id == course.columns.sem_id))

    try:
        results = connection.execute(stmt).fetchall()
        result_list = []

        for result in results:
            dict_course = dict()
            dict_course['Course Code'] = result.course_code
            dict_course['Title'] = result.course_title
            dict_course['Credit Hours'] = result.credit_hours
            dict_course['Description'] = result.course_descript
            dict_course['Full Marks'] = result.full_marks
            dict_course['Theory Marks'] = result.theory_marks
            dict_course['Practical Marks'] = result.practical_marks
            dict_course['Semester'] = result.sem_id
            dict_course['Department'] = result.dept_id

            semester_exists = False  # if semester doesn't already exist in the list
            for item in result_list:  # check if that semester record is already in response list (if so we need to append, course to course list)
                if item['Semester Details']['Semester ID'] == result.sem_id:
                    course_list = item['course_list']
                    # append the new dict to course list
                    course_list.append(dict_course)
                    item['course_list'] = course_list
                    item['Number of courses'] += 1
                    semester_exists = True
                    break

            if semester_exists:
                continue
            else:
                # the semester record is not already in response list, so add it to the list
                course_list = []
                course_list.append(dict_course)

                dict_semester = dict()
                dict_semester['Semester ID'] = result.sem_id
                dict_semester['Semester Number'] = result.sem_number

                result_list.append({
                    'Semester Details': dict_semester,
                    'Number of Courses': 1,
                    'Course List': course_list
                })

        return jsonify({
            'Status': 200,
            'Message': "Course list of all semesters successfully retrieved",
            'Data':{
                'Number of Rows Returned': len(results),
                'Records': result_list
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Failed to retrieve course list"})


# 13. List of sections of each semester
@app.route('/semester/section-list', methods=['GET', 'POST'])
def semester_section_list():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    semester = Table('semester', metadata, autoload=True, autoload_with=engine)
    section = Table('section', metadata, autoload=True, autoload_with=engine)

    # build a select statement
    stmt = select([semester.columns.sem_id, semester.columns.sem_number, section])
    stmt = stmt.select_from(semester.join(section, semester.columns.sem_id == section.columns.sem_id))
    stmt = stmt.group_by(semester.columns.sem_id, semester.columns.sem_number)

    try:
        results = connection.execute(stmt).fetchall()
        result_list = []

        for result in results:
            dict_section = dict()
            dict_section['Section Number'] = result.sec_num
            dict_section['Building'] = result.building
            dict_section['Classroom Number'] = result.classroom
            dict_section['Semester'] = result.sem_id

            semester_exists = False  # if semester doesn't already exist in the list
            for item in result_list:  # check if that semester record is already in response list (if so we need to append, course to course list)
                if item['Semester Details']['Semester ID'] == result.sem_id:
                    section_list = item['section_list']
                    # append the new dict to course list
                    section_list.append(dict_section)
                    item['section_list'] = section_list
                    item['Number of Sections'] += 1
                    semester_exists = True
                    break

            if semester_exists:
                continue
            else:
                # the semester record is not already in response list, so add it to the list
                section_list = []
                section_list.append(dict_section)

                dict_semester = dict()
                dict_semester['Semester ID'] = result.sem_id
                dict_semester['Semester Number'] = result.sem_number

                result_list.append({
                    'Semester Details': dict_semester,
                    'Number of Sections': 1,
                    'Section List': section_list
                })

        return jsonify({
            'status': 200,
            'message': "Section list of all semesters successfully retrieved",
            'data':{
                'Number of Rows Returned': len(results),
                'Records': result_list
            }
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Failed to retrieve section list"})


# 14. List of instructors of each semester
@app.route('/semester/instructor-list', methods=['GET', 'POST'])
def semester_instructor_list():

    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    program = Table('program', metadata, autoload=True, autoload_with=engine)
    department = Table('department', metadata, autoload=True, autoload_with=engine)
    semester = Table('semester', metadata, autoload=True, autoload_with=engine)
    instructor = Table('instructor', metadata, autoload=True, autoload_with=engine)

    # build a select statement
    stmt = select([semester.columns.sem_id, semester.columns.sem_number, instructor])
    stmt = stmt.select_from(((program
                              .join(semester, program.columns.program_id == semester.columns.program_id)
                              .join(department, program.columns.program_id == department.columns.program_id))
                             .join(instructor, department.columns.dept_id == instructor.columns.dept_id)))

    # try:
    results = connection.execute(stmt).fetchall()
    result_list = []

    for result in results:
        dict_instructor = dict()
        dict_instructor['Instructor ID'] = result.ins_id
        dict_instructor['Name'] = result.ins_name
        dict_instructor['Address'] = result.ins_address
        dict_instructor['Contact Number'] = result.ins_contact_no
        dict_instructor['Gender'] = result.ins_gender
        dict_instructor['Position'] = result.ins_post
        dict_instructor['Full Time?'] = result.is_full_time
        dict_instructor['Department'] = result.dept_id

        semester_exists = False  # if semester doesn't already exist in the list
        for item in result_list:  # check if that semester record is already in response list (if so we need to append, course to course list)
            if item['Semester Details']['Semester ID'] == result.sem_id:
                instructor_list = item['Instructor List']
                # append the new dictionary to instructor list
                instructor_list.append(dict_instructor)
                item['Instructor List'] = instructor_list
                item['Number of Instructors'] += 1
                semester_exists = True
                break

        if semester_exists:
            continue
        else:
            # if the record of the semester does not already exist in the result list,
            # then create a new list for instructor details
            # and add a new semester to represent it
            instructor_list = []
            instructor_list.append(dict_instructor)

            dict_semester = dict()
            dict_semester['Semester ID'] = result.sem_id
            dict_semester['Semester Number'] = result.sem_number

            result_list.append({
                'Semester Details': dict_semester,
                'Number of Instructors': 1,
                'Instructor List': instructor_list
            })

    return jsonify({
        'status': 200,
        'message': "Instructor list of all semesters successfully retrieved",
        'data':{
            'Number of Rows Returned': len(results),
            'Records': result_list
        }
    })

    # except Exception as e:
    #     return jsonify({
    #         'status': 400,
    #         'message': "Failed to retrieve instructor list"})



if __name__ == '__main__':
  app.run(debug=True)