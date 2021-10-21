import java.awt.*;
import java.awt.event.*;

public class KeyListenerDemo extends Frame implements KeyListener {
	TextField textField;
	
	KeyListenerDemo() {
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		setIconImage(icon);
		setTitle("KeyListenerDemo.java");
		setSize(420, 420);
		setLayout(new FlowLayout(FlowLayout.LEFT));
		textField = new TextField(25);
		textField.addKeyListener(this);
		add(textField);
		setVisible(true);
	}

	public void keyPressed(KeyEvent ke) {
		System.out.println("KeyPressed = " + ke.getKeyChar());
	}

	public void keyReleased(KeyEvent ke) {
		System.out.println("KeyReleased = " + ke.getKeyChar());
	}

	public void keyTyped(KeyEvent ke) {
		System.out.println("KeyTyped = " + ke.getKeyChar());
	}

	public static void main(String[] args) {
		new KeyListenerDemo();
	}
}