import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    s = input_data[1]
    
    max_beauty = 0
        
    alphabet = set(s)
    
    for char_target in alphabet:
        left = 0
        changes_used = 0
        
        for right in range(len(s)):
            if s[right] != char_target:
                changes_used += 1
            
            while changes_used > k:
                if s[left] != char_target:
                    changes_used -= 1
                left += 1
        
            current_length = right - left + 1
            if current_length > max_beauty:
                max_beauty = current_length
                
    print(max_beauty)

if __name__ == "__main__":
    solve()