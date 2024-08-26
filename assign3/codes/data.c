#include <stdio.h>
#include <math.h>
#include <stdlib.h>


#define WIDTH 80
#define HEIGHT 20

void plotLine(char canvas[HEIGHT][WIDTH], int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;
    int err = dx - dy;
    int e2;

    while (1) {
        canvas[y1][x1] = '#';
        if (x1 == x2 && y1 == y2) break;
        e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }
        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
    }
}

void plotPoint(char canvas[HEIGHT][WIDTH], int x, int y, char label) {
    if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
        canvas[y][x] = label;
    }
}

void printCanvasToFile(const char* filename, char canvas[HEIGHT][WIDTH]) {
    FILE *file = fopen("output.txt", "w");
    if (!file) {
        fprintf(stderr, "Error opening file %s for writing\n", filename);
        return;
    }

    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            fprintf(file, "%c", canvas[i][j] ? canvas[i][j] : ' ');
        }
        fprintf(file, "\n");
    }

    fclose(file);
}

int main() {
    char canvas[HEIGHT][WIDTH] = {0};

    // Define start and end points
    int startX = 10;
    int startY = 10;
    int endX = 70;
    int endY = 10;

    // Plot the line
    plotLine(canvas, startX, startY, endX, endY);

    // Calculate the points
    int points[4][2] = {
        {(int)(startX + 0.3 * (endX - startX)), startY},
        {(int)(startX + 0.6 * (endX - startX)), startY},
        {(int)(startX + 0.9 * (endX - startX)), startY},
        {(int)(startX + 1.5 * (endX - startX)), startY} // This point will be outside the segment
    };

    // Plot the points
    for (int i = 0; i < 4; ++i) {
        char label = (i == 3) ? 'C' : '*'; // 'C' for the 1.5BA point, '*' for others
        plotPoint(canvas, points[i][0], points[i][1], label);
    }

    // Print the canvas to a file
    printCanvasToFile("output.txt", canvas);

    printf("Plot saved to output.txt\n");
    return 0;
}

