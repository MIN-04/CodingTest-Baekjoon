package tag.greedy;

import java.util.Scanner;

public class No15904 {
	
	/**
	 	[Greedy] Bronze01 - 15904. UCPC�� ������ �����ϱ�?
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//�Է¹��� ����
		String str = sc.nextLine();
		String[] arrStr = str.split("");
		//UCPC ī��Ʈ
		int cnt = 0;
		
		for(int i=0; i<arrStr.length; i++) {
			if(cnt == 0 && arrStr[i].equals("U")) {
				cnt++;
				continue;
			}
			if(cnt == 1 && arrStr[i].equals("C")) {
				cnt++;
				continue;
			}
			if(cnt == 2 && arrStr[i].equals("P")) {
				cnt++;
				continue;
			}
			if(cnt == 3 && arrStr[i].equals("C")) {
				cnt++;
				break;
			}
		}
		
		if(cnt == 4) {
			System.out.print("I love UCPC");
		}else {
			System.out.print("I hate UCPC");
		}
	}
}
