/* 
<applet 
    code = "FirstApplet.class" 
    width = "420" 
    height = "420"
    
    alt = "Applet Here" 
    name = "FirstApplet" 
    align = "center"
>
<!--PARAMs to pass-->
</applet> 
*/

import java.applet.Applet;
import java.awt.*;

public class FirstApplet extends Applet{
    // public void init(){}
    public void paint(Graphics g) {
        g.drawString("Hello World", 10, 10);
    }
}

// code: Name of applet class file.
// width: Width of applet.
// height: Height of applet.
// codebase: Directory path for applet code eg:'/Applets'.
// alt: Text to show if applet failed to load.
// name: Name of applet.
// align: Setting alignment of the applet.
