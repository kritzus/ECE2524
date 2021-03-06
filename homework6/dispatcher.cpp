// Homework 6: pipeline for ECE 2524
// author: Laurin Mordhorst (mlaurin1)

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <signal.h>
#include <sys/wait.h>

int main(void)
{
    int p[2];
    int status1, status2;
    int childpid1, childpid2;
    pipe(p);
    
    // generator process
    childpid1 = fork();
    if (childpid1 == 0) {
        dup2(p[1], 1);
        close(p[0]);
        execve("./generator", NULL, NULL);
        exit(0);
    }
    sleep(1);
    kill(childpid1, SIGTERM);
    waitpid(childpid1, &status1, 0);
    std::cerr << "Process[" << childpid1 << "] exited with status " << status1 << std::endl; 
    close(p[1]);
    
    // child process
    childpid2 = fork();
    if (childpid2 == 0) {
        dup2(p[0], 0);
        execve("./consumer", NULL, NULL);
        exit(0);
    }
    waitpid(childpid2, &status2, 0);
    std::cerr << "Process[" << childpid2 << "] exited with status " << status2 << std::endl;
    return(0);
}
