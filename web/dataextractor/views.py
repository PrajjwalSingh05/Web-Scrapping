from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,login,logout
from django.contrib import messages
import requests
import pandas as pd
from bs4 import BeautifulSoup
# Create your views here.
from .models import *
import csv
import datetime


def index(request):
    return render(request,"index.html")
def user_home(request):
    return render(request,"user_home.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


def feedback(request):
    user = request.user
    data = Signup.objects.get(user=user)
    if request.method == 'POST':
        firstname = request.POST['fname']

        emaiid = request.POST['femail']
        ucomment = request.POST['fcomment']
        utime = current_time = datetime.datetime.now().strftime("%H:%M:%S")
        udate = datetime.date.today()
        try:
            result = Feedback(name=firstname, email=emaiid, feedback=ucomment,date=udate,time=utime)
            result.save()
            messages.success(request, "Feedback Submitted")

        except:
            messages.error(request, "Some error occurred")

    d = {'data': data}

    return render(request, "feedback.html", d)
def view_feedback(request):
    data=Feedback.objects.all()
    d={'data':data}
    return render(request,'view_feedback.html',d)
def view_user(request):
    data=Signup.objects.all()
    print(data)
    d={'data': data}
    return render(request,"view_user.html",d)
def delete_user(request,id):
    data=User.objects.get(id=id)
    data.delete()
    return redirect('view_user')
def delete_feedback(request,id):
    data=Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_feedback')
def signup(request):
    print("singup page")
    print("singup page")
    print("singup page")
    print("singup page")
    print("singup page")
    if request.method=='POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        fpasword = request.POST['ufpass']
        spasword = request.POST['uspass']
        email = request.POST['uemail']
        utime = current_time = datetime.datetime.now().strftime("%H:%M:%S")
        udate = datetime.date.today()

        try:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=email,
                                            password=fpasword)
            Signup.objects.create(user=user,time=utime,date=udate)
            messages.success(request, "User Created Successfully")
        except Exception as ep:
            print(ep)
            messages.error(request, "User Already Exist")

    return render(request,"signup.html")
def login(request):
    if request.method == 'POST':

        uname = request.POST['username']
        pasword = request.POST['psword']
        user = auth.authenticate(username=uname, password=pasword)
        try:
            if user.is_staff:
                print("admin login ")
                print("admin login ")
                print("admin login ")
                print("admin login ")
                # print("Inside  ")
                auth.login(request, user)
                messages.success(request, "Login Successfull")
                return redirect('admin_home')


            elif user is not None:
                print("not user")
                print("not user")
                print("not user")
                print("not user")
                auth.login(request, user)
                messages.success(request, "Login Successfull")
                return redirect('user_home')

            else:
                print("else")
                print("else")
                print("else")
                print("else")
                print("else")
                print("else")

                messages.error(request, "Some error occurred")
        except Exception as ep:
            print("ecepet")
            print(ep)
            print("ecepet")
            print("ecepet")
            print("ecepet")
            messages.error(request, "Invalid Login Credentials")

    return render(request, 'login.html', )

def admin_home(request):
    return  render(request,"admin_home.html")
def extrator(request):
    return render(request,"extrator.html")


def mobilephone_flipkart(request):
    print("Under Mobile Phone")

    url_template = "https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"

    # Define the number of pages to scrape
    num_pages = request.GET.get('page', 1)
    num_pages = int(num_pages)
    try:
        for page_num in range(1, num_pages+ 1):
            # Create the URL for the current page
            url = url_template.format(page_num)

            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')

            results = soup.find_all('div', {'class': '_2kHMtA'})

            for result in results:
                # Extract brand name
                try:

                    brand = result.find('div', {'class': '_4rR01T'}).text
                except:
                    brand = "not found"
                try:
                    # Extract price
                    price = result.find('div', {'class': '_30jeq3 _1_WHN1'}).text
                except:
                    price = "not found"

                # Extract memory, display, battery, and warranty
                features = result.find_all('ul', {'class': '_1xgFaf'})[0]
                feature_list = features.find_all('li')
                try:
                    memory = feature_list[0].text
                except:
                    memory = "not found"

                try:
                    display = feature_list[1].text
                except:
                    display = "not found"
                try:

                    camera = feature_list[2].text
                except:
                    camera = "not found"
                try:
                    battery_processor = feature_list[3].text

                    if battery_processor[0].isdigit():
                        battery = battery_processor
                        print(battery)
                    else:
                        battery = "not found"
                except:
                    battery = "not found"


                m = FlipkartMobileModel(brand=brand, price=price[1:], memory=memory, display=display, camera=camera,
                                        battery=battery)
                m.save()
                print('price: ', price[1:])
        messages.success(request, 'Data Extracted Successfully')

    except Exception as ep:
        messages.error(request, 'Data Extraction Failed')
        print(ep)
    # pkl_data = pickle.dumps(mobile_data)
    # response = HttpResponse(pkl_data, content_type='application/octet-stream')
    # response['Content-Disposition'] = 'attachment; filename="data.csv"'
    # pkl_url = request.build_absolute_uri(
    # for mobile in mobile_data:
    #     print(mobile)

    return redirect("extrator")

def retrivemobilephone_flipkart(request):
        data = FlipkartMobileModel.objects.all()
        print("Printing retive data")
        # students = Student.objects.all()
        response = HttpResponse('text/csv')

        response['Content-Disposition'] = 'attachment; filename=students.csv'
        writer = csv.writer(response)
        writer.writerow(['BRAND', 'PRICE', 'MEMORY', 'DISPLAY', 'CAMERA', 'BATTERY'])

        studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
        for std in studs:
            writer.writerow(std)
        return response


def retrive_specific_mobilephone_flipkart(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)
    data = FlipkartMobileModel.objects.all()[:record - 1]
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    writer.writerow(['BRAND', 'PRICE', 'MEMORY', 'DISPLAY', 'CAMERA', 'BATTERY'])

    studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
    for std in studs:
        writer.writerow(std)
    return response


#   return redirect("interface_download_dataset")
def delete_mobilephone_flipkart(request):
    try:
        data = FlipkartMobileModel.objects.all().delete()
        messages.success(request, 'Data Deleted Successfully')
    except:
        messages.error(request, 'Data Not Deleted')

    return redirect("extrator")


def laptop_flipkart(request):
    num_pages = request.GET.get('page', 1)
    num_pages = int(num_pages)
    # URL of the website to be scraped
    url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

    # Initialize an empty list to store the laptop details

    try:
        for page in range(1, num_pages + 1):
            # Send a request to the URL
            response = requests.get(url + '&page=' + str(page))

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the laptops on the page
            laptops = soup.find_all('div', {'class': '_2kHMtA'})

            # Loop through each laptop and extract the required details
            for laptop in laptops:
                # Find the name of the laptop
                try:

                    name = laptop.find('div', {'class': '_4rR01T'}).text
                except:
                    name = 'Not Found'
                try:
                    # Find the processor of the laptop
                    processor = laptop.find('ul', {'class': '_1xgFaf'}).find_all('li')[0].text
                except:
                    processor = 'Not Found'
                try:
                    # Find the RAM of the laptop
                    ram = laptop.find('ul', {'class': '_1xgFaf'}).find_all('li')[1].text
                except:
                    ram = 'Not Found'

                # Find the operating system of the laptop
                try:
                    os = laptop.find('ul', {'class': '_1xgFaf'}).find_all('li')[2].text
                except:
                    os = 'Not Found'
                try:

                    # Find the hard disk capacity of the laptop
                    hdd = laptop.find('ul', {'class': '_1xgFaf'}).find_all('li')[3].text
                except:
                    hdd = 'Not Found'
                try:
                    # Find the display size of the laptop
                    display = laptop.find('ul', {'class': '_1xgFaf'}).find_all('li')[4].text
                except:
                    display = 'Not Found'
                # Find the warranty of the laptop
                # warranty = laptop.find('ul', {'class': '_1xgFaf'}).find_all('li')[5].text
                try:
                    # Find the price of the laptop
                    price = laptop.find('div', {'class': '_30jeq3 _1_WHN1'}).text
                except:
                    price = 'Not Found'
                # laptops_list.append({
                #     "name":name,
                #     "Processor":processor,
                #     "RAM":ram,
                #     "Operating System":os,
                #     "Hard Disk":hdd,
                #     "Dsiplay Size":display,
                #     "price":price[1:]
                # })
                result = FlipkartLaptopModel(name=name, processor=processor, ram=ram, opearting_system=os,
                                             hard_disk=hdd, display=display, price=price[1:])
                result.save()
        messages.success(request, 'Data Extracted Successfully')
    except:
        messages.error(request, "Data Not Extracted")

    return redirect("extrator")


def retrivelaptop_flipkart(request):
    data = FlipkartLaptopModel.objects.all()
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    # writer.writerow(['BRAND', 'PRICE', 'MEMORY', 'DISPLAY', 'CAMERA', 'BATTERY'])
    writer.writerow(['NAME', 'PROCESSOR', 'RAM', 'OPERATING SYSTEM', 'HARD DISK', 'DISPLAY', 'PRICE'])

    # studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
    studs = data.values_list('name', 'processor', 'ram', 'opearting_system', 'hard_disk', 'display', 'price')
    for std in studs:
        writer.writerow(std)
    return response


def retrive_specific_laptop_flipkart(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)
    data = FlipkartLaptopModel.objects.all()[:record - 1]
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    # writer.writerow(['BRAND', 'PRICE', 'MEMORY', 'DISPLAY', 'CAMERA', 'BATTERY'])
    writer.writerow(['NAME', 'PROCESSOR', 'RAM', 'OPERATING SYSTEM', 'HARD DISK', 'DISPLAY', 'PRICE'])

    # studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
    studs = data.values_list('name', 'processor', 'ram', 'opearting_system', 'hard_disk', 'display', 'price')
    for std in studs:
        writer.writerow(std)
    return response


def delete_laptop_flipkart(request):
    try:
        data = FlipkartLaptopModel.objects.all().delete()
        messages.success(request, 'Data Deleted Successfully')
    except:
        messages.error(request, "No data to delete")
    return redirect("extrator")


def interface_television_flipkart(request):
    url = "https://www.flipkart.com/search?q=telivsion&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    num_pages = request.GET.get('page', 1)
    num_pages = int(num_pages)
    print((num_pages))
    try:
        for i in range(1, num_pages + 1):
            url_page = url + "&page=" + str(i)

            response = requests.get(url_page)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the products on the page
            try:
                products = soup.find_all("div", {"class": "_3pLy-c row"})

                # Loop through each product and extract the required information
                for product in products:
                    try:
                        # Extract the model name
                        model = product.find("div", {"class": "_4rR01T"}).text
                    except:
                        model = "NA"
                    try:

                        # Extract the operating system
                        os = product.find("ul", {"class": "_1xgFaf"}).li.text
                    except:
                        os = "NA"

                    try:
                        rating = product.find("div", {"class": "_3LWZlK"}).text
                    except:
                        rating = "NA"
                    try:
                        display = product.find("ul", {"class": "_1xgFaf"}).find_all("li")[1].text
                    except:
                        display = "NA"
                    try:
                        warranty = product.find("ul", {"class": "_1xgFaf"}).find_all("li")[2].text
                    except:
                        warranty = "NA"
                    try:
                        price = product.find("div", {"class": "_30jeq3 _1_WHN1"}).text
                    except:
                        price = "NA"

                    result = FlipkartTelivisionModel(name=model, operating_system=os, rating=rating, display=display,
                                                     warrently=warranty, price=price[1:])
                    result.save()

            except:
                pass
        messages.success(request, 'Data Extracted Successfully')

    except Exception as ep:
        print(ep)
        messages.error(request, 'Data Extracted Successfully')

    return redirect("extrator")


def retrive_television_flipkart(request):
    data = FlipkartTelivisionModel.objects.all()
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)

    writer.writerow(['NAME', 'OPERATING SYSTEM', 'RATING', 'DISPLAY', 'WARRANTY', 'PRICE'])

    # studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
    # studs = data.values_list('name', 'processor', 'ram', 'opearting_system', 'hard_disk', 'display', 'price')
    studs = data.values_list('name', 'operating_system', 'rating', 'display', 'warrently', 'price')
    for std in studs:
        writer.writerow(std)
    return response


def retrive_specific_telivision_flipkart(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)
    data = FlipkartTelivisionModel.objects.all()[:record - 1]
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    # writer.writerow(['BRAND', 'PRICE', 'MEMORY', 'DISPLAY', 'CAMERA', 'BATTERY'])
    writer.writerow(['NAME', 'OPERATING SYSTEM', 'RATING', 'DISPLAY', 'WARRANTY', 'PRICE'])

    # studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
    studs = data.values_list('name', 'operating_system', 'rating', 'display', 'warrently', 'price')
    for std in studs:
        writer.writerow(std)
    return response


def delete_television_flipkart(request):
    try:

        data = FlipkartTelivisionModel.objects.all().delete()
        messages.success(request, 'Data Deleted Successfully')
    except:
        messages.error(request, 'Data Not Deleted')
    return redirect("extrator")


def earphone_flipkart(request):
    base_url = "https://www.flipkart.com/search?q=earphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
    num_pages = request.GET.get('page', 1)
    num_pages = int(num_pages)
    print(num_pages)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Loop through each page of earphone search results
    for page in range(1, num_pages + 1):
        # Construct the URL for the current page
        url = base_url + str(page)

        # Send a GET request to the URL
        response = requests.get(url, headers=headers)

        # Create a BeautifulSoup object by parsing the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the links to the individual earphone product pages
        try:
            product_links = soup.find_all('a', class_='s1Q9rs')

            # Loop through each product link and scrape its details
            for link in product_links:
                # Extract the URL of the product page
                product_url = "https://www.flipkart.com" + link.get('href')

                # Send a GET request to the product URL
                product_response = requests.get(product_url, headers=headers)

                # Create a BeautifulSoup object by parsing the HTML content of the product page
                product_soup = BeautifulSoup(product_response.content, 'html.parser')

                # Find the general details for the earphonep
                model_detail = product_soup.find_all('li', class_='_21lJbe')
                try:
                    model_name = model_detail[0].get_text()
                except:
                    model_name = "Not Available"
                try:

                    color = model_detail[1].get_text()
                except:
                    color = "Not Available"
                try:

                    headphone_type = model_detail[2].get_text()
                except:
                    headphone_type = "Not Available"
                try:

                    inline_remote = model_detail[3].get_text()
                except:
                    inline_remote = "Not Available"
                try:

                    connectivity = model_detail[5].get_text()
                except:
                    connectivity = "Not Available"
                try:

                    price = product_soup.find('div', class_='_30jeq3 _16Jk6d').get_text()
                except:
                    price = "Not Available"

                print(model_name, color, headphone_type, inline_remote, connectivity, price)
                result = FlipkartEarphoneModel(name=model_name, color=color, headphone_type=headphone_type,
                                               inline_remote=inline_remote, connectivity=connectivity, price=price[1:])
                result.save()

            messages.success(request, 'Data Saved Successfully')
        except:
            messages.error(request, 'Data Not Saved')
        return redirect("extrator")


def retrive_earphone_flipkart(request):
    data = FlipkartEarphoneModel.objects.all()
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)

    writer.writerow(['NAME', 'COLOR', 'HEADPHONE TYPE', 'INLINE REMOTE', 'CONNECTIVITY', 'PRICE'])

    studs = data.values_list('name', 'color', 'headphone_type', 'inline_remote', 'connectivity', 'price')
    for std in studs:
        writer.writerow(std)
    return response


def retrive_specific_earphone_flipkart(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)
    data = FlipkartEarphoneModel.objects.all()[:record - 1]
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    # writer.writerow(['BRAND', 'PRICE', 'MEMORY', 'DISPLAY', 'CAMERA', 'BATTERY'])
    wti = ['NAME', 'COLOR', 'HEADPHONE TYPE', 'INLINE REMOTE', 'CONNECTIVITY', 'PRICE']

    # studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
    studs = data.values_list('name', 'color', 'headphone_type', 'inline_remote', 'connectivity', 'price')
    for std in studs:
        writer.writerow(std)
    return response


def delete_earphone_flipkart(request):
    try:

        data = FlipkartEarphoneModel.objects.all().delete()
        messages.success(request, "Data Deleted Successfully")
    except:
        messages.error(request, "Data Not Deleted")
    return redirect("extrator")


def bike_flipkart(request):
    bike_data = []
    num_pages = request.GET.get('page', 1)
    num_pages = int(num_pages)
    # Define the base URL, the number of pages to scrape, and the headers for the GET requests
    base_url = "https://www.autox.com/new-bike-launches-in-india/page"
    print(num_pages)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Loop through each page of bike launches
    try:
        for page in range(1, num_pages + 1):
            # Construct the URL for the current page
            url = f"{base_url}/{page}"

            # Send a GET request to the URL
            response = requests.get(url, headers=headers)

            # Create a BeautifulSoup object by parsing the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the links to the individual bike launch articles\
            article_links = soup.find_all('a', class_='model-title')

            # Loop through each article link and scrape its details
            for link in article_links:

                url = link.get('href')


                article_response = requests.get(url, headers=headers)


                article_soup = BeautifulSoup(article_response.content, 'html.parser')


                try:
                    model_name = article_soup.find('h1', class_='model-page-title').get_text()
                except:
                    model_name = "Not Available"
                try:
                    price = article_soup.find('span', class_='price').get_text()
                except:
                    price = "Not Available"

                try:
                    displacement = article_soup.find('td', text='Displacement').find_next_sibling('td').get_text()
                except:
                    displacement = "Not Available"
                try:
                    max_power = article_soup.find('td', text='Max Power').find_next_sibling('td').get_text()
                except:
                    max_power = "Not Available"
                try:

                    mileage = article_soup.find('td', text='Mileage').find_next_sibling('td').get_text()
                except:
                    mileage = "Not Available"
                result = FlipkartBikeModel(name=model_name, price=price[2:], displacement=displacement,
                                           max_power=max_power, mileage=mileage)
                result.save()

        messages.success(request, 'Data Saved Successfully')
    except Exception as ep:
        print(ep)
        messages.error(request, 'Data Not Saved')
    return redirect("extrator")


def retrive_bike_flipkart(request):
    data = FlipkartBikeModel.objects.all()
    print("Printing retive data")
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=Bike.csv'
    writer = csv.writer(response)
    writer.writerow(['NAME', 'PRICE', 'DISPLACEMENT', 'MAX POWER', 'MILEAGE'])

    # writer.writerow(['NAME', 'COLOR', 'HEADPHONE TYPE', 'INLINE REMOTE', 'CONNECTIVITY', 'PRICE'])
    studs = data.values_list('name', 'price', 'displacement', 'max_power', 'mileage')
    for std in studs:
        writer.writerow(std)
    return response


def retrive_specific_bike_flipkart(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)
    data = FlipkartBikeModel.objects.all()[:record - 1]
    print("Printing retive data")
    # students = Student.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    # writer.writerow(['BRAND', 'PRICE', 'MEMORY', 'DISPLAY', 'CAMERA', 'BATTERY'])
    writer.writerow(['NAME', 'PRICE', 'DISPLACEMENT', 'MAX POWER', 'MILEAGE'])

    # studs = data.values_list('brand', 'price', 'memory', 'display', 'camera', 'battery')
    studs = data.values_list('name', 'price', 'displacement', 'max_power', 'mileage')
    for std in studs:
        writer.writerow(std)
    return response


def delete_bike_flipkart(request):
    try:
        data = FlipkartBikeModel.objects.all().delete()
        messages.success(request, "Data Deleted Successfully")
    except:
        messages.error(request, "Data Not Deleted")
    return redirect("extrator")


def washing_machine_flipkart(request):

    num_pages = request.GET.get('page', 1)
    num_pages = int(num_pages)

    print(num_pages)
    base_url = "https://www.flipkart.com"
    search_term = "washing machine"
    query_params = {"q": search_term, "otracker": "search", "otracker1": "search",
                    "marketplace": "FLIPKART", "as-show": "on", "as": "off"}

    try:
        for page_num in range(1, num_pages+1):  # Change 4 to the number of pages you want to scrape
            # Create the search URL for the current page
            query_params["page"] = str(page_num)
            search_url = base_url + "/search?" + "&".join([f"{key}={value}" for key, value in query_params.items()])

            # Send a GET request to the search URL and parse the HTML response
            response = requests.get(search_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the washing machine product listings on the current page
            products = soup.find_all("div", {"class": "_2kHMtA"})
            print("product")
            print(products)

            # Loop through each product and extract the relevant data
            for product in products:
                # Extract the product URL and send a GET request to it
                product_url = base_url + product.find("a")["href"]
                response = requests.get(product_url)
                soup = BeautifulSoup(response.text, 'html.parser')

                try:
                    details = soup.find("table", {"class": "_14cfVK"}).find_all("li")
                    print(details)
                except:
                    pass
                try:

                    # function = details[0].text.strip()
                    brand = details[1].text.strip()
                except:
                    brand = "Not Available"
                try:

                    model_name = details[2].text.strip()
                except:
                    model_name = "Not Available"
                try:

                    energy_rating = details[4].text.strip()
                except:
                    energy_rating = "Not Available"
                try:
                    washing_capacity = details[5].text.strip()
                except:
                    washing_capacity = "Not Available"
                try:

                    maximum_spin_speed = details[7].text.strip()
                except:
                    maximum_spin_speed = "Not Available"
                try:

                    price = soup.find("div", {"class": "_30jeq3 _16Jk6d"}).text.strip()
                except:
                    price = "Not Available"

                print(brand, model_name, energy_rating, washing_capacity, maximum_spin_speed, price)
                result = FlipkartWachingMachineModel(model=model_name, brand=brand, energy_rating=energy_rating,
                                                     washing_capacity=washing_capacity,
                                                     maximum_spin_speed=maximum_spin_speed, price=price[1:])
                result.save()

        messages.success(request, "Data Downloaded Successfully")
    except Exception as ep:
        print(ep)
        messages.error(request, "Data Not Downloaded")
    return redirect("extrator")


def retrive_washing_machine_flipkart(request):
    data = FlipkartWachingMachineModel.objects.all()
    print("Printing retive data")
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=WashingMachine.csv'
    writer = csv.writer(response)

    writer.writerow(['BRAND', 'MODEL', 'ENERGY RATING', 'WASHING CAPACITY', 'MAXIMUM SPIN SPEED', 'PRICE'])
    studs = data.values_list('brand', 'model', 'energy_rating', 'washing_capacity', 'maximum_spin_speed', 'price')

    for std in studs:
        writer.writerow(std)
    return response


def delete_washing_machine_flipkart(request):
    try:
        data = FlipkartWachingMachineModel.objects.all().delete()
        messages.success(request, "Data Deleted Successfully")
    except:
        messages.error(request, "Data Not Deleted")

    return redirect("extrator")


def reterive_specific_washingmachine_flipkart(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)

    print("inside retirve specific record")
    data = FlipkartWachingMachineModel.objects.all()[:record - 1]
    print(data)
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=WashingMachine.csv'
    writer = csv.writer(response)
    writer.writerow(['BRAND', 'MODEL', 'ENERGY RATING', 'WASHING CAPACITY', 'MAXIMUM SPIN SPEED', 'PRICE'])
    studs = data.values_list('brand', 'model', 'energy_rating', 'washing_capacity', 'maximum_spin_speed', 'price')

    for std in studs:
        writer.writerow(std)

    return response


def user_extrator(request):
    return render(request,"user_extrator.html")

def telivion_view(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)

    print("inside retirve specific record")
    data = FlipkartTelivisionModel.objects.all()[:record - 1]
    print(data)
    d={"data":data}
    return render(request,"telivision_view.html",d)

def laptop_view(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)

    print("inside retirve specific record")
    data = FlipkartLaptopModel.objects.all()[:record - 1]
    print(data)
    d={"data":data}
    return render(request,"laptop_view.html",d)
def mobile_view(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)

    print("inside retirve specific record")
    data = FlipkartMobileModel.objects.all()[:record - 1]
    print(data)
    d={"data":data}
    return render(request,"mobile_view.html",d)

def bike_view(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)

    print("inside retirve specific record")
    data = FlipkartBikeModel.objects.all()[:record - 1]
    print(data)
    d={"data":data}
    return render(request,"bike_view.html",d)
def washingmachine_view(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)

    print("inside retirve specific record")
    data = FlipkartWachingMachineModel.objects.all()[:record - 1]
    print(data)
    d={"data":data}
    return render(request,"washingmachine_view.html",d)

def earphone_view(request):
    record = request.GET.get('page', 1)
    record = int(record)
    print(record)

    print("inside retirve specific record")
    data = FlipkartEarphoneModel.objects.all()[:record - 1]
    print(data)
    d={"data":data}
    return render(request,"earphone_view.html",d)
