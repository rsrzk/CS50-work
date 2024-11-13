// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 100000;

// Hash table
node *table[N];

int dict_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // alpabet multiply position + alpabet multiply position
    // index of alphabets to start from 1 rather than zero. For each position of letter can also add in its position index
    int output = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        output += (toupper(word[i]) - 'A' + 1) * (i + 1) * (i + 1) * (i + 1);
    }
    output %= N;

    return output;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    // NULL entire table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Open dictionary file
    FILE *infile = fopen(dictionary, "r");
    if (!infile)
    {
        printf("Error opening file!\n");
        return false;
    }

    char buffer[LENGTH + 1];

    // Add words to hash table
    while (fscanf(infile, "%s", buffer) != EOF)
    {
        int index = hash(buffer);
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            printf("Error creating node!\n");
            return false;
        }
        strcpy(n->word, buffer);
        n->next = table[index];
        table[index] = n;
        dict_size++;
    }

    fclose(infile);

    // TO REMOVE: Print hash table
    // for (int i = 0; i < N; i++)
    // {
    //     printf("table[%i]: ", i);

    //     node *cursor = table[i];
    //     int count = 0;
    //     while (cursor != NULL)
    //     {
    //         printf("%s, ", cursor->word);
    //         cursor = cursor->next;
    //         count++;
    //     }
    //     printf("\n%i\n", count);
    // }

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *del = NULL;
        while (cursor != NULL)
        {
            del = cursor;
            cursor = cursor->next;
            free(del);
        }
    }
    return true;
}
