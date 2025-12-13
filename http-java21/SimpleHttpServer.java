import com.sun.net.httpserver.HttpContext;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class SimpleHttpServer {
    private static final int listenPort = 8080;
    // Static variable to store startup duration for display in the browser
    private static long startupDuration = 0;
    public static void main(String[] args) throws IOException {
        long startTime = System.currentTimeMillis();
        HttpServer server = HttpServer.create(new InetSocketAddress(listenPort), 0);
        HttpContext context = server.createContext("/");
        context.setHandler(SimpleHttpServer::handleRequest);
        server.start();
        long endTime = System.currentTimeMillis();
        // Calculate duration and save it to the static variable
        startupDuration = endTime - startTime;
        // Display in server logs (visible via 'kraft cloud logs')
        System.out.println("------------------------------------------------");
        System.out.println(" [Log] Server started in " + startupDuration + " ms!");
        System.out.println(" Waiting for connections...");
        System.out.println("------------------------------------------------");
    }
    private static void handleRequest(HttpExchange exchange) throws IOException {
        // Combine the messages here:
        // 1. "Hello, World!"
        // 2. "\n" (new line)
        // 3. Startup time
        String response = "Hello, World!\n[Unikraft Speed] Boot time: " + startupDuration + " ms\n";
        exchange.sendResponseHeaders(200, response.getBytes().length);
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }
}
