import java.util.ArrayList;
import java.util.List;

public class SampleCode {
  
  public static void main(String[] args) {
    // Code Coverage
    printMessage("Hello, Codacy!");

    // Complexity
    int number = 10;
    System.out.println("Factorial of " + number + " is: " + factorial(number));

    // Security
    String username = "admin";
    String password = "password123";
    authenticateUser(username, password);

    // Performance
    long startTime = System.currentTimeMillis();
    performComplexCalculation();
    long endTime = System.currentTimeMillis();
    System.out.println("Execution time: " + (endTime - startTime) + " ms");

    // Compatibility
    List<String> list = new ArrayList<>();
    list.add("Item 1");
    list.add("Item 2");
    printList(list);

    // Error-Prone
    int[] numbers = {1, 2, 3};
    for (int i = 0; i <= numbers.length; i++) {
      System.out.println(numbers[i]);
    }
  }

  // Code Coverage
  public static void printMessage(String message) {
    if (message != null && !message.isEmpty()) {
      System.out.println(message);
    }
  }

  // Complexity
  public static int factorial(int n) {
    if (n == 0 || n == 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }

  // Security
  public static void authenticateUser(String username, String password) {
    if (username.equals("admin") && password.equals("secret")) {
      System.out.println("Authentication successful!");
    } else {
      System.out.println("Authentication failed!");
    }
  }

  // Performance
  public static void performComplexCalculation() {
    int result = 0;
    for (int i = 0; i < 1000000; i++) {
      result += i;
    }
  }

  // Compatibility
  public static void printList(List<String> list) {
    for (String item : list) {
      System.out.println(item);
    }
  }
}
