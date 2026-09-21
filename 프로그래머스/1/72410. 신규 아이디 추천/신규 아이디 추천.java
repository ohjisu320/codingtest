class Solution {

    public String solution(String new_id) {
        StringBuilder sb = new StringBuilder();

        new_id = new_id.toLowerCase(); // 1
        for (char c : new_id.toCharArray()) { //2
            if (c >= 'a' && c <= 'z' ||
                    c >= '0' && c <= '9' ||
                    c == '-' || c == '_' || c == '.') {
                sb.append(c);
            }
        }
        String answer = sb.toString();

        //3
        answer = answer.replaceAll("\\.+", ".");

        // 4
        if (answer.startsWith(".")) answer = answer.substring(1);
        if (answer.endsWith(".")) answer = answer.substring(0, answer.length() - 1);

        //5
        if (answer.length() == 0) {
            answer = "a";
        }
        //6
        if (answer.length() >= 16) {
            answer = answer.substring(0, 15);
            if (answer.endsWith(".")) answer = answer.substring(0, 14);
        } else { // 7
            while (answer.length() <= 2) {
                answer += answer.substring(answer.length() - 1);
            }
        }
        
        return answer;

    }
}