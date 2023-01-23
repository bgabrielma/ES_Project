import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpClient.Version;
import java.net.http.HttpRequest.BodyPublishers;
import java.net.http.HttpResponse.BodyHandlers;

public class HelloWorld {
    public static String DEFAULT_URL = "http://85.245.94.213:7777/login";
    public static void main(String[] args) {
        System.out.println("Hello World!");

        String inputJson = "{ \"username\":\"\", \"password\":\"\" }";
        
        try {
            HttpRequest request =  HttpRequest.newBuilder()
                .version(Version.HTTP_1_1)
                .uri(URI.create(DEFAULT_URL))
                .header("Content-Type", "application/json")
                .POST(BodyPublishers.ofString(inputJson))
                .build();

            HttpClient client = HttpClient.newHttpClient();
            HttpResponse response = client.send(request, BodyHandlers.ofString());

            System.out.println(response.statusCode());
            System.out.println(response.body());
        }
        catch(Exception error) {
            System.out.println("Error on request " + error.getMessage());
        }
    }
}
