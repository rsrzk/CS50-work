// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open input file.\n");
        return 2;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        fclose(input);
        printf("Could not open output file.\n");
        return 3;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    // Read infile's Header
    uint8_t header[HEADER_SIZE];
    fread(header, HEADER_SIZE, sizeof(uint8_t), input);

    // Write outfile's Header
    fwrite(header, HEADER_SIZE, sizeof(uint8_t), output);

    // TODO: Read samples from input file and write updated data to output file

    int16_t sample_buffer;
    while (fread(&sample_buffer, 1, sizeof(int16_t), input) == sizeof(int16_t))
    {
        sample_buffer *= factor;
        fwrite(&sample_buffer, 1, sizeof(int16_t), output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
