import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * 
 * @author foobar
 * p xasc. a zdmik qtng. yiy uist. easc os iye iq trmkbumk. gwv wolnrg kaqcs vi rlr.
 * Hint! The seven star-studded Pragyan walks into the hall of fame. Boom!
 * Hint! Robert Sedgewick
 *
 */
public class KamasutraCipher {
	
	private static String trim(String s){
		char[] chars = s.toUpperCase().toCharArray();
		Set<Character> charSet = new LinkedHashSet<Character>();
		for(char c: chars){
			charSet.add(c);
		}
		
		StringBuilder sb = new StringBuilder();
		for(Character character: charSet){
			sb.append(character);
		}
		return sb.toString();
	}
	
	public static String encode(String top, String bot, String s){
		String encoded = "";
		for(int i = 0; i < s.length(); i++){
			char c = s.charAt(i);
			if(top.indexOf(c) >= 0){
				encoded = encoded + Character.toString(bot.charAt(top.indexOf(c)));
			}else if(bot.indexOf(c) >= 0){
				encoded = encoded + Character.toString(top.charAt(bot.indexOf(c)));
			}else{
				encoded = encoded + Character.toString(c);
			}
			
		}
		return encoded;
	}
	
	public static String decode(String top, String bot, String so){
		so = so.toUpperCase();
		String decoded = "";
		for (int i = 0; i < so.length(); i++){
			char c = so.charAt(i);
			if(top.indexOf(c) >= 0){
				decoded = decoded + Character.toString(bot.charAt(top.indexOf(c)));
			}else if(bot.indexOf(c) >= 0){
				decoded = decoded + Character.toString(top.charAt(bot.indexOf(c)));
			}else{
				decoded = decoded + Character.toString(c);
			}
		}
		return decoded;
	}
	
	public static void main(String Args[]){
		String top = "THEQUICKBROWN";
		String bot = "FXJMPSVLAZYDG";
		String test = "MEET AT ELEVEN";
		String resEncode = encode(top, bot, test);
		System.out.println(resEncode);
		String resDecoded = decode(top, bot, resEncode);
		System.out.println(resDecoded);

	}

}
