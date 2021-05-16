import java.util.*;
 
public class Solution {
    static String slurpStdin() {
        String input = "";
        Scanner scan = new Scanner(System.in);
 
        while (true) {
            input += scan.nextLine();
            if (scan.hasNextLine()) {
                input += "\n";
            } else {
                break;
            }
        }
 
        return input;
    }
 
    public static void main(String[] args) {
        String input = slurpStdin();
 
        System.out.println(Integer.parseInt(input) + 25);
    }
}