package tag.greedy;

import java.util.Scanner;

public class No4796 {
	
	/**
	 	[Greedy] Silver05 - 4796. ķ�� 
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//test case
		int tc = 1;
		while(true) {
			//�ϼ� �Է�
			int L = sc.nextInt(); //��밡���� �ϼ�
			int P = sc.nextInt(); //ķ�� �ϼ�
			int V = sc.nextInt(); //�ް� �ϼ�
			
			if(L == 0) break;
			
			//��� �ϼ�
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
