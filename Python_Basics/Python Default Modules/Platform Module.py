"""
Help on module platform:

NAME
    platform

DESCRIPTION
    This module tries to retrieve as much platform-identifying data as
    possible. It makes this information available via function APIs.

    If called from the command line, it prints the platform
    information concatenated as single string to stdout. The output
    format is use able as part of a filename.

    or

    The Platform module is used to retrieve as much possible information about the platform
    on which the program is being currently executed. Now by platform info,
    it means information about the device, it’s OS, node, OS version, Python version, etc

CLASSES
    builtins.tuple(builtins.object)
        uname_result

    class uname_result(builtins.tuple)
     |  uname_result(system, node, release, version, machine, processor)
     |
     |  uname_result(system, node, release, version, machine, processor)
     |
     |  Method resolution order:
     |      uname_result
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getnewargs__(self)
     |      Return self as a plain tuple.  Used by copy and pickle.
     |
     |  __repr__(self)
     |      Return a nicely formatted representation string
     |
     |  _asdict(self)
     |      Return a new OrderedDict which maps field names to their values.
     |
     |  _replace(_self, **kwds)
     |      Return a new uname_result object replacing specified fields with new values
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  _make(iterable) from builtins.type
     |      Make a new uname_result object from a sequence or iterable
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(_cls, system, node, release, version, machine, processor)
     |      Create new instance of uname_result(system, node, release, version, machine, processor)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  system
     |      Alias for field number 0
     |
     |  node
     |      Alias for field number 1
     |
     |  release
     |      Alias for field number 2
     |
     |  version
     |      Alias for field number 3
     |
     |  machine
     |      Alias for field number 4
     |
     |  processor
     |      Alias for field number 5
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  _field_defaults = {}
     |
     |  _fields = ('system', 'node', 'release', 'version', 'machine', 'process...
     |
     |  _fields_defaults = {}
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
    architecture(executable='C:\\Program Files\\Python37\\pythonw.exe', bits='', linkage='')
        Queries the given executable (defaults to the Python interpreter
        binary) for various architecture information.

        Returns a tuple (bits, linkage) which contains information about
        the bit architecture and the linkage format used for the
        executable. Both values are returned as strings.

        Values that cannot be determined are returned as given by the
        parameter presets. If bits is given as '', the sizeof(pointer)
        (or sizeof(long) on Python version < 1.5.2) is used as
        indicator for the supported pointer size.

        The function relies on the system's "file" command to do the
        actual work. This is available on most if not all Unix
        platforms. On some non-Unix platforms where the "file" command
        does not exist and the executable is set to the Python interpreter
        binary defaults from _default_architecture are used.

    dist(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'fedora', 'redhat', 'centos', 'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo', 'UnitedLinux', 'turbolinux', 'arch', 'mageia'))
        Tries to determine the name of the Linux OS distribution name.

        The function first looks for a distribution release file in
        /etc and then reverts to _dist_try_harder() in case no
        suitable files are found.

        Returns a tuple (distname, version, id) which default to the
        args given as parameters.

    java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', ''))
        Version interface for Jython.

        Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
        a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
        tuple (os_name, os_version, os_arch).

        Values which cannot be determined are set to the defaults
        given as parameters (which all default to '').

    libc_ver(executable='C:\\Program Files\\Python37\\pythonw.exe', lib='', version='', chunksize=16384)
        Tries to determine the libc version that the file executable
        (which defaults to the Python interpreter) is linked against.

        Returns a tuple of strings (lib,version) which default to the
        given parameters in case the lookup fails.

        Note that the function has intimate knowledge of how different
        libc versions add symbols to the executable and thus is probably
        only useable for executables compiled using gcc.

        The file is read and scanned in chunks of chunksize bytes.

    linux_distribution(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'fedora', 'redhat', 'centos', 'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo', 'UnitedLinux', 'turbolinux', 'arch', 'mageia'), full_distribution_name=1)

    mac_ver(release='', versioninfo=('', '', ''), machine='')
        Get MacOS version information and return it as tuple (release,
        versioninfo, machine) with versioninfo being a tuple (version,
        dev_stage, non_release_version).

        Entries which cannot be determined are set to the parameter values
        which default to ''. All tuple entries are strings.

    machine()
        Returns the machine type, e.g. 'i386'

        An empty string is returned if the value cannot be determined.

    node()
        Returns the computer's network name (which may not be fully
        qualified)

        An empty string is returned if the value cannot be determined.

    platform(aliased=0, terse=0)
        Returns a single string identifying the underlying platform
        with as much useful information as possible (but no more :).

        The output is intended to be human readable rather than
        machine parseable. It may look different on different
        platforms and this is intended.

        If "aliased" is true, the function will use aliases for
        various platforms that report system names which differ from
        their common names, e.g. SunOS will be reported as
        Solaris. The system_alias() function is used to implement
        this.

        Setting terse to true causes the function to return only the
        absolute minimum information needed to identify the platform.

    popen(cmd, mode='r', bufsize=-1)
        Portable popen() interface.

    processor()
        Returns the (true) processor name, e.g. 'amdk6'

        An empty string is returned if the value cannot be
        determined. Note that many platforms do not provide this
        information or simply return the same value as for machine(),
        e.g.  NetBSD does this.

    python_branch()
        Returns a string identifying the Python implementation
        branch.

        For CPython this is the SCM branch from which the
        Python binary was built.

        If not available, an empty string is returned.

    python_build()
        Returns a tuple (buildno, builddate) stating the Python
        build number and date as strings.

    python_compiler()
        Returns a string identifying the compiler used for compiling
        Python.

    python_implementation()
        Returns a string identifying the Python implementation.

        Currently, the following implementations are identified:
          'CPython' (C implementation of Python),
          'IronPython' (.NET implementation of Python),
          'Jython' (Java implementation of Python),
          'PyPy' (Python implementation of Python).

    python_revision()
        Returns a string identifying the Python implementation
        revision.

        For CPython this is the SCM revision from which the
        Python binary was built.

        If not available, an empty string is returned.

    python_version()
        Returns the Python version as string 'major.minor.patchlevel'

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    python_version_tuple()
        Returns the Python version as tuple (major, minor, patchlevel)
        of strings.

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    release()
        Returns the system's release, e.g. '2.2.0' or 'NT'

        An empty string is returned if the value cannot be determined.

    system()
        Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

        An empty string is returned if the value cannot be determined.

    system_alias(system, release, version)
        Returns (system, release, version) aliased to common
        marketing names used for some systems.

        It also does some reordering of the information in some cases
        where it would otherwise cause confusion.

    uname()
        Fairly portable uname interface. Returns a tuple
        of strings (system, node, release, version, machine, processor)
        identifying the underlying platform.

        Note that unlike the os.uname function this also returns
        possible processor information as an additional tuple entry.

        Entries which cannot be determined are set to ''.

    version()
        Returns the system's release version, e.g. '#3 on degas'

        An empty string is returned if the value cannot be determined.

    win32_ver(release='', version='', csd='', ptype='')

DATA
    DEV_NULL = 'nul'
    __copyright__ = '\n    Copyright (c) 1999-2000, Marc-Andre Lemburg... ...

VERSION
    1.0.8


"""
import platform as pf

print(pf.system())  # Windows

print(pf.architecture())  # ('64bit', 'WindowsPE')

print(pf.java_ver())

print(pf.python_version())  # 3.7.5

print(pf.python_version_tuple())  # ('3', '7', '5')

print(pf.machine())  # AMD64

print(pf.release())  # 10

print(pf.platform())  # Windows-10-10.0.19041-SP0

print(pf.processor())  # Intel64 Family 6 Model 78 Stepping 3, GenuineIntel

print(pf.node())  # HIBACL99648
