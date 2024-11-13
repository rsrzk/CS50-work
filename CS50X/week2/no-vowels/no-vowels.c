// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string input);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string converted = replace(argv[1]);
        printf("%s\n", converted);
        return 0;
    }
    else
    {
        printf("Error, you may only submit one word as an argument!\n");
        return 1;
    }
}

string replace(string input)
{
    int length = strlen(input);
    for (int i = 0; i < length; i++)
    {
        switch (input[i])
        {
            case 'a':
            case 'A':
                input[i] = '6';
                break;

            case 'e':
            case 'E':
                input[i] = '3';
                break;

            case 'i':
            case 'I':
                input[i] = '1';
                break;

            case 'o':
            case 'O':
                input[i] = '0';
                break;

            default:
                input[i] = input[i];
                break;
        }
    }
    return input;
}