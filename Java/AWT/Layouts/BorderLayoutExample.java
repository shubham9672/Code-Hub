import java.awt.*;

public class BorderLayoutExample {
	public static void main(String[] args) {
		Frame frame = new Frame("BorderLayoutExample.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		frame.setLayout(new BorderLayout(10, 5)); // Default in Frame class // hGap == vGap == 5
		frame.setSize(420, 420);
		frame.add(new Button("One"), BorderLayout.NORTH);
		frame.add(new Button("Two"), BorderLayout.EAST);
		frame.add(new Button("Three"), BorderLayout.WEST);
		frame.add(new Button("Four"), BorderLayout.SOUTH);
		frame.add(new Button("Five"), BorderLayout.CENTER);
		frame.add(new Button("Six"), BorderLayout.SOUTH);

		frame.setVisible(true);
	}
}