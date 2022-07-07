import java.awt.*;

class TestFrame extends Frame {
	TestFrame(String title) {
		// super();
		setTitle(title);
		setSize(420, 420);
		Label l1 = new Label("Hello World!!");
		l1.setAlignment(Label.CENTER);
		add(l1);
		setVisible(true);
	}
}

public class HelloWorldFrame {
	public static void main(String[] args) {
		TestFrame f1 = new TestFrame("TestFrame.java");
	}
}