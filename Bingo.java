import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Bingo {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int numOfDatasets = Integer.parseInt(reader.readLine().trim());

        for (int i = 0; i < numOfDatasets; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine());

            int[] calledNumbers = new int[10];
            for (int j = 0; j < 10; j++) {
                calledNumbers[j] = Integer.parseInt(st.nextToken());
            }

            int[][] bingoCard = new int[5][5];
            for (int r = 0; r < 5; r++) {
                st = new StringTokenizer(reader.readLine());
                for (int c = 0; c < 5; c++) {
                    bingoCard[r][c] = Integer.parseInt(st.nextToken());
                }
            }

            boolean[][] bingoMark = new boolean[5][5];
            bingoMark[2][2] = true; // Center is marked as "free"

            // Mark the bingo card based on called numbers
            for (int num : calledNumbers) {
                for (int r = 0; r < 5; r++) {
                    for (int c = 0; c < 5; c++) {
                        if (bingoCard[r][c] == num) {
                            bingoMark[r][c] = true;
                        }
                    }
                }
            }

            // Check for a win
            boolean overallWin = checkWin(bingoMark);

            // Print the result
            System.out.println(overallWin ? "Yes" : "No");
        }

        reader.close();
    }

    // Method to check for winning conditions
    private static boolean checkWin(boolean[][] bingoMark) {
        // Check rows
        for (int r = 0; r < 5; r++) {
            if (allTrue(bingoMark[r])) {
                return true;
            }
        }

        // Check columns
        for (int c = 0; c < 5; c++) {
            boolean columnWin = true;
            for (int r = 0; r < 5; r++) {
                if (!bingoMark[r][c]) {
                    columnWin = false;
                    break;
                }
            }
            if (columnWin) {
                return true;
            }
        }

        // Check diagonal (top-left to bottom-right)
        boolean diagWin1 = true;
        for (int i = 0; i < 5; i++) {
            if (!bingoMark[i][i]) {
                diagWin1 = false;
                break;
            }
        }

        // Check diagonal (top-right to bottom-left)
        boolean diagWin2 = true;
        for (int i = 0; i < 5; i++) {
            if (!bingoMark[i][4 - i]) {
                diagWin2 = false;
                break;
            }
        }

        return diagWin1 || diagWin2;
    }

    // Helper method to check if all elements in a row/column are true
    private static boolean allTrue(boolean[] array) {
        for (boolean val : array) {
            if (!val) {
                return false;
            }
        }
        return true;
    }
}
