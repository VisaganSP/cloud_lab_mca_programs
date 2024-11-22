import java.io.*;
import java.net.*;

public class ChatClient {
    public static void main(String[] args) {
        try {
            // Replace with Windows Host IP
            String serverIP = "192.168.x.x"; // Update this with your Windows Host's IP
            Socket socket = new Socket(serverIP, 12345);
            System.out.println("Connected to the server: " + serverIP);

            // Create input and output streams
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // Chat loop
            BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
            String clientMessage, serverMessage;

            while (true) {
                // Send message to server
                System.out.print("Client: ");
                clientMessage = keyboard.readLine();
                out.println(clientMessage);

                if (clientMessage.equalsIgnoreCase("bye")) {
                    System.out.println("Disconnected from the server.");
                    break;
                }

                // Receive message from server
                serverMessage = in.readLine();
                System.out.println("Server: " + serverMessage);
            }

            // Close connection
            socket.close();
        } catch (IOException e) {
            System.err.println("Client Error: " + e.getMessage());
        }
    }
}
