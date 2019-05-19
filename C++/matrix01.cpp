#include<iostream>

using namespace std;

// Editing a program posted on Reddit
// "[C++] I'd like to write out an n*m matrix where the border is 0 and the inside is 1, but only writes garbage values."
// https://www.reddit.com/r/learnprogramming/comments/bkn3jq/c_id_like_to_write_out_an_nm_matrix_where_the/
// Error 1: == used in assignment
// Error 2: highest index is not n but n-1
// Compiled in WSL Ubuntu: g++ -o matrix01 matrix01.cpp
// Run: ./matrix01

int main()
{
    int n, m;
    cout<<"n pls"<<endl;
    cin>>n;
    cout<<"m pls"<<endl;
    cin>>m;
    int mtr[n][m];
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if(i!=0 && i!=n-1 && j!=0 && j!=m-1)
            {
                mtr[i][j]=1;
            }
            else
            {
                mtr[i][j]=0;
            }
            cout<<mtr[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
