package type;

public class GPU {
	private int rating, numberRated;
	private float price;
	private String name, nameGPU, nameBrand, memSize, effectiveMem, coreClock, cudaCores;
	
	public int getRating() {
		return rating;
	}
	public void setRating(int rating) {
		this.rating = rating;
	}
	public int getNumberRated() {
		return numberRated;
	}
	public void setNumberRated(int numberRated) {
		this.numberRated = numberRated;
	}
	public float getPrice() {
		return price;
	}
	public void setPrice(float price) {
		this.price = price;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getNameGPU() {
		return nameGPU;
	}
	public void setNameGPU(String nameGPU) {
		this.nameGPU = nameGPU;
	}
	public String getNameBrand() {
		return nameBrand;
	}
	public void setNameBrand(String nameBrand) {
		this.nameBrand = nameBrand;
	}
	public String getMemSize() {
		return memSize;
	}
	public void setMemSize(String memSize) {
		this.memSize = memSize;
	}
	public String getEffectiveMem() {
		return effectiveMem;
	}
	public void setEffectiveMem(String effectiveMem) {
		this.effectiveMem = effectiveMem;
	}
	public String getCoreClock() {
		return coreClock;
	}
	public void setCoreClock(String coreClock) {
		this.coreClock = coreClock;
	}
	public String getCudaCores() {
		return cudaCores;
	}
	public void setCudaCores(String cudaCores) {
		this.cudaCores = cudaCores;
	}
}
