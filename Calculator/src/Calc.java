import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

public class Calc extends JFrame implements ActionListener{

	private JButton first,second,third,fourth,fifth,sixth,seventh,eighth,nighnth,zero,point,equal,plus,mul,div,sub,reset,delete;
	private JTextField tf;
	private JLabel imglabel;
	private ImageIcon img;
	private JMenuBar menubar;
	private JMenu menu;
	private JMenuItem menuitem,menuitem2;
	private String operation,answer;
	private double num1,num2,result;
    private JRadioButton on,off;
    private ButtonGroup group; 
	
	
	public Calc() {
		super("Calculator...");
		this.setSize(290,350);
		this.setResizable(false);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(null);
		
		menubar=new JMenuBar();
		menu=new JMenu("File");
		menuitem=new JMenuItem("Exit");
		menuitem2=new JMenuItem("Help");
		setJMenuBar(menubar);
		menubar.add(menu);
		menu.add(menuitem);
		menu.add(menuitem2);
		
		on=new JRadioButton("ON",true);
		off=new JRadioButton("OFF",false);
		on.setBounds(30, 63, 50, 13);
		off.setBounds(30, 78, 50, 13);
		group=new ButtonGroup();
		group.add(on);
		group.add(off);
		add(on);
		add(off);
		on.addActionListener(
				new ActionListener() {
					
					@Override
					public void actionPerformed(ActionEvent on) {
						// TODO Auto-generated method stub
						first.setEnabled(true);
						second.setEnabled(true);
						third.setEnabled(true);
						fourth.setEnabled(true);
						fifth.setEnabled(true);
						sixth.setEnabled(true);
						seventh.setEnabled(true);
						eighth.setEnabled(true);
						nighnth.setEnabled(true);
						zero.setEnabled(true);
						point.setEnabled(true);
						equal.setEnabled(true);
						plus.setEnabled(true);
						mul.setEnabled(true);
						div.setEnabled(true);
						sub.setEnabled(true);
						reset.setEnabled(true);
						delete.setEnabled(true);
						tf.setEnabled(true);
					}
				}
				);
		off.addItemListener(
				new ItemListener() {
					
					@Override
					public void itemStateChanged(ItemEvent off) {
						// TODO Auto-generated method stub
						first.setEnabled(false);
						second.setEnabled(false);
						third.setEnabled(false);
						fourth.setEnabled(false);
						fifth.setEnabled(false);
						sixth.setEnabled(false);
						seventh.setEnabled(false);
						eighth.setEnabled(false);
						nighnth.setEnabled(false);
						zero.setEnabled(false);
						point.setEnabled(false);
						equal.setEnabled(false);
						plus.setEnabled(false);
						mul.setEnabled(false);
						div.setEnabled(false);
						sub.setEnabled(false);
						reset.setEnabled(false);
						delete.setEnabled(false);
						tf.setEnabled(false);
					}
				}
				);
		
		tf=new JTextField(25);
		tf.setBackground(Color.WHITE);
		tf.setForeground(Color.BLACK);
		tf.setFont(new Font("Tahoma",Font.BOLD +Font.PLAIN,20));
		tf.setBounds(8, 18, 270, 40);
		add(tf);
		
		
		reset=new JButton("C");
		reset.setBounds(20, 100, 42, 20);
		add(reset);
		
		first=new JButton("1");
		first.setBounds(68, 98, 45, 25);
		add(first);
		second=new JButton("2");
		second.setBounds(117, 98, 45, 25);
		add(second);
		third=new JButton("3");
		third.setBounds(166, 98, 45, 25);
		add(third);
		plus=new JButton("+");
		plus.setBounds(215, 100, 42, 20);
		add(plus);
		
		delete=new JButton("<=");
		delete.setBounds(18, 129, 48, 20);
		add(delete);
		fourth=new JButton("4");
		fourth.setBounds(68, 126, 45, 25);
		add(fourth);
		fifth=new JButton("5");
		fifth.setBounds(117, 126, 45, 25);
		add(fifth);
		sixth=new JButton("6");
		sixth.setBounds(166, 126, 45, 25);
		add(sixth);
		sub=new JButton("-");
		sub.setBounds(215, 129, 42, 20);
		add(sub);
		
		seventh=new JButton("7");
		seventh.setBounds(68, 153, 45, 25);
		add(seventh);
		eighth=new JButton("8");
		eighth.setBounds(117, 153, 45, 25);
		add(eighth);
		nighnth=new JButton("9");
		nighnth.setBounds(166, 153, 45, 25);
		add(nighnth);
		mul=new JButton("*");
		mul.setBounds(215, 156, 42, 20);
		add(mul);
		
		point=new JButton(".");
		point.setBounds(68, 182, 45, 25);
		add(point);
		zero=new JButton("0");
		zero.setBounds(117, 182, 45, 25);
		add(zero);
		equal=new JButton("=");
		equal.setBounds(166, 182, 45, 25);
		add(equal);
		div=new JButton("/");
		div.setBounds(215, 185, 42, 20);
		add(div);
		
		img=new ImageIcon(getClass().getResource("1366_768_71037947.jpg"));
		imglabel=new JLabel(img);
		imglabel.setBounds( 0, 0, 290, 350);
		add(imglabel);

		
		/*   LISTENERS Operations   */
		
		plus.addActionListener(this);
		mul.addActionListener(this);
		div.addActionListener(this);
		sub.addActionListener(this);
		reset.addActionListener(this);
		delete.addActionListener(this);
		equal.addActionListener(this);
		
		/*   LISTENERS Numbers   */
		first.addActionListener(this);
		second.addActionListener(this);
		third.addActionListener(this);
		fourth.addActionListener(this);
		fifth.addActionListener(this);
		sixth.addActionListener(this);
        seventh.addActionListener(this);
        eighth.addActionListener(this);
        nighnth.addActionListener(this);
        zero.addActionListener(this);
		point.addActionListener(this);
		
		
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		// TODO Auto-generated method stub
		Object option=event.getSource();
		
	try {
		/*   LISTENERS Operations   */
		
		if(option.equals(plus)) {
			num1=Double.parseDouble(tf.getText());
			tf.setText("");
			operation="+";
//			tf.setText(tf.getText()+"+");
		}
		else if(option.equals(sub)) {
			num1=Double.parseDouble(tf.getText());
			tf.setText("");
			operation="-";
//			tf.setText(tf.getText()+"-");
		}
        else if(option.equals(mul)) {
        	num1=Double.parseDouble(tf.getText());
			tf.setText("");
			operation="*";
//        	tf.setText(tf.getText()+"*");
		}
        else if(option.equals(div)) {
        	num1=Double.parseDouble(tf.getText());
			tf.setText("");
			operation="/";
//        	tf.setText(tf.getText()+"/");
        }
        else if(option.equals(delete)) {
//        	int text_length=tf.getText().length();
//        	tf.setText(tf.getText().substring(0, text_length-1));
        	StringBuilder str=new StringBuilder(tf.getText());
        	str.deleteCharAt(tf.getText().length()-1);
        	tf.setText(str.toString());	
        }
        else if(option.equals(reset)) {
        	tf.setText(null);
        }
        else if(option.equals(equal)) {
        	num2=Double.parseDouble(tf.getText());
        	if(operation.equals("+")) {
        		result=num1+num2;
        		answer=String.format("%.2f",result);
        		tf.setText(answer);
        	}
        	else if(operation.equals("-")) {
        		result=num1-num2;
        		answer=String.format("%.2f",result);
        		tf.setText(answer);
        	}
        	else if(operation.equals("*")) {
        		result=num1*num2;
        		answer=String.format("%.2f",result);
        		tf.setText(answer);
        	}
        	else if(operation.equals("/")) {
        		if(num1==0) {
        			JOptionPane.showMessageDialog(null, "u cant divide by 0","Stupid Msg",JOptionPane.ERROR_MESSAGE);
        		}
        		result=num1/num2;
        		answer=String.format("%.2f",result);
        		tf.setText(answer);
        		}
        }
		
		/*   LISTENERS Numbers   */
		
		if(option.equals(first)) {
			tf.setText(tf.getText()+"1");
		}
		else if(option.equals(second)) {
			tf.setText(tf.getText()+"2");
		}
        else if(option.equals(third)) {
        	tf.setText(tf.getText()+"3");
		}
        else if(option.equals(fourth)) {
        	tf.setText(tf.getText()+"4");
        }
        else if(option.equals(fifth)) {
        	tf.setText(tf.getText()+"5");
        }
        else if(option.equals(sixth)) {
        	tf.setText(tf.getText()+"6");
        }
        else if(option.equals(seventh)) {
        	tf.setText(tf.getText()+"7");
        }
        else if(option.equals(eighth)) {
        	tf.setText(tf.getText()+"8");
        }
        else if(option.equals(nighnth)) {
        	tf.setText(tf.getText()+"9");
        }
        else if(option.equals(zero)) {
        	tf.setText(tf.getText()+"0");
        }
        else if(option.equals(point)) {
        	tf.setText(tf.getText()+".");
        }
	}
	catch(StringIndexOutOfBoundsException e) {
		JOptionPane.showMessageDialog(null, "There is nothing to Remove", "Msg", JOptionPane.ERROR_MESSAGE);	
	     }
	 catch(Exception ex) {
		System.out.println(ex);
	     }
	 }
}
