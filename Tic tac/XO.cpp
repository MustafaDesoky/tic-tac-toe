#include<iostream>
using namespace std;

char matrix[3][3]={'1','2','3','4','5','6','7','8','9'};
char player='X';

void printMatrix(){
		 system("cls");
	     for(int a=0;a<3;a++){
		     for(int b=0;b<3;b++){
		       cout<<matrix[a][b]<<"  ";
			   }
			   cout<<"\n";
			}
}

void play(){
	char pos;
	cout<<"CHOOSE your Position player -- "<<player<<" -- ";
	cin>>pos;
	for(int a=0;a<3;a++){
		     for(int b=0;b<3;b++){
		       if(matrix[a][b]==pos){
				   matrix[a][b]=player;
			     }
			   }
			}
			if(player=='X')
				player='O';
			else
				player='X';
}
		
		
char whoWin(){
		int xCounter=0;
		int oCounter=0;
		int counter=0;
		for(int a=0;a<3;a++){
		     for(int b=0;b<3;b++){
				 if(matrix[a][b]!='X' && matrix[a][b]!='O')
					 counter++;
				if(matrix[a][b]=='X')
					xCounter++;
				else if(matrix[a][b]=='O')
					oCounter++;
				if(xCounter==3||oCounter==3){
					return xCounter>oCounter ? 'X':'O';
				}
			}
			xCounter=0;
			oCounter=0;
		}
		for(int a=0;a<3;a++){
		     for(int b=0;b<3;b++){
				if(matrix[b][a]=='X')
					xCounter++;
				else if(matrix[b][a]=='O')
					oCounter++;
				if(Xcounter==3||oCounter==3){
					return xCounter>oCounter ? 'X':'O';
				}
			}
			xCounter=0;
			oCounter=0;
		}
		
		if(matrix[0][0]=='X' && matrix[1][1]=='X' && matrix[2][2]=='X')
			return 'X';
		else if(matrix[0][0]=='O' && matrix[1][1]=='O' && matrix[2][2]=='O')
			return 'O';
		else if(matrix[0][2]=='X' && matrix[1][1]=='X' && matrix[2][0]=='X')
			return 'X';
		else if(matrix[0][2]=='O' && matrix[1][1]=='O' && matrix[2][0]=='O')
			return 'O';
		
		if(counter == 0 )
			return 'Z';
		
		return '.';
	}            

	
		

int main (){
	
	while(whoWin()=='.'){
		printMatrix();
		play();
	}
	printMatrix();
	if(whoWin()=='Z'){
		cout<<"\nNo one win "<<endl;
	}
	else
		cout<<"\nThe winner is "<<whoWin()<<endl;
	
    system("pause");
	return 0;
			
	
}
