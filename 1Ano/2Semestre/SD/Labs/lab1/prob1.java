import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
import java.util.LinkedList;

class prob1 {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Digite uma string:");
        String input = sc.nextLine();
        
        try {
            // empty String
            if (input.isEmpty()) {
                throw new IllegalArgumentException("A string não pode estar vazia.");
            }
            System.out.println("A string inserida é: " + input);


            // isPalindrome
            if(isPalindrome(input)){
                System.out.println("É um palindromo");
            }
            else{
                System.out.println("Não á um palindromo");
            }


        } catch (IllegalArgumentException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }



    public static boolean isPalindrome(String word){
        String palavra = word;                          // a palavra que queres testar, como String.
        Queue<Character> fila = new LinkedList<>();     // a fila que recebe a String palavra, letra-a-letra, ou seja, é uma fila de carateres.
        Stack<Character> pilha = new Stack<>();         // a pilha que recebe a String palavra, letra-a-letra, ou seja, é uma pilha de carateres.

        
        for(int i = 0; i < palavra.length(); i++){
            char c = palavra.charAt(i);
            fila.add(c);
            pilha.push(c);
        }

        while(!fila.isEmpty() && !pilha.isEmpty()){
            char charFila = fila.remove();
            char charPilha = pilha.pop();
            
            System.out.printf("%c -> %c\n", charFila, charPilha);
            
            if(charFila != charPilha){
                return false;
            }
        }
        
        if(!fila.isEmpty() || !pilha.isEmpty()){
            return false;
        }
        
        return true;
    }
}

