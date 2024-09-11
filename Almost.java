import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;


public class Almost
{
    public static void main(String[] args)
    {
        try
        {
            File temp = new File("almost.dat");
            Scanner kb = new Scanner(temp);
            int numDataSets = kb.nextInt();
            kb.nextLine();

            String answer = "";

            String line1 = "";
            String line2 = "";
            String line3 = "";

            String[][] arr = new String[3][3];

            for (int i = 0; i < numDataSets; i++)
            {
                line1 = kb.nextLine();
                line2 = kb.nextLine();
                line3 = kb.nextLine();

                arr[0][0] = line1.substring(0,1);
                arr[0][1] = line1.substring(1, 2);
                arr[0][2] = line1.substring(2);

                arr[1][0] = line2.substring(0,1);
                arr[1][1] = line2.substring(1, 2);
                arr[1][2] = line2.substring(2);

                arr[2][0] = line3.substring(0,1);
                arr[2][1] = line3.substring(1, 2);
                arr[2][2] = line3.substring(2);


                
                
                
                
                if (arr[0][0].equals("X") && arr[1][0].equals("X"))
                {
                    answer += "3 1";
                    answer += "\n";

                }

                else if (arr[0][0].equals("X") &&  arr[0][1].equals("X"))
                {
                    answer += "1 3";
                    answer += "\n";
                }


                else if (arr[0][0].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "3 3";
                    answer += "\n";
                
                }






                else if (arr[0][1].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "3 2";
                    answer += "\n";
                }

                else if (arr[0][1].equals("X") && arr[0][0].equals("X"))
                {
                    answer += "1 3";
                    answer += "\n";
                }

                else if (arr[0][1].equals("X") && arr[0][2].equals("X"))
                {
                    answer += "1 1";
                    answer += "\n";
                }

               
               
               
               
                else if (arr[0][2].equals("X") && arr[0][1].equals("X"))
                {
                    answer += "1 1";
                    answer += "\n";
                }

                else if (arr[0][2].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "3 1";
                    answer += "\n";
                }

                else if (arr[0][2].equals("X") && arr[1][2].equals("X"))
                {
                    answer += "3 3";
                    answer += "\n";
                }



              
                else if (arr[1][0].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "2 3";
                    answer += "\n";
                }
               
                else if (arr[1][0].equals("X") && arr[0][0].equals("X"))
                {
                    answer += "3 1";
                    answer += "\n";
                }

                else if (arr[1][0].equals("X") && arr[2][0].equals("X"))
                {
                    answer += "1 1";
                    answer += "\n";
                }

               
               
               
                
                else if (arr[1][1].equals("X") && arr[0][0].equals("X"))
                {
                    answer += "3 3";
                    answer += "\n";
                }

                else if (arr[1][1].equals("X") && arr[0][1].equals("X"))
                {
                    answer += "3 2";
                    answer += "\n";
                }

                else if (arr[1][1].equals("X") && arr[0][2].equals("X"))
                {
                    answer += "3 1";
                    answer += "\n";
                }

                else if (arr[1][1].equals("X") && arr[1][0].equals("X"))
                {
                    answer += "2 3";
                    answer += "\n";
                }

               

                else if (arr[1][1].equals("X") && arr[2][0].equals("X"))
                {
                    answer += "1 3";
                    answer += "\n";
                }
                
                else if (arr[1][1].equals("X") && arr[2][1].equals("X"))
                {
                    answer += "1 2";
                    answer += "\n";
                }

                else if (arr[1][1].equals("X") && arr[2][2].equals("X"))
                {
                    answer += "1 1";
                    answer += "\n";
                }

                
                
                
                else if (arr[1][2].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "2 1";
                    answer += "\n";
                }

                else  if (arr[1][2].equals("X") && arr[0][2].equals("X"))
                {
                    answer += "3 3";
                    answer += "\n";
                }

                else if (arr[1][2].equals("X") && arr[2][2].equals("X"))
                {
                    answer += "1 3";
                    answer += "\n";
                }





                else if (arr[2][0].equals("X") && arr[1][0].equals("X"))
                {
                    answer += "1 1";
                    answer += "\n";
                }

                else if (arr[2][0].equals("X") && arr[2][1].equals("X"))
                {
                    answer += "3 3";
                    answer += "\n";
                }

                else if (arr[2][0].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "1 3";
                    answer += "\n";
                }
                

               
               
               
               
                else if (arr[2][1].equals("X") && arr[2][0].equals("X"))
                {
                    answer += "3 3";
                    answer += "\n";
                }

                else if (arr[2][1].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "1 2";
                    answer += "\n";
                }

                else if (arr[2][1].equals("X") && arr[2][2].equals("X"))
                {
                    answer += "3 1";
                    answer += "\n";
                }


                else if (arr[2][2].equals("X") && arr[2][1].equals("X"))
                {
                    answer += "3 1";
                    answer += "\n";
                }

                else if (arr[2][2].equals("X") && arr[1][1].equals("X"))
                {
                    answer += "1 1";
                    answer += "\n";
                }

                else if (arr[2][2].equals("X") && arr[1][2].equals("X"))
                {
                    answer += "1 3";
                    answer += "\n";
                }

                else if (arr[1][1].equals("X") && arr[1][2].equals("X"))
                {
                    answer += "2 1";
                    answer += "\n";
                }


            }
            

            System.out.println(answer);

        }
        
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
        }
       
        

    }
}