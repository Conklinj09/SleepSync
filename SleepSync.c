#include <stdio.h>
#include <time.h>
#include <stdlib.h>

struct SleepEntry {
    char date[20];
    int sleep_hour;
    int sleep_minute;
    int wake_hour;
    int wake_minute;
    char notes[200];
};

// Function to log sleep data
void log_sleep_data(struct SleepEntry entry) {
    FILE *file = fopen("sleep_log.txt", "a");
    if (file != NULL) {
        fprintf(file, "%s %d:%d %d:%d %s\n", entry.date, entry.sleep_hour, entry.sleep_minute, entry.wake_hour, entry.wake_minute, entry.notes);
        fclose(file);
    } else {
        printf("Error opening file for writing.\n");
    }
}

//  Accept Sleep Quality Rating
def log_sleep_entry(date, sleep_time, wake_time, quality_rating, filename="sleep_log.csv"):
    from datetime import datetime

    # Calculate sleep duration
    fmt = "%H:%M"
    sleep_dt = datetime.strptime(sleep_time, fmt)
    wake_dt = datetime.strptime(wake_time, fmt)
    duration = (wake_dt - sleep_dt).seconds / 3600 if wake_dt > sleep_dt else ((wake_dt - sleep_dt).seconds + 86400) / 3600

    # Append data to CSV
    with open(filename, "a") as file:
        file.write(f"{date},{sleep_time},{wake_time},{duration:.2f},{quality_rating}\n")




// Function to calculate total sleep time in minutes
int calculate_sleep_duration(struct SleepEntry entry) {
    int sleep_minutes = entry.sleep_hour * 60 + entry.sleep_minute;
    int wake_minutes = entry.wake_hour * 60 + entry.wake_minute;
    int sleep_duration = wake_minutes - sleep_minutes;

    // If the wake time is earlier than the sleep time, assume it was the next day
    if (sleep_duration < 0) {
        sleep_duration += 24 * 60;
    }
    return sleep_duration;
}

// Function to analyze trends (weekday vs weekend)
void analyze_sleep_trends() {
    FILE *file = fopen("sleep_log.txt", "r");
    if (file == NULL) {
        printf("Error opening file for reading.\n");
        return;
    }

    struct SleepEntry entry;
    int weekday_sleep = 0, weekend_sleep = 0;
    int weekday_count = 0, weekend_count = 0;

    while (fscanf(file, "%s %d:%d %d:%d %[^\n]", entry.date, &entry.sleep_hour, &entry.sleep_minute, &entry.wake_hour, &entry.wake_minute, entry.notes) == 6) {
        // Get the weekday from the date
        time_t t = time(NULL);
        struct tm *tm_info = localtime(&t);
        strptime(entry.date, "%Y-%m-%d", tm_info);
        
        int day_of_week = tm_info->tm_wday;  // 0 = Sunday, 1 = Monday, ..., 6 = Saturday

        int sleep_duration = calculate_sleep_duration(entry);

        // Weekdays are Monday (1) to Friday (5), weekends are Saturday (6) and Sunday (0)
        if (day_of_week == 0 || day_of_week == 6) {
            weekend_sleep += sleep_duration;
            weekend_count++;
        } else {
            weekday_sleep += sleep_duration;
            weekday_count++;
        }
    }

    if (weekday_count > 0) {
        printf("Average weekday sleep duration: %d hours %d minutes\n", weekday_sleep / weekday_count / 60, weekday_sleep / weekday_count % 60);
    } else {
        printf("No weekday sleep data available.\n");
    }

    if (weekend_count > 0) {
        printf("Average weekend sleep duration: %d hours %d minutes\n", weekend_sleep / weekend_count / 60, weekend_sleep / weekend_count % 60);
    } else {
        printf("No weekend sleep data available.\n");
    }

    fclose(file);
}

// Function to analyze sleep consistency
void analyze_sleep_consistency() {
    FILE *file = fopen("sleep_log.txt", "r");
    if (file == NULL) {
        printf("Error opening file for reading.\n");
        return;
    }

    struct SleepEntry entry;
    int previous_sleep_minutes = -1;
    int consistent_days = 0, total_days = 0;

    while (fscanf(file, "%s %d:%d %d:%d %[^\n]", entry.date, &entry.sleep_hour, &entry.sleep_minute, &entry.wake_hour, &entry.wake_minute, entry.notes) == 6) {
        int sleep_duration = calculate_sleep_duration(entry);

        if (previous_sleep_minutes != -1) {
            // Compare sleep duration consistency with the previous day
            if (abs(sleep_duration - previous_sleep_minutes) <= 30) {  // within 30 minutes for consistency
                consistent_days++;
            }
        }

        previous_sleep_minutes = sleep_duration;
        total_days++;
    }

    if (total_days > 0) {
        printf("Sleep consistency: %.2f%%\n", (double)consistent_days / total_days * 100);
    } else {
        printf("No sleep data available to analyze consistency.\n");
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

    // Analyze trends and consistency
    analyze_sleep_trends();
    analyze_sleep_consistency();

    return 0;
}
