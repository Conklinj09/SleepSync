#include <stdio.h>
#include <time.h>

struct SleepEntry {
    char date[20];
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
    } else {
        printf("Error opening file for writing.\n");
    }
}

// Function to calculate total sleep time in hours and minutes
void calculate_sleep_duration(struct SleepEntry entry) {
    int sleep_minutes = entry.sleep_hour * 60 + entry.sleep_minute;
    int wake_minutes = entry.wake_hour * 60 + entry.wake_minute;
    int sleep_duration = wake_minutes - sleep_minutes;

    // If the wake time is earlier than the sleep time, assume it was the next day
    if (sleep_duration < 0) {
        sleep_duration += 24 * 60;
    }

    printf("Total sleep duration: %d hours %d minutes\n", sleep_duration / 60, sleep_duration % 60);
}

// Function to calculate average sleep duration from the log
void calculate_average_sleep_duration() {
    FILE *file = fopen("sleep_log.txt", "r");
    if (file == NULL) {
        printf("Error opening file for reading.\n");
        return;
    }

    struct SleepEntry entry;
    int total_sleep_minutes = 0;
    int total_entries = 0;

    while (fscanf(file, "%s %d:%d %d:%d %[^\n]", entry.date, &entry.sleep_hour, &entry.sleep_minute, &entry.wake_hour, &entry.wake_minute, entry.notes) == 6) {
        int sleep_minutes = entry.sleep_hour * 60 + entry.sleep_minute;
        int wake_minutes = entry.wake_hour * 60 + entry.wake_minute;
        int sleep_duration = wake_minutes - sleep_minutes;

        if (sleep_duration < 0) {
            sleep_duration += 24 * 60;
        }

        total_sleep_minutes += sleep_duration;
        total_entries++;
    }

    if (total_entries > 0) {
        printf("Average sleep duration: %d hours %d minutes\n", total_sleep_minutes / total_entries / 60, total_sleep_minutes / total_entries % 60);
    } else {
        printf("No sleep data available.\n");
    }

    fclose(file);
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

    // Calculate and display sleep duration
    calculate_sleep_duration(entry);

    // Optionally, calculate the average sleep duration
    calculate_average_sleep_duration();

    return 0;
}
