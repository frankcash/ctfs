/**
 * 
 * @author foobar
 * p xasc. a zdmik qtng. yiy uist. easc os iye iq trmkbumk. gwv wolnrg kaqcs vi rlr.
 * Hint! The seven star-studded Pragyan walks into the hall of fame. Boom!
 * Hint! Robert Sedgewick
 *
 */

public class VigenereCipher {
	
	/**
	 * 
	 * @param s
	 * @param key
	 * @return
	 */
	public static String encrypt(String s, String key){
		String encoded = "";
		
		s = s.toUpperCase();
		for (int i = 0, j = 0; i < s.length(); i++){
			char c = s.charAt(i);
			
			if(c < 'A' || c > 'Z'){
				continue;
			}
			encoded += (char) ((c + key.charAt(j) - 2 * 'A') % 26 + 'A');
            j = ++j % key.length();

		}
		
		return encoded;
	}
	
	/**
	 * 
	 * @param s
	 * @param key
	 * @return
	 */
	public static String decrypt(String s, String key){
		String decoded = "";
		
		s = s.toUpperCase();
		for(int i = 0, j = 0; i < s.length(); i++){
			char c = s.charAt(i);
			if(c < 'A' || c > 'Z'){
				continue;
			}
			
			decoded += (char) ((c - key.charAt(j) + 26) % 26 + 'A');
            j = ++j % key.length();

		}
		
		return decoded;
	}
	
	public static void main(String Args[]){
		String s = "p xasc. a zdmik qtng. yiy uist. easc os iye iq trmkbumk. gwv wolnrg kaqcs vi rlr.";
		String key ="PRAGYAN";
		System.out.println(decrypt(s, key)); // AGAMEAMOVIESTARHISWIFENAMEOFTHECSTEXTBOOKTHEWINNERTAKESITALL
		
		
		return;
	}

}
