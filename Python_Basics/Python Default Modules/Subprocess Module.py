"""
NAME
    subprocess - Subprocesses with accessible I/O streams

DESCRIPTION
    This module allows you to spawn processes, connect to their
    input/output/error pipes, and obtain their return codes.

    OR

    Execute os command and store output into a variable

    For a complete description of this module see the Python documentation.

    Main API
    ========
    run(...): Runs a command, waits for it to complete, then returns a
              CompletedProcess instance.
    Popen(...): A class for flexibly executing a command in a new process

    Constants
    ---------
    DEVNULL: Special value that indicates that os.devnull should be used
    PIPE:    Special value that indicates a pipe should be created
    STDOUT:  Special value that indicates that stderr should go to stdout


    Older API
    =========
    call(...): Runs a command, waits for it to complete, then returns
        the return code.
    check_call(...): Same as call() but raises CalledProcessError()
        if return code is not 0
    check_output(...): Same as check_call() but returns the contents of
        stdout instead of a return code
    getoutput(...): Runs a command in the shell, waits for it to complete,
        then returns the output
    getstatusoutput(...): Runs a command in the shell, waits for it to complete,
        then returns a (exitcode, output) tuple

CLASSES
    builtins.Exception(builtins.BaseException)
        SubprocessError
            CalledProcessError
            TimeoutExpired
    builtins.object
        CompletedProcess
        Popen
        STARTUPINFO

    class CalledProcessError(SubprocessError)
     |  CalledProcessError(returncode, cmd, output=None, stderr=None)
     |
     |  Raised when run() is called with check=True and the process
     |  returns a non-zero exit status.
     |
     |  Attributes:
     |    cmd, returncode, stdout, stderr, output
     |
     |  Method resolution order:
     |      CalledProcessError
     |      SubprocessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, returncode, cmd, output=None, stderr=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  stdout
     |      Alias for output attribute, to match stderr
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SubprocessError:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class CompletedProcess(builtins.object)
     |  CompletedProcess(args, returncode, stdout=None, stderr=None)
     |
     |  A process that has finished running.
     |
     |  This is returned by run().
     |
     |  Attributes:
     |    args: The list or str args passed to run().
     |    returncode: The exit code of the process, negative for signals.
     |    stdout: The standard output (None if not captured).
     |    stderr: The standard error (None if not captured).
     |
     |  Methods defined here:
     |
     |  __init__(self, args, returncode, stdout=None, stderr=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  check_returncode(self)
     |      Raise CalledProcessError if the exit code is non-zero.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class Popen(builtins.object)
     |  Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None, text=None)
     |
     |  Execute a child program in a new process.
     |
     |  For a complete description of the arguments see the Python documentation.
     |
     |  Arguments:
     |    args: A string, or a sequence of program arguments.
     |
     |    bufsize: supplied as the buffering argument to the open() function when
     |        creating the stdin/stdout/stderr pipe file objects
     |
     |    executable: A replacement program to execute.
     |
     |    stdin, stdout and stderr: These specify the executed programs' standard
     |        input, standard output and standard error file handles, respectively.
     |
     |    preexec_fn: (POSIX only) An object to be called in the child process
     |        just before the child is executed.
     |
     |    close_fds: Controls closing or inheriting of file descriptors.
     |
     |    shell: If true, the command will be executed through the shell.
     |
     |    cwd: Sets the current directory before the child is executed.
     |
     |    env: Defines the environment variables for the new process.
     |
     |    text: If true, decode stdin, stdout and stderr using the given encoding
     |        (if set) or the system default otherwise.
     |
     |    universal_newlines: Alias of text, provided for backwards compatibility.
     |
     |    startupinfo and creationflags (Windows only)
     |
     |    restore_signals (POSIX only)
     |
     |    start_new_session (POSIX only)
     |
     |    pass_fds (POSIX only)
     |
     |    encoding and errors: Text mode encoding and error handling to use for
     |        file objects stdin, stdout and stderr.
     |
     |  Attributes:
     |      stdin, stdout, stderr, pid, returncode
     |
     |  Methods defined here:
     |
     |  __del__(self, _maxsize=9223372036854775807, _warn=<built-in function warn>)
     |
     |  __enter__(self)
     |
     |  __exit__(self, exc_type, value, traceback)
     |
     |  __init__(self, args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None, text=None)
     |      Create new Popen instance.
     |
     |  communicate(self, input=None, timeout=None)
     |      Interact with process: Send data to stdin and close it.
     |      Read data from stdout and stderr, until end-of-file is
     |      reached.  Wait for process to terminate.
     |
     |      The optional "input" argument should be data to be sent to the
     |      child process, or None, if no data should be sent to the child.
     |      communicate() returns a tuple (stdout, stderr).
     |
     |      By default, all communication is in bytes, and therefore any
     |      "input" should be bytes, and the (stdout, stderr) will be bytes.
     |      If in text mode (indicated by self.text_mode), any "input" should
     |      be a string, and (stdout, stderr) will be strings decoded
     |      according to locale encoding, or by "encoding" if set. Text mode
     |      is triggered by setting any of text, encoding, errors or
     |      universal_newlines.
     |
     |  kill = terminate(self)
     |
     |  poll(self)
     |      Check if child process has terminated. Set and return returncode
     |      attribute.
     |
     |  send_signal(self, sig)
     |      Send a signal to the process.
     |
     |  terminate(self)
     |      Terminates the process.
     |
     |  wait(self, timeout=None)
     |      Wait for child process to terminate; returns self.returncode.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  universal_newlines

    class STARTUPINFO(builtins.object)
     |  STARTUPINFO(*, dwFlags=0, hStdInput=None, hStdOutput=None, hStdError=None, wShowWindow=0, lpAttributeList=None)
     |
     |  Methods defined here:
     |
     |  __init__(self, *, dwFlags=0, hStdInput=None, hStdOutput=None, hStdError=None, wShowWindow=0, lpAttributeList=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class SubprocessError(builtins.Exception)
     |  Common base class for all non-exit exceptions.
     |
     |  Method resolution order:
     |      SubprocessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class TimeoutExpired(SubprocessError)
     |  TimeoutExpired(cmd, timeout, output=None, stderr=None)
     |
     |  This exception is raised when the timeout expires while waiting for a
     |  child process.
     |
     |  Attributes:
     |      cmd, output, stdout, stderr, timeout
     |
     |  Method resolution order:
     |      TimeoutExpired
     |      SubprocessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, cmd, timeout, output=None, stderr=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  stdout
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SubprocessError:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

FUNCTIONS
    call(*popenargs, timeout=None, **kwargs)
        Run command with arguments.  Wait for command to complete or
        timeout, then return the returncode attribute.

        The arguments are the same as for the Popen constructor.  Example:

        retcode = call(["ls", "-l"])

    check_call(*popenargs, **kwargs)
        Run command with arguments.  Wait for command to complete.  If
        the exit code was zero then return, otherwise raise
        CalledProcessError.  The CalledProcessError object will have the
        return code in the returncode attribute.

        The arguments are the same as for the call function.  Example:

        check_call(["ls", "-l"])

    check_output(*popenargs, timeout=None, **kwargs)
        Run command with arguments and return its output.

        If the exit code was non-zero it raises a CalledProcessError.  The
        CalledProcessError object will have the return code in the returncode
        attribute and output in the output attribute.

        The arguments are the same as for the Popen constructor.  Example:

         check_output(["ls", "-l", "/dev/null"])
        b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

        The stdout argument is not allowed as it is used internally.
        To capture standard error in the result, use stderr=STDOUT.

         check_output(["/bin/sh", "-c",
        ...               "ls -l non_existent_file ; exit 0"],
        ...              stderr=STDOUT)
        b'ls: non_existent_file: No such file or directory\n'

        There is an additional optional argument, "input", allowing you to
        pass a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it too will be used internally.  Example:

         check_output(["sed", "-e", "s/foo/bar/"],
        ...              input=
        b"when in the course of fooman events\n")
        b'when in the course of barman events\n'

        By default, all communication is in bytes, and therefore any "input"
        should be bytes, and the return value will be bytes.  If in text mode,
        any "input" should be a string, and the return value will be a string
        decoded according to locale encoding, or by "encoding" if set. Text mode
        is triggered by setting any of text, encoding, errors or universal_newlines.

    getoutput(cmd)
        Return output (stdout or stderr) of executing cmd in a shell.

        Like getstatusoutput(), except the exit status is ignored and the return
        value is a string containing the command's output.  Example:

        import subprocess
        subprocess.getoutput('ls /bin/ls')
        '/bin/ls'

    getstatusoutput(cmd)
        Return (exitcode, output) of executing cmd in a shell.

        Execute the string 'cmd' in a shell with 'check_output' and
        return a 2-tuple (status, output). The locale encoding is used
        to decode the output and process newlines.

        A trailing newline is stripped from the output.
        The exit status for the command can be interpreted
        according to the rules for the function 'wait'. Example:

        #  import subprocess
        #  subprocess.getstatusoutput('ls /bin/ls')
        # (0, '/bin/ls')
        #  subprocess.getstatusoutput('cat /bin/junk')
        # (1, 'cat: /bin/junk: No such file or directory')
        #  subprocess.getstatusoutput('/bin/junk')
        # (127, 'sh: /bin/junk: not found')
        #  subprocess.getstatusoutput('/bin/kill $$')
        # (-15, '')

    run(*popenargs, input=None, capture_output=False, timeout=None, check=False, **kwargs)
        Run command with arguments and return a CompletedProcess instance.

        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them.

        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.

        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.

        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.

        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.

        The other arguments are the same as for the Popen constructor.

DATA
    ABOVE_NORMAL_PRIORITY_CLASS = 32768
    BELOW_NORMAL_PRIORITY_CLASS = 16384
    CREATE_BREAKAWAY_FROM_JOB = 16777216
    CREATE_DEFAULT_ERROR_MODE = 67108864
    CREATE_NEW_CONSOLE = 16
    CREATE_NEW_PROCESS_GROUP = 512
    CREATE_NO_WINDOW = 134217728
    DETACHED_PROCESS = 8
    DEVNULL = -3
    HIGH_PRIORITY_CLASS = 128
    IDLE_PRIORITY_CLASS = 64
    NORMAL_PRIORITY_CLASS = 32
    PIPE = -1
    REALTIME_PRIORITY_CLASS = 256
    STARTF_USESHOWWINDOW = 1
    STARTF_USESTDHANDLES = 256
    STDOUT = -2
    STD_ERROR_HANDLE = 4294967284
    STD_INPUT_HANDLE = 4294967286
    STD_OUTPUT_HANDLE = 4294967285
    SW_HIDE = 0
    __all__ = ['Popen', 'PIPE', 'STDOUT', 'call', 'check_call', 'getstatus...

============================  SYNTAX ==============================================================


import subprocess
sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'OUTPUT IS: {out}')
print(f'Error is: {err}')
==================================>
if shell=True then your cmd is a string (as your os command)
if shell=False then your cmd is a list

Note: shell=False dont work on your os environment variables

ex: cmd="ls -lrt" ==>shell=True
    shell=False ==> cmd="ls -lrt".split()  or ['ls','-lrt']
=======================================================================


shell=True always on windows
============================
cmd is a string
----------------------------------------------------------

"""
import subprocess

# cmd = 'cd'
cmd = 'dir'
sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

return_code = sp.wait()

print(f'command executed with code = {return_code}')

output, error = sp.communicate()

print(f'The Output is \n{output.splitlines()}')

# Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
# runfile('C:/Users/dsharman/Python_Workspace/Python_Basics/Python Default Modules/Subprocess Module.py', wdir='C:/Users/dsharman/Python_Workspace/Python_Basics/Python Default Modules')
# command executed with code = 0
# The Output is
# ['C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Python Default Modules']

# Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
# runfile('C:/Users/dsharman/Python_Workspace/Python_Basics/Python Default Modules/Subprocess Module.py', wdir='C:/Users/dsharman/Python_Workspace/Python_Basics/Python Default Modules')
# command executed with code = 0
# The Output is
# [' Volume in drive C is OSDisk', ' Volume Serial Number is 1C4F-FEE1', '', ' Directory of C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Python Default Modules', '', '09/15/2021  10:06 AM    <DIR>          .', '09/15/2021  10:06 AM    <DIR>          ..', '09/14/2021  10:09 AM            21,544 DateTime Module.py', '08/27/2021  12:48 PM             3,419 GetPass Module.py', '08/27/2021  11:21 AM             5,862 Math Module.py', '09/08/2021  03:44 PM           120,766 OS Module.py', '08/27/2021  12:25 PM            12,668 Platform Module.py', '09/14/2021  09:18 AM             2,051 Strftime.org.txt', '09/15/2021  10:06 AM            22,907 Subprocess Module.py', '08/27/2021  02:22 PM            15,481 Sys Module.py', '               8 File(s)        204,698 bytes', '               2 Dir(s)  406,118,838,272 bytes free']
