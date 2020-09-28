package tag.greedy;

import java.util.Scanner;

public class No4796 {
	
	/**
	 	[Greedy] Silver05 - 4796. 캠핑 
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//test case
		int tc = 1;
		while(true) {
			//일수 입력
			int L = sc.nextInt(); //사용가능한 일수
			int P = sc.nextInt(); //캠핑 일수
			int V = sc.nextInt(); //휴가 일수
			
			if(L == 0) break;
			
			//결과 일수
			int result = 0;
			
			result = V/P * L ;
			if(V%P<L) {
				result += V%P;
			} else {
				result += L;
			}
			
			System.out.printf("Case %d: %d\n",tc,result);
			
			tc++;
		}
	}
}
