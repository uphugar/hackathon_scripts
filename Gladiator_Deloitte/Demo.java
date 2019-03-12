import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Demo {
	static List<Fish> fishList = new ArrayList<Fish>();
	static List<group> groupList = new ArrayList<group>();

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter total count of fishes");
		int fCount = sc.nextInt();

		int id = 1;
		while (fCount-- > 0) {
			Fish fs = new Fish();
			fs.id = id;
			System.out.println("Position of fish No " + id);
			fs.head = sc.nextInt();
			System.out.println("Length of fish No " + id++);
			fs.length = sc.nextInt();
			fs.tail = fs.head + fs.length;
			fishList.add(fs);
		}

		getGroupList();

		int maxCount = 0, interval1 = 0, interval2 = 0;
		for (int i = 0; i < groupList.size() - 2; i++) {
			int c1 = groupList.get(i).fishList.size();
			for (int j = i + 1; j < groupList.size() - 1; j++) {
				int c2 = getApparentCount(groupList.get(i), groupList.get(j));

				if (maxCount < (c1 + c2)) {
					maxCount = c1 + c2;
					interval1 = groupList.get(i).id;
					interval2 = groupList.get(j).id;
				}
			}
		}

		System.out.println("First interval : " + interval1 + " Second interval : " + interval2+ " total count of fishes together : " + maxCount);
	}

	public static void getGroupList() {

		Fish lastFish = fishList.get(fishList.size() - 1);
		int groupId = 0;

		while (lastFish.tail >= 0) {
			group gr = new group();
			boolean found = false;
			for (Fish fs : fishList) {
				if (fs.head == 0 || fs.tail == 0 || (fs.head < 0 && fs.tail > 0)) {
					found = true;
					gr.fishList.add(fs);
				}
				fs.head = fs.head - 1;
				fs.tail = fs.tail - 1;
			}

			if (found) {
				gr.id = groupId;
				groupList.add(gr);
			}
			groupId++;
		}
	}

	public static int getApparentCount(group g1, group g2) {
		Set<Integer> set = new HashSet<Integer>(g1.getFishIds());
		for (int id : g2.getFishIds()) {
			set.add(id);
		}
		return set.size();
	}

}
