public class Main {
    public static void main(String[] args) {
        World world = new World(4);
        Agent agent = new Agent(world);
        agent.play();
    }
}


