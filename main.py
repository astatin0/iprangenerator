import os
os. system('cls')
print("""

                    ██╗██████╗   ██████╗  █████╗ ███╗  ██╗ ██████╗  ███████╗
                    ██║██╔══██╗  ██╔══██╗██╔══██╗████╗ ██║██╔════╝  ██╔════╝
                    ██║██████╔╝  ██████╔╝███████║██╔██╗██║██║    ██╗█████╗
                    ██║██╔═══╝   ██╔══██╗██╔══██║██║╚████║██║  ╚██╗ ██╔══╝  
                    ██║██║       ██║  ██║██║  ██║██║ ╚███║╚██████╔╝ ███████╗
                    ╚═╝╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝ ╚═════╝  ╚══════╝
           ██████╗ ███████╗███╗  ██╗███████╗██████╗  █████╗ ████████╗ █████╗ ██████╗ 
          ██╔════╝ ██╔════╝████╗ ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
          ██║  ██╗ █████╗  ██╔██╗██║█████╗  ██████╔╝███████║   ██║   ██║  ██║██████╔╝
          ██║  ╚██╗██╔══╝  ██║╚████║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║  ██║██╔══██╗
          ╚██████╔╝███████╗██║ ╚███║███████╗██║  ██║██║  ██║   ██║   ╚█████╔╝██║  ██║
           ╚═════╝ ╚══════╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚════╝ ╚═╝  ╚═╝

                                      ╚═════════════════════╗
                                        github.com/astatin0
                                      ╚═════════════════════╗



""")

İp = input('Enter İp Adress (Sample; 127.0.0.1): ')

İlkPort = input("Enter First Port (Sample; 80) ?: ")
İkinciPort = input("Enter Second Port (Sample; 443) ?: ")
f = open("range/iprange_" + İlkPort + "-" +İkinciPort +".txt","w")
while int(İlkPort) < int(İkinciPort) + 1:
    f.write(İp + ":" + str(İlkPort) + "\n")
    İlkPort = int(İlkPort)+1

