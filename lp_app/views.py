from django.shortcuts import render, redirect 
from .upload_image_forms import *
from django.http import HttpResponse 
import cv2
from .lp_deeplearning.E2E import E2E



# Create your views here.
def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            #lấy được tên ảnh từ form
            img = str(form.cleaned_data.get("image"))
            src_img = '/media/images/'+ img

            request.session['src_img'] = src_img
            request.session.set_expiry(0)

            #trả về render này 
            return render (request,'lp_app/upload_image.html',{'form' : form , 'src_image' : src_img ,'img' : img})
    else : 
        #còn nếu mới gọi vào thì là methog get nên chưa có gì , cứ để yên
        form = ImageUploadForm()
        #trả về render này với cái form rỗng chưa có gì
        return render (request,'lp_app/upload_image.html',{'form' : form})

def check_lp(request,image_name):
    src = 'C:\\Users\\nguyenbavu\\Desktop\\LP_Web\\media\\images\\'+ image_name
    img = cv2.imread(src)

    # su dung ham predict de du doan 
    result = E2E().predict(img)

    print(result)

    return  render (request,'lp_app/upload_image.html',{'form' : ImageUploadForm() , 'src_image' : request.session['src_img'] ,'rs':result })