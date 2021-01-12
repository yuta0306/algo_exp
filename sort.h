// ********
// ヘッダファイル
// ********

// ****
// マクロ
// ****

// データの個数
#define N 10000

// 正確な計算時間を得るための反復回数
#define REP 100

// ****
// 関数
// ****

// ２つのデータを交換する
void swap(
    double  *,
    double  *
);

// ランダムなデータを与える
void data_random(
    int,
    double  []
);

// 昇順のデータを与える
void data_ascending(
    int,
    double  []
);

// 降順のデータを与える
void data_descending(
    int,
    double  []
);

// アルゴリズム 5.1  選択ソート
void selectionsort(
    int,
    double  []
);

// アルゴリズム 5.2  挿入ソート
void insertionsort(
    int,
    double  []
);

// アルゴリズム 5.5  ヒープソート
void heapsort(
    int,
    double  []
);

// アルゴリズム 6.1  クイックソート
void quicksort(
    double  [],
    int,
    int,
    char []
);

// アルゴリズム 7.3  マージソート
void mergesort(
    double  [],
    int,
    int,
    double []
);

// **** EOF
