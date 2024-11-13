#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text, int n);
int count_words(string text, int n);
int count_sentences(string text, int n);
bool is_letter(char c);

int main(void)
{
    string text = get_string("Text: ");

    int n = strlen(text);

    int letters = count_letters(text, n);
    // printf("%i letters\n", letters);

    int words = count_words(text, n);
    // printf("%i words\n", words);

    int sentences = count_sentences(text, n);
    // printf("%i sentences\n", sentences);

    // Coleman-Liau index
    float L = letters / (float) words * 100;
    // printf("%.4f index\n", L);
    float S = sentences / (float) words * 100;
    // printf("%.4f index\n", S);
    float index = 0.0588 * L - 0.296 * S - 15.8;
    // printf("%.4f index\n", index);

    int grade = round(index);

    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int count_letters(string text, int n)
{
    int letters = 0;
    for (int i = 0; i < n; i++)
    {
        if (is_letter(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text, int n)
{
    int words = 0;
    bool lettersequence = false;

    for (int i = 0; i < n; i++)
    {
        if (text[i] == ' ')
        {
            lettersequence = false;
        }
        if (is_letter(text[i]))
        {
            if (lettersequence == false)
            {
                words++;
            }
            lettersequence = true;
        }
    }
    return words;
}

int count_sentences(string text, int n)
{
    int sentences = 0;
    bool lettersequence = false;

    for (int i = 0; i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            lettersequence = false;
        }
        if (is_letter(text[i]))
        {
            if (lettersequence == false)
            {
                sentences++;
            }
            lettersequence = true;
        }
    }
    return sentences;
}

bool is_letter(char c)
{
    if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
    {
        return true;
    }
    else
    {
        return false;
    }
}