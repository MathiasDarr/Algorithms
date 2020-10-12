#include <iostream>
#include <unordered_map>


using namespace std;

template<typename K, typename V>
void print_map(unordered_map<K,V> const &m){
    for(auto const& pair:m){
        cout << "{" << pair.first << ": " << pair.second << "}" << endl;
    }
}


int main(){

    unordered_map<int, char> m = {
        {1,'A'},
        {2,'B'}
    };
    print_map(m);

}