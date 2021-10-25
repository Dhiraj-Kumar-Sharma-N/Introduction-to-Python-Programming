"""


NAME
    os - OS routines for NT or Posix depending on what system we're on.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

CLASSES
    builtins.Exception(builtins.BaseException)
        builtins.OSError
    builtins.object
        nt.DirEntry
    builtins.tuple(builtins.object)
        nt.times_result
        nt.uname_result
        stat_result
        statvfs_result
        terminal_size

    class DirEntry(builtins.object)
     |  Methods defined here:
     |
     |  __fspath__(self, /)
     |      Returns the path for the entry.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  inode(self, /)
     |      Return inode of the entry; cached per entry.
     |
     |  is_dir(self, /, *, follow_symlinks=True)
     |      Return True if the entry is a directory; cached per entry.
     |
     |  is_file(self, /, *, follow_symlinks=True)
     |      Return True if the entry is a file; cached per entry.
     |
     |  is_symlink(self, /)
     |      Return True if the entry is a symbolic link; cached per entry.
     |
     |  stat(self, /, *, follow_symlinks=True)
     |      Return stat_result object for the entry; cached per entry.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  name
     |      the entry's base filename, relative to scandir() "path" argument
     |
     |  path
     |      the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)

    error = class OSError(Exception)
     |  Base class for I/O related errors.
     |
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
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
     |  Data descriptors inherited from BaseException:
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

    class stat_result(builtins.tuple)
     |  stat_result(iterable=(), /)
     |
     |  stat_result: Result from stat, fstat, or lstat.
     |
     |  This object may be accessed either as a tuple of
     |    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
     |  or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
     |
     |  Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
     |  or st_flags, they are available as attributes only.
     |
     |  See os.stat for more information.
     |
     |  Method resolution order:
     |      stat_result
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  st_atime
     |      time of last access
     |
     |  st_atime_ns
     |      time of last access in nanoseconds
     |
     |  st_ctime
     |      time of last change
     |
     |  st_ctime_ns
     |      time of last change in nanoseconds
     |
     |  st_dev
     |      device
     |
     |  st_file_attributes
     |      Windows file attribute bits
     |
     |  st_gid
     |      group ID of owner
     |
     |  st_ino
     |      inode
     |
     |  st_mode
     |      protection bits
     |
     |  st_mtime
     |      time of last modification
     |
     |  st_mtime_ns
     |      time of last modification in nanoseconds
     |
     |  st_nlink
     |      number of hard links
     |
     |  st_size
     |      total size, in bytes
     |
     |  st_uid
     |      user ID of owner
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  n_fields = 17
     |
     |  n_sequence_fields = 10
     |
     |  n_unnamed_fields = 3
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.

    class statvfs_result(builtins.tuple)
     |  statvfs_result(iterable=(), /)
     |
     |  statvfs_result: Result from statvfs or fstatvfs.
     |
     |  This object may be accessed either as a tuple of
     |    (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
     |  or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
     |
     |  See os.statvfs for more information.
     |
     |  Method resolution order:
     |      statvfs_result
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  f_bavail
     |
     |  f_bfree
     |
     |  f_blocks
     |
     |  f_bsize
     |
     |  f_favail
     |
     |  f_ffree
     |
     |  f_files
     |
     |  f_flag
     |
     |  f_frsize
     |
     |  f_fsid
     |
     |  f_namemax
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  n_fields = 11
     |
     |  n_sequence_fields = 10
     |
     |  n_unnamed_fields = 0
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.

    class terminal_size(builtins.tuple)
     |  terminal_size(iterable=(), /)
     |
     |  A tuple of (columns, lines) for holding terminal window size
     |
     |  Method resolution order:
     |      terminal_size
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  columns
     |      width of the terminal window in characters
     |
     |  lines
     |      height of the terminal window in characters
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  n_fields = 2
     |
     |  n_sequence_fields = 2
     |
     |  n_unnamed_fields = 0
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.

    class times_result(builtins.tuple)
     |  times_result(iterable=(), /)
     |
     |  times_result: Result from os.times().
     |
     |  This object may be accessed either as a tuple of
     |    (user, system, children_user, children_system, elapsed),
     |  or via the attributes user, system, children_user, children_system,
     |  and elapsed.
     |
     |  See os.times for more information.
     |
     |  Method resolution order:
     |      times_result
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  children_system
     |      system time of children
     |
     |  children_user
     |      user time of children
     |
     |  elapsed
     |      elapsed time since an arbitrary point in the past
     |
     |  system
     |      system time
     |
     |  user
     |      user time
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  n_fields = 5
     |
     |  n_sequence_fields = 5
     |
     |  n_unnamed_fields = 0
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.

    class uname_result(builtins.tuple)
     |  uname_result(iterable=(), /)
     |
     |  uname_result: Result from os.uname().
     |
     |  This object may be accessed either as a tuple of
     |    (sysname, nodename, release, version, machine),
     |  or via the attributes sysname, nodename, release, version, and machine.
     |
     |  See os.uname for more information.
     |
     |  Method resolution order:
     |      uname_result
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  machine
     |      hardware identifier
     |
     |  nodename
     |      name of machine on network (implementation-defined)
     |
     |  release
     |      operating system release
     |
     |  sysname
     |      operating system name
     |
     |  version
     |      operating system version
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  n_fields = 5
     |
     |  n_sequence_fields = 5
     |
     |  n_unnamed_fields = 0
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.

FUNCTIONS
    _exit(status)
        Exit to the system with specified status, without normal exit processing.

    abort()
        Abort the interpreter immediately.

        This function 'dumps core' or otherwise fails in the hardest way possible
        on the hosting operating system.  This function never returns.

    access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
        Use the real uid/gid to test for access to a path.

          path
            Path to be tested; can be string, bytes, or a path-like object.
          mode
            Operating-system mode bitfield.  Can be F_OK to test existence,
            or the inclusive-OR of R_OK, W_OK, and X_OK.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          effective_ids
            If True, access will use the effective uid/gid instead of
            the real uid/gid.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            access will examine the symbolic link itself instead of the file
            the link points to.

        dir_fd, effective_ids, and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.

        Note that most operations will use the effective uid/gid, therefore this
          routine can be used in a suid/sgid environment to test if the invoking user
          has the specified access to the path.

    chdir(path)
        Change the current working directory to the specified path.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.

    chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
        Change the access permissions of a file.

          path
            Path to be modified.  May always be specified as a str, bytes, or a path-like object.
            On some platforms, path may also be specified as an open file descriptor.
            If this functionality is unavailable, using it raises an exception.
          mode
            Operating-system mode bitfield.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            chmod will modify the symbolic link itself instead of the file
            the link points to.

        It is an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
        dir_fd and follow_symlinks may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.

    close(fd)
        Close a file descriptor.

    closerange(fd_low, fd_high, /)
        Closes all file descriptors in [fd_low, fd_high), ignoring errors.

    cpu_count()
        Return the number of CPUs in the system; return None if indeterminable.

        This number is not equivalent to the number of CPUs the current process can
        use.  The number of usable CPUs can be obtained with
        ``len(os.sched_getaffinity(0))``

    device_encoding(fd)
        Return a string describing the encoding of a terminal's file descriptor.

        The file descriptor must be attached to a terminal.
        If the device is not a terminal, return None.

    dup(fd, /)
        Return a duplicate of a file descriptor.

    dup2(fd, fd2, inheritable=True)
        Duplicate file descriptor.

    execl(file, *args)
        execl(file, *args)

        Execute the executable file with argument list args, replacing the
        current process.

    execle(file, *args)
        execle(file, *args, env)

        Execute the executable file with argument list args and
        environment env, replacing the current process.

    execlp(file, *args)
        execlp(file, *args)

        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.

    execlpe(file, *args)
        execlpe(file, *args, env)

        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env, replacing the current
        process.

    execv(path, argv, /)
        Execute an executable path with arguments, replacing current process.

        path
          Path of executable file.
        argv
          Tuple or list of strings.

    execve(path, argv, env)
        Execute an executable path with arguments, replacing current process.

        path
          Path of executable file.
        argv
          Tuple or list of strings.
        env
          Dictionary of strings mapping to strings.

    execvp(file, args)
        execvp(file, args)

        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
        args may be a list or tuple of strings.

    execvpe(file, args, env)
        execvpe(file, args, env)

        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env, replacing the
        current process.
        args may be a list or tuple of strings.

    fdopen(fd, *args, **kwargs)
        # Supply os.fdopen()

    fsdecode(filename)
        Decode filename (an os.PathLike, bytes, or str) from the filesystem
        encoding with 'surrogateescape' error handler, return str unchanged. On
        Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).

    fsencode(filename)
        Encode filename (an os.PathLike, bytes, or str) to the filesystem
        encoding with 'surrogateescape' error handler, return bytes unchanged.
        On Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).

    fspath(path)
        Return the file system path representation of the object.

        If the object is str or bytes, then allow it to pass through as-is. If the
        object defines __fspath__(), then return the result of that method. All other
        types raise a TypeError.

    fstat(fd)
        Perform a stat system call on the given file descriptor.

        Like stat(), but for an open file descriptor.
        Equivalent to os.stat(fd).

    fsync(fd)
        Force write of fd to disk.

    ftruncate(fd, length, /)
        Truncate a file, specified by file descriptor, to a specific length.

    get_exec_path(env=None)
        Returns the sequence of directories that will be searched for the
        named executable (similar to a shell) when launching a process.

        *env* must be an environment variable dict or None.  If *env* is None,
        os.environ will be used.

    get_handle_inheritable(handle, /)
        Get the close-on-exe flag of the specified file descriptor.

    get_inheritable(fd, /)
        Get the close-on-exe flag of the specified file descriptor.

    get_terminal_size(...)
        Return the size of the terminal window as (columns, lines).

        The optional argument fd (default standard output) specifies
        which file descriptor should be queried.

        If the file descriptor is not connected to a terminal, an OSError
        is thrown.

        This function will only be defined if an implementation is
        available for this system.

        shutil.get_terminal_size is the high-level function which should
        normally be used, os.get_terminal_size is the low-level implementation.

    getcwd()
        Return a unicode string representing the current working directory.

    getcwdb()
        Return a bytes string representing the current working directory.

    getenv(key, default=None)
        Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are str.

    getlogin()
        Return the actual login name.

    getpid()
        Return the current process id.

    getppid()
        Return the parent's process id.

        If the parent process has already exited, Windows machines will still
        return its id; others systems will return the id of the 'init' process (1).

    isatty(fd, /)
        Return True if the fd is connected to a terminal.

        Return True if the file descriptor is an open file descriptor
        connected to the slave end of a terminal.

    kill(pid, signal, /)
        Kill a process with a signal.

    link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
        Create a hard link to a file.

        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        If follow_symlinks is False, and the last element of src is a symbolic
          link, link will create a link to the symbolic link itself instead of the
          file the link points to.
        src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
          platform.  If they are unavailable, using them will raise a
          NotImplementedError.

    listdir(path=None)
        Return a list containing the names of the files in the directory.

        path can be specified as either str, bytes, or a path-like object.  If path is bytes,
          the filenames returned will also be bytes; in all other circumstances
          the filenames returned will be str.
        If path is None, uses the path='.'.
        On some platforms, path may also be specified as an open file descriptor;\
          the file descriptor must refer to a directory.
          If this functionality is unavailable, using it raises NotImplementedError.

        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.

    lseek(fd, position, how, /)
        Set the position of a file descriptor.  Return the new position.

        Return the new cursor position in number of bytes
        relative to the beginning of the file.

    lstat(path, *, dir_fd=None)
        Perform a stat system call on the given path, without following symbolic links.

        Like stat(), but do not follow symbolic links.
        Equivalent to stat(path, follow_symlinks=False).

    makedirs(name, mode=511, exist_ok=False)
        makedirs(name [, mode=0o777][, exist_ok=False])

        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, raise an OSError if exist_ok is False. Otherwise no exception is
        raised.  This is recursive.

    mkdir(path, mode=511, *, dir_fd=None)
        Create a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

        The mode argument is ignored on Windows.

    open(path, flags, mode=511, *, dir_fd=None)
        Open a file for low level IO.  Returns a file descriptor (integer).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

    pipe()
        Create a pipe.

        Returns a tuple of two file descriptors:
          (read_fd, write_fd)

    popen(cmd, mode='r', buffering=-1)
        # Supply os.popen()

    putenv(name, value, /)
        Change or add an environment variable.

    read(fd, length, /)
        Read from a file descriptor.  Returns a bytes object.

    readlink(...)
        readlink(path, *, dir_fd=None) -> path

        Return a string representing the path to which the symbolic link points.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

    remove(path, *, dir_fd=None)
        Remove a file (same as unlink()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

    removedirs(name)
        removedirs(name)

        Super-rmdir; remove a leaf directory and all empty intermediate
        ones.  Works like rmdir except that, if the leaf directory is
        successfully removed, directories corresponding to rightmost path
        segments will be pruned away until either the whole path is
        consumed or an error occurs.  Errors during this latter phase are
        ignored -- they generally mean that a directory was not empty.

    rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
        Rename a file or directory.

        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.

    renames(old, new)
        renames(old, new)

        Super-rename; create directories as necessary and delete any left
        empty.  Works like rename, except creation of any intermediate
        directories needed to make the new pathname good is attempted
        first.  After the rename, directories corresponding to rightmost
        path segments of the old name will be pruned until either the
        whole path is consumed or a nonempty directory is found.

        Note: this function can fail with the new directory structure made
        if you lack permissions needed to unlink the leaf directory or
        file.

    replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
        Rename a file or directory, overwriting the destination.

        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.

    rmdir(path, *, dir_fd=None)
        Remove a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

    scandir(path=None)
        Return an iterator of DirEntry objects for given path.

        path can be specified as either str, bytes, or a path-like object.  If path
        is bytes, the names of yielded DirEntry objects will also be bytes; in
        all other circumstances they will be str.

        If path is None, uses the path='.'.

    set_handle_inheritable(handle, inheritable, /)
        Set the inheritable flag of the specified handle.

    set_inheritable(fd, inheritable, /)
        Set the inheritable flag of the specified file descriptor.

    spawnl(mode, file, *args)
        spawnl(mode, file, *args) -> integer

        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.

    spawnle(mode, file, *args)
        spawnle(mode, file, *args, env) -> integer

        Execute file with arguments from args in a subprocess with the
        supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.

    spawnv(mode, path, argv, /)
        Execute the program specified by path in a new process.

        mode
          Mode of process creation.
        path
          Path of executable file.
        argv
          Tuple or list of strings.

    spawnve(mode, path, argv, env, /)
        Execute the program specified by path in a new process.

        mode
          Mode of process creation.
        path
          Path of executable file.
        argv
          Tuple or list of strings.
        env
          Dictionary of strings mapping to strings.

    startfile(filepath, operation=None)
        startfile(filepath [, operation])

        Start a file with its associated application.

        When "operation" is not specified or "open", this acts like
        double-clicking the file in Explorer, or giving the file name as an
        argument to the DOS "start" command: the file is opened with whatever
        application (if any) its extension is associated.
        When another "operation" is given, it specifies what should be done with
        the file.  A typical operation is "print".

        startfile returns as soon as the associated application is launched.
        There is no option to wait for the application to close, and no way
        to retrieve the application's exit status.

        The filepath is relative to the current directory.  If you want to use
        an absolute path, make sure the first character is not a slash ("/");
        the underlying Win32 ShellExecute function doesn't work if it is.

    stat(path, *, dir_fd=None, follow_symlinks=True)
        Perform a stat system call on the given path.

          path
            Path to be examined; can be string, bytes, a path-like object or
            open-file-descriptor int.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be a relative string; path will then be relative to
            that directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            stat will examine the symbolic link itself instead of the file
            the link points to.

        dir_fd and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.

        It's an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.

    strerror(code, /)
        Translate an error code to a message string.

    symlink(src, dst, target_is_directory=False, *, dir_fd=None)
        Create a symbolic link pointing to src named dst.

        target_is_directory is required on Windows if the target is to be
          interpreted as a directory.  (On Windows, symlink requires
          Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
          target_is_directory is ignored on non-Windows platforms.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

    system(command)
        Execute the command in a subshell.

    times()
        Return a collection containing process timing information.

        The object returned behaves like a named tuple with these fields:
          (utime, stime, cutime, cstime, elapsed_time)
        All fields are floating point numbers.

    truncate(path, length)
        Truncate a file, specified by path, to a specific length.

        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.

    umask(mask, /)
        Set the current numeric umask and return the previous umask.

    unlink(path, *, dir_fd=None)
        Remove a file (same as remove()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

    urandom(size, /)
        Return a bytes object containing random bytes suitable for cryptographic use.

    utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True)
        Set the access and modified time of path.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.

        If times is not None, it must be a tuple (atime, mtime);
            atime and mtime should be expressed as float seconds since the epoch.
        If ns is specified, it must be a tuple (atime_ns, mtime_ns);
            atime_ns and mtime_ns should be expressed as integer nanoseconds
            since the epoch.
        If times is None and ns is unspecified, utime uses the current time.
        Specifying tuples for both times and ns is an error.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, utime will modify the symbolic link itself instead of the file the
          link points to.
        It is an error to use dir_fd or follow_symlinks when specifying path
          as an open file descriptor.
        dir_fd and follow_symlinks may not be available on your platform.
          If they are unavailable, using them will raise a NotImplementedError.

    waitpid(pid, options, /)
        Wait for completion of a given process.

        Returns a tuple of information regarding the process:
            (pid, status << 8)

        The options argument is ignored on Windows.

    walk(top, topdown=True, onerror=None, followlinks=False)
        Directory tree generator.

        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple

            dirpath, dirnames, filenames

        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).

        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).

        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune the
        search, or to impose a specific order of visiting.  Modifying dirnames when
        topdown is false has no effect on the behavior of os.walk(), since the
        directories in dirnames have already been generated by the time dirnames
        itself is generated. No matter the value of topdown, the list of
        subdirectories is retrieved before the tuples for the directory and its
        subdirectories are generated.

        By default errors from the os.scandir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an OSError instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.

        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.

        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.

        Example:

        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum([getsize(join(root, name)) for name in files]), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories

    write(fd, data, /)
        Write a bytes object to a file descriptor.

DATA
    F_OK = 0
    O_APPEND = 8
    O_BINARY = 32768
    O_CREAT = 256
    O_EXCL = 1024
    O_NOINHERIT = 128
    O_RANDOM = 16
    O_RDONLY = 0
    O_RDWR = 2
    O_SEQUENTIAL = 32
    O_SHORT_LIVED = 4096
    O_TEMPORARY = 64
    O_TEXT = 16384
    O_TRUNC = 512
    O_WRONLY = 1
    P_DETACH = 4
    P_NOWAIT = 1
    P_NOWAITO = 3
    P_OVERLAY = 2
    P_WAIT = 0
    R_OK = 4
    SEEK_CUR = 1
    SEEK_END = 2
    SEEK_SET = 0
    TMP_MAX = 2147483647
    W_OK = 2
    X_OK = 1
    __all__ = ['altsep', 'curdir', 'pardir', 'sep', 'pathsep', 'linesep', ...
    altsep = '/'
    curdir = '.'
    defpath = r'.;C:\bin'
    devnull = 'nul'
    environ = environ({'ALLUSERSPROFILE': 'C:\\ProgramData', '... 'C:\\Use...
    extsep = '.'
    linesep = '\r\n'
    name = 'nt'
    pardir = '..'
    pathsep = ';'
    sep = r'\'
    supports_bytes_environ = False


"""

import os

print(os.sep)  # \
print(os.pathsep)  # ;

print(os.getpid())  # 15432

print(os.getcwd())  # C:\Users\dsharman\Python_Workspace\Python_Basics\Python Default Modules

print(os.listdir())  # ['GetPass Module.py', 'Math Module.py', 'OS Module.py', 'Platform Module.py', 'Sys Module.py']

print(os.listdir(
    'C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Basics of Python'))  # ['Arithmetic_Operations.py', 'Assignment_Operations.py', 'Bitwise_Operations.py', 'Comparision Operations.py', 'Dictionary_DataStructure_Functions.py', 'Eval_Input_Function.py', 'Identity_Operations.py', 'List_DataStructure_Functions.py', 'Logical_Operations.py', 'Membership_Operations.py', 'Set_DataStructure_Functions.py', 'String_Variable_Functions.py', 'Tuples_DataStructure_Functions.py']

os.chdir("C:\\Users\\dsharman")
print(os.getcwd())
print(os.listdir())

os.mkdir("SampleTestFile")

print(os.listdir())

os.rmdir("SampleTestFile")

print(
    os.environ)  # environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\dsharman\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'HIBACL99648', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\dsharman', 'IDEA_INITIAL_DIRECTORY': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\jbr\\bin', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.8.0_281', 'LOCALAPPDATA': 'C:\\Users\\dsharman\\AppData\\Local', 'LOGONSERVER': '\\\\INBAW16DCAD02', 'MAVEN_HOME': 'C:\\Selenium_Artifacts\\apache-maven-3.8.1-bin\\apache-maven-3.8.1', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\dsharman\\OneDrive - HARMAN', 'ONEDRIVECOMMERCIAL': 'C:\\Users\\dsharman\\OneDrive - HARMAN', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\dsharman\\Python_Workspace\\venv\\Scripts;C:\\Program Files\\Python37\\Scripts\\;C:\\Program Files\\Python37\\;C:\\Program Files\\Python39\\Scripts\\;C:\\Program Files\\Python39\\;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Webex\\Plugins;C:\\Program Files\\Git\\cmd;C:\\Program Files\\PuTTY\\;C:\\Program Files (x86)\\Sennheiser\\SenncomSDK\\;C:\\Program Files\\Java\\jdk1.8.0_281\\bin;C:\\Program Files\\Java\\jdk1.8.0_281\\jre1.8.0_281\\bin;C:\\Selenium_Artifacts\\apache-maven-3.8.1-bin\\apache-maven-3.8.1\\bin;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\ProgramData\\DockerDesktop\\version-bin;C:\\Program Files\\nodejs\\;C:\\Users\\dsharman\\AppData\\Local\\Programs\\Python\\Python39\\Scripts;C:\\Users\\dsharman\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\dsharman\\AppData\\Local\\GitHubDesktop\\bin;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin;C:\\Users\\dsharman\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\dsharman\\AppData\\Roaming\\npm;C:\\Users\\dsharman\\AppData\\Local\\Programs\\Fiddler;C:\\Users\\dsharman\\AppData\\Roaming\\Python\\Python37\\Scripts;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 78 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '4e03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files (x86)\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\AutoIt3\\AutoItX', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM COMMUNITY EDITION': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin;', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\dsharman\\Python_Workspace', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\dsharman\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\dsharman\\AppData\\Local\\Temp', 'UATDATA': 'C:\\WINDOWS\\CCM\\UATData\\D9F8C395-CAB8-491d-B8AC-179A1FE1BE77', 'USERDNSDOMAIN': 'AD.HARMAN.COM', 'USERDOMAIN': 'ADHARMAN', 'USERDOMAIN_ROAMINGPROFILE': 'ADHARMAN', 'USERNAME': 'dsharman', 'USERPROFILE': 'C:\\Users\\dsharman', 'VIRTUAL_ENV': 'C:\\Users\\dsharman\\Python_Workspace\\venv', 'WINDIR': 'C:\\WINDOWS', '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Python37\\Scripts\\;C:\\Program Files\\Python37\\;C:\\Program Files\\Python39\\Scripts\\;C:\\Program Files\\Python39\\;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Webex\\Plugins;C:\\Program Files\\Git\\cmd;C:\\Program Files\\PuTTY\\;C:\\Program Files (x86)\\Sennheiser\\SenncomSDK\\;C:\\Program Files\\Java\\jdk1.8.0_281\\bin;C:\\Program Files\\Java\\jdk1.8.0_281\\jre1.8.0_281\\bin;C:\\Selenium_Artifacts\\apache-maven-3.8.1-bin\\apache-maven-3.8.1\\bin;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\ProgramData\\DockerDesktop\\version-bin;C:\\Program Files\\nodejs\\;C:\\Users\\dsharman\\AppData\\Local\\Programs\\Python\\Python39\\Scripts;C:\\Users\\dsharman\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\dsharman\\AppData\\Local\\GitHubDesktop\\bin;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin;C:\\Users\\dsharman\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\dsharman\\AppData\\Roaming\\npm;C:\\Users\\dsharman\\AppData\\Local\\Programs\\Fiddler;C:\\Users\\dsharman\\AppData\\Roaming\\Python\\Python37\\Scripts;', '_OLD_VIRTUAL_PROMPT': '$P$G'})

os.chdir('C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Basics of Python')

print(os.getcwd())  # C:\Users\dsharman\Python_Workspace\Python_Basics\Basics of Python

# os.makedirs("C:\\Users\\dsharman\\DemoFiles\\SampleTestFile\\xyzFile")

# os.removedirs("C:\\Users\\dsharman\\DemoFiles\\SampleTestFile\\xyzFile")

print(os.listdir("C:\\Users\\dsharman\\DemoFiles\\SampleTestFile"))  # ['xyzFile']

# os.rename("C:\\Users\\dsharman\\DemoFiles\\SampleTestFile\\xyzFile","C:\\Users\\dsharman\\DemoFiles\\SampleTestFile\\ABCFile")

print(os.listdir("C:\\Users\\dsharman\\DemoFiles\\SampleTestFile"))  # ['ABCFile']

# os.rename("C:\\Users\\dsharman\\DemoFiles\\SampleTestFile\\ABCFile","C:\\Users\\dsharman\\DemoFiles\\SampleTestFile\\xyzFile")

print(
    "=================================   OS PATH SUB MODULE =============================================================")
"""

Help on module ntpath:

NAME
    ntpath - Common pathname manipulations, WindowsNT/95 version.

DESCRIPTION
    Instead of importing this module directly, import os and refer to this
    module as os.path.

FUNCTIONS
    abspath(path)
        Return the absolute version of a path.
    
    basename(p)
        Returns the final component of a pathname
    
    commonpath(paths)
        Given a sequence of path names, returns the longest common sub-path.
    
    commonprefix(m)
        Given a list of pathnames, returns the longest common leading component
    
    dirname(p)
        Returns the directory component of a pathname
    
    exists(path)
        Test whether a path exists.  Returns False for broken symbolic links
    
    expanduser(path)
        Expand ~ and ~user constructs.
        
        If user or $HOME is unknown, do nothing.
    
    expandvars(path)
        Expand shell variables of the forms $var, ${var} and %var%.
        
        Unknown variables are left unchanged.
    
    getatime(filename)
        Return the last access time of a file, reported by os.stat().
    
    getctime(filename)
        Return the metadata change time of a file, reported by os.stat().
    
    getmtime(filename)
        Return the last modification time of a file, reported by os.stat().
    
    getsize(filename)
        Return the size of a file, reported by os.stat().
    
    isabs(s)
        Test whether a path is absolute
    
    isdir = _isdir(path, /)
        Return true if the pathname refers to an existing directory.
    
    isfile(path)
        Test whether a path is a regular file
    
    islink(path)
        Test whether a path is a symbolic link.
        This will always return false for Windows prior to 6.0.
    
    ismount(path)
        Test whether a path is a mount point (a drive root, the root of a
        share, or a mounted volume)
    
    join(path, *paths)
        # Join two (or more) paths.
    
    lexists(path)
        Test whether a path exists.  Returns True for broken symbolic links
    
    normcase(s)
        Normalize case of pathname.
        
        Makes all characters lowercase and all slashes into backslashes.
    
    normpath(path)
        Normalize path, eliminating double slashes, etc.
    
    realpath = abspath(path)
        Return the absolute version of a path.
    
    relpath(path, start=None)
        Return a relative version of a path
    
    samefile(f1, f2)
        Test whether two pathnames reference the same actual file or directory
        
        This is determined by the device number and i-node number and
        raises an exception if an os.stat() call on either pathname fails.
    
    sameopenfile(fp1, fp2)
        Test whether two open file objects reference the same file
    
    samestat(s1, s2)
        Test whether two stat buffers reference the same file
    
    split(p)
        Split a pathname.
        
        Return tuple (head, tail) where tail is everything after the final slash.
        Either part may be empty.
    
    splitdrive(p)
        Split a pathname into drive/UNC sharepoint and relative path specifiers.
        Returns a 2-tuple (drive_or_unc, path); either part may be empty.
        
        If you assign
            result = splitdrive(p)
        It is always true that:
            result[0] + result[1] == p
        
        If the path contained a drive letter, drive_or_unc will contain everything
        up to and including the colon.  e.g. splitdrive("c:/dir") returns ("c:", "/dir")
        
        If the path contained a UNC path, the drive_or_unc will contain the host name
        and share up to but not including the fourth directory separator character.
        e.g. splitdrive("//host/computer/dir") returns ("//host/computer", "/dir")
        
        Paths cannot contain both a drive letter and a UNC path.
    
    splitext(p)
        Split the extension from a pathname.
        
        Extension is everything from the last dot to the end, ignoring
        leading dots.  Returns "(root, ext)"; ext may be empty.

DATA
    __all__ = ['normcase', 'isabs', 'join', 'splitdrive', 'split', 'splite...
    altsep = '/'
    curdir = '.'
    defpath = r'.;C:\bin'
    devnull = 'nul'
    extsep = '.'
    pardir = '..'
    pathsep = ';'
    sep = r'\'
    supports_unicode_filenames = True
    
"""
print(os.path.sep)  # \

print(os.path.pathsep)  # ;

path = "C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Basics of Python\\Arithmetic_Operations.py"

print(os.path.basename(path))  # PythonDemo.py

print(os.path.dirname(path))  # C:\Users\dsharman\Python_Workspace\Python_Basics\Basics of Python

path1 = "C:\\Users\\dsharman\\Python_Workspace"
path2 = "Python_Basics\\Basics of Python\\PythonDemo.py"

Path_List = [path, path1]

print(os.path.join(path1, path2))  # C:\Users\dsharman\Python_Workspace\Python_Basics\Basics of Python\PythonDemo.py

print(
    os.path.split(path))  # ('C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Basics of Python', 'PythonDemo.py')

print(type(os.path.split(path)))  # <class 'tuple'>

print(os.path.getsize(path))  # 1898

print(
    os.path.abspath(path))  # C:\Users\dsharman\Python_Workspace\Python_Basics\Basics of Python\Arithmetic_Operations.py

print(os.path.commonpath(Path_List))  # C:\Users\dsharman\Python_Workspace

print(os.path.exists(path1))  # True

print(os.path.isfile(path))  # True

print(os.path.isdir(path1))  # True

print(os.path.isabs(path2))  # False

print(
    "=================================   OS SYSTEM() SUB MODULE =============================================================")

command = "dir"

os.system(command)  # List Directory

print(os.getcwd())  # C:\Users\dsharman\Python_Workspace\Python_Basics\Basics of Python

command1 = "cd C:\\Intel"

rt = os.system(command1)

print(rt)

print(os.getcwd())

# ==================== To Execute os specific commands we use os.system() =============================

"""

Help on generator object:

walk = class generator(object)
 |  Methods defined here:
 |  
 |  __del__(...)
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  close(...)
 |      close() -> raise GeneratorExit inside generator.
 |  
 |  send(...)
 |      send(arg) -> send 'arg' into generator,
 |      return next yielded value or raise StopIteration.
 |  
 |  throw(...)
 |      throw(typ[,val[,tb]]) -> raise exception in generator,
 |      return next yielded value or raise StopIteration.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  gi_code
 |  
 |  gi_frame
 |  
 |  gi_running
 |  
 |  gi_yieldfrom
 |      object being iterated by yield from, or None
 
 
 OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

root : Prints out directories only from what you specified.
dirs : Prints out sub-directories from root.
files : Prints out all files from root and directories.

tuple = (path,[Directory/folder list],[file list])


"""
print(
    "=================================   OS.main() SUB MODULE =============================================================")

Main_path = "C:\\Users\\dsharman\\Python_Workspace"
add_path = "Python_Basics"
print(os.walk(Main_path))  # <generator object walk at 0x0000024739562D48> return type is a list of tuples

print(list(os.walk(
    Main_path)))  # [('C:\\Users\\dsharman\\Python_Workspace', ['.idea', 'Python Exercise', 'Python_Basics', 'venv'], ['main.py']), ('C:\\Users\\dsharman\\Python_Workspace\\.idea', ['inspectionProfiles'], ['.gitignore', 'misc.xml', 'modules.xml', 'Python_Workspace.iml', 'workspace.xml']), ('C:\\Users\\dsharman\\Python_Workspace\\.idea\\inspectionProfiles', [], ['profiles_settings.xml']), ('C:\\Users\\dsharman\\Python_Workspace\\Python Exercise', [], ['Platform Independent Script to Clear Screen  on any OS.py']), ('C:\\Users\\dsharman\\Python_Workspace\\Python_Basics', ['Basics of Python', 'Python Default Modules'], []), ('C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Basics of Python', [], ['Arithmetic_Operations.py', 'Assignment_Operations.py', 'Bitwise_Operations.py', 'Comparision Operations.py', 'Dictionary_DataStructure_Functions.py', 'Eval_Input_Function.py', 'Identity_Operations.py', 'List_DataStructure_Functions.py', 'Logical_Operations.py', 'Membership_Operations.py', 'Set_DataStructure_Functions.py', 'String_Variable_Functions.py', 'Tuples_DataStructure_Functions.py']), ('C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Python Default Modules', [], ['GetPass Module.py', 'Math Module.py', 'OS Module.py', 'Platform Module.py', 'Sys Module.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv', ['Include', 'Lib', 'Scripts'], ['pyvenv.cfg']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Include', [], []), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib', ['site-packages'], []), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages', ['a-1.0-py3.7.egg-info', 'et_xmlfile', 'et_xmlfile-1.1.0.dist-info', 'openpyxl', 'openpyxl-3.0.7.dist-info', 'pip', 'pip-21.2.2.dist-info', 'pkg_resources', 'setuptools', 'setuptools-57.4.0.dist-info', '_distutils_hack', '__pycache__'], ['a.py', 'distutils-precedence.pth']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\a-1.0-py3.7.egg-info', [], ['dependency_links.txt', 'installed-files.txt', 'PKG-INFO', 'SOURCES.txt', 'top_level.txt']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\et_xmlfile', ['__pycache__'], ['xmlfile.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\et_xmlfile\\__pycache__', [], ['xmlfile.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\et_xmlfile-1.1.0.dist-info', [], ['AUTHORS.txt', 'INSTALLER', 'LICENCE.rst', 'METADATA', 'RECORD', 'top_level.txt', 'WHEEL']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl', ['cell', 'chart', 'chartsheet', 'comments', 'compat', 'descriptors', 'drawing', 'formatting', 'formula', 'packaging', 'pivot', 'reader', 'styles', 'utils', 'workbook', 'worksheet', 'writer', 'xml', '__pycache__'], ['_constants.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\cell', ['__pycache__'], ['cell.py', 'read_only.py', 'text.py', '_writer.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\cell\\__pycache__', [], ['cell.cpython-37.pyc', 'read_only.cpython-37.pyc', 'text.cpython-37.pyc', '_writer.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\chart', ['__pycache__'], ['area_chart.py', 'axis.py', 'bar_chart.py', 'bubble_chart.py', 'chartspace.py', 'data_source.py', 'descriptors.py', 'error_bar.py', 'label.py', 'layout.py', 'legend.py', 'line_chart.py', 'marker.py', 'picture.py', 'pie_chart.py', 'pivot.py', 'plotarea.py', 'print_settings.py', 'radar_chart.py', 'reader.py', 'reference.py', 'scatter_chart.py', 'series.py', 'series_factory.py', 'shapes.py', 'stock_chart.py', 'surface_chart.py', 'text.py', 'title.py', 'trendline.py', 'updown_bars.py', '_3d.py', '_chart.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\chart\\__pycache__', [], ['area_chart.cpython-37.pyc', 'axis.cpython-37.pyc', 'bar_chart.cpython-37.pyc', 'bubble_chart.cpython-37.pyc', 'chartspace.cpython-37.pyc', 'data_source.cpython-37.pyc', 'descriptors.cpython-37.pyc', 'error_bar.cpython-37.pyc', 'label.cpython-37.pyc', 'layout.cpython-37.pyc', 'legend.cpython-37.pyc', 'line_chart.cpython-37.pyc', 'marker.cpython-37.pyc', 'picture.cpython-37.pyc', 'pie_chart.cpython-37.pyc', 'pivot.cpython-37.pyc', 'plotarea.cpython-37.pyc', 'print_settings.cpython-37.pyc', 'radar_chart.cpython-37.pyc', 'reader.cpython-37.pyc', 'reference.cpython-37.pyc', 'scatter_chart.cpython-37.pyc', 'series.cpython-37.pyc', 'series_factory.cpython-37.pyc', 'shapes.cpython-37.pyc', 'stock_chart.cpython-37.pyc', 'surface_chart.cpython-37.pyc', 'text.cpython-37.pyc', 'title.cpython-37.pyc', 'trendline.cpython-37.pyc', 'updown_bars.cpython-37.pyc', '_3d.cpython-37.pyc', '_chart.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\chartsheet', ['__pycache__'], ['chartsheet.py', 'custom.py', 'properties.py', 'protection.py', 'publish.py', 'relation.py', 'views.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\chartsheet\\__pycache__', [], ['chartsheet.cpython-37.pyc', 'custom.cpython-37.pyc', 'properties.cpython-37.pyc', 'protection.cpython-37.pyc', 'publish.cpython-37.pyc', 'relation.cpython-37.pyc', 'views.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\comments', ['__pycache__'], ['author.py', 'comments.py', 'comment_sheet.py', 'shape_writer.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\comments\\__pycache__', [], ['author.cpython-37.pyc', 'comments.cpython-37.pyc', 'comment_sheet.cpython-37.pyc', 'shape_writer.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\compat', ['__pycache__'], ['abc.py', 'numbers.py', 'product.py', 'singleton.py', 'strings.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\compat\\__pycache__', [], ['abc.cpython-37.pyc', 'numbers.cpython-37.pyc', 'product.cpython-37.pyc', 'singleton.cpython-37.pyc', 'strings.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\descriptors', ['__pycache__'], ['base.py', 'excel.py', 'namespace.py', 'nested.py', 'sequence.py', 'serialisable.py', 'slots.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\descriptors\\__pycache__', [], ['base.cpython-37.pyc', 'excel.cpython-37.pyc', 'namespace.cpython-37.pyc', 'nested.cpython-37.pyc', 'sequence.cpython-37.pyc', 'serialisable.cpython-37.pyc', 'slots.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\drawing', ['__pycache__'], ['colors.py', 'connector.py', 'drawing.py', 'effect.py', 'fill.py', 'geometry.py', 'graphic.py', 'image.py', 'line.py', 'picture.py', 'properties.py', 'relation.py', 'spreadsheet_drawing.py', 'text.py', 'xdr.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\drawing\\__pycache__', [], ['colors.cpython-37.pyc', 'connector.cpython-37.pyc', 'drawing.cpython-37.pyc', 'effect.cpython-37.pyc', 'fill.cpython-37.pyc', 'geometry.cpython-37.pyc', 'graphic.cpython-37.pyc', 'image.cpython-37.pyc', 'line.cpython-37.pyc', 'picture.cpython-37.pyc', 'properties.cpython-37.pyc', 'relation.cpython-37.pyc', 'spreadsheet_drawing.cpython-37.pyc', 'text.cpython-37.pyc', 'xdr.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\formatting', ['__pycache__'], ['formatting.py', 'rule.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\formatting\\__pycache__', [], ['formatting.cpython-37.pyc', 'rule.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\formula', ['__pycache__'], ['tokenizer.py', 'translate.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\formula\\__pycache__', [], ['tokenizer.cpython-37.pyc', 'translate.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\packaging', ['__pycache__'], ['core.py', 'extended.py', 'interface.py', 'manifest.py', 'relationship.py', 'workbook.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\packaging\\__pycache__', [], ['core.cpython-37.pyc', 'extended.cpython-37.pyc', 'interface.cpython-37.pyc', 'manifest.cpython-37.pyc', 'relationship.cpython-37.pyc', 'workbook.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\pivot', ['__pycache__'], ['cache.py', 'fields.py', 'record.py', 'table.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\pivot\\__pycache__', [], ['cache.cpython-37.pyc', 'fields.cpython-37.pyc', 'record.cpython-37.pyc', 'table.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\reader', ['__pycache__'], ['drawings.py', 'excel.py', 'strings.py', 'workbook.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\reader\\__pycache__', [], ['drawings.cpython-37.pyc', 'excel.cpython-37.pyc', 'strings.cpython-37.pyc', 'workbook.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\styles', ['__pycache__'], ['alignment.py', 'borders.py', 'builtins.py', 'cell_style.py', 'colors.py', 'differential.py', 'fills.py', 'fonts.py', 'named_styles.py', 'numbers.py', 'protection.py', 'proxy.py', 'styleable.py', 'stylesheet.py', 'table.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\styles\\__pycache__', [], ['alignment.cpython-37.pyc', 'borders.cpython-37.pyc', 'builtins.cpython-37.pyc', 'cell_style.cpython-37.pyc', 'colors.cpython-37.pyc', 'differential.cpython-37.pyc', 'fills.cpython-37.pyc', 'fonts.cpython-37.pyc', 'named_styles.cpython-37.pyc', 'numbers.cpython-37.pyc', 'protection.cpython-37.pyc', 'proxy.cpython-37.pyc', 'styleable.cpython-37.pyc', 'stylesheet.cpython-37.pyc', 'table.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\utils', ['__pycache__'], ['bound_dictionary.py', 'cell.py', 'dataframe.py', 'datetime.py', 'escape.py', 'exceptions.py', 'formulas.py', 'indexed_list.py', 'inference.py', 'protection.py', 'units.py', '_accel.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\utils\\__pycache__', [], ['bound_dictionary.cpython-37.pyc', 'cell.cpython-37.pyc', 'dataframe.cpython-37.pyc', 'datetime.cpython-37.pyc', 'escape.cpython-37.pyc', 'exceptions.cpython-37.pyc', 'formulas.cpython-37.pyc', 'indexed_list.cpython-37.pyc', 'inference.cpython-37.pyc', 'protection.cpython-37.pyc', 'units.cpython-37.pyc', '_accel.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\workbook', ['external_link', '__pycache__'], ['child.py', 'defined_name.py', 'external_reference.py', 'function_group.py', 'properties.py', 'protection.py', 'smart_tags.py', 'views.py', 'web.py', 'workbook.py', '_writer.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\workbook\\external_link', ['__pycache__'], ['external.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\workbook\\external_link\\__pycache__', [], ['external.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\workbook\\__pycache__', [], ['child.cpython-37.pyc', 'defined_name.cpython-37.pyc', 'external_reference.cpython-37.pyc', 'function_group.cpython-37.pyc', 'properties.cpython-37.pyc', 'protection.cpython-37.pyc', 'smart_tags.cpython-37.pyc', 'views.cpython-37.pyc', 'web.cpython-37.pyc', 'workbook.cpython-37.pyc', '_writer.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\worksheet', ['__pycache__'], ['cell_range.py', 'cell_watch.py', 'controls.py', 'copier.py', 'custom.py', 'datavalidation.py', 'dimensions.py', 'drawing.py', 'errors.py', 'filters.py', 'header_footer.py', 'hyperlink.py', 'merge.py', 'ole.py', 'page.py', 'pagebreak.py', 'picture.py', 'properties.py', 'protection.py', 'related.py', 'scenario.py', 'smart_tag.py', 'table.py', 'views.py', 'worksheet.py', '_reader.py', '_read_only.py', '_writer.py', '_write_only.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\worksheet\\__pycache__', [], ['cell_range.cpython-37.pyc', 'cell_watch.cpython-37.pyc', 'controls.cpython-37.pyc', 'copier.cpython-37.pyc', 'custom.cpython-37.pyc', 'datavalidation.cpython-37.pyc', 'dimensions.cpython-37.pyc', 'drawing.cpython-37.pyc', 'errors.cpython-37.pyc', 'filters.cpython-37.pyc', 'header_footer.cpython-37.pyc', 'hyperlink.cpython-37.pyc', 'merge.cpython-37.pyc', 'ole.cpython-37.pyc', 'page.cpython-37.pyc', 'pagebreak.cpython-37.pyc', 'picture.cpython-37.pyc', 'properties.cpython-37.pyc', 'protection.cpython-37.pyc', 'related.cpython-37.pyc', 'scenario.cpython-37.pyc', 'smart_tag.cpython-37.pyc', 'table.cpython-37.pyc', 'views.cpython-37.pyc', 'worksheet.cpython-37.pyc', '_reader.cpython-37.pyc', '_read_only.cpython-37.pyc', '_writer.cpython-37.pyc', '_write_only.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\writer', ['__pycache__'], ['excel.py', 'theme.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\writer\\__pycache__', [], ['excel.cpython-37.pyc', 'theme.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\xml', ['__pycache__'], ['constants.py', 'functions.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\xml\\__pycache__', [], ['constants.cpython-37.pyc', 'functions.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl\\__pycache__', [], ['_constants.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\openpyxl-3.0.7.dist-info', [], ['INSTALLER', 'LICENCE.rst', 'METADATA', 'RECORD', 'REQUESTED', 'top_level.txt', 'WHEEL']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip', ['_internal', '_vendor', '__pycache__'], ['py.typed', '__init__.py', '__main__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal', ['cli', 'commands', 'distributions', 'index', 'locations', 'metadata', 'models', 'network', 'operations', 'req', 'resolution', 'utils', 'vcs', '__pycache__'], ['build_env.py', 'cache.py', 'configuration.py', 'exceptions.py', 'main.py', 'pyproject.py', 'self_outdated_check.py', 'wheel_builder.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\cli', ['__pycache__'], ['autocompletion.py', 'base_command.py', 'cmdoptions.py', 'command_context.py', 'main.py', 'main_parser.py', 'parser.py', 'progress_bars.py', 'req_command.py', 'spinners.py', 'status_codes.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\cli\\__pycache__', [], ['autocompletion.cpython-37.pyc', 'base_command.cpython-37.pyc', 'cmdoptions.cpython-37.pyc', 'command_context.cpython-37.pyc', 'main.cpython-37.pyc', 'main_parser.cpython-37.pyc', 'parser.cpython-37.pyc', 'progress_bars.cpython-37.pyc', 'req_command.cpython-37.pyc', 'spinners.cpython-37.pyc', 'status_codes.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\commands', ['__pycache__'], ['cache.py', 'check.py', 'completion.py', 'configuration.py', 'debug.py', 'download.py', 'freeze.py', 'hash.py', 'help.py', 'index.py', 'install.py', 'list.py', 'search.py', 'show.py', 'uninstall.py', 'wheel.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\commands\\__pycache__', [], ['cache.cpython-37.pyc', 'check.cpython-37.pyc', 'completion.cpython-37.pyc', 'configuration.cpython-37.pyc', 'debug.cpython-37.pyc', 'download.cpython-37.pyc', 'freeze.cpython-37.pyc', 'hash.cpython-37.pyc', 'help.cpython-37.pyc', 'index.cpython-37.pyc', 'install.cpython-37.pyc', 'list.cpython-37.pyc', 'search.cpython-37.pyc', 'show.cpython-37.pyc', 'uninstall.cpython-37.pyc', 'wheel.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\distributions', ['__pycache__'], ['base.py', 'installed.py', 'sdist.py', 'wheel.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\distributions\\__pycache__', [], ['base.cpython-37.pyc', 'installed.cpython-37.pyc', 'sdist.cpython-37.pyc', 'wheel.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\index', ['__pycache__'], ['collector.py', 'package_finder.py', 'sources.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\index\\__pycache__', [], ['collector.cpython-37.pyc', 'package_finder.cpython-37.pyc', 'sources.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\locations', ['__pycache__'], ['base.py', '_distutils.py', '_sysconfig.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\locations\\__pycache__', [], ['base.cpython-37.pyc', '_distutils.cpython-37.pyc', '_sysconfig.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\metadata', ['__pycache__'], ['base.py', 'pkg_resources.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\metadata\\__pycache__', [], ['base.cpython-37.pyc', 'pkg_resources.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\models', ['__pycache__'], ['candidate.py', 'direct_url.py', 'format_control.py', 'index.py', 'link.py', 'scheme.py', 'search_scope.py', 'selection_prefs.py', 'target_python.py', 'wheel.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\models\\__pycache__', [], ['candidate.cpython-37.pyc', 'direct_url.cpython-37.pyc', 'format_control.cpython-37.pyc', 'index.cpython-37.pyc', 'link.cpython-37.pyc', 'scheme.cpython-37.pyc', 'search_scope.cpython-37.pyc', 'selection_prefs.cpython-37.pyc', 'target_python.cpython-37.pyc', 'wheel.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\network', ['__pycache__'], ['auth.py', 'cache.py', 'download.py', 'lazy_wheel.py', 'session.py', 'utils.py', 'xmlrpc.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\network\\__pycache__', [], ['auth.cpython-37.pyc', 'cache.cpython-37.pyc', 'download.cpython-37.pyc', 'lazy_wheel.cpython-37.pyc', 'session.cpython-37.pyc', 'utils.cpython-37.pyc', 'xmlrpc.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\operations', ['build', 'install', '__pycache__'], ['check.py', 'freeze.py', 'prepare.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\operations\\build', ['__pycache__'], ['metadata.py', 'metadata_legacy.py', 'wheel.py', 'wheel_legacy.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\operations\\build\\__pycache__', [], ['metadata.cpython-37.pyc', 'metadata_legacy.cpython-37.pyc', 'wheel.cpython-37.pyc', 'wheel_legacy.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\operations\\install', ['__pycache__'], ['editable_legacy.py', 'legacy.py', 'wheel.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\operations\\install\\__pycache__', [], ['editable_legacy.cpython-37.pyc', 'legacy.cpython-37.pyc', 'wheel.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\operations\\__pycache__', [], ['check.cpython-37.pyc', 'freeze.cpython-37.pyc', 'prepare.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\req', ['__pycache__'], ['constructors.py', 'req_file.py', 'req_install.py', 'req_set.py', 'req_tracker.py', 'req_uninstall.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\req\\__pycache__', [], ['constructors.cpython-37.pyc', 'req_file.cpython-37.pyc', 'req_install.cpython-37.pyc', 'req_set.cpython-37.pyc', 'req_tracker.cpython-37.pyc', 'req_uninstall.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\resolution', ['legacy', 'resolvelib', '__pycache__'], ['base.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\resolution\\legacy', ['__pycache__'], ['resolver.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\resolution\\legacy\\__pycache__', [], ['resolver.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\resolution\\resolvelib', ['__pycache__'], ['base.py', 'candidates.py', 'factory.py', 'found_candidates.py', 'provider.py', 'reporter.py', 'requirements.py', 'resolver.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\resolution\\resolvelib\\__pycache__', [], ['base.cpython-37.pyc', 'candidates.cpython-37.pyc', 'factory.cpython-37.pyc', 'found_candidates.cpython-37.pyc', 'provider.cpython-37.pyc', 'reporter.cpython-37.pyc', 'requirements.cpython-37.pyc', 'resolver.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\resolution\\__pycache__', [], ['base.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\utils', ['__pycache__'], ['appdirs.py', 'compat.py', 'compatibility_tags.py', 'datetime.py', 'deprecation.py', 'direct_url_helpers.py', 'distutils_args.py', 'encoding.py', 'entrypoints.py', 'filesystem.py', 'filetypes.py', 'glibc.py', 'hashes.py', 'inject_securetransport.py', 'logging.py', 'misc.py', 'models.py', 'packaging.py', 'parallel.py', 'pkg_resources.py', 'setuptools_build.py', 'subprocess.py', 'temp_dir.py', 'unpacking.py', 'urls.py', 'virtualenv.py', 'wheel.py', '_log.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\utils\\__pycache__', [], ['appdirs.cpython-37.pyc', 'compat.cpython-37.pyc', 'compatibility_tags.cpython-37.pyc', 'datetime.cpython-37.pyc', 'deprecation.cpython-37.pyc', 'direct_url_helpers.cpython-37.pyc', 'distutils_args.cpython-37.pyc', 'encoding.cpython-37.pyc', 'entrypoints.cpython-37.pyc', 'filesystem.cpython-37.pyc', 'filetypes.cpython-37.pyc', 'glibc.cpython-37.pyc', 'hashes.cpython-37.pyc', 'inject_securetransport.cpython-37.pyc', 'logging.cpython-37.pyc', 'misc.cpython-37.pyc', 'models.cpython-37.pyc', 'packaging.cpython-37.pyc', 'parallel.cpython-37.pyc', 'pkg_resources.cpython-37.pyc', 'setuptools_build.cpython-37.pyc', 'subprocess.cpython-37.pyc', 'temp_dir.cpython-37.pyc', 'unpacking.cpython-37.pyc', 'urls.cpython-37.pyc', 'virtualenv.cpython-37.pyc', 'wheel.cpython-37.pyc', '_log.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\vcs', ['__pycache__'], ['bazaar.py', 'git.py', 'mercurial.py', 'subversion.py', 'versioncontrol.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\vcs\\__pycache__', [], ['bazaar.cpython-37.pyc', 'git.cpython-37.pyc', 'mercurial.cpython-37.pyc', 'subversion.cpython-37.pyc', 'versioncontrol.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_internal\\__pycache__', [], ['build_env.cpython-37.pyc', 'cache.cpython-37.pyc', 'configuration.cpython-37.pyc', 'exceptions.cpython-37.pyc', 'main.cpython-37.pyc', 'pyproject.cpython-37.pyc', 'self_outdated_check.cpython-37.pyc', 'wheel_builder.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor', ['cachecontrol', 'certifi', 'chardet', 'colorama', 'distlib', 'html5lib', 'idna', 'msgpack', 'packaging', 'pep517', 'pkg_resources', 'progress', 'requests', 'resolvelib', 'tenacity', 'tomli', 'urllib3', 'webencodings', '__pycache__'], ['appdirs.py', 'distro.py', 'pyparsing.py', 'six.py', 'vendor.txt', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\cachecontrol', ['caches', '__pycache__'], ['adapter.py', 'cache.py', 'compat.py', 'controller.py', 'filewrapper.py', 'heuristics.py', 'serialize.py', 'wrapper.py', '_cmd.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\cachecontrol\\caches', ['__pycache__'], ['file_cache.py', 'redis_cache.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\cachecontrol\\caches\\__pycache__', [], ['file_cache.cpython-37.pyc', 'redis_cache.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\cachecontrol\\__pycache__', [], ['adapter.cpython-37.pyc', 'cache.cpython-37.pyc', 'compat.cpython-37.pyc', 'controller.cpython-37.pyc', 'filewrapper.cpython-37.pyc', 'heuristics.cpython-37.pyc', 'serialize.cpython-37.pyc', 'wrapper.cpython-37.pyc', '_cmd.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\certifi', ['__pycache__'], ['cacert.pem', 'core.py', '__init__.py', '__main__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\certifi\\__pycache__', [], ['core.cpython-37.pyc', '__init__.cpython-37.pyc', '__main__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\chardet', ['cli', 'metadata', '__pycache__'], ['big5freq.py', 'big5prober.py', 'chardistribution.py', 'charsetgroupprober.py', 'charsetprober.py', 'codingstatemachine.py', 'compat.py', 'cp949prober.py', 'enums.py', 'escprober.py', 'escsm.py', 'eucjpprober.py', 'euckrfreq.py', 'euckrprober.py', 'euctwfreq.py', 'euctwprober.py', 'gb2312freq.py', 'gb2312prober.py', 'hebrewprober.py', 'jisfreq.py', 'jpcntx.py', 'langbulgarianmodel.py', 'langgreekmodel.py', 'langhebrewmodel.py', 'langhungarianmodel.py', 'langrussianmodel.py', 'langthaimodel.py', 'langturkishmodel.py', 'latin1prober.py', 'mbcharsetprober.py', 'mbcsgroupprober.py', 'mbcssm.py', 'sbcharsetprober.py', 'sbcsgroupprober.py', 'sjisprober.py', 'universaldetector.py', 'utf8prober.py', 'version.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\chardet\\cli', ['__pycache__'], ['chardetect.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\chardet\\cli\\__pycache__', [], ['chardetect.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\chardet\\metadata', ['__pycache__'], ['languages.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\chardet\\metadata\\__pycache__', [], ['languages.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\chardet\\__pycache__', [], ['big5freq.cpython-37.pyc', 'big5prober.cpython-37.pyc', 'chardistribution.cpython-37.pyc', 'charsetgroupprober.cpython-37.pyc', 'charsetprober.cpython-37.pyc', 'codingstatemachine.cpython-37.pyc', 'compat.cpython-37.pyc', 'cp949prober.cpython-37.pyc', 'enums.cpython-37.pyc', 'escprober.cpython-37.pyc', 'escsm.cpython-37.pyc', 'eucjpprober.cpython-37.pyc', 'euckrfreq.cpython-37.pyc', 'euckrprober.cpython-37.pyc', 'euctwfreq.cpython-37.pyc', 'euctwprober.cpython-37.pyc', 'gb2312freq.cpython-37.pyc', 'gb2312prober.cpython-37.pyc', 'hebrewprober.cpython-37.pyc', 'jisfreq.cpython-37.pyc', 'jpcntx.cpython-37.pyc', 'langbulgarianmodel.cpython-37.pyc', 'langgreekmodel.cpython-37.pyc', 'langhebrewmodel.cpython-37.pyc', 'langhungarianmodel.cpython-37.pyc', 'langrussianmodel.cpython-37.pyc', 'langthaimodel.cpython-37.pyc', 'langturkishmodel.cpython-37.pyc', 'latin1prober.cpython-37.pyc', 'mbcharsetprober.cpython-37.pyc', 'mbcsgroupprober.cpython-37.pyc', 'mbcssm.cpython-37.pyc', 'sbcharsetprober.cpython-37.pyc', 'sbcsgroupprober.cpython-37.pyc', 'sjisprober.cpython-37.pyc', 'universaldetector.cpython-37.pyc', 'utf8prober.cpython-37.pyc', 'version.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\colorama', ['__pycache__'], ['ansi.py', 'ansitowin32.py', 'initialise.py', 'win32.py', 'winterm.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\colorama\\__pycache__', [], ['ansi.cpython-37.pyc', 'ansitowin32.cpython-37.pyc', 'initialise.cpython-37.pyc', 'win32.cpython-37.pyc', 'winterm.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\distlib', ['_backport', '__pycache__'], ['compat.py', 'database.py', 'index.py', 'locators.py', 'manifest.py', 'markers.py', 'metadata.py', 'resources.py', 'scripts.py', 't32.exe', 't64.exe', 'util.py', 'version.py', 'w32.exe', 'w64.exe', 'wheel.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\distlib\\_backport', ['__pycache__'], ['misc.py', 'shutil.py', 'sysconfig.cfg', 'sysconfig.py', 'tarfile.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\distlib\\_backport\\__pycache__', [], ['misc.cpython-37.pyc', 'shutil.cpython-37.pyc', 'sysconfig.cpython-37.pyc', 'tarfile.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\distlib\\__pycache__', [], ['compat.cpython-37.pyc', 'database.cpython-37.pyc', 'index.cpython-37.pyc', 'locators.cpython-37.pyc', 'manifest.cpython-37.pyc', 'markers.cpython-37.pyc', 'metadata.cpython-37.pyc', 'resources.cpython-37.pyc', 'scripts.cpython-37.pyc', 'util.cpython-37.pyc', 'version.cpython-37.pyc', 'wheel.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib', ['filters', 'treeadapters', 'treebuilders', 'treewalkers', '_trie', '__pycache__'], ['constants.py', 'html5parser.py', 'serializer.py', '_ihatexml.py', '_inputstream.py', '_tokenizer.py', '_utils.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\filters', ['__pycache__'], ['alphabeticalattributes.py', 'base.py', 'inject_meta_charset.py', 'lint.py', 'optionaltags.py', 'sanitizer.py', 'whitespace.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\filters\\__pycache__', [], ['alphabeticalattributes.cpython-37.pyc', 'base.cpython-37.pyc', 'inject_meta_charset.cpython-37.pyc', 'lint.cpython-37.pyc', 'optionaltags.cpython-37.pyc', 'sanitizer.cpython-37.pyc', 'whitespace.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\treeadapters', ['__pycache__'], ['genshi.py', 'sax.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\treeadapters\\__pycache__', [], ['genshi.cpython-37.pyc', 'sax.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\treebuilders', ['__pycache__'], ['base.py', 'dom.py', 'etree.py', 'etree_lxml.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\treebuilders\\__pycache__', [], ['base.cpython-37.pyc', 'dom.cpython-37.pyc', 'etree.cpython-37.pyc', 'etree_lxml.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\treewalkers', ['__pycache__'], ['base.py', 'dom.py', 'etree.py', 'etree_lxml.py', 'genshi.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\treewalkers\\__pycache__', [], ['base.cpython-37.pyc', 'dom.cpython-37.pyc', 'etree.cpython-37.pyc', 'etree_lxml.cpython-37.pyc', 'genshi.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\_trie', ['__pycache__'], ['py.py', '_base.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\_trie\\__pycache__', [], ['py.cpython-37.pyc', '_base.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\html5lib\\__pycache__', [], ['constants.cpython-37.pyc', 'html5parser.cpython-37.pyc', 'serializer.cpython-37.pyc', '_ihatexml.cpython-37.pyc', '_inputstream.cpython-37.pyc', '_tokenizer.cpython-37.pyc', '_utils.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\idna', ['__pycache__'], ['codec.py', 'compat.py', 'core.py', 'idnadata.py', 'intranges.py', 'package_data.py', 'uts46data.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\idna\\__pycache__', [], ['codec.cpython-37.pyc', 'compat.cpython-37.pyc', 'core.cpython-37.pyc', 'idnadata.cpython-37.pyc', 'intranges.cpython-37.pyc', 'package_data.cpython-37.pyc', 'uts46data.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\msgpack', ['__pycache__'], ['exceptions.py', 'ext.py', 'fallback.py', '_version.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\msgpack\\__pycache__', [], ['exceptions.cpython-37.pyc', 'ext.cpython-37.pyc', 'fallback.cpython-37.pyc', '_version.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\packaging', ['__pycache__'], ['markers.py', 'requirements.py', 'specifiers.py', 'tags.py', 'utils.py', 'version.py', '_manylinux.py', '_musllinux.py', '_structures.py', '__about__.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\packaging\\__pycache__', [], ['markers.cpython-37.pyc', 'requirements.cpython-37.pyc', 'specifiers.cpython-37.pyc', 'tags.cpython-37.pyc', 'utils.cpython-37.pyc', 'version.cpython-37.pyc', '_manylinux.cpython-37.pyc', '_musllinux.cpython-37.pyc', '_structures.cpython-37.pyc', '__about__.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\pep517', ['in_process', '__pycache__'], ['build.py', 'check.py', 'colorlog.py', 'compat.py', 'dirtools.py', 'envbuild.py', 'meta.py', 'wrappers.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\pep517\\in_process', ['__pycache__'], ['_in_process.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\pep517\\in_process\\__pycache__', [], ['_in_process.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\pep517\\__pycache__', [], ['build.cpython-37.pyc', 'check.cpython-37.pyc', 'colorlog.cpython-37.pyc', 'compat.cpython-37.pyc', 'dirtools.cpython-37.pyc', 'envbuild.cpython-37.pyc', 'meta.cpython-37.pyc', 'wrappers.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\pkg_resources', ['__pycache__'], ['py31compat.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\pkg_resources\\__pycache__', [], ['py31compat.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\progress', ['__pycache__'], ['bar.py', 'counter.py', 'spinner.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\progress\\__pycache__', [], ['bar.cpython-37.pyc', 'counter.cpython-37.pyc', 'spinner.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\requests', ['__pycache__'], ['adapters.py', 'api.py', 'auth.py', 'certs.py', 'compat.py', 'cookies.py', 'exceptions.py', 'help.py', 'hooks.py', 'models.py', 'packages.py', 'sessions.py', 'status_codes.py', 'structures.py', 'utils.py', '_internal_utils.py', '__init__.py', '__version__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\requests\\__pycache__', [], ['adapters.cpython-37.pyc', 'api.cpython-37.pyc', 'auth.cpython-37.pyc', 'certs.cpython-37.pyc', 'compat.cpython-37.pyc', 'cookies.cpython-37.pyc', 'exceptions.cpython-37.pyc', 'help.cpython-37.pyc', 'hooks.cpython-37.pyc', 'models.cpython-37.pyc', 'packages.cpython-37.pyc', 'sessions.cpython-37.pyc', 'status_codes.cpython-37.pyc', 'structures.cpython-37.pyc', 'utils.cpython-37.pyc', '_internal_utils.cpython-37.pyc', '__init__.cpython-37.pyc', '__version__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\resolvelib', ['compat', '__pycache__'], ['providers.py', 'reporters.py', 'resolvers.py', 'structs.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\resolvelib\\compat', ['__pycache__'], ['collections_abc.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\resolvelib\\compat\\__pycache__', [], ['collections_abc.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\resolvelib\\__pycache__', [], ['providers.cpython-37.pyc', 'reporters.cpython-37.pyc', 'resolvers.cpython-37.pyc', 'structs.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\tenacity', ['__pycache__'], ['after.py', 'before.py', 'before_sleep.py', 'nap.py', 'retry.py', 'stop.py', 'tornadoweb.py', 'wait.py', '_asyncio.py', '_utils.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\tenacity\\__pycache__', [], ['after.cpython-37.pyc', 'before.cpython-37.pyc', 'before_sleep.cpython-37.pyc', 'nap.cpython-37.pyc', 'retry.cpython-37.pyc', 'stop.cpython-37.pyc', 'tornadoweb.cpython-37.pyc', 'wait.cpython-37.pyc', '_asyncio.cpython-37.pyc', '_utils.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\tomli', ['__pycache__'], ['_parser.py', '_re.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\tomli\\__pycache__', [], ['_parser.cpython-37.pyc', '_re.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3', ['contrib', 'packages', 'util', '__pycache__'], ['connection.py', 'connectionpool.py', 'exceptions.py', 'fields.py', 'filepost.py', 'poolmanager.py', 'request.py', 'response.py', '_collections.py', '_version.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\contrib', ['_securetransport', '__pycache__'], ['appengine.py', 'ntlmpool.py', 'pyopenssl.py', 'securetransport.py', 'socks.py', '_appengine_environ.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\contrib\\_securetransport', ['__pycache__'], ['bindings.py', 'low_level.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\contrib\\_securetransport\\__pycache__', [], ['bindings.cpython-37.pyc', 'low_level.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\contrib\\__pycache__', [], ['appengine.cpython-37.pyc', 'ntlmpool.cpython-37.pyc', 'pyopenssl.cpython-37.pyc', 'securetransport.cpython-37.pyc', 'socks.cpython-37.pyc', '_appengine_environ.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\packages', ['backports', 'ssl_match_hostname', '__pycache__'], ['six.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\packages\\backports', ['__pycache__'], ['makefile.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\packages\\backports\\__pycache__', [], ['makefile.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\packages\\ssl_match_hostname', ['__pycache__'], ['_implementation.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\packages\\ssl_match_hostname\\__pycache__', [], ['_implementation.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\packages\\__pycache__', [], ['six.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\util', ['__pycache__'], ['connection.py', 'proxy.py', 'queue.py', 'request.py', 'response.py', 'retry.py', 'ssltransport.py', 'ssl_.py', 'timeout.py', 'url.py', 'wait.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\util\\__pycache__', [], ['connection.cpython-37.pyc', 'proxy.cpython-37.pyc', 'queue.cpython-37.pyc', 'request.cpython-37.pyc', 'response.cpython-37.pyc', 'retry.cpython-37.pyc', 'ssltransport.cpython-37.pyc', 'ssl_.cpython-37.pyc', 'timeout.cpython-37.pyc', 'url.cpython-37.pyc', 'wait.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\urllib3\\__pycache__', [], ['connection.cpython-37.pyc', 'connectionpool.cpython-37.pyc', 'exceptions.cpython-37.pyc', 'fields.cpython-37.pyc', 'filepost.cpython-37.pyc', 'poolmanager.cpython-37.pyc', 'request.cpython-37.pyc', 'response.cpython-37.pyc', '_collections.cpython-37.pyc', '_version.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\webencodings', ['__pycache__'], ['labels.py', 'mklabels.py', 'tests.py', 'x_user_defined.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\webencodings\\__pycache__', [], ['labels.cpython-37.pyc', 'mklabels.cpython-37.pyc', 'tests.cpython-37.pyc', 'x_user_defined.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\_vendor\\__pycache__', [], ['appdirs.cpython-37.pyc', 'distro.cpython-37.pyc', 'pyparsing.cpython-37.pyc', 'six.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip\\__pycache__', [], ['__init__.cpython-37.pyc', '__main__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pip-21.2.2.dist-info', [], ['entry_points.txt', 'INSTALLER', 'LICENSE.txt', 'METADATA', 'RECORD', 'top_level.txt', 'WHEEL']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources', ['extern', 'tests', '_vendor', '__pycache__'], ['__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\extern', ['__pycache__'], ['__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\extern\\__pycache__', [], ['__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\tests', ['data'], []), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\tests\\data', ['my-test-package-source'], []), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\tests\\data\\my-test-package-source', ['__pycache__'], ['setup.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\tests\\data\\my-test-package-source\\__pycache__', [], ['setup.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\_vendor', ['packaging', '__pycache__'], ['appdirs.py', 'pyparsing.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\_vendor\\packaging', ['__pycache__'], ['markers.py', 'requirements.py', 'specifiers.py', 'tags.py', 'utils.py', 'version.py', '_compat.py', '_structures.py', '_typing.py', '__about__.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\_vendor\\packaging\\__pycache__', [], ['markers.cpython-37.pyc', 'requirements.cpython-37.pyc', 'specifiers.cpython-37.pyc', 'tags.cpython-37.pyc', 'utils.cpython-37.pyc', 'version.cpython-37.pyc', '_compat.cpython-37.pyc', '_structures.cpython-37.pyc', '_typing.cpython-37.pyc', '__about__.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\_vendor\\__pycache__', [], ['appdirs.cpython-37.pyc', 'pyparsing.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\pkg_resources\\__pycache__', [], ['__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools', ['command', 'extern', '_distutils', '_vendor', '__pycache__'], ['archive_util.py', 'build_meta.py', 'cli-32.exe', 'cli-64.exe', 'cli.exe', 'config.py', 'depends.py', 'dep_util.py', 'dist.py', 'errors.py', 'extension.py', 'glob.py', 'gui-32.exe', 'gui-64.exe', 'gui.exe', 'installer.py', 'launch.py', 'lib2to3_ex.py', 'monkey.py', 'msvc.py', 'namespaces.py', 'package_index.py', 'py34compat.py', 'sandbox.py', 'script (dev).tmpl', 'script.tmpl', 'unicode_utils.py', 'version.py', 'wheel.py', 'windows_support.py', '_deprecation_warning.py', '_imp.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\command', ['__pycache__'], ['alias.py', 'bdist_egg.py', 'bdist_rpm.py', 'build_clib.py', 'build_ext.py', 'build_py.py', 'develop.py', 'dist_info.py', 'easy_install.py', 'egg_info.py', 'install.py', 'install_egg_info.py', 'install_lib.py', 'install_scripts.py', 'launcher manifest.xml', 'py36compat.py', 'register.py', 'rotate.py', 'saveopts.py', 'sdist.py', 'setopt.py', 'test.py', 'upload.py', 'upload_docs.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\command\\__pycache__', [], ['alias.cpython-37.pyc', 'bdist_egg.cpython-37.pyc', 'bdist_rpm.cpython-37.pyc', 'build_clib.cpython-37.pyc', 'build_ext.cpython-37.pyc', 'build_py.cpython-37.pyc', 'develop.cpython-37.pyc', 'dist_info.cpython-37.pyc', 'easy_install.cpython-37.pyc', 'egg_info.cpython-37.pyc', 'install.cpython-37.pyc', 'install_egg_info.cpython-37.pyc', 'install_lib.cpython-37.pyc', 'install_scripts.cpython-37.pyc', 'py36compat.cpython-37.pyc', 'register.cpython-37.pyc', 'rotate.cpython-37.pyc', 'saveopts.cpython-37.pyc', 'sdist.cpython-37.pyc', 'setopt.cpython-37.pyc', 'test.cpython-37.pyc', 'upload.cpython-37.pyc', 'upload_docs.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\extern', ['__pycache__'], ['__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\extern\\__pycache__', [], ['__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_distutils', ['command', '__pycache__'], ['archive_util.py', 'bcppcompiler.py', 'ccompiler.py', 'cmd.py', 'config.py', 'core.py', 'cygwinccompiler.py', 'debug.py', 'dep_util.py', 'dir_util.py', 'dist.py', 'errors.py', 'extension.py', 'fancy_getopt.py', 'filelist.py', 'file_util.py', 'log.py', 'msvc9compiler.py', 'msvccompiler.py', 'py35compat.py', 'py38compat.py', 'spawn.py', 'sysconfig.py', 'text_file.py', 'unixccompiler.py', 'util.py', 'version.py', 'versionpredicate.py', '_msvccompiler.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_distutils\\command', ['__pycache__'], ['bdist.py', 'bdist_dumb.py', 'bdist_msi.py', 'bdist_rpm.py', 'bdist_wininst.py', 'build.py', 'build_clib.py', 'build_ext.py', 'build_py.py', 'build_scripts.py', 'check.py', 'clean.py', 'config.py', 'install.py', 'install_data.py', 'install_egg_info.py', 'install_headers.py', 'install_lib.py', 'install_scripts.py', 'py37compat.py', 'register.py', 'sdist.py', 'upload.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_distutils\\command\\__pycache__', [], ['bdist.cpython-37.pyc', 'bdist_dumb.cpython-37.pyc', 'bdist_msi.cpython-37.pyc', 'bdist_rpm.cpython-37.pyc', 'bdist_wininst.cpython-37.pyc', 'build.cpython-37.pyc', 'build_clib.cpython-37.pyc', 'build_ext.cpython-37.pyc', 'build_py.cpython-37.pyc', 'build_scripts.cpython-37.pyc', 'check.cpython-37.pyc', 'clean.cpython-37.pyc', 'config.cpython-37.pyc', 'install.cpython-37.pyc', 'install_data.cpython-37.pyc', 'install_egg_info.cpython-37.pyc', 'install_headers.cpython-37.pyc', 'install_lib.cpython-37.pyc', 'install_scripts.cpython-37.pyc', 'py37compat.cpython-37.pyc', 'register.cpython-37.pyc', 'sdist.cpython-37.pyc', 'upload.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_distutils\\__pycache__', [], ['archive_util.cpython-37.pyc', 'bcppcompiler.cpython-37.pyc', 'ccompiler.cpython-37.pyc', 'cmd.cpython-37.pyc', 'config.cpython-37.pyc', 'core.cpython-37.pyc', 'cygwinccompiler.cpython-37.pyc', 'debug.cpython-37.pyc', 'dep_util.cpython-37.pyc', 'dir_util.cpython-37.pyc', 'dist.cpython-37.pyc', 'errors.cpython-37.pyc', 'extension.cpython-37.pyc', 'fancy_getopt.cpython-37.pyc', 'filelist.cpython-37.pyc', 'file_util.cpython-37.pyc', 'log.cpython-37.pyc', 'msvc9compiler.cpython-37.pyc', 'msvccompiler.cpython-37.pyc', 'py35compat.cpython-37.pyc', 'py38compat.cpython-37.pyc', 'spawn.cpython-37.pyc', 'sysconfig.cpython-37.pyc', 'text_file.cpython-37.pyc', 'unixccompiler.cpython-37.pyc', 'util.cpython-37.pyc', 'version.cpython-37.pyc', 'versionpredicate.cpython-37.pyc', '_msvccompiler.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_vendor', ['more_itertools', 'packaging', '__pycache__'], ['ordered_set.py', 'pyparsing.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_vendor\\more_itertools', ['__pycache__'], ['more.py', 'recipes.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_vendor\\more_itertools\\__pycache__', [], ['more.cpython-37.pyc', 'recipes.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_vendor\\packaging', ['__pycache__'], ['markers.py', 'requirements.py', 'specifiers.py', 'tags.py', 'utils.py', 'version.py', '_compat.py', '_structures.py', '_typing.py', '__about__.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_vendor\\packaging\\__pycache__', [], ['markers.cpython-37.pyc', 'requirements.cpython-37.pyc', 'specifiers.cpython-37.pyc', 'tags.cpython-37.pyc', 'utils.cpython-37.pyc', 'version.cpython-37.pyc', '_compat.cpython-37.pyc', '_structures.cpython-37.pyc', '_typing.cpython-37.pyc', '__about__.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\_vendor\\__pycache__', [], ['ordered_set.cpython-37.pyc', 'pyparsing.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools\\__pycache__', [], ['archive_util.cpython-37.pyc', 'build_meta.cpython-37.pyc', 'config.cpython-37.pyc', 'depends.cpython-37.pyc', 'dep_util.cpython-37.pyc', 'dist.cpython-37.pyc', 'errors.cpython-37.pyc', 'extension.cpython-37.pyc', 'glob.cpython-37.pyc', 'installer.cpython-37.pyc', 'launch.cpython-37.pyc', 'lib2to3_ex.cpython-37.pyc', 'monkey.cpython-37.pyc', 'msvc.cpython-37.pyc', 'namespaces.cpython-37.pyc', 'package_index.cpython-37.pyc', 'py34compat.cpython-37.pyc', 'sandbox.cpython-37.pyc', 'unicode_utils.cpython-37.pyc', 'version.cpython-37.pyc', 'wheel.cpython-37.pyc', 'windows_support.cpython-37.pyc', '_deprecation_warning.cpython-37.pyc', '_imp.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\setuptools-57.4.0.dist-info', [], ['entry_points.txt', 'INSTALLER', 'LICENSE', 'METADATA', 'RECORD', 'top_level.txt', 'WHEEL']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\_distutils_hack', ['__pycache__'], ['override.py', '__init__.py']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\_distutils_hack\\__pycache__', [], ['override.cpython-37.pyc', '__init__.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Lib\\site-packages\\__pycache__', [], ['a.cpython-37.pyc']), ('C:\\Users\\dsharman\\Python_Workspace\\venv\\Scripts', [], ['activate', 'activate.bat', 'Activate.ps1', 'deactivate.bat', 'pip.exe', 'pip3.7.exe', 'pip3.exe', 'python.exe', 'pythonw.exe'])]

Main_path = os.path.join(Main_path, add_path)
print(Main_path)
for root, dir_lists, file_lists in os.walk(Main_path):
    print(root)
    if len(file_lists) != 0:
        print(file_lists)
"""
C:\\Users\\dsharman\\Python_Workspace\\Python_Basics
C:\\Users\\dsharman\\Python_Workspace\\Python_Basics
C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Basics of Python
['Arithmetic_Operations.py', 'Assignment_Operations.py', 'Bitwise_Operations.py', 'Comparision Operations.py', 'Dictionary_DataStructure_Functions.py', 'Eval_Input_Function.py', 'Identity_Operations.py', 'List_DataStructure_Functions.py', 'Logical_Operations.py', 'Membership_Operations.py', 'Set_DataStructure_Functions.py', 'String_Variable_Functions.py', 'Tuples_DataStructure_Functions.py']
C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Python Default Modules
['GetPass Module.py', 'Math Module.py', 'OS Module.py', 'Platform Module.py', 'Sys Module.py']


"""
