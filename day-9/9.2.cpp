#include <iostream>
// #define SIZE 20
#define SIZE 98460

using namespace std;

char **floor_map;
int number;

bool try_fill(int x, int y)
{
    number++;
    // cout << x << " " << y << "\n";
    // cout << number << "\n";
    if (x < 0 or x >= SIZE)
    {
        number--;
        return false;
    }
    if (y < 0 or y >= SIZE)
    {
        number--;
        return false;
    }
    if (floor_map[y][x] == 1 || floor_map[y][x] == 2)
    {
        number--;
        return true;
    }
    cout << x << " " << y << "\n";
    if (floor_map[y][x] == -2)
    {
        number--;
        return false;
    }
    floor_map[y][x] = 2;
    if (try_fill(x + 1, y) && try_fill(x - 1, y) && try_fill(x, y + 1) && try_fill(x, y - 1))
    {
        cout << x << " " << y << "\n";
        floor_map[y][x] = 1;
        number--;
        return true;
    }
    else
    {
        floor_map[y][x] = -2;
        number--;
        return false;
    }
}

int main(int argc, char const *argv[])
{
    number = 0;

    floor_map = (char **)malloc(sizeof(char *) * SIZE);
    for (int i = 0; i < SIZE; i++)
    {
        floor_map[i] = (char *)malloc(sizeof(char) * SIZE);
    }

    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
        {
            floor_map[i][j] = 0;
        }
    }

    cout << "ready\n";

    int n;
    cin >> n;

    int red_x[n], red_y[n];

    for (int i = 0; i < n; i++)
    {
        cin >> red_x[i] >> red_y[i];
    }

    int cur_x, cur_y;
    int prev_x, prev_y;
    for (int i = 0; i < n; i++)
    {
        cur_x = red_x[i];
        cur_y = red_y[i];

        floor_map[cur_y][cur_x] = true;

        if (i > 0)
        {
            prev_x = red_x[i - 1];
            prev_y = red_y[i - 1];
        }
        else
        {
            prev_x = red_x[n - 1];
            prev_y = red_y[n - 1];
        }

        if (prev_x == cur_x)
        {
            for (int y = min(cur_y, prev_y) + 1; y < max(cur_y, prev_y); y++)
            {
                floor_map[y][cur_x] = true;
            }
        }
        else
        {
            for (int x = min(cur_x, prev_x) + 1; x < max(cur_x, prev_x); x++)
            {
                floor_map[cur_y][x] = true;
            }
        }
    }

    int x = red_x[0];
    int y = red_y[0];
    cout << x << " " << y << "\n";

    for (int i = y - 50; i < y + 50; i++)
    {
        for (int j = x - 50; j < x + 50; j++)
        {
            if (floor_map[i][j] == 0) cout << "0";
            else if (floor_map[i][j] == 1) cout << "1";
            else if (floor_map[i][j] == 2) cout << "2";
            else if (floor_map[i][j] == -2) cout << "u";
        }
        cout << "\n";
    }

    cout << x << " " << y << "\n";
    cin >> x >> y;
    if (floor_map[y][x] == 0 && try_fill(x, y))
    {
        cout << "success!\n";
    }

    for (int i = y - 50; i < y + 50; i++)
    {
        for (int j = x - 50; j < x + 50; j++)
        {
            if (floor_map[i][j] == 0) cout << "0";
            else if (floor_map[i][j] == 1) cout << "1";
            else if (floor_map[i][j] == 2) cout << "2";
            else if (floor_map[i][j] == -2) cout << "u";
        }
        cout << "\n";
    }

    // if ((floor_map[y + 1][x] == 0 && try_fill(x, y + 1)) || (floor_map[y - 1][x] == 0 && try_fill(x, y - 1)) || (floor_map[y][x + 1] == 0 && try_fill(x + 1, y)) || (floor_map[y + 1][x + 1] == 0 && try_fill(x + 1, y + 1)) || (floor_map[y - 1][x + 1] == 0 && try_fill(x + 1, y - 1)) || (floor_map[y][x - 1] == 0 && try_fill(x - 1, y)) || (floor_map[y + 1][x - 1] == 0 && try_fill(x - 1, y + 1)) || (floor_map[y - 1][x - 1] == 0 && try_fill(x - 1, y - 1)))
    // {
    //     cout << "success!\n";
    // }

    // if (SIZE <= 20)
    // {
    //     for (int i = 0; i < SIZE; i++)
    //     {
    //         for (int j = 0; j < SIZE; j++)
    //         {
    //             if (floor_map[i][j] == 0) cout << "0";
    //             else if (floor_map[i][j] == 1) cout << "1";
    //             else if (floor_map[i][j] == 2) cout << "2";
    //             else if (floor_map[i][j] == -2) cout << "u";
    //         }
    //         cout << "\n";
    //     }
    // }

    return 0;
}
