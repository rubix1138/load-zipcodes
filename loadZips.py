from uszipcode import ZipcodeSearchEngine
import psycopg2, pprint, sys

debug = True
zipSearch = ZipcodeSearchEngine()
zipNumber = 600
conString = "dbname=yourDBname user=postgres"
con = psycopg2.connect(conString)
con.autocommit = True

sqlString = """INSERT INTO zipcode(city, density, houseofunits, landarea, latitude, longitude, 
               neboundlatitude, neboundlongitude, population, state_id, swboundlatitude, 
               swbounglongitude, totalwages, waterarea, wealthy, zipcode, zipcodetype) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""

while zipNumber < 100000:
    zipString = str('%0*d' % (5, zipNumber))
    if debug: print"Trying zipNumber %s as %s" % (zipNumber, zipString)
    zipObj = zipSearch.by_zipcode(zipNumber)
    if zipObj is not None:
        if debug: pprint.pprint(zipObj.to_dict())
        cur = con.cursor()
        try:
            cur.execute(sqlString, (zipObj.City, zipObj.Density, zipObj.HouseOfUnits, 
                                    zipObj.LandArea, zipObj.Latitude, zipObj.Longitude, 
                                    zipObj.NEBoundLatitude, zipObj.NEBoundLongitude, 
                                    zipObj.Population, zipObj.State, 
                                    zipObj.SWBoundLatitude, zipObj.SWBoungLongitude, 
                                    zipObj.TotalWages, zipObj.WaterArea, zipObj.Wealthy, 
                                    zipObj.Zipcode, zipObj.ZipcodeType))
        except psycopg2.Error as e:
            print(e.pgcode)
            print(e.pgerror)
            print(e.diag.severity)
            print(e.diag.message_primary)
            sys.exit(1)
        cur.close()
        if debug: print("%s success" % zipString)
    else:
        if debug: print("%s not found" % zipString)
    zipNumber += 1
    
