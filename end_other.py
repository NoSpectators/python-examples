def main():
    array = [end_other('Hiabc','abc'), end_other('AbC', 'HiaBc')
		,end_other('abc', 'abXabc')]
    print_results(array)

def print_results(arr):
    for i in arr:
	print i

def end_other(a,b):
    a = a.lower()
    b = b.lower()

    if a == b[-(len(a)):] or b == a[-(len(b)):]:
        return True
    else:
        return False

main() 

