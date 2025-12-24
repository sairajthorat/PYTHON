#include <iostream>

int main() {
    int limit;
    std::cout << "Enter the limit: ";
    std::cin >> limit;

    std::cout << "Prime numbers: ";
    for (int num = 2; num <= limit; num++) {
        bool isPrime = true;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            std::cout << num << " ";
        }
    }
    std::cout << std::endl;
    return 0;
}
