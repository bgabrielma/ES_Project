create database coins;
use coins;
 create table coin(
 name varchar(100) not null ,
 acronyum varchar(20) not null,
 lowestValue int not null ,
 highestValue int not null,
 currentValue int not null,
 createdAt TIMESTAMP,
 updatedAt TIMESTAMP 
 );

 
 
