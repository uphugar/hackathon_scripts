import java.util.ArrayList;

public class group {
	int id;
	ArrayList<Fish> fishList = new ArrayList<Fish>();
	
	ArrayList<Integer> getFishIds() {
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (Fish fs : fishList) {
			list.add(fs.id);
		}
		return list;
	}

	int getFishCount() {
		return fishList.size();
	}
}
