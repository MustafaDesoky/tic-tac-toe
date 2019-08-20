import java.util.Scanner;

public class BankingSystem {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		Bank myBank = new Bank();

		int user_choice ;

		do {

			System.out.println();
			System.out.println("enter(1) To open a new bank account");
			System.out.println("enter(2) To deposit to a bank account");
			System.out.println("enter(3) To Withdraw to bank account");
			System.out.println("enter(4) To Print short account information");
			System.out.println("enter(5) To Transfer balance");
			System.out.println("enter(6) To Quit");
			user_choice = s.nextInt();
			switch (user_choice) {
			case 1: System.out.print("Enter Your Name : ");
			s.nextLine();
			String name=s.nextLine();
			System.out.print("Enter Your Account Type :"
					+ "\nsaving "
					+ "\ncurrent "
					+ "\ncredit \n");
			String accType=s.nextLine();
			myBank.createNewAcc(accType, name);;
			break;

			case 2: System.out.println("Enter a account number");
			int an = s.nextInt();
			// to test if the account nom existed
			if (myBank.getUser(an)==null) {
				System.out.println("Account not found");
			}
			else {
				System.out.println("Enter a deposit amount");
				double da = s.nextDouble();
				myBank.depositTo(da, an);
				
			}
			break;

			case 3: System.out.println("Enter a account number");
			int acn = s.nextInt();
			if (myBank.getUser(acn)==null) {
				System.out.println("Account not found");
			}
			else {
				System.out.println("Enter a withdraw amount");
				double wa = s.nextDouble();
				myBank.withdrawFrom(wa, acn);
				
			}
			break;

			case 4: System.out.println("Enter a account number");
			int anum = s.nextInt();
			if (myBank.getUser(anum)==null) {
				System.out.println("Account not found");
			}
			else {
				myBank.accountDetails(anum);
			}
			
			break;

			case 5:System.out.println("Enter the account nom of sender");
			int Snum=s.nextInt();
			if (myBank.getUser(Snum)==null) {
				System.out.println("Sender account not found");
			}
			else {
				System.out.println("Enter the account nom of reciever");
				int Rnum=s.nextInt();
				if (myBank.getUser(Rnum)==null) {
					System.out.println("reciever account not found");
				}
				else {
					System.out.println("Enter amount of money");
					double amount=s.nextDouble();
					myBank.transferTo(Snum, Rnum, amount);
					}
			}
				
			break;

			default: System.out.println("Invalid option. Please try again.");

			}
		}

		while (user_choice !=6);

	}
}