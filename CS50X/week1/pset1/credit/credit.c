#include <cs50.h>
#include <stdio.h>

bool checksum(long card);
long power(int base, int exp);

int main(void)
{
    long card = get_long("Number: ");
    if (card < power(10, 12) || card >= power(10, 16))
    {
        printf("INVALID\n");
    }
    else
    {
        if (checksum(card))
        {
            // printf("Checksum TRUE\n");
            // if 15 digit and start w 34 or 37 then AMEX
            if ((card >= 34 * power(10, 13) && card < 35 * power(10, 13)) ||
                (card >= 37 * power(10, 13) && card < 38 * power(10, 13)))
            {
                printf("AMEX\n");
            }

            // else if 16 digit and start w 51, 52, 53, 54 or 55 then MASTERCARD
            else if (card >= 51 * power(10, 14) && card < 56 * power(10, 14))
            {
                printf("MASTERCARD\n");
            }

            // else if 13 or 16 digit and start with 4 then VISA
            else if ((card >= 4 * power(10, 12) && card < 5 * power(10, 12)) ||
                     (card >= 4 * power(10, 15) && card < 5 * power(10, 15)))
            {
                printf("VISA\n");
            }

            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
}

bool checksum(long card)
{
    int total = 0;
    for (int i = 0; i < 16; i++)
    {
        long place = power(10, i + 1);
        long placeb4 = power(10, i);
        int digit = (card % place - card % placeb4) / placeb4;
        if (i % 2 != 0)
        {
            digit *= 2;
        }
        // printf("%i\n", digit);
        if (digit >= 10)
        {
            int subtotal = 0;
            for (int j = 0; j < 2; j++)
            {
                place = power(10, j + 1);
                placeb4 = power(10, j);
                int subdigit = (digit % place - digit % placeb4) / placeb4;
                subtotal += subdigit;
            }
            digit = subtotal;
        }
        total += digit;
        // printf("TOTAL %i\n", total);
    }
    if (total % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

long power(int base, int exp)
{
    long result = 1;
    while (exp != 0)
    {
        result *= base;
        --exp;
    }
    return result;
}