#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

map<int, vector<int>> devices_dict;
set<int> no_out;

int check_paths(int curr_device, set<int> prev_devices)
{
    if (prev_devices.count(curr_device) > 0)
    {
        return 0;
    }

    if (no_out.count(curr_device) > 0 && prev_devices.count(2) == 0 && prev_devices.count(3) == 0)
    {
        return 0;
    }

    prev_devices.insert(curr_device);
    int paths = 0;
    for (int output_device: devices_dict[curr_device])
    {
        if (output_device == 1)
        {
            if (prev_devices.count(2) > 0 && prev_devices.count(3) > 0)
            {
                paths++;
            }
        }
        else
        {
            paths += check_paths(output_device, prev_devices);
        }
    }
    
    if (paths == 0)
    {
        if (no_out.count(curr_device) == 0)
        {
            no_out.insert(curr_device);
            cout << curr_device << "\n";
        }
    }
    if (paths > 10000)
    {
        cout << paths << "\n";
    }
    return paths;
}

int main()
{
    no_out = set<int>();
    devices_dict = map<int, vector<int>>();
    vector<int> devices = vector<int>();

    int num;
    cout << "ready\n";
    cin >> num;

    for (int i = 0; i < num; i++)
    {
        int dev, len;
        cin >> dev >> len;
        vector<int> outputs = vector<int>();
        for (int j = 0; j < len; j++)
        {
            int niput;
            cin >> niput;
            outputs.push_back(niput);
        }

        devices_dict[dev] = outputs;
        devices.push_back(dev);
    }

    int result;
    result = check_paths(0, set<int>());
    cout << "\n\nsuccess!!!!!!\n\n" << result << "\n";

    // for (int dev: devices)
    // {
    //     cout << dev << ": ";
    //     for (int out: devices_dict[dev])
    //     {
    //         cout << out << " ";
    //     }
    //     cout << "\n";
    // }

    return 0;
}
