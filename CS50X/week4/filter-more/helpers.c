#include "helpers.h"
#include "math.h"
#include "stdio.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            BYTE grey = round((image[h][w].rgbtBlue + image[h][w].rgbtGreen + image[h][w].rgbtRed) / 3.0);
            image[h][w].rgbtBlue = grey;
            image[h][w].rgbtGreen = grey;
            image[h][w].rgbtRed = grey;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        RGBTRIPLE temp[width];
        for (int w = 0; w < width; w++)
        {
            temp[width - 1 - w].rgbtBlue = image[h][w].rgbtBlue;
            temp[width - 1 - w].rgbtGreen = image[h][w].rgbtGreen;
            temp[width - 1 - w].rgbtRed = image[h][w].rgbtRed;
        }
        for (int w = 0; w < width; w++)
        {
            image[h][w].rgbtBlue = temp[w].rgbtBlue;
            image[h][w].rgbtGreen = temp[w].rgbtGreen;
            image[h][w].rgbtRed = temp[w].rgbtRed;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // int grid = 10;

    // // print image
    // printf("Image ori\n");
    // for (int h = 0; h < grid; h++)
    // {
    //     for (int w = 0; w < grid; w++)
    //     {
    //         printf("[%i %i %i] ", image[h][w].rgbtBlue, image[h][w].rgbtGreen, image[h][w].rgbtRed);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");

    // initialize temporary array to store blurred image with all values 0
    RGBTRIPLE temp[height][width];

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            temp[h][w].rgbtBlue = 0;
            temp[h][w].rgbtGreen = 0;
            temp[h][w].rgbtRed = 0;
        }
    }

    // // print temp
    // printf("Temp init\n");
    // for (int h = 0; h < grid; h++)
    // {
    //     for (int w = 0; w < grid; w++)
    //     {
    //         printf("[%i %i %i] ", temp[h][w].rgbtBlue, temp[h][w].rgbtGreen, temp[h][w].rgbtRed);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");

    // printf("Before division\n");

    // add relevant rows and columns
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            // iterate over kernel
            float n = 0;
            // initialize temp int variables because RGBTRIPLE uses bytes which can't store large numbers
            int blue = 0, green = 0, red = 0;

            for (int i = h - 1; i < h + 2; i++)
            {
                if (i >= 0 && i < height)
                {
                    for (int j = w - 1; j < w + 2; j++)
                    {
                        if (j >= 0 && j < width)
                        {
                            n++;
                            blue += image[i][j].rgbtBlue;
                            green += image[i][j].rgbtGreen;
                            red += image[i][j].rgbtRed;
                        }
                    }
                }
            }
            // if (h < grid && w < grid)
            //     printf("[%i %i %i]/%.1f ", blue, green, red, n);

            temp[h][w].rgbtBlue = round(blue / n);
            temp[h][w].rgbtGreen = round(green / n);
            temp[h][w].rgbtRed = round(red / n);
        }
        // if (h < grid)
        //     printf("\n");
    }
    // printf("\n\n");

    // copy temp blurred image to original image array
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            image[h][w].rgbtBlue = temp[h][w].rgbtBlue;
            image[h][w].rgbtGreen = temp[h][w].rgbtGreen;
            image[h][w].rgbtRed = temp[h][w].rgbtRed;
        }
    }

    // // print image
    // printf("Image final\n");
    // for (int h = 0; h < grid; h++)
    // {
    //     for (int w = 0; w < grid; w++)
    //     {
    //         printf("[%i %i %i] ", image[h][w].rgbtBlue, image[h][w].rgbtGreen, image[h][w].rgbtRed);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int Gx_arr[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy_arr[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // int grid = 3;
    // // print image
    // printf("Image ori\n");
    // for (int h = 0; h < grid; h++)
    // {
    //     for (int w = 0; w < grid; w++)
    //     {
    //         printf("[%i %i %i] ", image[h][w].rgbtBlue, image[h][w].rgbtGreen, image[h][w].rgbtRed);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");

    // initialize temporary array to store edge image with all values 0
    RGBTRIPLE temp[height][width];

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            temp[h][w].rgbtBlue = 0;
            temp[h][w].rgbtGreen = 0;
            temp[h][w].rgbtRed = 0;
        }
    }

    // // print temp
    // printf("Temp init\n");
    // for (int h = 0; h < grid; h++)
    // {
    //     for (int w = 0; w < grid; w++)
    //     {
    //         printf("[%i %i %i] ", temp[h][w].rgbtBlue, temp[h][w].rgbtGreen, temp[h][w].rgbtRed);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");

    // weighted sum temp over Gx and Gy
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            // iterate over kernel
            double Gxblue = 0, Gxgreen = 0, Gxred = 0;
            double Gyblue = 0, Gygreen = 0, Gyred = 0;

            for (int i = h - 1, k = 0; i < h + 2; i++, k++)
            {
                if (i >= 0 && i < height)
                {
                    for (int j = w - 1, l = 0; j < w + 2; j++, l++)
                    {
                        if (j >= 0 && j < width)
                        {
                            int Gx = Gx_arr[k][l];
                            Gxblue += image[i][j].rgbtBlue * Gx;
                            Gxgreen += image[i][j].rgbtGreen * Gx;
                            Gxred += image[i][j].rgbtRed * Gx;

                            int Gy = Gy_arr[k][l];
                            Gyblue += image[i][j].rgbtBlue * Gy;
                            Gygreen += image[i][j].rgbtGreen * Gy;
                            Gyred += image[i][j].rgbtRed * Gy;
                        }
                    }
                }
            }

            // combine Gx and Gy
            int sobBlue = round(sqrt(pow(Gxblue, 2) + pow(Gyblue, 2)));
            if (sobBlue > 255)
                sobBlue = 255;
            int sobGreen = round(sqrt(pow(Gxgreen, 2) + pow(Gygreen, 2)));
            if (sobGreen > 255)
                sobGreen = 255;
            int sobRed = round(sqrt(pow(Gxred, 2) + pow(Gyred, 2)));
            if (sobRed > 255)
                sobRed = 255;

            temp[h][w].rgbtBlue = sobBlue;
            temp[h][w].rgbtGreen = sobGreen;
            temp[h][w].rgbtRed = sobRed;
        }
    }

    // copy temp edge image to original image array
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            image[h][w].rgbtBlue = temp[h][w].rgbtBlue;
            image[h][w].rgbtGreen = temp[h][w].rgbtGreen;
            image[h][w].rgbtRed = temp[h][w].rgbtRed;
        }
    }

    // // print image
    // printf("Image final\n");
    // for (int h = 0; h < grid; h++)
    // {
    //     for (int w = 0; w < grid; w++)
    //     {
    //         printf("[%i %i %i] ", image[h][w].rgbtBlue, image[h][w].rgbtGreen, image[h][w].rgbtRed);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");

    return;
}
