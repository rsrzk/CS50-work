#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompting user for starting # of llamas
    int starting_llamas;
    do
    {
        starting_llamas = get_int("Start size: ");
    }
    while (starting_llamas < 9);

    // Prompting user for ending # of llamas
    int ending_llamas;
    do
    {
        ending_llamas = get_int("End size: ");
    }
    while (ending_llamas < starting_llamas);

    // How many years will it take to get to goal?
    // Every year, 1/3 of llamas are born and 1/4 llamas die
    int years = 0;
    for (int i = starting_llamas; i < ending_llamas; years++)
    {
        // printf("Year: %i. ", years+1);
        // printf("Start %i. ", i);
        int born = i / 3;
        // printf("Born %i. ", born);
        int died = i / 4;
        // printf("Died %i. ", died);
        i = i + born - died;
        // printf("End %i.\n", i);
    }
    printf("Years: %i\n", years);
}