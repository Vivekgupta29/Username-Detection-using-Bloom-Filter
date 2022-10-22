from django.http import HttpResponse
from django.shortcuts import render
from UsernameDetection.bloomfilter import BloomFilter
from random import shuffle
from pandas import *
from csv import writer

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


# Create your views here.
def index(request):
    if request.method == 'POST':
        word = request.POST.get('username')
        data = read_csv("UsernameDetection/usernames.csv")
        username = data['username'].tolist()
        word_present = username

        n = len(word_present) #no of items to add
        p = 0.05 #false positive probability

        bloomf = BloomFilter(n,p)
        print("Size of bit array:{}".format(bloomf.size))
        for item in word_present:
            bloomf.add(item)
        if bloomf.check(word):
            data = "'" + word +"' Username Maybe Exists / False Positive!"
        else:
            data = "'" + word +"' Username is Available! / Surely not present in Bitarray"
    else:
        data = ''
    return render(request,'index.html',{'data' : data})