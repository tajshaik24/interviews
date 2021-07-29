/*
LeetCode 175. Combine Two Tables

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people: FirstName, LastName, City, State*/

SELECT pers.FirstName,
       pers.LastName,
       addr.City,
       addr.State
    FROM Person pers
    left join Address addr
    ON addr.PersonId = pers.PersonId
