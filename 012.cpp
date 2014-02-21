#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int iterator = 0;
	int triangle = 0;
	int divcount = 0;
	while(true)
	{
		iterator += 1;
		triangle += iterator;
		int divtest = 0;
		divcount = 0;
		while(divtest <= sqrt(triangle))
		{
			divtest += 1;
			if (triangle % divtest == 0)
				divcount += 1;
		}
		divcount *= 2;
		if (iterator % 1000 == 0)
			cout << triangle << ";" << divcount << endl;
		if (divcount > 500)
			break;
	}
	cout << triangle << ";" << divcount << endl;
	cout << "Answer:\t" << triangle << endl;
	return 0;
}
// answer : 76576500