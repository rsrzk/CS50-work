#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool alpha_check(string key, int n);
string str_upper(string str, int n);
bool unique_check(string key, int n);

int const alpha_len = 26;

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Error: %i arguments provided. You should only submit 1 as your key. E.g.: ./substitution key\n", argc - 1);
        return 1;
    }

    string key = argv[1];
    int n = strlen(key);

    if (n != alpha_len)
    {
        printf("Error: %i character(s) provided in key. Key should contain %i unique alphabets. E.g.: ./substitution "
            "VCHPRZGJNTLSKFBDQWAXEUYMOI\n",
            n, alpha_len);
        return 1;
    }

    if (alpha_check(key, n))
    {
        printf("Error: Non-alphabetical characters provided in key. Key should contain %i unique alphabets. E.g.: ./substitution "
            "VCHPRZGJNTLSKFBDQWAXEUYMOI\n",
            alpha_len);
        return 1;
    }

    key = str_upper(key, n);

    if (unique_check(key, n))
    {
        printf("Error: You have duplicated some alphabets in your key. Alphabets should be unique.\n");
        return 1;
    }

    string plaintext = get_string("plaintext: ");
    int plain_len = strlen(plaintext);
    string ciphertext = plaintext;

    for (int i = 0; i < plain_len; i++)
    {
        char c = plaintext[i];
        if (isupper(c))
        {
            int index = c - 'A'; // to know index of c in alphabet
            c += key[index] - 'A' - index; // adding variance to retain case. Minus index because it already accounts for itself
        }
        if (islower(c))
        {
            int index = c - 'a'; // lower case 'a' because c is lower case
            c += key[index] - 'A' - index; //retain uppercase 'A' because key has been converted to uppercase
        }
        ciphertext[i] = c;
    }

    printf("ciphertext: %s\n", ciphertext);
    return 0;
}

bool alpha_check(string key, int n)
{
    for (int i = 0; i < n; i++)
    {
        if (!isalpha(key[i]))
        {
            return true;
        }
    }
    return false;
}

string str_upper(string str, int n)
{
    for (int i = 0; i < n; i++)
    {
        str[i] = toupper(str[i]);
    }
    return str;
}

bool unique_check(string key, int n)
{
    //check for uniqueness
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            // printf("%c vs %c\n", key[i], key[j]);
            if (key[i] == key[j])
            {
                return true;
            }
        }
    }

    //check that sum equals to uppercase alphabet
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int sum = 0;
    for (int i = 0; i < alpha_len; i++)
    {
        sum += alphabet[i];
    }

    for (int i = 0; i < n; i++)
    {
        sum -= key[i];
    }

    if (sum == 0)
    {
        return false;
    }
    else
    {
        return true;
    }
}