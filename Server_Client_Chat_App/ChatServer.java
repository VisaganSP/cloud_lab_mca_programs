import java.io.*;
import java.net.*;

public class ChatServer {
    public static void main(String[] args) {
        try {
            // Server socket on port 12345
            ServerSocket serverSocket = new ServerSocket(12345);
            System.out.println("Server is running... Waiting for a client.");

            // Accept client connection
            Socket socket = serverSocket.accept();
            System.out.println("Client connected: " + socket.getInetAddress().getHostAddress());

            // Create input and output streams
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // Chat loop
            BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
            String clientMessage, serverMessage;

            while (true) {
                // Receive message from client
                clientMessage = in.readLine();
                if (clientMessage.equalsIgnoreCase("bye")) {
                    System.out.println("Client disconnected.");
                    break;
                }
                System.out.println("Client: " + clientMessage);

                // Send response to client
                System.out.print("Server: ");
                serverMessage = keyboard.readLine();
                out.println(serverMessage);
            }

            // Close connections
            socket.close();
            serverSocket.close();
        } catch (IOException e) {
            System.err.println("Server Error: " + e.getMessage());
        }
    }
}
