import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Streams {
    public static void main(String[] args) {
        // Given a collection of birds
        Bird[] birds = new Bird[]{
                new Chicken("chicken"),
                new Chicken("chicken"),
                new Chicken("chicken"),
                new Hawk("hawk"),
                new Chicken("chicken")
        };

        // Filter using the power of the Streams and lambda function
        List<Bird> birdList = Arrays.stream(birds).filter(bird -> bird.getName().equals("chicken"))
                .collect(Collectors.toList());

        // Assert that the intruder is filtered
        assert birdList.size() == birds.length - 1;
        assert birdList.stream().allMatch(bird -> bird.getName().equals("chicken"));
    }

    //Dummy code to explain the power of Streams
    static class Bird {
        private final String name;

        Bird(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }
    }

    static class Chicken extends Bird {
        Chicken(String name) {
            super(name);
        }
    }

    static class Hawk extends Bird {
        Hawk(String name) {
            super(name);
        }
    }
}
