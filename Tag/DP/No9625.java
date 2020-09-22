package tag.dp;

import java.util.Scanner;

public class No9625 {
	
	/**
	 	[DP] Bronze01 - 9625. BABBA 
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//입력받을 버튼 횟수
		int K = sc.nextInt();
		//A,B 갯수
		int A = 1;
		int B = 0;
		int cnt = 0;
		int tmp;
		
		//문제 풀이
		while(K!=cnt) {
			tmp = A;
			A = B;
			B += tmp;
			cnt++;
		}
		System.out.print(A+" "+B);
	}
}
