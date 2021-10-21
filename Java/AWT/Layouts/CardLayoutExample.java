import java.awt.*;
import java.awt.event.*;

public class CardLayoutExample implements ActionListener{
	Frame frame = new Frame("CardLayoutExample.java");
	CardLayout card = new CardLayout();
	CardLayoutExample() {
		frame.setLayout(card);
		frame.setSize(420, 420);
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		
		Button b1 = new Button("One");
		b1.addActionListener(this);
		frame.add(b1);

		Button b2 = new Button("Two");
		b2.addActionListener(this);
		frame.add(b2);

		Button b3 = new Button("Three");
		b3.addActionListener(this);
		frame.add(b3, "Three");

		Button b4 = new Button("Four");
		b4.addActionListener(this);
		frame.add(b4);

		Button b5 = new Button("Five");
		b5.addActionListener(this);
		frame.add(b5);

		card.show(frame, "Three"); // TODO: WTF does this do!?
		card.setHgap(5);
		System.out.println("card.getHgap() = " + card.getHgap());
		card.setVgap(5);
		System.out.println("card.getVgap() = " + card.getVgap());
		frame.setVisible(true);
	}
	public void actionPerformed(ActionEvent ae){
		// card.first(frame); // Method 1
		// card.last(frame); // Method 2
		card.next(frame); // Method 3
		// card.previous(frame); // Method 4
	}
	public static void main(String[] args) {
		CardLayoutExample cL = new CardLayoutExample();
	}
}