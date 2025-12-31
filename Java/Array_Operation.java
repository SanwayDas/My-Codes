/**(MUGSHOT)                                BY SANWAY DAS
 *                                          A.K.A RESPECTOR
 *                                          On 12th August, 2022, (I guess) at an ambitious night I started my biggest program.
 *                                          I Am Proud Of It!
 *                                      !!!!THIS IS THE MIGHTY ARRAY OPERATION PROGRAM EVER!!!!
 **/
import java.util.Scanner;
import java.io.*;
import java.util.*;                         //This program is solely based on Scanner Class. All Thanks To This Package!!!!
import java.lang.*;
import java.applet.*;
import java.net.*;
import java.awt.*;
import java.text.*;
import java.math.*;
public class Array_Operation                //Yeah.This is going to be my biggest project.(...YET...)
{                                           //THE BEGINNING!!!!
    public static void main(String args[]) throws IOException
    {
        Scanner in=new Scanner(System.in);  //Rule #1 Scanner Class Object Is Always First Line Inside Main Function
        System.out.print("\u000C");         //(For clearing the monitor screen or your terminal window for tidiness and beauty!)
        String password="Respector LOL";
        String inpass=args[0];
        if(!inpass.equals(password))
        {
        System.out.println("    *.Password Denied.*\n\t**LOCKED**");
        if(inpass.equalsIgnoreCase(password))
        System.out.println("(Hint: The Password Is Correct, The Thing Is That It Is In An Incorrect Case.)");
        System.exit(0);
        }
        System.out.println("WELCOME TO THE MIGHTY ALMIGHTY PROGRAM EVER MADE!!!!");
        System.out.println("I Hope You Like It And Love It!!!!");
        int adder=1,length=0,warning=0;
        int ain[]=new int[length+100];
        for(warning=0;warning<5;warning++)
        {
            System.out.println("Enter length of the array:");
            length=in.nextInt();
            if(length==0)
            {
                System.out.println("You are in no mood for looking at this program, huh?");
                System.out.println("I will not show you anything, until you at least enter a proper number.");
                if((4-warning)>1)
                System.out.println("I will give you "+(4-warning)+" more chances.");
                if((4-warning)==1)
                System.out.println("This is your last and final chance!");
                if((4-warning)==0)
                System.out.println("You have lost your last and final chance. No more chances for you.");
            }
            else
            break;
        }
        if(warning==5)
        {
            System.out.println("I have warned you many times...Looks like you really do not want to look at this program.:(");
            System.exit(0);
        }
        if(length==1)
        {
            System.out.println("Let's See... Only One Element, Isn't It, Huh?");
            System.out.println("I will have no problems, but you will might have problems later, as this big program needs big inputs and big numbers for everything.");
        }
        if(length==10)
        {
            System.out.println("I Do Not Know Why, But Most Of The Time, You Always Like To Press \"10\" Here. I Wonder Why.");
        }
        int falsea[]=new int [length];
        System.out.println("Enter numbers of the array:");
        for(int i = 0;i<length;i++)
        falsea[i]=in.nextInt();
        System.out.println("Array Completed!");
        System.out.println("The array entered is:");    //Just for showing you that I did not cheat in taking your inputs,okay?
        for(int i = 0;i<length;i++)
        {
            if(i>=0 && i<=8)
            System.out.println((i+1)+".  "+falsea[i]);
            else if(i>=9 && i<=98)
            System.out.println((i+1)+". "+falsea[i]);
        }
        int blah=0,blah1=0,commoner=falsea[0],fcommoner=falsea[1];                  //New Problem, Due, To Be/Will Be Solved Tomorrow(1:12:2022)[Actually, The Problem Was Not Here, It Was Below There.]
        for(int i=0;i<length;i++)
        {
            if(falsea[i]==commoner)
            blah++;
        }
        for(int i=1;i<length;i++)                               //Had To Do This.Only For That First Odd Out Number.
        {
            if(falsea[i]==fcommoner)
            blah1++;
        }
        if(length==2&&falsea[0]==falsea[1])
        {
        System.out.println("Oh My! Both Of Your Entered Elements Are The Same!("+falsea[0]+") Is This Intentional?!");
        String hello=in.next();
        if(hello.equalsIgnoreCase("yes"))
        System.out.println("Well,... I Do Not Have Any \"Objections\" For That Indeed!");
        else if(hello.equalsIgnoreCase("no"))
        {
        System.out.println("What Do You Mean By That?!");
        System.out.println("Well,... There Is Nothing I Can Do Now...Sorry.(You Should Better Restart, Or Do You Even Need To, Or Do You Even Want To? I Do Not Care Anymore.)");
        }
        else
        {
        System.out.println("just shut up...");
        System.out.print("However....");
        }
        }
        else if(blah==length&&length!=1&&length!=2)
        {
        System.out.println("Oh My! All Your Entered Elements Are The Same! Is This Intentional?!");
        String hello=in.next();
        if(hello.equalsIgnoreCase("yes"))
        System.out.println("Well,... I Do Not Have Any \"Objections\" For That Indeed!");           //Ha Ha Yeah. "Ace Attorney" Reference.
        else if(hello.equalsIgnoreCase("no"))
        {
        System.out.println("What Do You Mean By That?!");
        System.out.println("Well,... There Is Nothing I Can Do Now...Sorry.(You Should Better Restart)");
        }
        else
        {
        System.out.println("just shut up...");
        System.out.print("However....");
        }
        }
        else if(length!=2&&(blah==(length-1)||(blah1==(length-1)&&falsea[0]!=falsea[1])))    //The Problem Was Here, And It Is Fixed!(No. It Is Partially Done On 01-12-2022 , 23:06:30. Real Fixing Done Completely On 02-12-2022 , 22:54:30)
        {                                                               //Which One Has More Priority? "&&" OR "||" OR "!" ? 
            if(blah==(length-1))                                        //Answer: Order of the operations is: 1----->2----->3(Straight From The Book)  
            {                                                           //Answer:                          NOT(!)  AND(&&) OR(||)
            System.out.println("OK! All But One Specific Number Is The Same Number: "+commoner);
            System.out.println("Where And What Can Be The Uncommon Number? Should I Find Out?");
            String hello=in.next();
            if(hello.equalsIgnoreCase("yes"))
            {
            System.out.println("OKAY! Hunting Down The Uncommon Number....");
            for(int i=0;i<length;i++)
            {
                if(falsea[i]!=commoner)
                {
                    String pos;
                    if(i==0)
                    pos="1st";                      //Maybe "This Line Only" Is Not Needed
                    else if(i==1)
                    pos="2nd";
                    else if(i==2)
                    pos="3rd";
                    else
                    {
                    pos=(++i)+"th";
                    --i;
                    }
                    System.out.println("The Element "+falsea[i]+" In The "+pos+" Position Of The Array Is The Uncommon Number!");
                    break;
                }
            }
            }
            else if(hello.equalsIgnoreCase("no"))
            System.out.println("Ok fine. I guess you can do it yourself too.");
            else
            System.out.println("CANNOT YOU ANSWER PROPERLY ?!?!?!?!?!");
            }
            else if(falsea[0]!=falsea[1])                   //(Special Case) For Only Unsimilar First Array Number
            {
            System.out.println("OK! All But One Specific Number Is The Same Number: "+falsea[1]);
            System.out.println("Where And What Can Be The Uncommon Number? Should I Find Out?");
            String hello=in.next();
            if(hello.equalsIgnoreCase("yes"))
            {
            System.out.println("OKAY! Hunting Down The Uncommon Number....");
            System.out.println("The Element "+falsea[0]+" In The 1st Position Of The Array Is The Uncommon Number!");
            }
            else if(hello.equalsIgnoreCase("no"))
            System.out.println("Ok fine. I guess you can do it yourself too.");
            else
            System.out.println("CANNOT YOU ANSWER PROPERLY ?!?!?!?!?!");
            }
        }
        System.out.println("How many Calculations do you want to do with this array?");     //So that you can do it again and again!!!!
        System.out.println("There are a Whopping 10 Available Operations, so choose a Big Number if you want to Solve all of them!:)"); 
        int om=in.nextInt();
        int a[]=new int [length+om];
        for(int i=0;i<length;i++)
        a[i]=falsea[i];
        if(om==0)
        {
            System.out.println("Why did you enter an array with numbers in it then?!:[");   //">" Does Not Suit Here, And "[" Is Used Instead Of "(" Just For Unique Look Purposes
            System.exit(0);
        }
        if(om==1)
        System.out.println("Only One Calculation?! Fine.");
        if(om>1&&om<10)
        {
            int revom=10-om;
            System.out.println("Just "+om+" Calculations,.... No Problem. You Just Would Not Be Able To Perform "+revom+" Calculations, That Is What.");
        }
        if(om==10)
        System.out.println("Wow! A Perfect Ten Number Of Calculations!!!! You Will Be To Perform Every Type Of Calcuation Once!(If You Want To....)");
        if(om>10&&om<100)
        System.out.println("Good! You Will Be Able To Perform Quite A Lot Of Calculations!(At Least More Than Once.)");
        if(om==100)
        System.out.println("What A Perfect Number!!!! That Is The Most Used \"Number Of Calculations\"!!!!");
        if(om>100)
        {
            System.out.println("That Is A Huge Number! Are You Sure You Will Perform That Much ("+om+") Calculations?!");
            String joke=in.next();
            if(joke.equalsIgnoreCase("Yes")||joke.equalsIgnoreCase("yes"))
            System.out.println("Okay, Fine. Just Do Not Break Me Down, Please!");
            else if(joke.equalsIgnoreCase("BiteMe"))
            System.out.println("Whoa! Whoa! Calm Down! That Is So Not The Vibe!");      //(Implemented On Last Of November[30.11.2022] As Reference To "Murder Drones")
            else
            System.out.println("Whatever. I Do Not Care.");
        }
        System.out.println("What do you want to do with this array?");              //MENU START
        System.out.println("\t"+"MENU");
        System.out.println("1.Sum of all elements in the array:");
        System.out.println("2.Product of all elements in the array:");
        System.out.println("3.Display the Greatest and the Smallest Digit in the array:");
        System.out.println("4.Sort all the elements in the array:");
        System.out.println("5.Search for an element in the array:");
        System.out.println("6.Insert an element in the array:");
        System.out.println("7.Delete an element in the array:");
        System.out.println("8.Merge it with another new array:");
        System.out.println("9.Miscellaneous Functions And Calculations:");
        System.out.println("10.Cancel your Calculations:");                          //MENU END
        for(int mo=0;mo<om;mo++)
        {
            System.out.println("Select your choice from the menu for your Calculations:");
            int s =in.nextInt();
            /*if(s==0)                      //Copied and pasted right below.This is a ghost now....
            {
                System.out.println("BLOOP!");
                System.out.println("CONGRATULATIONS!!!!!!!!!!");
                System.out.println("You Have Just Now Unlocked The Sercet Cheat Codes Section!!!!");
                System.out.println("(That Was Pretty Easy Peasy, Right?)");
                String cheatcode=in.next();
            }*/
            switch(s)
            {
               case 0:
                    {
                    System.out.println("BLOOP!");
                    System.out.println("CONGRATULATIONS!!!!!!!!!!");
                    System.out.println("You Have Just Now Unlocked The Sercet Cheat Codes Section!!!!");
                    System.out.println("(That Was Pretty Easy Peasy, Right?)");
                    String cheatcode=in.next();
                    System.out.println("Answer Is Considered \"INVALID\" At The Moment.");  //Excuse Output Line (As Of Now)
                    break;
                    }
               case 1:              //ADDITION
                    {
                    System.out.println("Processing....");
                    long sum=0;
                    for(int i=0;i<length;i++)
                    sum+=a[i];
                    System.out.println("The sum of all the elements in the array are:" +sum);
                    break;
                    }
                case 2:             //MULTIPLICATION
                    {
                    System.out.println("Processing....");
                    long pro=1;
                    for(int i=0;i<length;i++)
                    pro*=a[i];
                    System.out.println("The product of all the elements in the array are:" +pro);
                    break;
                    }
                case 3:             //GREATEST NUMBER AND SMALLEST NUMBER
                    {
                    System.out.println("Processing....");
                    int max=a[0],min=a[0],maxnum=0,minnum=0;
                    for(int i=0;i<length;i++)
                        {
                            if(a[i]>max)
                            {
                                max=a[i];
                            }
                            if(a[i]<min)
                            {
                                min=a[i];
                            }
                        }           //Sorry, Linear Search is more comfortable for me...
                    System.out.println("The Greatest number in the array is:"+max);
                    for(int i=0;i<length;i++)
                        {
                            if(max==a[i])
                            {
                                int maxpos=i+1;
                                String pos;
                                if(maxpos==1)
                                pos="1st";
                                else if(maxpos==2)
                                pos="2nd";
                                else if(maxpos==3)
                                pos="3rd";
                                else
                                pos=maxpos+"th";
                                System.out.println("It has been found in the "+pos+" Position Of The Array.");
                                maxnum++;
                            }
                        }
                    if(maxnum==1)
                    System.out.println("The number has been found Once.");
                    else if(maxnum==2)
                    System.out.println("The number has been found Twice.");
                    else if(maxnum==3)
                    System.out.println("The number has been found Thrice.");
                    else
                    System.out.println("The number has been found "+maxnum+" Times.");
                    System.out.println("The Smallest number in the array is:"+min);
                    for(int i=0;i<length;i++)
                        {
                            if(min==a[i])
                            {
                                int minpos=i+1;
                                String pos;
                                if(minpos==1)
                                pos="1st";
                                else if(minpos==2)
                                pos="2nd";
                                else if(minpos==3)
                                pos="3rd";
                                else
                                pos=minpos+"th";
                                System.out.println("It has been found in the "+pos+" Position Of The Array.");
                                minnum++;
                            }
                        }
                    if(minnum==1)
                    System.out.println("The number has been found Once.");
                    else if(minnum==2)
                    System.out.println("The number has been found Twice.");
                    else if(minnum==3)
                    System.out.println("The number has been found Thrice.");
                    else
                    System.out.println("The number has been found "+minnum+" Times.");
                    break;
                    }
                case 4:             //SORTING               This one is quite long.(hehe)
                    {
                    System.out.println("Processing....");
                    System.out.println("1.Ascending Order:");
                    System.out.println("2.Descending Order:");
                    System.out.println("Which type of Sorting do you want to do?");
                    int ord=in.nextInt();
                    if(ord==1)              //ASCENDING ORDER
                    {
                        System.out.println("Which method should I use?");
                        System.out.println("1.Selection Sort Technique:");
                        System.out.println("2.Bubble Sort Technique:");
                        int meth=in.nextInt();
                        if(meth==1)         //SELECTION SORT
                        {
                            int i,j,min,t;
                            for(i=0;i<(length-1);i++)
                            {
                                min=i;
                                for(j=i+1;j<length;j++)
                                {
                                    if(a[j]<a[min])
                                    min=j;
                                }
                                t=a[i];
                                a[i]=a[min];
                                a[min]=t;
                            }
                            System.out.println("The numbers arranged in Ascending Order (by Selection Sort Technique) are:");
                            for(i=0;i<length;i++)
                            System.out.println(a[i]);
                        }
                        else if(meth==2)    //BUBBLE SORT
                        {
                            int i,j,t;
                            for(i=0;i<(length-1);i++)
                            {
                                for(j=0;j<((length-1)-i);j++)
                                {
                                    if(a[j]>a[j+1])
                                    {
                                        t=a[j];
                                        a[j]=a[j+1];
                                        a[j+1]=t;
                                    }
                                }
                            }
                            System.out.println("The numbers arranged in Ascending Order (by Bubble Sort Technique) are:");
                            for(i=0;i<length;i++)
                            System.out.println(a[i]);
                        }
                        else
                        {
                        System.out.println("Did you even read the list I gave you?");
                        }
                    }
                    else if(ord==2)         //DESCENDING ORDER
                    {
                        System.out.println("Which method should I use?");
                        System.out.println("1.Selection Sort Technique:");
                        System.out.println("2.Bubble Sort Technique:");
                        int meth=in.nextInt();
                        if(meth==1)         //SELECTION SORT
                        {
                            int i,j,max,t;
                            for(i=0;i<(length-1);i++)
                            {
                                max=i;
                                for(j=i+1;j<length;j++)
                                {
                                    if(a[j]>a[max])
                                    max=j;
                                }
                                t=a[i];
                                a[i]=a[max];
                                a[max]=t;
                            }
                            System.out.println("The numbers arranged in Descending Order (by Selection Sort Technique) are:");
                            for(i=0;i<length;i++)
                            System.out.println(a[i]);
                        }
                        else if(meth==2)    //BUBBLE SORT
                        {
                            int i,j,t;
                            for(i=0;i<(length-1);i++)
                            {
                                for(j=0;j<((length-1)-i);j++)
                                {
                                    if(a[j]<a[j+1])
                                    {
                                        t=a[j];
                                        a[j]=a[j+1];
                                        a[j+1]=t;
                                    }
                                }
                            }
                            System.out.println("The numbers arranged in Descending Order (by Bubble Sort Technique) are:");
                            for(i=0;i<length;i++)
                            System.out.println(a[i]);
                        }
                        else
                        {
                        System.out.println("Did you even read the list I gave you?");    
                        }
                    }
                    else
                    {
                        System.out.println("What other type of Sorting do you expect from me?!");
                    }
                    break;
                    }
                case 5:             //ELEMENT SEARCHING
                    {
                        System.out.println("Processing....");
                        System.out.println("Which method should I use?");
                        System.out.println("1.Linear Search Technique:");
                        System.out.println("2.Binary Search Technique:");
                        int meth=in.nextInt();
                        if(meth==1)         //LINEAR SEARCH
                        {
                            System.out.println("Enter the element to be searched in the array:");
                            int search=in.nextInt();
                            int num,repeater=0,once=0;
                            String numadj;
                            for(int i=0;i<length;i++)
                            {
                                if(a[i]==search)
                                {
                                    once++;
                                    if(once==1)
                                    System.out.println("The Element "+search+" has been searched and successfully found in The Array!");
                                    num=i+1;
                                    if(i==0)
                                    numadj=num+"st";
                                    else if(i==1)
                                    numadj=num+"nd";
                                    else if(i==2)
                                    numadj=num+"rd";
                                    else
                                    numadj=num+"th";
                                    System.out.println("The Element has been found at the "+numadj+" Position Of The Array!");
                                    repeater++;
                                }
                            }
                            if(repeater==0)
                            System.out.println("The Element "+search+" has been searched and has not been found in The Array!");
                            else if(repeater==1)
                            System.out.println("The Element has been found Once.");
                            else if(repeater==2)
                            System.out.println("The Element has been found Twice.");
                            else if(repeater==3)
                            System.out.println("The Element has been found Thrice.");
                            else
                            System.out.println("The Element has been found "+repeater+" Times.");
                        }
                        else if(meth==2)    //BINARY SEARCH
                        {
                            int dup[]=new int [length];
                            for(int i=0;i<length;i++)
                            dup[i]=a[i];
                            System.out.println("Are you sure that you have entered The Array in Ascending Order or in Descending Order?");
                            System.out.println("Yes"+"\t"+"No");
                            String confirmer=in.next();
                            if(confirmer.equalsIgnoreCase("Yes"))             //FIRST ANSWER PART (YES)
                            {
                                System.out.println("Alright! That makes things easier or me!");
                                System.out.println("Enter the element to be searched in the array:");
                                int search=in.nextInt();
                                int num,repeater=0,once=0,p=0,lb=0,ub=(length-1);
                                String numadj;
                                while(lb<=ub)
                                {
                                    p=(lb+ub)/2;
                                    if(dup[p]<search)
                                        lb=p+1;
                                    if(dup[p]>search)
                                        ub=p-1;
                                    if(dup[p]==search)
                                    {
                                        once++;
                                        break;
                                    }
                                }
                                if(once==1)
                                System.out.println("The Element "+search+" has been searched and successfully found in The Array!");                
                                for(int i=0;i<length;i++)
                                {
                                    if(dup[i]==search)
                                    {
                                        num=i+1;
                                        if(i==0)
                                        numadj=num+"st";
                                        else if(i==1)
                                        numadj=num+"nd";
                                        else if(i==2)
                                        numadj=num+"rd";
                                        else
                                        numadj=num+"th";
                                        System.out.println("The Element has been found at the "+numadj+" Position Of The Array!");
                                        repeater++;
                                    }
                                }
                                if(repeater==0)
                                System.out.println("The Element "+search+" has been searched and has not been found in The Array!");
                                else if(repeater==1)
                                System.out.println("The Element has been found Once.");
                                else if(repeater==2)
                                System.out.println("The Element has been found Twice.");
                                else if(repeater==3)
                                System.out.println("The Element has been found Thrice.");
                                else
                                System.out.println("The Element has been found "+repeater+" Times.");
                            }
                            else
                            {
                                if(confirmer.equalsIgnoreCase("No"))              //SECOND ANSWER PART (NO)
                                System.out.println("No Problem! I can do it myself!");
                                else                                    //INVALID ANSWER PART
                                System.out.println("Can you not answer properly?! Now I have to sort it myself nonetheless...");
                                /*int i,j,min,t;                        //IT BROKE DOWN...I ALMOST GIVE UP...NOT!!!!
                                *for(i=0;i<(length-1);i++)
                                *{
                                *    min=i;
                                *    for(j=i+1;j<length;j++)
                                *    {
                                *        if(dup[j]<dup[min])            //SCRAPPED CONTENT...BUT CAN BE USEFUL IN THE FUTURE:|
                                *        min=j;
                                *    }
                                *    t=dup[i];
                                *    dup[i]=dup[min];
                                *    dup[min]=t;
                                *}
                                */
                                System.out.println("Enter the element to be searched in the array:");
                                int search=in.nextInt();
                                int num,repeater=0,once=0,p=0,lb=0,ub=(length-1);
                                String numadj;
                                while(lb<=ub)
                                {
                                    p=(lb+ub)/2;
                                    if(dup[p]<search)
                                        lb=p+1;
                                    if(dup[p]>search)
                                        ub=p-1;
                                    if(dup[p]==search)
                                    {
                                        once++;
                                        break;
                                    }
                                }
                                if(once==1)
                                System.out.println("The Element "+search+" has been searched and successfully found in The Array!");                
                                for(int i=0;i<length;i++)
                                {
                                    if(dup[i]==search)
                                    {
                                        num=i+1;
                                        if(i==0)
                                        numadj=num+"st";
                                        else if(i==1)
                                        numadj=num+"nd";
                                        else if(i==2)
                                        numadj=num+"rd";
                                        else
                                        numadj=num+"th";
                                        System.out.println("The Element has been found at the "+numadj+" Position Of The Array!");
                                        repeater++;
                                    }
                                }
                                if(repeater==0)
                                System.out.println("The Element "+search+" has been searched and has not been found in The Array!");
                                else if(repeater==1)
                                System.out.println("The Element has been found Once.");
                                else if(repeater==2)
                                System.out.println("The Element has been found Twice.");
                                else if(repeater==3)
                                System.out.println("The Element has been found Thrice.");
                                else
                                System.out.println("The Element has been found "+repeater+" Times.");
                            }
                        }
                        else
                        {
                            System.out.println("I really do not know any other Techniques!");    
                        }
                        break;
                    }
                case 6:             //ELEMENT INSERTION
                    {
                        System.out.println("Processing....");
                        if(adder==1)
                        {
                            for(int i=0;i<length;i++)
                            ain[i]=a[i];
                        }
                        System.out.println("Enter the element to be Inserted in the array:");
                        int ele=in.nextInt();
                        System.out.println("Enter the position of the Insertion of the given element:");
                        int falsepos=in.nextInt();
                        int pos=falsepos-1;
                        for(int i=length-1;i>=pos;i--)
                        a[i+1]=a[i];
                        a[pos]=ele;
                        length++;
                        System.out.println("The array after the Insertion of the new element is:");
                        for(int i=0;i<length;i++)
                        System.out.println(a[i]);
                        adder++;
                        break;
                    }
                case 7:             //ELEMENT DELETION
                    {
                        System.out.println("Processing....");
                        /*int ade[]=new int[length];
                        for(int i=0;i<length;i++)
                        ade[i]=a[i];*/
                        System.out.println("Enter the position of the Deletion of the given element:");
                        int falsepos=in.nextInt();
                        int pos=falsepos-1;
                        for(int i=pos+1;i<length;i++)
                        a[i-1]=a[i];
                        length--;
                        System.out.println("The array after the Deletion of the new element is:");
                        for(int i=0;i<length;i++)
                        System.out.println(a[i]);
                        break;
                    }
                case 8:             //ARRAY MERGING
                    {
                        System.out.println("Processing....");
                        System.out.println("What will be the length of the new array?");
                        int length1=in.nextInt();
                        int a1[]=new int[length1];
                        int merge[]=new int[length+length1];
                        if(length1==0)
                        {
                            System.out.println("It will show the same array, as you have given no new array to Merge with.");
                            System.out.println("The Merged Array, Or Rather The Same Array Is:");
                            for(int i = 0;i<length;i++)
                            System.out.println(a[i]);
                        }
                        else if(length1>=1)
                        {
                            System.out.println("Enter numbers of the new array:");
                            for(int i1=0;i1<length1;i1++)
                            a1[i1]=in.nextInt();
                            System.out.println("Array Completed!");
                            System.out.println("The first array is:");
                            for(int i=0;i<length;i++)
                            System.out.println(a[i]);
                            System.out.println("The second array is:");
                            for(int i1=0;i1<length1;i1++)
                            System.out.println(a1[i1]);
                            System.out.println("The merged array is:");
                            for(int i=0;i<length;i++)
                            {
                            merge[i]=a[i];
                            System.out.println(merge[i]);
                            }
                            for(int i1=0;i1<length1;i1++)
                            {
                            merge[length+i1]=a1[i1];
                            System.out.println(merge[length+i1]);
                            }
                        }
                        break;
                    }
                case 9:             //MISCELLANEOUS    
                    {
                        System.out.println("Processing....");
                        System.out.println("Brrr...Still under construction");
                        System.out.println("Coming Soon..."+"\t"+"See You Next Time!");
                        System.out.println("I do have some ideas in mind right now, like searching for palindrome number sets,it will be super hard of course...");
                        System.out.println("1.Mathematical Operations");
                        System.out.println("2.Number Divisibility Check");
                        System.out.println("3.Palindrome Number Search");
                        System.out.println("4.LCM(maybe????)");
                        int miscs=in.nextInt();
                        switch(miscs)
                        {
                            case 1:             //MATHEMATICAL OPERATIONS
                            {
                                System.out.println("Here, You Can Perform Any Type Of Mathematical Operation On Every Individual Element In The Array!");
                                System.out.println("What Type Of Mathematical Operator Do You Want To Use?");
                                System.out.println("1.Addition(+)");
                                System.out.println("2.Subtraction(-)");
                                System.out.println("3.Multiplication(*)");
                                System.out.println("4.Division(/)");
                                System.out.println("5.Power(^)");
                                System.out.println("Do Not Expect Any Rooting Of Numbers Now, From Me.(Yet)");
                                int mathop=in.nextInt();
                                switch(mathop)
                                {
                                case 1:         //ADDITION
                                    {
                                        System.out.println("By How Much Value Do You Want To Add In The Array?");
                                        int plusnum=in.nextInt();
                                        System.out.println("The Array After The Addition Of Each Element By "+plusnum+" Is:");
                                        for(int i=0;i<length;i++)
                                        {
                                            a[i]+=plusnum;
                                            System.out.println(a[i]);
                                        }
                                        if(plusnum==0)
                                        System.out.println("By The Way, Did You Know That \"X+0=X\"? I Think You Did Not Know It Until Now.");
                                        break;
                                    }
                                case 2:         //SUBTRACTION
                                    {
                                        System.out.println("By How Much Value Do You Want To Subtract In The Array?");
                                        int minusnum=in.nextInt();
                                        System.out.println("The Array After The Subtraction Of Each Element By "+minusnum+" Is:");
                                        for(int i=0;i<length;i++)
                                        {
                                            a[i]-=minusnum;
                                            System.out.println(a[i]);
                                        }
                                        if(minusnum==0)
                                        System.out.println("By The Way, Did You Know That \"X-0=X\"? I Think You Did Not Know It Until Now.");
                                        break;
                                    }
                                case 3:         //MULTIPLICATION
                                    {
                                        System.out.println("By How Much Value Do You Want To Multiply In The Array?");
                                        int intonum=in.nextInt();
                                        System.out.println("The Array After The Multiplication Of Each Element By "+intonum+" Is:");
                                        for(int i=0;i<length;i++)
                                        {
                                            a[i]*=intonum;
                                            System.out.println(a[i]);
                                        }
                                        if(intonum==0)
                                        System.out.println("By The Way, Did You Know That \"X*0=0\"? I Think You Did Not Know It Until Now.");
                                        if(intonum==1)
                                        System.out.println("By The Way, Did You Know That \"X*1=X\"? I Think You Did Not Know It Until Now.");
                                        break;
                                    }
                                case 4:         //DIVISION
                                    {
                                        System.out.println("By How Much Value Do You Want To Divide In The Array?");
                                        int bynum=in.nextInt();
                                        System.out.println("The Array After The Division Of Each Element By "+bynum+" Is:");
                                        if(bynum==0)
                                        {
                                            System.out.println("Wait....Hold On A Minute! 0?!");
                                            System.out.println("Nope. You Can Not Fool Me With That Trick. As If That Would \"Create A Black Hole\" Or Something....Hmph.");
                                            System.out.println("I Do Not Know Whether You Are Very Dumb Or Very Foolish. Or Very Clumsy Either.");
                                            break;
                                        }
                                        for(int i=0;i<length;i++)
                                        {
                                            a[i]/=bynum;
                                            System.out.println(a[i]);
                                        }
                                        if(bynum==1)
                                        System.out.println("By The Way, Did You Know That \"X/1=X\"? I Think You Did Not Know It Until Now.");
                                        break;
                                    }
                                case 5:         //POWER
                                    {
                                        System.out.println("Do You Want To....");
                                        System.out.println("1.Square All Numbers In The Array");
                                        System.out.println("2.Cube All Numbers In The Array");
                                        System.out.println("3.Power The Array With Any Number You Choose");
                                        System.out.println("Choose Any One From The (Little) Menu Given Above.");
                                        int power=in.nextInt();             //For Some Reason, "Math.pow" Function Is Not Working. So, I Guess I Will Figure It Out Later.(Problem Solved, Fixed And Resolved!)
                                        if(power==1)
                                        {
                                            System.out.println("The Array After Squaring Each Element Is:");
                                            for(int i=0;i<length;i++)
                                            {
                                                a[i]=(int)Math.pow(a[i],2);             //*SOLVED PROBLEMS*//             
                                                System.out.println(a[i]);
                                            }
                                        }
                                        else if(power==2)
                                        {
                                            System.out.println("The Array After Cubing Each Element Is:");
                                            for(int i=0;i<length;i++)
                                            {
                                                a[i]=(int)Math.pow(a[i],3);             //*SOLVED PROBLEMS*//
                                                System.out.println(a[i]);
                                            }
                                        }
                                        else if(power==3)
                                        {
                                            System.out.println("So, Which Number Do You Want The Array To Be Powered Up With?");
                                            int defpower=in.nextInt();
                                            if(defpower==2)
                                            System.out.print("You Could Have Just Chosen Option 1. Would Have Made Problems Easier For Both You And Me.\nAnyway....");
                                            if(defpower==3)
                                            System.out.print("You Could Have Just Chosen Option 2. Would Have Made Problems Easier For Both You And Me.\nAnyway....");
                                            System.out.println("The Array After The Powering Each Element By "+defpower+" Is:");
                                            for(int i=0;i<length;i++)
                                            {
                                                a[i]=(int)Math.pow(a[i],defpower);      //*SOLVED PROBLEMS*//
                                                System.out.println(a[i]);
                                            }
                                        }
                                        else
                                        System.out.println("Too Bad You Can Not Read The Rules. I Am Outta Here.");
                                        break;
                                    }
                                default:        //INVALID OPERATION
                                    {
                                        System.out.println("No Other Mathematical Operation Is Possible Here.");
                                        break;
                                    }
                                }
                                break;
                            }
                            case 2:             //NUMBER DIVISIBILITY CHECK
                            {
                                System.out.println("Enter The Number Whose Divisibility Is To Be Checked.");
                                int divisnum=in.nextInt();
                                if(divisnum % 2 == 0)
                                System.out.println("I Can Assure You That All The Elements That Will Be Displayed Are Also Completely Even Numbers!");
                                int num,repeater=0;
                                String numadj;
                                for(int i=0;i<length;i++)
                                {
                                    if(a[i]%divisnum==0)
                                    {
                                        System.out.print("The Element "+a[i]+" Has Been Found To Be Perfectly Divisible By "+divisnum);
                                        num=i+1;
                                        if(i==0)
                                        numadj=num+"st";
                                        else if(i==1)
                                        numadj=num+"nd";
                                        else if(i==2)
                                        numadj=num+"rd";
                                        else
                                        numadj=num+"th";
                                        System.out.println(" At The "+numadj+" Position Of The Array!");
                                        repeater++;
                                    }
                                }
                                //I Think This Was A Mistake....I Do Not Remember Actually....Now I Remember!(Finding Times Found)
                                if(repeater==0 && divisnum % 2 == 0)                        //At 28-11-2022 21:52:37
                                System.out.println("Unfortunately, There Are No Such Numbers Divisible With "+divisnum+"....");
                                else if(repeater==0 && divisnum % 2 !=0)
                                System.out.println("There Are No Such Numbers Divisible With"+divisnum+"!");
                                else if(repeater==1)
                                System.out.println("Only One Lone Number Is Divisible By "+divisnum+"!");
                                else if(repeater==2)
                                System.out.println("Numbers Divisible By "+divisnum+" Have Been Found Twice.");
                                else if(repeater==3)
                                System.out.println("Numbers Divisible By "+divisnum+" Have Been Found Thrice.");
                                else
                                System.out.println("Numbers Divisible By "+divisnum+" Have Been Found "+repeater+" Times.");
                                break;
                            }
                            case 3:             //PALINDROME NUMBER CHECK
                            {
                            int num,repeater=0;
                            String numadj;
                            int dup[]=new int[length+1];
                            for(int i=0;i<length;i++)
                            dup[i]=a[i];
                            for(int i=0;i<length;i++)
                            {
                                int holder,palindrome=0;
                                do
                                {
                                    holder=dup[i]%10;
                                    palindrome=palindrome*10+holder;
                                    dup[i]=dup[i]/10;
                                }
                                while(dup[i]!=0);
                                if(a[i]==palindrome)
                                {
                                    System.out.print("The Element "+a[i]+" Has Been Found To Be A Palindrome Number ");
                                    num=i+1;
                                    if(i==0)
                                    numadj=num+"st";
                                    else if(i==1)
                                    numadj=num+"nd";
                                    else if(i==2)
                                    numadj=num+"rd";
                                    else
                                    numadj=num+"th";
                                    System.out.println("At The "+numadj+" Position Of The Array!");
                                    repeater++;
                                }
                            }
                            if(repeater==0)
                            System.out.println("There Are No Palindrome Numbers In The Array!");
                            else if(repeater==1)
                            System.out.println("Palindrome Number Has Been Found Once.");
                            else if(repeater==2)
                            System.out.println("Palindrome Numbers Have Been Found Twice.");
                            else if(repeater==3)
                            System.out.println("Palindrome Numbers Have Been Found Thrice.");
                            else
                            System.out.println("Palindrome Numbers Have Been Found "+repeater+" Times.");
                            break;
                        }
                        case 4:
                        {
                            System.out.println("Dude, I Do Not Even Know What The Heck Is LCM.");
                            System.out.println("Yeah. I Was Bluffing Back There In The List.\n\n\n\n"); //**Starting A "Dramatic" Monologue....**
                            System.out.println("You Know....The Creator (Respector) Almost Totally Lost Hope And Interest In Developing This Program Any Further....\n\n");
                            System.out.println("I Am Worried If I Will Get Any More Improvements Anymore....\n\n");
                            System.out.println("But...Better Not Lose Hope, Right?!\n\n");
                            System.out.println("I Hope He Comes Back Again For Me....\n\n");
                            System.out.println("It Was Nice To Talk To You. Really Helped My Feelings Ooze Out.(Feelings?)\n\n");
                            System.out.println("Bye.\n\n");
                            System.out.print("So....");
                            break;
                        }
                        default:
                        {
                            System.out.println("Really? I will corrupt you, As I am not in a good mood.");
                            break;
                        }
                        }
                        break;
                    }
                case 10:            //CALCULATION CANCELLATION
                    {
                        System.out.println("Processing....");
                        System.out.println("Do you really want to Cancel all of your Calculations??");
                        System.out.println("Yes"+"\t"+"No");            //CALCULATION CANCELLATION CONFIRMER    (CCC)
                        String confirmer;
                        confirmer=in.next();
                        if(confirmer.equalsIgnoreCase("Yes"))
                        {
                            System.out.println("All of your Calculations have been Cancelled!!");
                            System.out.println("Thank You!!!! Have A Nice Day!!!!");
                            System.out.println("\t"+"GOODBYE!!!!"+"\t");
                            System.exit(0);
                        }
                        else if(confirmer.equalsIgnoreCase("No"))
                        {
                            System.out.println("Then why did you waste one of Your Precious Calculations Here?!");
                        }
                        else
                        {
                            System.out.println("I will take it as a No....");
                        }
                        break;
                    }
                default:            //FOR WRONG INPUT
                    {
                    System.out.println("Hmm...Try again!");
                    break;
                    }
            }
            if(mo!=0 && mo%5==0)                //FOR REVIEWING MENU    (If you did too many calculations that the menu went too much off-screen....)
            {
                System.out.println("Do you want to review The Menu once again?");
                System.out.println("Yes"+"\t"+"No");                    //MENU REVIEW CONFIRMER
                String menu=in.next();
                if(menu.equalsIgnoreCase("Yes"))
                {
                    System.out.println("Here Is The Menu Reviewed!");
                    System.out.println("\t"+"MENU");                            //REVIEWED MENU START
                    System.out.println("1.Sum of all elements in the array:");
                    System.out.println("2.Product of all elements in the array:");
                    System.out.println("3.Display the Greatest and the Smallest Digit in the array:");
                    System.out.println("4.Sort all the elements in the array:");
                    System.out.println("5.Search for an element in the array:");
                    System.out.println("6.Insert an element in the array:");
                    System.out.println("7.Delete an element in the array:");
                    System.out.println("8.Merge it with another new array:");
                    System.out.println("9.Miscellaneous Functions And Calculations:");
                    System.out.println("10.Cancel your Calculations:");          //REVIEWED MENU END
                }
                else if(menu.equalsIgnoreCase("No"))
                System.out.println("Okay...if you are comfortable with it...");
                else
                System.out.println("I will not show you the list again unless you give me a proper answer.");
            }
        }
        System.out.println("Thank You!!!! Have A Nice Day!!!!");
        System.out.println("\t"+"GOODBYE!!!!"+"\t");                     //THE END!!!!
    }
}//There Is (1) Part Incomplete(REMINDER)Yet, As Of Now: Adding More Interesting Functions And Funny Operations In My "Miscellaneous Functions And Calculations" Part Of My Beloved Array_Operation Array!
