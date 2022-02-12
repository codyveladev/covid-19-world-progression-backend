try: 
    from app import app
    import unittest
    import json
except Exception as e: 
    print("Some modules are missing {}".format(e))

class FlaskRestTest(unittest.TestCase):
    #util function
    def route_success_util(self, route): 
        tester = app.test_client(self)
        response = tester.get(route)
        response_code = response.status_code
        #Ensure the route is working 
        return response_code
    
    #test the index route 
    def test_index_route_success(self): 
        response_code = self.route_success_util('/')
        self.assertEqual(str(response_code), "200")

    #Ensure the response is JSON 
    def test_iso_code_content(self): 
        tester = app.test_client(self)
        response = tester.get('/api/country/USA')
        self.assertEqual(response.content_type, "application/json")
    
    #test the iso code route 
    def test_iso_code_route_success(self):
        response_code = self.route_success_util('/api/country/USA')
        self.assertEqual(str(response_code), "200")    
    
    #Given the iso code route is returning accurate data 
    def test_iso_code_route(self): 
        tester = app.test_client(self)
        iso_codes = ["USA", "ARG", "RUS"]
        countries = ["United States", "Argentina", "Russia"]
        for i in range(len(iso_codes)):
            response = tester.get('/api/country/{}'.format(iso_codes[i]))
            response_body = response.data
            #bytes --> json --> dict 
            formatted_response = dict(json.loads(response_body.decode('utf8').replace("'", '"')))
            #make sure that the ISO code is giving the correct country 
            self.assertEqual(formatted_response['country'], countries[i])


if __name__ == "__main__": 
    unittest.main()
