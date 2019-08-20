
public class SavingAccount extends BankAccount{

	double fees=0.12;
	
	SavingAccount(String name, String accType){
		this.cusName=name;
		this.accType=accType;
		
	}
	
	
	public void addFees() {
		// TODO Auto-generated method stub
		balance+=balance*fees;
	}
	
	
}
