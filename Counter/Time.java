import java.awt.*;
import java.awt.event.*;
import javax.swing.event.*;
import javax.swing.*;

public class Time extends JFrame {

	private JButton button;
	private Timer timer;
	private JTextField tf;
	private JLabel label1,label2,bl;
	
	public Time() {
		
		super("Timer");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setSize(650,650);
		this.setLocationRelativeTo(null);
		this.setAlwaysOnTop(true);
		this.setLayout(null);
		this.setResizable(true);
		this.setBackground(getBackground());
		
		JPanel panel=new JPanel();
		
		label1=new JLabel("Enter Seconds");
		add(label1);
		tf=new JTextField(6);
		add(tf);
		button=new JButton("Timing?");
		add(button);
		label2=new JLabel("Waiting...");
		add(label2);
		label1.setBounds(10, 10, 100, 40);
		tf.setBounds(100, 20, 70, 25);
		button.setBounds(10, 46, 80, 30);
		label2.setBounds(98, 45, 60, 30);
		button.addActionListener(
				new ActionListener() {

					@Override
					public void actionPerformed(ActionEvent e) {
						// TODO Auto-generated method stub
						int count =(Integer.valueOf(tf.getText()));
						label2.setText(""+count);
						
						window w=new window(count);
						timer=new Timer(1000, w);
						timer.start();
					}
					
				}
				
				);
		panel.add(label1);panel.add(tf);panel.add(button);panel.add(label2);
		panel.setBounds(420, 100, 200, 50);
		add(panel);
				
	}
	
	
	private class window implements ActionListener{

		private int counter;
		public window(int counter) {
			this.counter=counter;
		}
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			counter--;
			if(counter>=1) {
				
				label2.setText("time left :"+counter);
				
			}else {
			label2.setText("Done!");
			timer.stop();
			bl=new JLabel();
			bl.setIcon(new ImageIcon(getClass().getResource("1366_768_31005316.jpg")));
			bl.setBounds(0, 0, 1080, 800);
			add(bl);
			Toolkit.getDefaultToolkit().beep();
			
		}
			}
		
	}

		
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		new Time().setVisible(true);
		
	}

}
