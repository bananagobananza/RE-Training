#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h> 

// Placeholder functions for the original code's external functions
void FUN_0040d2c0() {
    // Placeholder for any necessary initialization or setup
}

void FUN_0040ce90() {
    // Placeholder for any necessary initialization or setup
}

void FUN_00431fe0(int *ptr, const char *message) {
    printf("%s", message); // Simulate the functionality of displaying a message
}

void FUN_00432880(int *ptr, char *buffer) {
    // Simulate input reading, equivalent to a scanf
    scanf("%s", buffer);
}

int main() {
    size_t name_len;
    int iVar1;
    char local_40b[255] = {0}; // Initialize to 0
    char local_30c[255] = {0}; // Corrected to array to store string result
    char local_30b[255] = {0}; // Initialize to 0
    char serial[255] = {0};    // Corrected to array to store input string
    char name[255] = {0};      // Corrected to array to store input string
    char local_10b[259] = {0}; // Initialize to 0

    FUN_0040d2c0();
    FUN_0040ce90();

    // Initialize arrays
    memset(local_10b, 0, sizeof(local_10b));
    memset(local_30b, 0, sizeof(local_30b));
    memset(local_40b, 0, sizeof(local_40b));

    system("cls");
    FUN_00431fe0(NULL, "###########################\n");
    FUN_00431fe0(NULL, "# Bkis                    #\n");
    FUN_00431fe0(NULL, "# Keygen exercise lv4     #\n");
    FUN_00431fe0(NULL, "#                         #\n");
    FUN_00431fe0(NULL, "# 2009                    #\n");
    FUN_00431fe0(NULL, "###########################\n\n\n");
    FUN_00431fe0(NULL, "Your Name: ");
    FUN_00432880(NULL, name); // Read name
    FUN_00431fe0(NULL, "Your Serial: ");
    FUN_00432880(NULL, serial); // Read serial

    name_len = strlen(name);
    unsigned long long result = ((name_len * 554445) / 100) * -880;
    sprintf(local_30c, "%i-x019871", (double) result);

    iVar1 = strcmp(serial, local_30c);
    if (iVar1 == 0) {
        FUN_00431fe0(NULL, "Correct :: Good Work\n");
        FUN_00431fe0(NULL, "Now write a KeyGen!\n\n\n");
        system("pause");
        system("cls");
    } else {
        FUN_00431fe0(NULL, "Error :: Not a correct Serial\n");
        printf(local_30c);
        system("pause");
        system("cls");
    }

    return 0;
}
