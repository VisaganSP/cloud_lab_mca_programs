import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            Adder adder = (Adder) Naming.lookup("rmi://localhost/AdderService");

            int result = adder.add(100, 20);
            System.out.println("Result of Addition: " + result);
        } catch (Exception e) {
            System.out.println("Client error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
