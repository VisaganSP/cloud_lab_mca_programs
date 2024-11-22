import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            Adder adder = new AdderImpl();

            LocateRegistry.createRegistry(1099);

            Naming.rebind("rmi://localhost/AdderService", adder);

            System.out.println("Server is ready!...");
        } catch(Exception e) {
            System.out.println("Server error: " + e.getMessage());
            e.printStackTrace();
        }
    }    
}