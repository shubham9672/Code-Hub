import java.awt.*;
import java.awt.event.*;

public class ActionListenerDemo extends Frame implements ActionListener {
	Button b;
	Label l;
	ActionListenerDemo() {
		b = new Button("Buttom");
		l = new Label("Click it!");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		setIconImage(icon);
		setTitle("ActionDemo.java");
		setSize(420, 420);
		setLayout(new FlowLayout(FlowLayout.CENTER));
		b.addActionListener(this);
		add(b);
		add(l);
		setVisible(true);
	}
	public void actionPerformed(ActionEvent ae) {
		l.setText("Clicked " + ae.getActionCommand());
	}
	public static void main(String[] args) {
		new ActionListenerDemo();
	}
}