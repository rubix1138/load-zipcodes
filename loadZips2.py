from uszipcode import ZipcodeSearchEngine
import psycopg2, pprint, sys

debug = True
zipSearch = ZipcodeSearchEngine()
zipNumber = 0
conString = "dbname=yourDBname user=postgres"
con = psycopg2.connect(conString)
con.autocommit = True

sqlString = """INSERT INTO zipcode(city, density, houseofunits, landarea, latitude, longitude, 
               neboundlatitude, neboundlongitude, population, state_id, swboundlatitude, 
               swbounglongitude, totalwages, waterarea, wealthy, zipcode, zipcodetype) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""
stateDict = {"AL":1,"AK":2,"AZ":3,"AR":4,"CA":5,"CO":6,"CT":7,"DE":8,"FL":9,"GA":10,"HI":11,
             "ID":12,"IL":13,"IN":14,"IA":15,"KS":16,"KY":17,"LA":18,"ME":19,"MD":20,"MA":21,
             "MI":22,"MN":23,"MS":24,"MO":25,"MT":26,"NE":27,"NV":28,"NH":29,"NJ":30,"NM":31,
             "NY":32,"NC":33,"ND":34,"OH":35,"OK":36,"OR":37,"PA":38,"RI":39,"SC":40,"SD":41,
             "TN":42,"TX":43,"UT":44,"VT":45,"VA":46,"WA":47,"WV":48,"WI":49,"WY":50,"DC":51,
             "PR":52,"VI":53,"AS":54,"GU":55,"MP":56,"AB":57,"BC":58,"MB":59,"NB":60,"NL":61,
             "NS":62,"ON":63,"PE":64,"QC":65,"SK":66,"NT":67,"NU":68,"YT":69,"AA":81,"AE":82,
             "AP":83}


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
                                    zipObj.Population, stateDict[zipObj.State], 
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
    
