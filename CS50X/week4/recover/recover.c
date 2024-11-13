#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

// each Blocksize is 512 bytes
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Remember filenames
    char *infile = argv[1];

    // Open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }

    BYTE *buffer = malloc(BLOCK_SIZE * sizeof(BYTE));

    // create file name and store in buffer using sprintf
    char *outfile = malloc(8 * sizeof(char));
    if (outfile == NULL)
    {
        printf("Not enough memory to store outfile name.\n");
        fclose(inptr);
        return 2;
    }

    int imgcount = -1;

    FILE *outptr;

    // read card file in 512B blocks
    while (fread(buffer, 1, BLOCK_SIZE, inptr) == BLOCK_SIZE)
    {
        // if signature in first 4 bytes
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            if (imgcount >= 0)
            {
                fclose(outptr);
            }

            // create new file name
            imgcount++;
            sprintf(outfile, "%03i.jpg", imgcount);

            // Open output file
            outptr = fopen(outfile, "w");
            if (outptr == NULL)
            {
                fclose(inptr);
                printf("Could not create %s.\n", outfile);
                free(buffer);
                free(outfile);
                return 3;
            }

            // write to new file
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outptr);
        }
        else if (imgcount >= 0)
        {
            // write to new file
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outptr);
        }
    }
    // free malloc
    free(buffer);
    free(outfile);

    // close files when end reached
    fclose(inptr);
    fclose(outptr);
}