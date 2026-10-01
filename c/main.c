#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <glob.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

/* The Makefile supplies the location of the C project. */
#ifndef EULER_DIR
#define EULER_DIR "."
#endif

static int prompt(const char *message, long *number)
{
    char *line = NULL;
    size_t capacity = 0;
    printf("%s", message);
    fflush(stdout);
    if (getline(&line, &capacity, stdin) == -1) {
        free(line);
        return 0;
    }
    if (strcmp(line, "q\n") == 0 || strcmp(line, "Q\n") == 0 ||
        strcmp(line, "q") == 0 || strcmp(line, "Q") == 0) {
        free(line);
        return 0;
    }
    char *end;
    errno = 0;
    *number = strtol(line, &end, 10);
    while (*end == ' ' || *end == '\t' || *end == '\n')
        end++;
    int valid = errno == 0 && end != line && *end == '\0' && *number > 0;
    free(line);
    return valid ? 1 : -1;
}

static int run(char *const arguments[])
{
    fflush(stdout);
    pid_t child = fork();
    if (child == -1) {
        perror("fork");
        return 1;
    }
    if (child == 0) {
        execvp(arguments[0], arguments);
        perror(arguments[0]);
        _exit(127);
    }
    int status;
    while (waitpid(child, &status, 0) == -1) {
        if (errno != EINTR) {
            perror("waitpid");
            return 1;
        }
    }
    return WIFEXITED(status) ? WEXITSTATUS(status) : 128 + WTERMSIG(status);
}

int main(void)
{
    if (chdir(EULER_DIR) == -1) {
        perror(EULER_DIR);
        return 1;
    }
    glob_t sources = {0};
    int found = glob("problems/p[0-9]*_*/solution*.c", 0, NULL, &sources);
    if (found != 0) {
        puts(found == GLOB_NOMATCH ? "No C solutions found. Add a .c file to a problem folder." :
             "Could not list C solutions.");
        globfree(&sources);
        return found == GLOB_NOMATCH ? 0 : 1;
    }

    puts("Available solutions:");
    for (size_t i = 0; i < sources.gl_pathc; i++)
        printf("  %s\n", sources.gl_pathv[i]);

    size_t selected = 0;
    for (;;) {
        long number;
        int answer = prompt("\nProblem number (q to quit): ", &number);
        if (answer == 0) {
            globfree(&sources);
            return 0;
        }
        size_t matches = 0;
        if (answer == 1) {
            for (size_t i = 0; i < sources.gl_pathc; i++) {
                if (strtol(strchr(sources.gl_pathv[i], '/') + 2, NULL, 10) == number) {
                    selected = i;
                    matches++;
                }
            }
        }
        if (matches == 0) {
            puts("Please enter one of the available problem numbers.");
            continue;
        }
        if (matches > 1) {
            size_t index = 0;
            for (size_t i = 0; i < sources.gl_pathc; i++)
                if (strtol(strchr(sources.gl_pathv[i], '/') + 2, NULL, 10) == number)
                    printf("  %zu: %s\n", ++index, sources.gl_pathv[i]);
            for (;;) {
                long choice;
                answer = prompt("Which solution? (q to quit): ", &choice);
                if (answer == 0) {
                    globfree(&sources);
                    return 0;
                }
                if (answer == 1 && (size_t)choice <= matches) {
                    index = 0;
                    for (size_t i = 0; i < sources.gl_pathc; i++) {
                        if (strtol(strchr(sources.gl_pathv[i], '/') + 2, NULL, 10) == number &&
                            ++index == (size_t)choice) {
                            selected = i;
                            break;
                        }
                    }
                    break;
                }
                puts("Please enter a solution number from the list.");
            }
        }
        break;
    }

    char *source = sources.gl_pathv[selected];
    char *target = malloc(strlen(source) + sizeof("build/"));
    if (target == NULL) {
        globfree(&sources);
        return 1;
    }
    sprintf(target, "build/%s", source);
    target[strlen(target) - 2] = '\0';
    char *build[] = {"make", target, NULL};
    int result = run(build);
    if (result == 0) {
        printf("\nRunning %s\n", source);
        /* Run beside the source, so relative input-data paths work. */
        char *slash = strrchr(source, '/');
        *slash = '\0';
        char *executable = malloc(strlen(EULER_DIR) + strlen(target) + 2);
        if (executable == NULL) {
            result = 1;
        } else {
            sprintf(executable, "%s/%s", EULER_DIR, target);
            if (chdir(source) == -1) {
                perror(source);
                result = 1;
            } else {
                char *arguments[] = {executable, NULL};
                result = run(arguments);
            }
            free(executable);
        }
    }
    free(target);
    globfree(&sources);
    return result;
}
