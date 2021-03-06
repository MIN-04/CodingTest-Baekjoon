package tag.dp;

import java.util.Scanner;

public class No2748 {

	/**
	 * [DP] Silver05 - 2748. 피보나치 수 2
	 */

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 입력받을 수
		int n = sc.nextInt();
		// 피보나치 결과 값을 저장할 배열
		long[] arr = new long[n + 1];

		// 피보나치 계산
		for (int i = 0; i <= n; i++) {
			if (i == 0)
				arr[i] = 0;
			else if (i == 1)
				arr[i] = 1;
			else
				arr[i] = arr[i - 1] + arr[i - 2];
		}

		System.out.print(arr[n]);
	}

}
