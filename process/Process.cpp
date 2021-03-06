#include "Process.h"
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <stdexcept>

/* Initialize the process, create input/output pipes */
Process::Process(const std::vector<std::string>& args) { 
    if (pipe(writepipe) != 0) {
        closePipes();
        throw std::runtime_error(std::string("Process pipe writepipe ") + strerror(errno));
    }
    if (pipe(readpipe) != 0) {
        closePipes();   
        throw std::runtime_error(std::string("Process pipe readpipe ") + strerror(errno));
    }
    m_pid = fork();
    if (m_pid < 0) {
        closePipes();
        throw std::runtime_error(std::string("Process fork ") + strerror(errno));      
    } else if (m_pid == 0) {
        if (dup2(writepipe[0], 0) == -1) {
            closePipes();
            perror((std::string("Process dup2 writepipe ") + strerror(errno)).c_str());
        }
        if (dup2(readpipe[1], 1) == -1) {
            closePipes();
            perror((std::string("Process dup2 readpipe ") + strerror(errno)).c_str());
        }
        std::vector<const char*> cargs;
        std::transform(args.begin(), args.end(), std::back_inserter(cargs), [](std::string s){return s.c_str();});
        cargs.push_back(NULL);
        execvp(cargs[0], const_cast<char**>(&cargs[0]));
        throw std::runtime_error(std::string("Process execvp ") + strerror(errno));
    } else {
        m_pread = fdopen(readpipe[0], "r");
        std::cout << "Process [" << getpid() << "] constructor " << std::endl;
    }
}

/* Close any open file streams or file descriptors,
   insure that the child has terminated */
Process::~Process() { 
    kill(m_pid, SIGTERM);
    int status;
    pid_t pid = waitpid(m_pid, &status, 0);
    if (pid < 0) {
        closePipes();
        perror("~Process waitpid");
    }
}
    
/* write a string to the child process */
void Process::write(const std::string &text) {
    ::write(writepipe[1], text.c_str(), strlen(text.c_str()));
}

/* read a full line from child process, 
   if no line is available, block until one becomes available */
std::string Process::readline() {
    char *line = 0;
    size_t len = 0;
    while(not(getline(&line, &len, m_pread)));
    return line;
}

void Process::closePipes() {
    close(readpipe[0]);
    close(readpipe[1]);
    close(writepipe[0]);
    close(writepipe[1]);
    close(*writepipe);
    close(*readpipe);
}
