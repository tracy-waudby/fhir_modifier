# fhir_modifier
Python FHIR Reference Modifier for SQL friendly JSON

Building upon the recommendation from [sql-on-fhir](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) that recommends adding an additional resourceType Id (patientId, groupId, deviceId, locationId) to FHIR references.  This will allow equijoins across FHIR json objects.

Example:

Currently a reference to a subject is formatted as "Patient/f001", where "f001" is the ID on the Patient resource.

``` subject": {
          "reference": "Patient/f001",
          "display": "P. van den Heuvel"
        }
```

This python script will append a new field within the subject dict:
``` subject": {
          "reference": "Patient/f001",
          "display": "P. van den Heuvel",
          "patientId": "f001"
        }
```