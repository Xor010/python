''' 
    -- welcome message : with option [select games numbers][Exit]
    -- input for Enter Game Number
    -- ask play again or close
        Main Games: 
        - repeat the paragraph without repeat 
        - print number accept dev in to
'''


class G:
    def __init__(self) -> None:
        self.xo ='y'
        while self.xo == 'y':        
            print('''Welcome into my games if you wanna play game please select between[1,2]
                    1 - First Game
                    2 - Sec Game 
                    3 - Exit''')
            self.Game_n = int(input('Select Games Number :'))

            if self.Game_n == 1:
                pae = input('Enter Paragraph:')
                self.paragraph(pae)
                self.p_agn()
            elif self.Game_n == 2:
                i = int(input('num 1:'))
                io =int(input('num 2:'))
                self.numr(i, io)
                self.p_agn()
            elif self.Game_n == 3:
                print('Good By')
                return
            else:
                print('Please Enter Number Between 1 : 3')
                
    def p_agn(self):
        self.xo = input('Play Again ?')        
    def paragraph(self, p):
        g = []
        pa = p.split(' ')
        for l in pa:
            if l not in g:
                g.append(l)
        print (' '.join(g))
        return

    def numr(self,n1,n2):
        r = []
        for x in range(1,101):
            if x%n1 == 0 and x%n2 == 0:
                r.append(x)
        print(r)    
        return
start = G()










