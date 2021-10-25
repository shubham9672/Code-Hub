import java.util.Iterator;
import java.util.NoSuchElementException;

public class SLList<T> implements Iterable<T> {

	private static class Node<T> {
		private Node<T> next;
		private T data;

		public Node(T val) {
			this(val, null);
		}

		public Node(T data, Node<T> next) {
			this.data = data;
			this.next = next;
		}
	}

	private static class SLListIterator<T> implements Iterator<T> {

		private Node<T> node;

		public SLListIterator(Node<T> head) {
			this.node = head;
		}

		@Override
		public boolean hasNext() {

			return node != null;
		}

		@Override
		public T next() {
			if (!hasNext())
				throw new NoSuchElementException();
			T val = node.data;
			node = node.next;
			return val;
		}

	}

	@Override
	public Iterator<T> iterator() {
		return new SLListIterator<T>(head);
	}

	private Node<T> head, tail;
	private int size;

	public void prepend(T obj) {
		head = new Node<>(obj, head);
		if (tail == null)
			tail = head;
		++size;
	}

	public void append(T obj) {
		Node<T> node = new Node<>(obj);
		if (head == null)
			head = tail = node;
		else
			tail = tail.next = node;
		++size;
	}

	public int size() {
		return size;
	}

	public T first() {
		if (head == null)
			throw new NoSuchElementException();
		return head.data;
	}

	public T last() {
		if (tail == null)
			throw new NoSuchElementException();
		return tail.data;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		for (Iterator<T> it = iterator(); it.hasNext();) {
			sb.append(it.next()).append(" ");
		}
		sb.append("]");
		return sb.toString();
	}
}