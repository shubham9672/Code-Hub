import java.awt.*;
import java.awt.event.*;

public class MouseMotionListenerDemo extends Frame implements MouseMotionListener {
	Label label;
	int x, y;
	
	MouseMotionListenerDemo() {
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		setIconImage(icon);
		setTitle("MouseMotionListenerDemo.java");
		setSize(420, 420);
		setLayout(new FlowLayout());
		label = new Label("(Coordinates)");
		add(label);
		addMouseMotionListener(this);
		setVisible(true);
	}

	public void mouseMoved(MouseEvent me) {
		x = me.getX();
		y = me.getY();
		label.setText("(" + x + ", " + y + ")");
	}
	public void mouseDragged(MouseEvent me) {} // Compulsory to override

	public static void main(String[] args) {
		new MouseMotionListenerDemo();	
	}
}