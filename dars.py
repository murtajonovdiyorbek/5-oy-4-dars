# from threading import Thread
# import time 



# def download():
#     print("dastur ishga tushdi...")
#     time.sleep(3)
#     print("Video yuklandi") 
    
# start = time.time()
    
# threades = []
# for i in range(30):
#     th = Thread(target=download)
#     th.start()
#     threades.append(th)    
    
    
# for th in threades:
#     th.join()
    

# end = time.time()


# print(f"Video yuklab olish uchun: {round(end-start, 2)}")











# from concurrent.futures import ThreadPoolExecutor
# import time



# def download(value):
#     print("Dastur ishga tushdi...")
#     time.sleep(3)
#     print("Video yuklandi") 
    
    
    
# start = time.time()


# with ThreadPoolExecutor() as exe:
#     exe.map(download, [1,2,3,4,5])
    
# end = time.time()
# print(f"yuklandi: {round(end-start, 2)}")    















from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import time


import requests



img_urls = [
   'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
   'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
   'https://images.unsplash.com/photo-1524429656589-6633a470097c',
   'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
   'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
   'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
   'https://images.unsplash.com/photo-1522364723953-452d3431c267',
   'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
   'https://images.unsplash.com/photo-1507143550189-fed454f93097',
   'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
   'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
   'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
   'https://images.unsplash.com/photo-1516972810927-80185027ca84',
   'https://images.unsplash.com/photo-1550439062-609e1531270e',
   'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]



def download(image_url):
    image_name = image_url.split("/")[-1]+ ".jpg"
    print(f"{image_name} yuklab olish boshlandi...")
    
    
    content = requests.get(image_url).content
    
    
    with open(f"images/{image_name}", mode="wb") as image:
        
        image.write(content)

    print(f"{image_name} yuklab olindi 😉")
    
    
start = time.time()
thrades = []
for img_url in img_urls:
    th = Thread(target=download, args=(img_url,))
    th.start()
    thrades.append(th)
    
    
    
for th in thrades:
    th.join()
    
    
end= time.time()


print(f"Rasmlarni yuklab olish uchun: {round(end - start, 2)} s vaqt ketdi")



