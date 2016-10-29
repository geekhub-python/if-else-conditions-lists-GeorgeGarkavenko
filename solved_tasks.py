#!/usr/bin/env python3

def handle_task_1(year):
    from calendar import isleap
    return 'YES' if isleap(year) else 'NO'

def handle_task_2(a, b, c):
    arguments = locals().values()
    original_len = len(set(arguments))
    return 4 - original_len if original_len < 3 else 0
    
def handle_task_3(n, m, k):
    condition_not= (m * n < k) or (k % n) and (k % m)
    return 'NO' if condition_not else 'YES'

def handle_task_4(params):
    from itertools import combinations
    comb = combinations(params, 2)
    equl_pairs = filter( lambda pair: pair[0] == pair[1] , comb)
    return len(tuple(equl_pairs))

def handle_task_5(params):
    pairs  = zip(params[:-1], params[1:])
    needed_pairs_gen = filter((lambda pair: pair[0] * pair[1] > 0 ), pairs)
    needed_pairs = tuple(needed_pairs_gen)
    if needed_pairs:
        return needed_pairs[0]
    else:
        return None
    
    
 
def main():
    
    test_inputs = (
        (1, (2012,)),
        (1, (2011,)),
        (1, (1492,)),
        (1, (1800,)),
        
        (2, (10, 5, 10)),
        (2, (17, 17, -9)),
        (2, (4, -82, -82)),
        (2, (5, 2, 4)),
        (2, (-149, -146, -142)),
        (2, (666, 666, 666)),
        
        (3, (4, 2, 6)),
        (3, (2, 10, 7)),
        (3, (5, 7, 1)),
        (3, (7, 4, 21)),
        (3, (5, 12, 100)),
        
        (4, ([1, 2, 3, 2, 3],) ), 
        (4, ([1, 1, 1, 1, 1],) ), 
        (4, ([1, 2, 3],) ), 
        (4, ([1, 1, 1],) ), 
        (4, ([2, 3],) ), 
        (4, ([2, 2],) ), 
        (4, ([0, 0],) ), 
        (4, ([0, 0, 6, 1, 1, 4, 2, 1, 2, 2],) ), 
        (4, ([0, 1, 43, 10, 13, 33, 15, 8, 18, 21],)), 
        (4, ([3, 2, 1, 2, 2, 4, 3, 2, 5, 3, 2],)), 
        
        (5, ([-1, 2, 3, -1, -2], )), 
        (5, ([1, 2, -3, -4, -5], )), 
        (5, ([1, -2, 3, -4, -5], )), 
        (5, ([1, -2, 3, -4, 5, 6], ))
    )
    
    for i, values in test_inputs:
        print('Task {0} '.format(i))
        print('Input: ' + str(values))
        print('Output: ', end='')
        handler_name = 'handle_task_' + str(i)
        handler = globals()[handler_name]
        print(handler(*values))
        print('=================================')

  
if __name__ == '__main__':
    main()