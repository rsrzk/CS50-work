// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool upper = false;
    bool lower = false;
    bool number = false;
    bool symbol = false;
    int n = strlen(password);
    for (int i = 0; i < n; i++)
    {
        char c = password[i];
        if (c >= 'A' && c <= 'Z')
        {
            upper = true;
        }
        else if (c >= 'a' && c <= 'z')
        {
            lower = true;
        }
        else if (c >= '0' && c <= '9')
        {
            number = true;
        }
        else
        {
            symbol = true;
        }
    }

    if (upper && lower && number && symbol)
    {
        return true;
    }
    else
    {
        return false;
    }
}
