import java.net.*;
import java.io.*;
public class FilePOC
{
      public static void main(String[] args) throws Exception{

	    URL url = new URL("file://127.0.0.1:21/file");
	    System.out.println(url.getProtocol());


	    StringBuilder stringBuilder = new StringBuilder();

	    DataInputStream dis = new DataInputStream(url.openConnection().getInputStream());
            String inputLine;

            while ((inputLine = dis.readLine()) != null) {
                System.out.println(inputLine);
            }
            dis.close();

	}
}
