CREATE TABLE parents AS
SELECT
    "abraham" AS parent,
    "barack" AS child
UNION
SELECT
    "abraham",
    "clinton"
UNION
SELECT
    "delano",
    "herbert"
UNION
SELECT
    "fillmore",
    "abraham"
UNION
SELECT
    "fillmore",
    "delano"
UNION
SELECT
    "fillmore",
    "grover"
UNION
SELECT
    "eisenhower",
    "fillmore";

CREATE TABLE dogs AS
SELECT
    "abraham" AS name,
    "long" AS fur,
    26 AS height
UNION
SELECT
    "barack",
    "short",
    52
UNION
SELECT
    "clinton",
    "long",
    47
UNION
SELECT
    "delano",
    "long",
    46
UNION
SELECT
    "eisenhower",
    "short",
    35
UNION
SELECT
    "fillmore",
    "curly",
    32
UNION
SELECT
    "grover",
    "short",
    28
UNION
SELECT
    "herbert",
    "curly",
    31;

CREATE TABLE sizes AS
SELECT
    "toy" AS size,
    24 AS min,
    28 AS max
UNION
SELECT
    "mini",
    28,
    35
UNION
SELECT
    "medium",
    35,
    45
UNION
SELECT
    "standard",
    45,
    60;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
SELECT
    parents.child
from
    dogs as ch,
    dogs as pa,
    parents
where
    ch.name = parents.child
    AND pa.name = parents.parent
order by
    pa.height DESC;

-- The size of each dog
CREATE TABLE size_of_dogs AS
SELECT
    dogs.name AS name,
    sizes.size AS size
from
    dogs
    JOIN sizes ON dogs.height > sizes.min
    AND dogs.height <= sizes.max;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
SELECT
    older.child as sib1,
    younger.child as sib2
FROM
    parents as older
    JOIN parents as younger ON older.parent = younger.parent
    AND older.child < younger.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
SELECT
    "The two siblings, " || sib1 || " plus " || sib2 || " have the same size: " || s1.size
from
    siblings
    JOIN size_of_dogs as s1 ON siblings.sib1 = s1.name
    JOIN size_of_dogs as s2 ON siblings.sib2 = s2.name
WHERE
    s1.size = s2.size;

-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
SELECT
    fur,
    max(height) - min(height)
FROM
    dogs
GROUP BY
    fur
HAVING
    min(height) >= avg(height) * 0.7
    AND max(height) <= avg(height) * 1.3;