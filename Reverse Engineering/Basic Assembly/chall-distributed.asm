main:
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], 10
        mov     DWORD PTR [rbp-8], 2
        mov     eax, DWORD PTR [rbp-4]
        imul    eax, DWORD PTR [rbp-8]
        imul    eax, eax, 130
        sub     eax, 13337
        mov     DWORD PTR [rbp-12], eax
        mov     eax, 0
        pop     rbp
        ret