d="""
> How to change `workspace`?

files--> switch workspace

> How to reset window

windows--> Perspective--> Reset perspective

> How to create project?

File--> new--> other--> java project--> next--> `enter your project name`--> finish--> open perspective.

> How to add packages, inteface and class?

Right click on project--> New--> choose `class` or `packages` or `inteface`--> Enter `class` name--> mark check on `public static void main(String[] args)`--> finish.

> How to configure `OJDBC 14` `JAR` file for oracle database?

Right click on the project--> select `build path`--> click on `confifure build path`--> click on `library` tab--> click on `Add ectrenal JARs`--> choose `OJDBC 14`
	> Directory to find `JAR` file. `C:\oraclexe\app\oracle product\10.2.01\Server\jdbc\lib`

> How to register driver?

```java
import java.sql.*;

import oracle.jdbc.driver.*;

  

public class Test

{

    public static void main(String[] args)

    {

        System.out.println("Register Driver");

       
        String myLine="CREATE TABLE Student(Roll int)";

        DriverManager.registerDriver(new OracleDriver());

        System.out.println("Driver Registered");

        System.out.println("Establish connection");

        Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","system", "password");

        System.out.println("Connected successfully!");

        Statement st=con.createStatement();

        st.execute(myLine);

        System.out.println("Table created successufully!");

        con.close();

    }

}
```

"""

new=d.replace("-->",">")
fp=open("README.md","w")
for i in new:
    fp.write(i)
#print(new)
