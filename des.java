import java.io.*;
import java.security.spec.AlgorithmParameterSpec;
import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;

public class des {
	private static Cipher encrypt;
	private static Cipher decrypt;
	private static final byte[] iv = { 22, 33, 11, 44, 55, 99, 66, 77, 88, 12, 13, 14, 15, 16, 27, 56 };
	public static void main(String[] args){
		String tf = "data.txt";
		String ef = "encrypted.txt";
		String df = "decrypted.txt";
		SecretKey key;
		try {
			key = KeyGenerator.getInstance("AES").generateKey();
			AlgorithmParameterSpec aps =new IvParameterSpec(iv);
			encrypt=Cipher.getInstance("AES/CBC/PKCS5Padding");
			encrypt.init(Cipher.ENCRYPT_MODE,key,aps);
			decrypt=Cipher.getInstance("AES/CBC/PKCS5Padding");
			decrypt.init(Cipher.DECRYPT_MODE,key,aps);
			encryption(new FileInputStream(tf),new FileOutputStream(ef));
			decryption(new FileInputStream(ef),new FileOutputStream(df));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	private static void encryption(InputStream in,OutputStream out) throws IOException
	{
		out=new CipherOutputStream(out,encrypt);
		wb(in,out);
	}
	private static void decryption(InputStream in,OutputStream out) throws IOException
	{
		in=new CipherInputStream(in,decrypt);
		wb(in,out);
	}
	private static void wb(InputStream in,OutputStream out) throws IOException
	{
		byte[] buff = new byte[512];
		int rb = 0 ;
		while((rb = in.read(buff))>=0)
		{
			out.write(buff,0,rb);
		}
		out.close();
		in.close();
	}
}
