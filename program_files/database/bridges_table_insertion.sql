 -- For making Bridges
INSERT INTO npi_grants_bridge (npi_id, grants_id)
SELECT npi.id AS npi_id, grants.id AS grants_id
FROM npi 
JOIN grants 
ON LOWER(npi.lastname) = LOWER(grants.lastname)
WHERE grants.forename IS NOT NULL
AND grants.city IS NOT NULL
LIMIT 50000;
