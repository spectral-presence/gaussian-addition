def consecutive_sum():
    global n2
    n2 = int(input("\nHow many consecutive natural numbers do you want to know the sum of? "))
    n = n2/2
    in_list = list(range(1, n2 + 1))
    num = 1
    while num <= n2/2:
        if len(in_list) == 0:
            break
        else:
            gt1 = in_list.pop(0)
            gt2 = in_list.pop(-1)
            g_sum = gt1 + gt2
            print("\n%d + %d = %d." % (gt1, gt2, g_sum))
            num = num + 1
            global s1
            s1 = n * g_sum
    print("\nFinal result: %d" % s1)

print("Welcome to Gaussian addition!")
start = ' '
while start != 'end':
    start = input("Press any key! ('end' to quit) ")
    if start == 'end':
        break
    else:
        consecutive_sum()
        print("\nThere were %d partial sums.\n" % (n2/2))

print("Okay, see you later!")
