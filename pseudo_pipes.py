at begining of execution:

	int tmp_fd = dup(STDIN)

int execute_me(some staff,f,f,f)
{
	dup2(tmp_fd, STDIN);
	close(tmp_fd);
	execve(...);
}

//last command, or single command

//child
	execute_me
//in parent
	close(tmp_fd)
	tmp_fd = dup(STDIN)
	wait

//before pipe
pipe(fd)
//child
	dup2(fd[1], STDOUT);
	close(...)
	execute_me(...);  (inside this one happens dup2(tmp_fd, IN))
//parent
	close (fd[1])
	close(tmp_fd)
	tmp_fd = fd[0];


ls |echo | grep | wc

while 
{
	executeion
}
while 
wait


while ()
{
	exe;
	wati;
	exec;
	wait;
}