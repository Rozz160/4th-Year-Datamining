import sql.DBManager;
import type.GPU;

public class DBMain {
	private static int amd, amdPurchased, amdSumRating, ati, atiPurchased, atiSumRating, nvidia, nvidiaPurchased, nvidiaSumRating;
	
	public static void main(String[] args) {
		amd = amdPurchased = amdSumRating = ati = atiPurchased = atiSumRating = nvidia = nvidiaPurchased = nvidiaSumRating = 0;
		
		DBManager db = new DBManager();
		for(GPU gpu: db.getQuery().queryStatement()) {
			if("AMD".equals(gpu.getName())) {
				amd++;
				if(gpu.getRating() != 0 && gpu.getNumberRated() != 0) {
					amdPurchased++;
					amdSumRating = amdSumRating + gpu.getRating();
				}
			}else if("ATI".equals(gpu.getName())) {
				ati++;
				if(gpu.getRating() != 0 && gpu.getNumberRated() != 0) {
					atiPurchased++;
					atiSumRating = atiSumRating + gpu.getRating();
				}
			}else if("NVIDIA".equals(gpu.getName())) {
				nvidia++;
				if(gpu.getRating() != 0 && gpu.getNumberRated() != 0) {
					nvidiaPurchased++;
					nvidiaSumRating = nvidiaSumRating + gpu.getRating();
				}
			}
		}
		
		double gpuSuccessAMD = (((double)amdSumRating/amd)/5)*((double)amdPurchased/amd);
		double gpuSuccessATI = (((double)atiSumRating/ati)/5)*((double)atiPurchased/ati);
		double gpuSuccessNVIDIA = (((double)nvidiaSumRating/nvidia)/5)*((double)nvidiaPurchased/nvidia);
		
		System.out.println("Probability GPU type successful:");
		System.out.println("AMD: " + 100*gpuSuccessAMD + "%");
		System.out.println("ATI: " + 100*gpuSuccessATI + "%");
		System.out.println("NVIDIA: " + 100*gpuSuccessNVIDIA + "%");
		
		db.close();
	}
}
