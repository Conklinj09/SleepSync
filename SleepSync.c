#include <stdio.h>
#include <time.h>

struct SleepEntry {
    char date[20]; // e.g., "2025-03-13"
    int sleep_hour;
    int sleep_minute;
    int wake_hour;
    int wake_minute;
    char notes[200];
};

void log_sleep_data(struct SleepEntry entry) {
    FILE *file = fopen("sleep_log.txt", "a");
    if (file != NULL) {
        fprintf(file, "%s %d:%d %d:%d %s\n", entry.date, entry.sleep_hour, entry.sleep_minute, entry.wake_hour, entry.wake_minute, entry.notes);
        fclose(file);
    }
}

int main() {
    struct SleepEntry entry;

    // Ask for user input
    printf("Enter sleep time (hour minute): ");
    scanf("%d %d", &entry.sleep_hour, &entry.sleep_minute);

    printf("Enter wake-up time (hour minute): ");
    scanf("%d %d", &entry.wake_hour, &entry.wake_minute);

    printf("Enter any notes (optional): ");
    getchar(); // consume newline character from previous input
    fgets(entry.notes, sizeof(entry.notes), stdin);

    // Get current date
    time_t t = time(NULL);
    struct tm *tm_info = localtime(&t);
    strftime(entry.date, sizeof(entry.date), "%Y-%m-%d", tm_info);

    // Log the data
    log_sleep_data(entry);
    
    printf("Sleep data saved.\n");

    return 0;
}
