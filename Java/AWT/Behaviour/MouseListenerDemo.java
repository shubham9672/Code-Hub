import java.awt.*;
import java.awt.event.*;

public class MouseListenerDemo extends Frame implements MouseListener {
	MouseListenerDemo() {
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		setIconImage(icon);
		setTitle("MouseListenerDemo.java");
		setSize(420, 420);
		addMouseListener(this);
		setVisible(true);
	}

	public void mouseEntered(MouseEvent me) {
		System.out.println("Mouse Entered");
	}
	public void mousePressed(MouseEvent me) {
		System.out.println("Mouse Pressed");
	}
	public void mouseReleased(MouseEvent me) {
		System.out.println("Mouse Released");
	}
	public void mouseClicked(MouseEvent me) {
		System.out.println("Mouse Clicked");
	}
	public void mouseExited(MouseEvent me) {
		System.out.println("Mouse Exited");
	}

	public static void main(String[] args) {
		new MouseListenerDemo();
	}
}