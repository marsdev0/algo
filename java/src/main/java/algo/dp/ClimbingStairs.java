package algo.dp;

/**
 * 70. 爬楼梯 (Climbing Stairs)
 * https://leetcode.cn/problems/climbing-stairs/
 */
public class ClimbingStairs {

    /**
     * dp[i] = 到达第 i 阶的方法数 = dp[i-1] + dp[i-2]
     */
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        int prev2 = 1, prev1 = 2;
        for (int i = 3; i <= n; i++) {
            int cur = prev1 + prev2;
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }

    public static void main(String[] args) {
        ClimbingStairs solution = new ClimbingStairs();
        System.out.println(solution.climbStairs(10)); // 89
    }
}
