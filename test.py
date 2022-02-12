try: 
    from app import app
    import unittest
    import requests
    import json
except Exception as e: 
    print("Some modules are missing {}".format(e))

class FlaskRestTest(unittest.TestCase):
    #test the index route 
    def test_index_route(self): 
        tester = app.test_client(self)
        response = tester.get('/')
        response_code = response.status_code
        #Ensure the route is working 
        self.assertEqual(str(response_code), "200")
    
    #Ensure the response is JSON 
    def test_iso_code_content(self): 
        tester = app.test_client(self)
        response = tester.get('/api/country/USA')
        self.assertEqual(response.content_type, "application/json")
    
    #Given the iso code in the 
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
