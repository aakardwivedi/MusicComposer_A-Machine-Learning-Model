import urllib
import zipfile
import nottingham_util
import rnn

# collect the data
#url = "http://www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
#urllib.urlretrieve(url, "tester.zip")

zip = zipfile.ZipFile('tester.zip', 'r')  
zip.extractall('data')  

# build the model
nottingham_util.create_model()

# train the model
rnn.train_model()
