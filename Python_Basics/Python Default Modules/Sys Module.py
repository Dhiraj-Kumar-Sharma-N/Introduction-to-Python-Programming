"""

NAME
    sys

MODULE REFERENCE
    https://docs.python.org/3.7/library/sys

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter of Python.

    Dynamic objects:

    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules

    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.

    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.

    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.

    Static objects:

    builtin_module_names -- tuple of module names built into this interpreter
    copyright -- copyright notice pertaining to this interpreter
    exec_prefix -- prefix used to find the machine-specific Python library
    executable -- absolute path of the executable binary of the Python interpreter
    float_info -- a named tuple with information about the float implementation.
    float_repr_style -- string indicating the style of repr() output for floats
    hash_info -- a named tuple with information about the hash algorithm.
    hexversion -- version information encoded as a single integer
    implementation -- Python implementation information.
    int_info -- a named tuple with information about the int implementation.
    maxsize -- the largest supported length of containers.
    maxunicode -- the value of the largest Unicode code point
    platform -- platform identifier
    prefix -- prefix used to find the Python library
    thread_info -- a named tuple with information about the thread implementation.
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    dllhandle -- [Windows only] integer handle of the Python DLL
    winver -- [Windows only] version number of the Python DLL
    _enablelegacywindowsfsencoding -- [Windows only]
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!

    Functions:

    displayhook() -- print an object to the screen, and save it in builtins._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- return thread-safe information about the current exception
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setcheckinterval() -- control how often the interpreter checks for events
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function

FUNCTIONS
    __breakpointhook__ = breakpointhook(...)
        breakpointhook(*args, **kws)

        This hook function is called by built-in breakpoint().

    __displayhook__ = displayhook(...)
        displayhook(object) -> None

        Print an object to sys.stdout and also save it in builtins._

    __excepthook__ = excepthook(...)
        excepthook(exctype, value, traceback) -> None

        Handle an exception by displaying it with a traceback on sys.stderr.

    breakpointhook(...)
        breakpointhook(*args, **kws)

        This hook function is called by built-in breakpoint().

    call_tracing(...)
        call_tracing(func, args) -> object

        Call func(*args), while tracing is enabled.  The tracing state is
        saved, and restored afterwards.  This is intended to be called from
        a debugger from a checkpoint, to recursively debug some other code.

    callstats(...)
        callstats() -> tuple of integers

        Return a tuple of function call statistics, if CALL_PROFILE was defined
        when Python was built.  Otherwise, return None.

        When enabled, this function returns detailed, implementation-specific
        details about the number of function calls executed. The return value is
        a 11-tuple where the entries in the tuple are counts of:
        0. all function calls
        1. calls to PyFunction_Type objects
        2. PyFunction calls that do not create an argument tuple
        3. PyFunction calls that do not create an argument tuple
           and bypass PyEval_EvalCodeEx()
        4. PyMethod calls
        5. PyMethod calls on bound methods
        6. PyType calls
        7. PyCFunction calls
        8. generator calls
        9. All other calls
        10. Number of stack pops performed by call_function()

    exc_info(...)
        exc_info() -> (type, value, traceback)

        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.

    excepthook(...)
        excepthook(exctype, value, traceback) -> None

        Handle an exception by displaying it with a traceback on sys.stderr.

    exit(...)
        exit([status])

        Exit the interpreter by raising SystemExit(status).
        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is an integer, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).

    get_asyncgen_hooks(...)
        get_asyncgen_hooks()

        Return a namedtuple of installed asynchronous generators hooks (firstiter, finalizer).

    get_coroutine_origin_tracking_depth()
        Check status of origin tracking for coroutine objects in this thread.

    get_coroutine_wrapper(...)
        get_coroutine_wrapper()

        Return the wrapper for coroutine objects set by sys.set_coroutine_wrapper.

    getallocatedblocks(...)
        getallocatedblocks() -> integer

        Return the number of memory blocks currently allocated, regardless of their
        size.

    getcheckinterval(...)
        getcheckinterval() -> current check interval; see setcheckinterval().

    getdefaultencoding(...)
        getdefaultencoding() -> string

        Return the current default string encoding used by the Unicode
        implementation.

    getfilesystemencodeerrors(...)
        getfilesystemencodeerrors() -> string

        Return the error mode used to convert Unicode filenames in
        operating system filenames.

    getfilesystemencoding(...)
        getfilesystemencoding() -> string

        Return the encoding used to convert Unicode filenames in
        operating system filenames.

    getprofile(...)
        getprofile()

        Return the profiling function set with sys.setprofile.
        See the profiler chapter in the library manual.

    getrecursionlimit(...)
        getrecursionlimit()

        Return the current value of the recursion limit, the maximum depth
        of the Python interpreter stack.  This limit prevents infinite
        recursion from causing an overflow of the C stack and crashing Python.

        This IDLE wrapper subtracts 30 to compensate for the 30 IDLE adds when
        setting the limit.

    getrefcount(...)
        getrefcount(object) -> integer

        Return the reference count of object.  The count returned is generally
        one higher than you might expect, because it includes the (temporary)
        reference as an argument to getrefcount().

    getsizeof(...)
        getsizeof(object, default) -> int

        Return the size of object in bytes.

    getswitchinterval(...)
        getswitchinterval() -> current thread switch interval; see setswitchinterval().

    gettrace(...)
        gettrace()

        Return the global debug tracing function set with sys.settrace.
        See the debugger chapter in the library manual.

    getwindowsversion(...)
        getwindowsversion()

        Return information about the running version of Windows as a named tuple.
        The members are named: major, minor, build, platform, service_pack,
        service_pack_major, service_pack_minor, suite_mask, and product_type. For
        backward compatibility, only the first 5 items are available by indexing.
        All elements are numbers, except service_pack and platform_type which are
        strings, and platform_version which is a 3-tuple. Platform is always 2.
        Product_type may be 1 for a workstation, 2 for a domain controller, 3 for a
        server. Platform_version is a 3-tuple containing a version number that is
        intended for identifying the OS rather than feature detection.

    intern(...)
        intern(string) -> string

        ``Intern'' the given string.  This enters the string in the (global)
        table of interned strings whose purpose is to speed up dictionary lookups.
        Return the string itself or the previously interned string object with the
        same value.

    is_finalizing(...)
        is_finalizing()
        Return True if Python is exiting.

    set_asyncgen_hooks(...)
        set_asyncgen_hooks(*, firstiter=None, finalizer=None)

        Set a finalizer for async generators objects.

    set_coroutine_origin_tracking_depth(depth)
        Enable or disable origin tracking for coroutine objects in this thread.

        Coroutine objects will track 'depth' frames of traceback information about
        where they came from, available in their cr_origin attribute. Set depth of 0
        to disable.

    set_coroutine_wrapper(...)
        set_coroutine_wrapper(wrapper)

        Set a wrapper for coroutine objects.

    setcheckinterval(...)
        setcheckinterval(n)

        Tell the Python interpreter to check for asynchronous events every
        n instructions.  This also affects how often thread switches occur.

    setprofile(...)
        setprofile(function)

        Set the profiling function.  It will be called on each function call
        and return.  See the profiler chapter in the library manual.

    setrecursionlimit(...)
        setrecursionlimit(n)

        Set the maximum depth of the Python interpreter stack to n.  This
        limit prevents infinite recursion from causing an overflow of the C
        stack and crashing Python.  The highest possible limit is platform-
        dependent.

        This IDLE wrapper adds 30 to prevent possible uninterruptible loops.

    setswitchinterval(...)
        setswitchinterval(n)

        Set the ideal thread switching delay inside the Python interpreter
        The actual frequency of switching threads can be lower if the
        interpreter executes long sequences of uninterruptible code
        (this is implementation-specific and workload-dependent).

        The parameter must represent the desired switching delay in seconds
        A typical value is 0.005 (5 milliseconds).

    settrace(...)
        settrace(function)

        Set the global debug tracing function.  It will be called on each
        function call.  See the debugger chapter in the library manual.

DATA
    __stderr__ = None
    __stdin__ = None
    __stdout__ = None
    api_version = 1013
    argv = ['']
    base_exec_prefix = r'C:\Program Files\Python37'
    base_prefix = r'C:\Program Files\Python37'
    builtin_module_names = ('_abc', '_ast', '_bisect', '_blake2', '_codecs...
    byteorder = 'little'
    copyright = 'Copyright (c) 2001-2019 Python Software Foundati...ematis...
    dllhandle = 140727510761472
    dont_write_bytecode = False
    exec_prefix = r'C:\Program Files\Python37'
    executable = r'C:\Program Files\Python37\pythonw.exe'
    flags = sys.flags(debug=0, inspect=0, interactive=0, opt...ation=1, is...
    float_info = sys.float_info(max=1.7976931348623157e+308, max_...epsilo...
    float_repr_style = 'short'
    hash_info = sys.hash_info(width=64, modulus=2305843009213693...iphash2...
    hexversion = 50791920
    implementation = namespace(cache_tag='cpython-37', hexversion=507...in...
    int_info = sys.int_info(bits_per_digit=30, sizeof_digit=4)
    last_value = NameError("name 'clear' is not defined")
    maxsize = 9223372036854775807
    maxunicode = 1114111
    meta_path = [<class '_frozen_importlib.BuiltinImporter'>, <class '_fro...
    modules = {'__future__': <module '__future__' from 'C:\\Program Files\...
    path = ['', r'C:\Program Files\Python37\Lib\idlelib', r'C:\Program Fil...
    path_hooks = [<class 'zipimport.zipimporter'>, <function FileFinder.pa...
    path_importer_cache = {'': FileFinder('.'), r'C:\Program Files\Python3...
    platform = 'win32'
    prefix = r'C:\Program Files\Python37'
    stderr = <idlelib.run.PseudoOutputFile object>
    stdin = <idlelib.run.PseudoInputFile object>
    stdout = <idlelib.run.PseudoOutputFile object>
    thread_info = sys.thread_info(name='nt', lock=None, version=None)
    version = '3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC ...
    version_info = sys.version_info(major=3, minor=7, micro=5, releaseleve...
    warnoptions = []
    winver = '3.7'

FILE
    (built-in)

"""

import sys

print(sys.version_info)  # sys.version_info(major=3, minor=7, micro=5, releaselevel='final', serial=0)

print(sys.version)  # 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)]

print(sys.getwindowsversion())  # sys.getwindowsversion(major=10, minor=0, build=19043, platform=2, service_pack='')

print(sys.platform)  # win32

print(sys.modules)

print(sys.path)

print(sys.exit())

print("Python execution stopped by sys.exit()")

# sys.argv() = returns a list of command line arguments ( By default script name is 0th element in List)
