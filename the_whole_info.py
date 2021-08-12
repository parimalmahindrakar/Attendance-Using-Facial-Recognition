import json

# data = {

# 	'1':'rv.landge77@gmail.com',
# 	'18':'parimalm4653@gmail.com',
# 	'4':'padu.pmc@gmail.com'
# }

data = {

    '23231': 'parimalm4653@gmail.com',
    '23232': 'parimalm4653@gmail.com',
    '23233': 'parimalm4653@gmail.com',
    '23234': 'parimalm4653@gmail.com',
    '23235':'parimalm4653@gmail.com',
    '23236':'parimalm4653@gmail.com',
    '23237':'parimalm4653@gmail.com',
    '23238':'parimalm4653@gmail.com'

}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

