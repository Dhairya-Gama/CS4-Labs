import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class SeatingArrangement {

   
    private static final int VIP_SEATS = 8;
    private static final int PREMIUM_SEATS = 12;
    private static final int REGULAR_SEATS = 25;

  
    private static List<String> vipSeats = new ArrayList<>();
    private static List<String> premiumSeats = new ArrayList<>();
    private static List<String> regularSeats = new ArrayList<>();

    public static void main(String[] args) {
       
        initializeSeats();

      
         try {
            Scanner scanner = new Scanner(new File("input.txt"));
           
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(" ");
                int groupSize = Integer.parseInt(parts[0]);
                String status = parts[1];

                assignSeats(groupSize, status);
            }

            scanner.close();
        } catch (FileNotFoundException e) {
           System.out.println("Input file not found.");
        }
    }

   
    private static void initializeSeats() {
        for (int i = 1; i <= VIP_SEATS; i++) {
            vipSeats.add("A" + i);
        }
        for (int i = 1; i <= PREMIUM_SEATS; i++) {
            premiumSeats.add("B" + i);
        }
        for (int i = 1; i <= REGULAR_SEATS; i++) {
            regularSeats.add("C" + i);
        }
    }

   
    private static void assignSeats(int groupSize, String status) {
        List<String> assignedSeats = new ArrayList<>();

        
        if (status.equals("VIP")) {
            assignedSeats.addAll(getSeats(vipSeats, groupSize));
            if (assignedSeats.size() < groupSize) {
                assignedSeats.addAll(getSeats(premiumSeats, groupSize - assignedSeats.size()));
            }
            if (assignedSeats.size() < groupSize) {
                assignedSeats.addAll(getSeats(regularSeats, groupSize - assignedSeats.size()));
            }
        } else if (status.equals("Premium")) {
            assignedSeats.addAll(getSeats(premiumSeats, groupSize));
            if (assignedSeats.size() < groupSize) {
                assignedSeats.addAll(getSeats(regularSeats, groupSize - assignedSeats.size()));
            }
        } else if (status.equals("Regular")) {
            assignedSeats.addAll(getSeats(regularSeats, groupSize));
        }

      
        if (assignedSeats.size() == groupSize) {
            System.out.println(String.join(" ", assignedSeats));
        } else {
            System.out.println("not enough seats");
        }
    }

   
    private static List<String> getSeats(List<String> sectionSeats, int groupSize) {
        List<String> result = new ArrayList<>();
        if (sectionSeats.size() >= groupSize) {
            result = new ArrayList<>(sectionSeats.subList(0, groupSize));
            sectionSeats.subList(0, groupSize).clear();
        } else if (!sectionSeats.isEmpty()) {
            result = new ArrayList<>(sectionSeats);
            sectionSeats.clear();
        }
        return result;
    }
}
