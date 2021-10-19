
#include <iostream>

/*
Comb Sort Algorithm
Author: Captainhampton
*/

using namespace std;

//newGap Function
int createGap( int gap ) 
{
  gap = ( gap * 10 ) / 1.3;
  
  if ( gap == 9 || gap == 10 )
    gap = 11;
  
  if (gap < 1)
    gap = 1;
  
  return gap;
}//end newGap Function


void combSort(int data[], int size) 
{
  int gap = size;
  
  while(true) {
   	  gap = createGap( gap );
	  bool swapped = false;
    
	for (int i = 0; i < size - gap; i++) {
      int j = i + gap;

      if ( data[i] > data[j] ){
        swap(data[i], data[j]);
        swapped = true;
      }//end if
    
	}//end for
    
	if (gap == 1 && !swapped)
      break;
  }//end for
}//end combSort Function


int main()
{
	//Test data set
	int data[5] = { 5, 2, 3, 1, 4 };
	int size = 5;

	cout << "***Combsort Algorithm***" <<endl <<endl;

	//Print presorted data items
	cout << "Pre-Sorted Data Set: "<<endl;
	for ( int i = 0; i < 5; i++ )
		cout << data[i] << " ";
	cout << endl;

	combSort(data, size);
	cout << endl;

	//Print sorted data items
	cout << "Combsorted Data Set: " <<endl;
	for ( int i = 0; i < 5; i++ )
		cout << data[i] << " ";
	cout << endl <<endl;

  return 0;
}


// a type of Shell Sort, is a "diminishing increment sort." Basically, it Insertion Sorts the elements of the list (L) that are Y elements apart (comparing L[x] with L[x+Y]). Y, over the iterations, decreases by some amount. The algorithm shown here uses a formula that has been shown to be efficient. This is one of the most efficient of the N2 sorting algorithms. The reason for this is that the Insertion Sort becomes more efficient if the list is already c
