
public class CreditAccount extends BankAccount {

	double fees=0.15;
	
	CreditAccount(String name,String accType){
		this.cusName=name;
		this.accType=accType;
	}
	
	public void addFees() {
		// TODO Auto-generated method stub
		balance+=balance*fees;
	}
	
}
