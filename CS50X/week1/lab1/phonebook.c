#include <stdio.h>
#include <cs50.h>

int main (void)
{
    string name = get_string("What's your name? ");
    int age = get_int("How old are you? ");
    string phone_number = get_string("What is your phone number? ");
    printf("%s\n%i\n%s\n", name, age, phone_number);
}