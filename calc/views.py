from django.shortcuts import render , redirect

# Create your views here.
def calculator(request):
    context = {}
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        action = request.POST.get('action')
    
        if action == '1':
            ans = int(num1) + int(num2)
        elif action == '2':
            ans = int(num1) - int(num2)
        elif action == '3':
            ans = int(num1) / int(num2)
        elif action == '4':
            ans = int(num1) * int(num2)
        else:
            print('Invalid Request')
        print(ans)

        if ans is not None:
            context = {
                'answer' : ans
            }
            
    return render(request,'index.html',context)