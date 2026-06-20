data = {
      'subbu':{'stat':True,'pyton':98,'mysql':95,'falsk':94},
      'nagendra':{'stat':True,'pyton':78,'mysql':65,'falsk':84},
      'dinesh':{'stat':False,'pyton':None,'mysql':None,'falsk':None},
      'naresh':{'stat':True,'pyton':68,'mysql':55,'falsk':64},
      'rishi':{'stat':True,'pyton':33,'mysql':25,'falsk':34},
}

name = input()

if name in data:
    if data[name]['stat']:
        total = data[name]['pyton'] + data[name]['mysql'] + data[name]['falsk']
        avg = total/3

        if avg > 90:
            print(f"congrations {name},you got the first class ")
        elif avg > 70:
            print(f"good {name},keep it up for the next time")
        elif avg > 35:
            print(f"better {name},work hard next time!")
        else:
            print(f"{name} didnt write the exam. Bring your parents")
else:
    print("not found in the data")