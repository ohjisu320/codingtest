class Solution {
    public int solution(String s) {
        String[] numbers = {"zero", "one", "two", "three", "four", "five", "six","seven","eight", "nine"};

        StringBuilder answer = new StringBuilder();
        while (!s.isEmpty()) {
            char c = s.charAt(0);

            if (c >= '0' && c <= '9') {

                answer.append(c);
                s = s.substring(1);
            } else {
                for (int i = 0 ; i < numbers.length ; i ++) {
                    if (s.startsWith(numbers[i])) {
                        answer.append(i);
                        s = s.substring(numbers[i].length());
                        break;
                    }
                }
            }

        }
        return Integer.parseInt(answer.toString());

    }

}