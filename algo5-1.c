#include "sort.h"

// ********
// アルゴリズム 5.1  選択ソート
// ********
void selectionsort(
    int     n,      // データの個数
    double  D[]     // データ D[0], ..., D[n-1]
)
{
    int     i, j, max_index;
    double  max;

    for( i = n-1; i > 0; i-- ) {
        max = D[0];
        max_index = 0;
        for( j = 1; j <= i; j++ ) {
            if( D[j] >= max ) {
                max = D[j];
                max_index = j;
            }
        }
        swap( &(D[max_index]), &(D[i]) );
    }
}

// **** EOF
