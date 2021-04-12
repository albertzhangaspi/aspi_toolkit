# aspi_toolkit
# Functions added in chronological order

import re
import pdfkit

def urls2pdf(string):
    # Get all urls#
    urls = re.findall(r'(https?://\S+)', string)
    # Convert urls to pdfs
    i = 1 # Counter for pdf serialisation
    for url in urls:
        # The string 'findall' function below doesn't remove the period at the end of strings. This funciton fixes that.
        if url[-1] == ".":
            url = url[]:-1]
        else:
            continue
        out_pdf = str(i)+'_'+url.replace("http://","").replace("https://","").replace("/","")+'.pdf' # Clean string for pdf output
        print('Saving: '+ url + ' as file: '+ out_pdf)
        pdfkit.from_url(url, out_pdf)
        i += 1




