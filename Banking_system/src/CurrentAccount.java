
public class CurrentAccount extends BankAccount {

		double fees=0.10;
		
		CurrentAccount(String name,String accType){
			this.cusName=name;
			this.accType=accType;
		}
		
		public void addFees() {
			// TODO Auto-generated method stub
			balance+=balance*fees;
		}
		
}
