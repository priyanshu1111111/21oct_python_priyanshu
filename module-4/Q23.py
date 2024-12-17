# Q23. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class rectangle:

    def calculate(self):
        length=int(input('Enter Value of length: '))
        width=int(input('Enter Value of Width: '))

        area=length * width

        print(f'Area Of Rectangle is: {area}')

ra=rectangle()

ra.calculate()