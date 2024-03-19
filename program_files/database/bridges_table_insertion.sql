-- For making Bridges
INSERT INTO npi_grants_bridge
(npi_id, grants_id)

SELECT npi.id, g.id
FROM npi 
JOIN grants g
ON LOWER(npi.lastname) = LOWER(g.lastname)
WHERE g.forename IS NOT NULL
AND g.city IS NOT NULL;
