#include <stdio.h>
#include <time.h>   // for clock()
#include "sort.h"                                                                                                 

// データ
double  A[N];

// ********
// メイン関数
// ********
void main( void )
{
    int     i, k;
    clock_t time_all, time_start, time_end;

    // ++++ 計算時間の合計
    time_all = 0;

    // 正確な計算時間を得るための反復
    for( k = 0; k < REP; k++ ) {

        // **** データの入力
        // ランダム
        data_random( N, A );
        // 昇順
        // data_ascending( N, A );
        // 降順
        // data_descending( N, A );

        /* データの表示（ソート前） */
        // printf( "input:\n" );
        // for( i = 0; i < N; i++ ) {
        //     printf( "%lf\n", A[i] );
        // }

        // ++++ 計算時間の計測開始
        time_start = clock();

        // **** ソート
        // アルゴリズム 5.1  選択ソート
        // selectionsort( N, A );                                                                                                 
        // アルゴリズム 5.2  挿入ソート
        // insertionsort( N, A );                                                                                                 
        // アルゴリズム 5.5  ヒープソート
        // heapsort( N, A );                                                                                                 
        // アルゴリズム 6.1  クイックソート
        // quicksort( A, 0, N-1, "rand" );                                                                                                 
        // アルゴリズム 7.3  マージソート
        double M[N] = {0.0}; mergesort( A, 0, N-1, M );                                                                                                 

        // ++++ 計算時間の計測終了
        time_end = clock();

        // ++++ 計算時間の合計
        time_all += ( time_end - time_start );

        /* データの表示（ソート後） */
        // printf( "output:\n" );
        // for( i = 0; i < N; i++ ) {
        //     printf( "%lf\n", A[i] );
        // }

        /* 計算時間 */
        // printf( "data: N = %d  ", N );
        // printf( "time: %lf sec.\n", ( (double)( time_end - time_start ) / (double)CLOCKS_PER_SEC ) );

    } // for( k )

    // 計算時間（平均）
    printf( "-------- avg. by REP = %d\n", REP );
    printf( "data: N = %d  ", N );
    printf( "time: %lf sec.\n", ( ( (double)time_all / (double)REP ) / (double)CLOCKS_PER_SEC ) );
}

// **** EOF
