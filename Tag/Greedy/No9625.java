package tag.greedy;

import java.util.Scanner;

public class No9625 {
	
	/**
	 	[Greedy] Bronze03 - 5585. �Ž�����
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//�����ؾ��ϴ� ��
		int price = sc.nextInt();
		//�Ž����� �迭
		int[] money = {500,100,50,10,5,1};
		//�Ž�������� ��
		int change = 1000 - price;
		//�Ž����� ����
		int cnt = 0;
		
		for(int i=0; i<6; i++) {
			cnt += (change / money[i]);
			change %= money[i];
			if(change == 0) break;
		}
		
		System.out.print(cnt);
	}
}
