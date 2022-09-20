from sqlalchemy import create_engine, MetaData, insert, inspect
from sqlalchemy import Table, Column, Integer, String, Float, Boolean, Date
from sqlalchemy import ForeignKey, UniqueConstraint
import MySQLdb


def create_schema(engine):
    # create metadata object and connect it to the engine
    metadata = MetaData(bind=engine)
    MetaData.reflect(metadata)

    program = Table('program', metadata,
                    Column('program_id', Integer, primary_key=True),
                    Column('program_abbreviation', String(30), nullable=False),
                    Column('program_name', String(255), nullable=False),
                    Column('program_degree', String(10), nullable=False)
                    )

    semester = Table('semester', metadata,
                     Column('sem_id', Integer, primary_key=True, autoincrement=True),
                     Column('sem_number', Integer, nullable=False),
                     Column('program_id', Integer,
                            ForeignKey('program.program_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
                     )
    department = Table('department', metadata,
                       Column('dept_id', String(10), primary_key=True),
                       Column('dept_name', String(100), nullable=False),
                       Column('program_id', Integer, ForeignKey('program.program_id', onupdate="CASCADE",
                                                                ondelete="CASCADE"), nullable = False)
                       )

    course = Table('course', metadata,
                   Column('course_code', String(10), primary_key=True),
                   Column('course_title', String(255), nullable=False),
                   Column('credit_hours', Integer, nullable=False),
                   Column('course_descript', String(255), nullable=True),
                   Column('full_marks', Integer, nullable = False),
                   Column('theory_marks', Integer, nullable=False, default=0),
                   Column('practical_marks', Integer, nullable=False, default=0),
                   Column('sem_id', Integer,
                            ForeignKey('semester.sem_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False),
                   Column('dept_id', String(10), ForeignKey('department.dept_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
                   )


    instructor = Table('instructor', metadata,
                       Column('ins_id', Integer, primary_key=True, autoincrement=True),
                       Column('ins_name', String(100), nullable=False),
                       Column('ins_address', String(255), nullable=False),
                       Column('ins_contact_no', String(15), nullable=False),
                       Column('ins_gender', String(1), nullable=True),
                       Column('ins_post', String(100), nullable=False),
                       Column('is_full_time', Boolean, default = True),
                       Column('dept_id', String(10), ForeignKey('department.dept_id', onupdate="CASCADE"),
                              nullable=True)
                       )

    instructor_course = Table('instructor_course', metadata,
                              Column('ins_id', Integer,
                                     ForeignKey('instructor.ins_id', onupdate="CASCADE", ondelete="CASCADE"),
                                     primary_key=True),
                              Column('course_code', String(10),
                                     ForeignKey('course.course_code', onupdate="CASCADE", ondelete="CASCADE"),
                                     primary_key=True)
                              )

    section = Table('section', metadata,
                    Column('sec_num', String(10), primary_key=True),
                    Column('building', String(10), nullable=True),
                    Column('classroom', Integer, nullable=True),
                    Column('sem_id', Integer,
                           ForeignKey('semester.sem_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
                    )

    student = Table('student', metadata,
                    Column('student_id', Integer, primary_key=True, autoincrement=True),
                    Column('student_name', String(100), nullable=False),
                    Column('student_gender', String(1), nullable=True),
                    Column('student_dob', Date, nullable=False),
                    Column('permanent_address', String(255), nullable=False),
                    Column('current_address', String(255), nullable=False),
                    Column('student_contact_no', String(15), nullable=False),
                    Column('sec_num', String(10), ForeignKey('section.sec_num', onupdate="CASCADE"), nullable=True)
                    )

#create all of the above tables in the metadata
    metadata.create_all(engine)


def insert_data(engine):
    # make connection to the engine using connect() method
    connection = engine.connect()

    # create a MetaData object: metadata
    metadata = MetaData(bind=engine)

    #reflect the MetaData
    MetaData.reflect(metadata)

    #Reflect tables from the engine using SQLalchemy Table object
    program = Table('program', metadata, autoload=True, autoload_with=engine)
    semester = Table('semester', metadata, autoload=True, autoload_with=engine)
    department = Table('department', metadata,autoload=True, autoload_with=engine)
    course = Table('course', metadata, autoload=True, autoload_with=engine)
    instructor = Table('instructor', metadata, autoload=True, autoload_with=engine)
    instructor_course = Table('instructor_course', metadata, autolaod=True, autoload_with=engine)
    section = Table('section', metadata, audoload=True, autoload_with=engine)
    student = Table('student', metadata, autoload=True, autoload_with=engine)

    #Building list of dictionaries for each table representing column:value pairs for each record to be inserted
    #these lists will be passed to the connection.execute() method alongside insert() statement
    program_list = [
        {'program_id': '101', 'program_name': 'Bachelors of Science in Agriculture', 'program_abbreviation': 'Bsc Ag', 'program_degree': 'Bachelors'},
        {'program_id': '103', 'program_name': 'Bachelors of Science in Aquaculture and Fisheries', 'program_abbreviation': 'BSc Fisheries','program_degree': 'Bachelors'},
        {'program_id': '104', 'program_name': 'Bachelors of Veterinary Sciences','program_abbreviation': 'BVSc', 'program_degree': 'Bachelors'},
        {'program_id': '201', 'program_name': 'Masters of Science in Horticulture', 'program_abbreviation': 'MSc Horticulture', 'program_degree': 'Masters'},
        {'program_id': '202', 'program_name': 'Masters of Science in Agricultural Economics', 'program_abbreviation': 'MSc AgriEconomics', 'program_degree': 'Masters'}
    ]

    semester_list = [
        {'sem_id': 10101, 'sem_number': 1, 'program_id': 101},
        {'sem_id': 10103, 'sem_number': 3, 'program_id': 101},
        {'sem_id': 10301, 'sem_number': 1, 'program_id': 103},
        {'sem_id': 10401, 'sem_number': 1, 'program_id': 104},
        {'sem_id': 20101, 'sem_number': 1, 'program_id': 201},
        {'sem_id': 20201, 'sem_number': 1, 'program_id': 202}

    ]

    department_list = [
        {'dept_id':'PLB', 'dept_name':'Department of Genetics and Plant Breeding', 'program_id':101},
        {'dept_id':'MIB', 'dept_name':'Department of Microbiology', 'program_id':101},
        {'dept_id': 'AQU', 'dept_name': 'Department of Aquaculture', 'program_id':103},
        {'dept_id': 'VMC', 'dept_name': 'Department of Veterinary Medicine', 'program_id':104},
        {'dept_id': 'HRT', 'dept_name': 'Department of Horticulture', 'program_id':201},
        {'dept_id': 'ECO', 'dept_name': 'Department of Economics', 'program_id':202}
    ]

    course_list = [
        {'course_code': 'PLB 101', 'course_title': 'Introductory Genetics', 'credit_hours': 3, 'course_descript': 'fundamentals of genetics of plants',
         'dept_id': 'PLB', 'full_marks':75, 'theory_marks':50, 'practical_marks':25, 'sem_id':10101},
        {'course_code': 'MIB 202', 'course_title': 'Agricultural Microbiology', 'credit_hours': 2, 'course_descript': 'science of microbiology in plants',
         'dept_id': 'MIB', 'full_marks':50, 'theory_marks':50, 'practical_marks':0, 'sem_id':10103},
        {'course_code': 'AQU 201', 'course_title': 'Principles of Aquaculture', 'credit_hours': 3, 'course_descript': 'basic principles of aquaculutre and fisheries',
         'dept_id': 'AQU', 'full_marks':75, 'theory_marks':50, 'practical_marks':25, 'sem_id':10301},
        {'course_code': 'VMC 101', 'course_title': 'Animal Health', 'credit_hours': 3, 'course_descript': 'fundamentals of animal diseases and their control',
         'dept_id': 'VMC', 'full_marks':75, 'theory_marks':50, 'practical_marks':25, 'sem_id':10401},
        {'course_code': 'HRT 501', 'course_title': 'Pomology', 'credit_hours': 5, 'course_descript': 'scientific study of fruits',
         'dept_id': 'HRT', 'full_marks':100, 'theory_marks':75, 'practical_marks':25, 'sem_id':20101},
        {'course_code': 'ECO 501', 'course_title': 'Agribusiness Management', 'credit_hours': 4, 'course_descript': 'strategies for management of agricultural businesses',
         'dept_id': 'ECO', 'full_marks':80, 'theory_marks':60, 'practical_marks':20, 'sem_id':20201}
    ]

    instructor_list = [
        {'ins_id': 1, 'ins_name': 'Hira Kaji Manandhar', 'ins_address': 'Rampur, Chitwan', 'ins_contact_no': '+9779855045678',
         'ins_gender': 'M', 'dept_id': 'PLB', 'ins_post': 'Professor', 'is_full_time':True},
        {'ins_id': 2, 'ins_name': 'Sundar Man Shrestha', 'ins_address': 'Bharatpur-2, Chitwan', 'ins_contact_no': '+9779855034890',
         'ins_gender': 'M', 'dept_id': 'MIB', 'ins_post': 'Professor', 'is_full_time': True},
        {'ins_id': 3, 'ins_name': 'Roshani Pandey', 'ins_address': 'Bharatpur-5, Chitwan', 'ins_contact_no': '+9779861289678',
         'ins_gender': 'F', 'dept_id': 'AQU', 'ins_post': 'Associate Professor', 'is_full_time':True},
        {'ins_id': 4, 'ins_name': 'Rabin Raut', 'ins_address': 'Sharadpur-1, Chitwan', 'ins_contact_no': '+9779845523901',
         'ins_gender': 'M', 'dept_id': 'VMC', 'ins_post': 'Assistant Professor', 'is_full_time':False},
        {'ins_id': 5, 'ins_name': 'Ananta Raj Devkota', 'ins_address': 'Rampur, Chitwan', 'ins_contact_no': '+9779855034890',
         'ins_gender': 'M', 'dept_id': 'HRT', 'ins_post': 'Assistant Professor', 'is_full_time': True},
        {'ins_id': 6, 'ins_name': 'Sramika Rijal', 'ins_address': 'Bharatpur-11, Chitwan', 'ins_contact_no': '+9779855036677',
         'ins_gender': 'F', 'dept_id': 'ECO', 'ins_post': 'Professor', 'is_full_time': True}
        ]

    instructor_course_list = [
        {'ins_id': 1, 'course_code': 'PLB 101'},
        {'ins_id': 2, 'course_code': 'MIB 202'},
        {'ins_id': 3, 'course_code': 'AQU 201'},
        {'ins_id': 4, 'course_code': 'VMC 101'},
        {'ins_id': 5, 'course_code': 'HRT 501'},
        {'ins_id': 6, 'course_code': 'ECO 501'}
    ]

    section_list = [
        {'sec_num': '10101A', 'building': 'UG A', 'classroom': 102, 'sem_id': 10101},
        {'sec_num': '10103B', 'building': 'UG A', 'classroom': 106, 'sem_id': 10103},
        {'sec_num': '10301A', 'building': 'UG B', 'classroom': 205, 'sem_id': 10301},
        {'sec_num': '10401A', 'building': 'UG C', 'classroom': 307, 'sem_id': 10401},
        {'sec_num': '20101A', 'building': 'PG A', 'classroom': 201, 'sem_id': 20101}
    ]

    student_list = [
        {'student_id': 101, 'student_name': 'Pallavi Shrestha', 'student_gender':'F', 'student_dob': '1998-05-27',
         'permanent_address': 'Sundarbazar, Lamjung', 'current_address': 'Bharatpur, Chitwan',
         'student_contact_no':'+9779861280100', 'sec_num': '10101A'},
        {'student_id': 102, 'student_name': 'Kirti Poudel', 'student_gender':'F', 'student_dob': '1997-03-27',
         'permanent_address': 'Bharatpur, Chitwan', 'current_address': 'Rampur, Chitwan',
         'student_contact_no':'+9779845678939', 'sec_num': '10103B'},
        {'student_id': 103, 'student_name': 'Ramesh Gurung', 'student_gender':'M', 'student_dob': '1995-01-01',
         'permanent_address': 'Pokhara, Kaski', 'current_address': 'Bharatpur, Chitwan',
         'student_contact_no':'+9779860987654', 'sec_num': '10103B'},
        {'student_id': 104, 'student_name': 'Nishan Khatri', 'student_gender':'M', 'student_dob': '1999-12-12',
         'permanent_address': 'Tandi, Chitwan', 'current_address': 'Rampur, Chitwan',
         'student_contact_no':'+9779845098345', 'sec_num': '10101A'},
        {'student_id': 105, 'student_name': 'Nabina Karki', 'student_gender':'F', 'student_dob': '1998-03-15',
         'permanent_address': 'Baneshwor, Kathmandu', 'current_address': 'Rampur, Chitwan',
         'student_contact_no':'+9779805892213', 'sec_num': '10301A'}
    ]

#creating dictionary for all tables
    dict_tables = {
        program: program_list,
        semester: semester_list,
        department: department_list,
        course: course_list,
        instructor: instructor_list,
        instructor_course: instructor_course_list,
        section: section_list,
        student: student_list
    }

# execute all insert operations in a loop
    for (table, table_list) in dict_tables.items():
        connection.execute(insert(table), table_list)

#create loop
if __name__ == '__main__':
    # engine for connecting to database and performing operations
    # engine = create_engine('[DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]')
    engine = create_engine('mysql://root:pallu.SQL.123@localhost:3306/ORM')

    # inspector to inspect database elements
    inspector = inspect(engine)

    # create database schema
    create_schema(engine)

    # insert data into the database
    insert_data(engine)

