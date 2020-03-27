# fhir_modifier
Python FHIR Reference Modifier for SQL friendly JSON

Builds upon the recommendation from [sql-on-fhir](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) to add an additional resourceType Id (patientId, groupId, deviceId, locationId) to FHIR references.  This will allow equijoins across FHIR json objects.

Example:

Currently a reference is formatted as "Patient/f001", where "f001" is the ID on the Patient resource.

```
"subject": {
          "reference": "Patient/f001",
          "display": "P. van den Heuvel"
        }
```

This python script append a new "patientId" field within the subject dict:
``` 
"subject": {
          "reference": "Patient/f001",
          "display": "P. van den Heuvel",
          "patientId": "f001"
        }
```
