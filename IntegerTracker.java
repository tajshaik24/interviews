import java.util.HashMap; //importing the HashMap Class

public class IntegerTracker{
    int count; //total number of elements
    float mean; //mean of all the elements
    int mode; //mode of the elements
    Integer max; //max of the elements
    Integer min; //min of the elements
    HashMap<Integer, Integer> it; //HashMap which will store the count of each integer

    public IntegerTracker(){ //initializer which will initialize all the values
        count = 0;
        mean = 0;
        mode = 0;
        max = null;
        min = null;
        it = new HashMap<>();
    }

    public void track(int i){ //O(1) time complexity
        if(it.containsKey(i)){ //checks if number in HashMap
            it.put(i, it.get(i) + 1); //updates value
        }
        else{
            it.put(i, 1);
        }
        float totalSum = mean * count; //gathers total sum
        count++; //increments the count
        totalSum += i; //adds value just added to totalSum
        this.mean = totalSum/count; //calculates the new mean
        if(max == null){
            max = i;
        }
        else{
            this.max = Math.max(this.max, i); //finds a new max
        }
        if(min == null){
            min = i;
        }
        else{
            this.min = Math.min(this.min, i); //finds a new min
        }
        if(!it.containsKey(mode) || it.get(i) > it.get(mode)){ //checks to see if we can set i to be the next mode
            this.mode = i; //sets the mode
            //mode will the first value ever set to be the mode if the count of all the values are all the same
        }
    }

    public int get_max(){ //O(1) time complexity
        return max;
    }

    public int get_min(){ //O(1) time complexity
        return min;
    }

    public float get_mean(){ //O(1) time complexity
        return mean;
    }

    public int get_mode(){ //O(1) time complexity
        return mode;
    }

    /*public static void main(String[] args){ //Made main function to test functionality
        IntegerTracker it = new IntegerTracker();
        //it.track(1);
        it.track(-1);
        System.out.println("max: " + it.get_max());
        System.out.println("min: " + it.get_min());
        System.out.println("mean: " + it.get_mean());
        System.out.println("mode: " + it.get_mode());
        //it.track(3);
        it.track(0);
        it.track(0);
        it.track(0);
        //it.track(1);
        System.out.println("max: " + it.get_max());
        System.out.println("min: " + it.get_min());
        System.out.println("mean: " + it.get_mean());
        System.out.println("mode: " + it.get_mode());
    }*/
}