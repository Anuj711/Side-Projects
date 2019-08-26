import java.util.*;

public class CutOrBulk {
	static Scanner s = new Scanner(System.in);

	public static void main(String[] args) {
		greeting();
		System.out.println("\nPlease enter your weight in killograms:");
		double weight = s.nextDouble();
		System.out.println("\nPlease enter your height in meters:");
		double height = s.nextDouble();
		BMI(weight, height);
	}

	private static void greeting () 
	{
		System.out.println("Hello, welcome to the cut or bulk program. \nThis program is intended for those who are working out for the first time.\nThis program uses metric units.\nCurrently this program is used for male bodybuilders.");
	}
	
	private static void BMI (double weight, double height) 
	{
		double bmi;
		bmi = (Math.round(weight/(height*height)*10d)/10d);
		BFP(bmi);
	}

	private static void BFP (double bmi)
	{
		System.out.println("\nPlease enter your age:");
		int age = s.nextInt();
		System.out.println("\nBMI:" +bmi);
		double bfp = Math.round(((1.39*bmi) + (0.16*age) - 19.34)*10d)/10d;
		System.out.println("\nBody fat percentage:" + bfp);
		cutOrbulk(bmi,bfp);
	}
	
	private static void cutOrbulk(double bmi, double bfp)
	{
		System.out.println("\nHere are your results:");
		if ((bmi <= 18) && (bfp <= 6))
		{
			System.out.println("You're pretty skinny, you need to build some mass. Try bulking!");
		}
		else if ((bmi >= 25) && (bfp >=23)) 
		{
			System.out.println("You're kind of heavy already, you need to get leaner. Try cutting!");
		}
		else if ((18 < bmi) && (bmi < 25) && (bfp <= 17))
		{
			System.out.println("Your body composition is fine, however you might have some stubborn fat in some minor areas and skinny arms. You need to build some mass overall. Try bulking!");
		}
		else if ((18 < bmi) && (bmi < 25) && (bfp > 17 ))
		{
			System.out.println("Your body composition is fine however, you might have some stubborn fat in some noticeable areas. You need to get leaner. Try cutting!");
		}
	}
}
