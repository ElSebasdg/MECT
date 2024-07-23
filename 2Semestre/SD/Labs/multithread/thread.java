public class thread{
    public static void main(String[] args){

        for(int i = 1; i <= 5; i++){
            multiThreadThing cena = new multiThreadThing(i);
            cena.start();
        }
    }
}