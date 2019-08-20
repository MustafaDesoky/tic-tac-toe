public abstract class BankAccount {
	
	public double balance;
	private int accNo;
	public String cusName;
	public String accType;
	
	BankAccount(){
		
	}
	
	
	public void setAccNo(int accNo) {
		this.accNo=accNo;
	}
	public int getAccountNom() {
		return accNo;
	}
	
	
	public abstract void addFees();
	
	public void deposit(double amount) {
		if(amount<=0) {
			System.out.println("Amount should be positive :-D ");
		}
		else
		{
			balance+=amount;
		}
	}
	
	
	public void withdraw(double amount) {
		if(amount<=0) {
			System.out.println("Amount should be positive to withdraw ");
		}
		else if(balance<amount){
			System.out.println("you dont have that amount of money");
		}
		else {
			balance-=amount;
		}
	}
	
	
	
	void transfer( int ToAccNumber,double amount, BankAccount reciever )
	{
		if(this.balance>=amount) {
		this.balance-=amount;
		reciever.balance+=amount;
		}else {
			System.out.println("Sorry you dont have that amount of money . :-)");
		}
	}
	
	public void getDetails() {
		System.out.println("Account Number : " + this.accNo 
							+ "\nCustomer Name : "+ this.cusName 
							+"\nAccount Type : "+ this.accType
							+"\nBalance : "+this.balance);
	}
}
