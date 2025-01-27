

# wap to return true if a string contain recursive vowels


def recursive(*args):


   vowels = "aeiouAEIOU"

   result = ""

   for i in args:
      
      for j in i:

         if j in vowels:          # and text.count(i) > 1
 
            if j in result:

             return (True)
            
         result += j

      return(False) 

           
              
           
input = "helloworld"          
output = recursive(input)

print(f"output is :{output}")
       



         

  



