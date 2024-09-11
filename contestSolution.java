import java.util.HashMap;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class contestSolution
{
   public static void main(String[] args)
   {
       try
       {
           File f = new File("judgeInput.txt");
           Scanner kb = new Scanner(f);
           String inp = kb.nextLine();


           HashMap<Character, Integer> map = new HashMap<>();
          
           char ans = 0;
           int maxCount = 0;


           // Process each character in the input string
           for (int i = 0; i < inp.length(); i++)
           {
               char temp = inp.charAt(i);
               // Check if the character is an alphabetical letter
               if (Character.isLetter(temp))
               {
                   // Convert to lowercase to ignore case sensitivity
                   temp = Character.toLowerCase(temp);
                   map.put(temp, map.getOrDefault(temp, 0) + 1);


                   // Update the most frequent character
                   if (map.get(temp) > maxCount || (map.get(temp) == maxCount && temp < ans))
                   {
                       maxCount = map.get(temp);
                       ans = temp;
                   }
               }
           }


           System.out.println("Dear lil joe please remove the " + ans + " key from your keyboard.");
       }
       catch(FileNotFoundException e)
       {
           System.out.println("Error finding the file");
       }
   }
}



