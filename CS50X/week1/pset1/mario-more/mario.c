#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // height or num of rows
    for (int i = 1; i <= height; i++)
    {
        // spaces before pyramid
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        // left pyramid
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        // gap
        printf("  ");

        // right pyramid
        for (int l = 0; l < i; l++)
        {
            printf("#");
        }

        printf("\n");
    }
}