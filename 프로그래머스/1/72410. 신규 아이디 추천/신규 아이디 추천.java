
class Solution {
    public String solution(String new_id) {
       StringBuilder sb = new StringBuilder();
        new_id = new_id.toLowerCase(); // 1단계: 소문자로 치환
        
        for (char c: new_id.toCharArray()) {
            if (c >=  'a' && c <= 'z'|| c >= '0' && c <= '9'  
                || c == '-' || c == '_' || c == '.') { //2단계
                sb.append(c);
            }
        }
        String answer = sb.toString();
        
        answer = answer.replaceAll("\\.+", "."); // 3단계 연속되는 .은 다 . 하나로 치환;
            
        if  (answer.startsWith(".")) { // 4단계
            answer = answer.substring(1);
        }
        
        if (answer.endsWith(".")) {
            answer = answer.substring(0, answer.length() - 1);
        }
        
        if (answer.length() == 0){ // 5단계
            answer= "a";
        }
        
        if (answer.length() >= 16) { //6단계
            answer = answer.substring(0, 15);
            if (answer.endsWith(".")) {
                answer = answer.substring(0, 14);
            }
            
        } 
        while (answer.length() <= 2)  { //7단계
            answer += answer.substring(answer.length() -1);
            
        }

        return answer;
    }
}