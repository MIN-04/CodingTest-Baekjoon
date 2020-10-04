package tag.math;

import java.util.Scanner;

public class No1075 {

	/**
 		[Math] Bronze02 - 1075. 나누기
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int F = sc.nextInt();
		
		N = (N/100) * 100;
		
		while(true) {
			if(N%F == 0) break;
			N += 1;
		}
		
		String answer = Integer.toString(N%100);
		if(answer.length()<2) answer = "0"+answer;
		
		System.out.println(answer);
		
	}

}
