import java.util.Scanner;


public class Bank {

	private BankAccount[] accounts;
	private int noOfAccount;

	Bank(){
		accounts=new BankAccount[50];
		noOfAccount=0;
	}

	private Scanner input=new Scanner(System.in);

	public void createNewAcc(String accType, String name) 
	{
		BankAccount acc= null;
		switch (accType.toLowerCase()) {
		case "saving":acc=new SavingAccount(name,accType);
		acc.setAccNo(noOfAccount);
		break;
		case "current":acc=new CurrentAccount(name,accType);
		acc.setAccNo(noOfAccount);
		break;
		case "credit":acc=new CreditAccount(name,accType);
		acc.setAccNo(noOfAccount);
		break;
		default : System.out.println("make sure of ur account type .");
		break;
		}
		accounts[noOfAccount]=acc;
		noOfAccount++;
	}


	public void accountDetails( int accNom) {
		accounts[accNom].getDetails();		
	}



	void depositTo ( double amount, int accountNom)
	{
			BankAccount customer=getUser(accountNom);
			customer.deposit(amount);
	}

	void withdrawFrom( double amount, int accountNom)
	{

		if(noOfAccount>=accountNom) {
			BankAccount customer=getUser(accountNom);
			customer.withdraw(amount);
		}
		else {
			System.out.println("Account not found to withdraw");
		}
	}

	void transferTo(int FromAccNumber, int ToAccNumber,double amount )
	{
		

				BankAccount sender=getUser(FromAccNumber);
				BankAccount reciever=getUser(ToAccNumber);
				sender.transfer(ToAccNumber, amount, reciever);
	}

	public BankAccount getUser( int accNom )
	{
		for(int i=0;i<noOfAccount;i++) {
			if(accNom==accounts[i].getAccountNom()) {
				return accounts[i] ;
			}
		}
		return null;
	}

}
