package tag.dp;

import java.util.Scanner;

public class No9625 {
	
	/**
	 	[DP] Bronze01 - 9625. BABBA 
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//�Է¹��� ��ư Ƚ��
		int K = sc.nextInt();
		//A,B ����
		int A = 1;
		int B = 0;
		int cnt = 0;
		int tmp;
		
		//���� Ǯ��
		while(K!=cnt) {
			tmp = A;
			A = B;
			B += tmp;
			cnt++;
		}
		System.out.print(A+" "+B);
	}
}
