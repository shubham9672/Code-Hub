
public class ConvertName{

	public static void main(String []args){
        
        String name = "madam";
        char[] nameArray = new char[name.length()];
        String convertedName= "";
        
        	// Copy character by character into array
        	for (int i = 0; i < name.length(); i++) {
            		convertedName = convertedName+name.charAt(i);
        	}
        
        System.out.println(convertedName);
     	}
}