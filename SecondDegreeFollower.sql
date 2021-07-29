/*
LeetCode 614. Second Degree Follower

In Facebook, there is a follow table with two columns: followee, follower.
Please write a sql query to get the amount of each follower’s follower if he/she has one.
*/
SELECT follower, follower_num as num
FROM
(SELECT follower, count(distinct followee) as followee_num FROM follow group by follower) a
LEFT JOIN
(SELECT followee, count(distinct follower) as follower_num FROM follow group by followee) b
ON a.follower = b.followee
WHERE followee is not null
