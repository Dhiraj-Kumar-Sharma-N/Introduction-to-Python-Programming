"""

NAME
    shutil - Utility functions for copying and archiving files and directory trees.

DESCRIPTION
    XXX The functions here don't copy the resource fork or other metadata on Mac.

CLASSES
    builtins.OSError(builtins.Exception)
        Error
            SameFileError
        ExecError
        SpecialFileError

    class Error(builtins.OSError)
     |  Base class for I/O related errors.
     |
     |  Method resolution order:
     |      Error
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
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
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
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
     |  Methods inherited from builtins.BaseException:
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

    class ExecError(builtins.OSError)
     |  Raised when a command could not be executed
     |
     |  Method resolution order:
     |      ExecError
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
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
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
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
     |  Methods inherited from builtins.BaseException:
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

    class SameFileError(Error)
     |  Raised when source and destination are the same file.
     |
     |  Method resolution order:
     |      SameFileError
     |      Error
     |      builtins.OSError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.OSError:
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
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
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
     |  Methods inherited from builtins.BaseException:
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

    class SpecialFileError(builtins.OSError)
     |  Raised when trying to do a kind of operation (e.g. copying) which is
     |  not supported on a special file (e.g. a named pipe)
     |
     |  Method resolution order:
     |      SpecialFileError
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
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
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
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
     |  Methods inherited from builtins.BaseException:
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
    chown(path, user=None, group=None)
        Change owner user and group of the given path.

        user and group can be the uid/gid or the user/group names, and in that case,
        they are converted to their respective uid/gid.

    copy(src, dst, *, follow_symlinks=True)
        Copy data and mode bits ("cp src dst"). Return the file's destination.

        The destination may be a directory.

        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".

        If source and destination are the same file, a SameFileError will be
        raised.

    copy2(src, dst, *, follow_symlinks=True)
        Copy data and metadata. Return the file's destination.

        Metadata is copied with copystat(). Please see the copystat function
        for more information.

        The destination may be a directory.

        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".

    copyfile(src, dst, *, follow_symlinks=True)
        Copy data from src to dst.

        If follow_symlinks is not set and src is a symbolic link, a new
        symlink will be created instead of copying the file it points to.

    copyfileobj(fsrc, fdst, length=16384)
        copy data from file-like object fsrc to file-like object fdst

    copymode(src, dst, *, follow_symlinks=True)
        Copy mode bits from src to dst.

        If follow_symlinks is not set, symlinks aren't followed if and only
        if both `src` and `dst` are symlinks.  If `lchmod` isn't available
        (e.g. Linux) this method does nothing.

    copystat(src, dst, *, follow_symlinks=True)
        Copy file metadata

        Copy the permission bits, last access time, last modification time, and
        flags from `src` to `dst`. On Linux, copystat() also copies the "extended
        attributes" where possible. The file contents, owner, and group are
        unaffected. `src` and `dst` are path names given as strings.

        If the optional flag `follow_symlinks` is not set, symlinks aren't
        followed if and only if both `src` and `dst` are symlinks.

    copytree(src, dst, symlinks=False, ignore=None, copy_function=<function copy2 at 0x000001964C18F9D8>, ignore_dangling_symlinks=False)
        Recursively copy a directory tree.

        The destination directory must not already exist.
        If exception(s) occur, an Error is raised with a list of reasons.

        If the optional symlinks flag is true, symbolic links in the
        source tree result in symbolic links in the destination tree; if
        it is false, the contents of the files pointed to by symbolic
        links are copied. If the file pointed by the symlink doesn't
        exist, an exception will be added in the list of errors raised in
        an Error exception at the end of the copy process.

        You can set the optional ignore_dangling_symlinks flag to true if you
        want to silence this exception. Notice that this has no effect on
        platforms that don't support os.symlink.

        The optional ignore argument is a callable. If given, it
        is called with the `src` parameter, which is the directory
        being visited by copytree(), and `names` which is the list of
        `src` contents, as returned by os.listdir():

            callable(src, names) -> ignored_names

        Since copytree() is called recursively, the callable will be
        called once for each directory that is copied. It returns a
        list of names relative to the `src` directory that should
        not be copied.

        The optional copy_function argument is a callable that will be used
        to copy each file. It will be called with the source path and the
        destination path as arguments. By default, copy2() is used, but any
        function that supports the same signature (like copy()) can be used.

    disk_usage(path)
        Return disk usage statistics about the given path.

        Returned values is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.

    get_archive_formats()
        Returns a list of supported formats for archiving and unarchiving.

        Each element of the returned sequence is a tuple (name, description)

    get_terminal_size(fallback=(80, 24))
        Get the size of the terminal window.

        For each of the two dimensions, the environment variable, COLUMNS
        and LINES respectively, is checked. If the variable is defined and
        the value is a positive integer, it is used.

        When COLUMNS or LINES is not defined, which is the common case,
        the terminal connected to sys.__stdout__ is queried
        by invoking os.get_terminal_size.

        If the terminal size cannot be successfully queried, either because
        the system doesn't support querying, or because we are not
        connected to a terminal, the value given in fallback parameter
        is used. Fallback defaults to (80, 24) which is the default
        size used by many terminal emulators.

        The value returned is a named tuple of type os.terminal_size.

    get_unpack_formats()
        Returns a list of supported formats for unpacking.

        Each element of the returned sequence is a tuple
        (name, extensions, description)

    ignore_patterns(*patterns)
        Function that can be used as copytree() ignore parameter.

        Patterns is a sequence of glob-style patterns
        that are used to exclude files

    make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)
        Create an archive file (eg. zip or tar).

        'base_name' is the name of the file to create, minus any format-specific
        extension; 'format' is the archive format: one of "zip", "tar", "gztar",
        "bztar", or "xztar".  Or any other registered format.

        'root_dir' is a directory that will be the root directory of the
        archive; ie. we typically chdir into 'root_dir' before creating the
        archive.  'base_dir' is the directory where we start archiving from;
        ie. 'base_dir' will be the common prefix of all files and
        directories in the archive.  'root_dir' and 'base_dir' both default
        to the current directory.  Returns the name of the archive file.

        'owner' and 'group' are used when creating a tar archive. By default,
        uses the current owner and group.

    move(src, dst, copy_function=<function copy2 at 0x000001964C18F9D8>)
        Recursively move a file or directory to another location. This is
        similar to the Unix "mv" command. Return the file or directory's
        destination.

        If the destination is a directory or a symlink to a directory, the source
        is moved inside the directory. The destination path must not already
        exist.

        If the destination already exists but is not a directory, it may be
        overwritten depending on os.rename() semantics.

        If the destination is on our current filesystem, then rename() is used.
        Otherwise, src is copied to the destination and then removed. Symlinks are
        recreated under the new name if os.rename() fails because of cross
        filesystem renames.

        The optional `copy_function` argument is a callable that will be used
        to copy the source or it will be delegated to `copytree`.
        By default, copy2() is used, but any function that supports the same
        signature (like copy()) can be used.

        A lot more could be done here...  A look at a mv.c shows a lot of
        the issues this implementation glosses over.

    register_archive_format(name, function, extra_args=None, description='')
        Registers an archive format.

        name is the name of the format. function is the callable that will be
        used to create archives. If provided, extra_args is a sequence of
        (name, value) tuples that will be passed as arguments to the callable.
        description can be provided to describe the format, and will be returned
        by the get_archive_formats() function.

    register_unpack_format(name, extensions, function, extra_args=None, description='')
        Registers an unpack format.

        `name` is the name of the format. `extensions` is a list of extensions
        corresponding to the format.

        `function` is the callable that will be
        used to unpack archives. The callable will receive archives to unpack.
        If it's unable to handle an archive, it needs to raise a ReadError
        exception.

        If provided, `extra_args` is a sequence of
        (name, value) tuples that will be passed as arguments to the callable.
        description can be provided to describe the format, and will be returned
        by the get_unpack_formats() function.

    rmtree(path, ignore_errors=False, onerror=None)
        Recursively delete a directory tree.

        If ignore_errors is set, errors are ignored; otherwise, if onerror
        is set, it is called to handle the error with arguments (func,
        path, exc_info) where func is platform and implementation dependent;
        path is the argument to that function that caused it to fail; and
        exc_info is a tuple returned by sys.exc_info().  If ignore_errors
        is false and onerror is None, an exception is raised.

    unpack_archive(filename, extract_dir=None, format=None)
        Unpack an archive.

        `filename` is the name of the archive.

        `extract_dir` is the name of the target directory, where the archive
        is unpacked. If not provided, the current working directory is used.

        `format` is the archive format: one of "zip", "tar", "gztar", "bztar",
        or "xztar".  Or any other registered format.  If not provided,
        unpack_archive will use the filename extension and see if an unpacker
        was registered for that extension.

        In case none is found, a ValueError is raised.

    unregister_archive_format(name)

    unregister_unpack_format(name)
        Removes the pack format from the registry.

    which(cmd, mode=1, path=None)
        Given a command, mode, and a PATH string, return the path which
        conforms to the given mode on the PATH, or None if there is no such
        file.

        `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
        of os.environ.get("PATH"), or can be overridden with a custom search
        path.

DATA
    __all__ = ['copyfileobj', 'copyfile', 'copymode', 'copystat', 'copy', ...

FILE
    c:\program files\python37\lib\shutil.py


>>>

"""

# !/usr/local/bin/python3
import shutil

# copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'

# copyfile-->copy --> copy2
# src="/home/Automation/working_with_remote_server.py"
src = "/home/Automation/shutil_part_1.py"
dest = "/home/Automation/working_with_remote_server.py_bkp"
# shutil.copyfile(src,dest)  # Copies the content without permission or metadata
# shutil.copy(src,dest)   #same permissions for src and dest
# shutil.copy2(src,dest)   #same meta data for dest as well
# shutil.copymode(src,dest) # Copies only the permission of the src to dest but not the content
# shutil.copystat(src,dest) # Copies both  permission  and metadata ( created date )of the src to dest but not the content

# f1=open('xyz.txt','r')
# f2=open('pqr.txt','w')
# shutil.copyfileobj(f1,f2) # copies fileobject of the opened file content

# src="/home/Automation/tomcat7"
# shutil.copytree(src,'/tmp/tomcat') # copies content with permission & metadata recursively

shutil.rmtree('/tmp/tomcat')  # deletes content with permission & metadata recursively
