package tag.greedy;

import java.util.Scanner;

public class No2839 {
	
	/**
	 	[Greedy] Bronze01 - 2839. ���� ���
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//����� ���� ų�α׷�
		int N = sc.nextInt();
		//��� ���� ���� ����
		int cnt = 0;
		
		while(true) {
			if(N>0 && N%5!=0) {
				N -= 3;
				cnt++;
			}else if(N>0 && N%5==0) {
				cnt += (N/5);
				N %= 5;
			}else if(N<0){
				System.out.print(-1);
				break;
			}else {
				System.out.print(cnt);
				break;
			}
		}
	}
}
