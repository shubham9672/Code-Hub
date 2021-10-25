public class HeapQueue {

	private int[] heap;
	private int size;

	private int parentIndex(int i) {
		return (i - 1) / 2;
	}

	private int leftIndex(int i) {
		return (i * 2) + 1;
	}

	@SuppressWarnings("unused")
	private int rightIndex(int i) {
		return (i * 2) + 2;
	}

	private void upHeap(int index) {
		if (size <= 1)
			return;
		int e = heap[index];
		while (index > 0 && heap[parentIndex(index)] < e) {
			heap[index] = heap[parentIndex(index)];
			index = parentIndex(index);
		}
		heap[index] = e;
	}

	private void downHeap(int index) {
		int e = heap[index];
		while (index <= parentIndex(size - 1)) {
			int j = leftIndex(index);
			if (j < size - 1 && heap[j] < heap[j + 1])
				++j;
			if (e >= heap[j])
				break;
			heap[index] = heap[j];
			index = j;
		}
	}

	public HeapQueue() {
		this(100);
	}

	public HeapQueue(int maxSize) {
		heap = new int[maxSize];
	}

	public void insert(int elem) {
		++size;
		heap[size - 1] = elem;
		upHeap(size - 1);
	}

	public int max() {
		return heap[0];
	}

	public boolean isEmpty() {
		return size() == 0;
	}

	public int size() {
		return this.size;
	}

	public void removeMax() {
		--size;
		heap[0] = heap[size];
		downHeap(0);
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("[ ");
		for (int i = 0; i < size; ++i)
			sb.append(heap[i]).append(" ");
		sb.append("]");
		return sb.toString();
	}
}