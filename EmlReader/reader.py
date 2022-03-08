import email
from email import policy
from email.parser import BytesParser
import glob
# file_list = glob.glob('*.eml') # returns list of files
file_name = "original_msg.eml"
with open(file_name, 'rb') as fp:  # select a specific email file from the list
    msg = BytesParser(policy=policy.default).parse(fp)
text = msg.get_body(preferencelist=('plain')).get_content()

# footer = msg.get_all()
print(text)  # print the email content