import java.awt.*;
import java.awt.event.*;

public class WindowListenerDemo extends Frame implements WindowListener {
	WindowListenerDemo() {
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		setIconImage(icon);
		setTitle("WindowListenerDemo.java");
		setSize(420, 420);
		addWindowListener(this);
		setVisible(true);
	}

	public void windowOpened(WindowEvent we) {
		System.out.println("Window Opened");
	}
	public void windowClosing(WindowEvent we) {
		System.out.println("Window Closing");
		System.exit(0);
	}
	public void windowClosed(WindowEvent we) {
		System.out.println("Window Closed");
	}
	public void windowIconified(WindowEvent we) {
		System.out.println("Window Iconified");
	}
	public void windowDeiconified(WindowEvent we) {
		System.out.println("Window Deiconified");
	}
	public void windowActivated(WindowEvent we) {
		System.out.println("Window Activated");
	}
	public void windowDeactivated(WindowEvent we) {
		System.out.println("Window Deactivated");
	}

	public static void main(String[] args) {
		new WindowListenerDemo();	
	}
}