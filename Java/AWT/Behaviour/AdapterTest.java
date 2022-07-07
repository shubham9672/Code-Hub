import java.awt.*;
import java.awt.event.*;

public class AdapterTest extends MouseAdapter {
	AdapterTest() {
		Frame frame = new Frame();
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		frame.setTitle("AdapterTest.java");
		frame.setSize(420, 420);
		frame.addMouseListener(this);
		frame.setVisible(true);
	}

	public void mouseClicked(MouseEvent me) {
		System.out.println("Mouse Clicked");
	}
	
	public static void main(String[] args) {
		new AdapterTest();
	}
}