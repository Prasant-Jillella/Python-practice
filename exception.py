__author__ = 'PrasantJillella'
while True:
    '''This program deals with exception handling and its cases '''
    try:
        no= int(input("Enter a number"))
        count=47/no
        print (count)
        break
    except ValueError:
        print("Must enter only numbers not strings and other values")
    except ZeroDivisionError:
        print("Must not enter 0")
    except:
        break
    finally:
        print("loop complete")