#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main() {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    char access_key[64];
    int access_level_1 = -1;
    int access_level_2 = -1;
    int access_level_3 = -1;
    int access_level_4 = -1;
    int access_level_5 = -1;

    printf("Enter your access key: ");

    gets(access_key); 

    if (strcmp(access_key, "S3cR3t") == 0) {
        puts("Access granted! Verifying mission clearance levels...");
        printf("Checking access_level_1......");
        if (access_level_1 == 42) {
            printf("Checking access_level_2......");
            if (access_level_2 == 255) {
                printf("Checking access_level_3......");
                if (access_level_3 == 1337) {
                    printf("Checking access_level_4......");
                    if (access_level_4 == 12345) {
                        printf("Checking access_level_5......");
                        if (access_level_5 == 54321) {
                            printf("____Welcome to the Admin Zone____");
                            char flag[128];
                            char agent_alias[28];
                            FILE *f = fopen("flag.txt", "r");
                            if (!f) {
                                printf("Missing flag.txt. Contact the admin if this occurs remotely.");
                                exit(1);
                            }
                            fgets(flag, 128, f);
                            puts("Enter your alias: ");
                            fgets(agent_alias, 25, stdin);
                            printf("Welcome, ");
                            printf(agent_alias); 
                            printf("\nFlag: %s\n", flag);
                            fclose(f);
                            return;
                        }
                    }
                }
            }
        }
        puts("Mission clearance denied! Security alert triggered.");
    } else {
        puts("Invalid access key!");
    }
}
