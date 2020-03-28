/**
Setup Main MySQL database
*/

CREATE DATABASE amizone;

CREATE TABLE amizone.homepage_tt (
    `#` INT auto_increment NOT NULL, 
    `date` DATE, 
    class_time varchar(255), 
    course_code varchar(255),
    course_name varchar(255),
    teacher varchar(255),
    class_loc varchar(255),
    attendance_status varchar(255),
    KEY(`#`), 
    PRIMARY KEY(`date`(50),class_time(50), course_code(50), course_name(50), teacher(50),class_loc(50)));

