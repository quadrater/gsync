#!/usr/bin/env python
# -*- coding: utf8 -*-

# Copyright (C) 2013 Craig Phillips.  All rights reserved.

"""
gsync version %s

Copyright (C) 2013 Craig Phillips.  All rights reserved.

gsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
are welcome to redistribute it under certain conditions.  See the BSD
Licence for details.

gsync is a file transfer program based on the rsync file transfer program.
The only functional difference is that gsync is intended to be used for
synchronising between a source directory and remote Google Drive directory.

Usage:
 gsync ( --authenticate | [options]... <path> <path>... )

Arguments:
 <path>                      path to a local file, directory, remote file or 
                             remote directory.  The last argument in the list
                             of provided paths is considered the destination.
                             The destination must be specified along with at
                             least one source.  If a source or destination is
                             remote, then it must be specified in the form:

                                drive:///some/folder

                             any local file or directory can be specified by
                             absolute path or relative to the current working
                             directory.

Options:
     --authenticate          setup authentication with your Google Drive
 -v, --verbose               enable verbose output
     --debug                 enable debug output
 -q, --quiet                 suppress non-error messages
 -c, --checksum              skip based on checksum, not mod-time & size
 -r, --recursive             recurse into directories
 -R, --relative              use relative path names
     --no-implied-dirs       don't send implied dirs with --relative
 -b, --backup                make backups (see --suffix & --backup-dir)
     --backup-dir=DIR        make backups into hierarchy based in DIR
     --suffix=SUFFIX         set backup suffix (default ~ w/o --backup-dir)
 -u, --update                skip files that are newer on the receiver
     --append                append data onto shorter files
 -d, --dirs                  transfer directories without recursing
 -l, --links                 copy symlinks as symlinks
 -L, --copy-links            transform symlink into referent file/dir
     --copy-unsafe-links     only "unsafe" symlinks are transformed
     --safe-links            ignore symlinks that point outside the source tree
 -k, --copy-dirlinks         transform symlink to a dir into referent dir
 -K, --keep-dirlinks         treat symlinked dir on receiver as dir
 -H, --hard-links            preserve hard links
 -p, --perms                 preserve permissions
 -E, --executability         preserve the file's executability
     --chmod=CHMOD           affect file and/or directory permissions
 -o, --owner                 preserve owner (super-user only)
 -g, --group                 preserve group
 -t, --times                 preserve modification times
 -O, --omit-dir-times        omit directories from --times
     --super                 receiver attempts super-user activities
     --fake-super            store/recover privileged attrs using xattrs
 -S, --sparse                handle sparse files efficiently
 -n, --dry-run               perform a trial run with no changes made
 -x, --one-file-system       don't cross filesystem boundaries
     --existing              skip creating new files on receiver
     --ignore-existing       skip updating files that already exist on receiver
     --remove-source-files   sender removes synchronized files (non-dirs)
     --del                   an alias for --delete-during
     --delete                delete extraneous files from destination dirs
     --delete-before         receiver deletes before transfer, not during
     --delete-during         receiver deletes during the transfer
     --delete-delay          find deletions during, delete after
     --delete-after          receiver deletes after transfer, not during
     --delete-excluded       also delete excluded files from destination dirs
     --ignore-errors         delete even if there are I/O errors
     --force                 force deletion of directories even if not empty
     --max-delete=NUM        don't delete more than NUM files
     --max-size=SIZE         don't transfer any file larger than SIZE
     --min-size=SIZE         don't transfer any file smaller than SIZE
     --partial               keep partially transferred files
     --partial-dir=DIR       put a partially transferred file into DIR
     --delay-updates         put all updated files into place at transfer's end
 -m, --prune-empty-dirs      prune empty directory chains from the file-list
     --timeout=SECONDS       set I/O timeout in seconds
     --contimeout=SECONDS    set daemon connection timeout in seconds
 -I, --ignore-times          don't skip files that match in size and mod-time
     --size-only             skip files that match in size
     --modify-window=NUM     compare mod-times with reduced accuracy
 -T, --temp-dir=DIR          create temporary files in directory DIR
 -y, --fuzzy                 find similar file for basis if no dest file
     --compare-dest=DIR      also compare destination files relative to DIR
     --copy-dest=DIR         ... and include copies of unchanged files
 -C, --cvs-exclude           auto-ignore files the same way CVS does
 -fd, --filter=RULE           add a file-filtering RULE
 -F                          same as --filter='dir-merge /.rsync-filter'
                             repeated: --filter='- .rsync-filter'
     --exclude=PATTERN       exclude files matching PATTERN
     --exclude-from=FILE     read exclude patterns from FILE
     --include=PATTERN       don't exclude files matching PATTERN
     --include-from=FILE     read include patterns from FILE
     --files-from=FILE       read list of source-file names from FILE
 -0, --from0                 all *-from/filter files are delimited by 0s
 -s, --protect-args          no space-splitting; only wildcard special-chars
     --stats                 give some file-transfer stats
 -8, --8-bit-output          leave high-bit chars unescaped in output
 -h, --human-readable        output numbers in a human-readable format
     --progress              show progress during transfer
 -P                          same as --partial --progress
 -i, --itemize-changes       output a change-summary for all updates
     --out-format=FORMAT     output updates using the specified FORMAT
     --log-file=FILE         log what we're doing to the specified FILE
     --log-file-format=FMT   log updates using the specified FMT
     --list-only             list the files instead of copying them
     --bwlimit=KBPS          limit I/O bandwidth; KBytes per second
     --version               print version number
     --proxy                 use http_proxy or https_proxy environment
                             variables for web proxy configuration
 -h, --help                  show this help

See https://github.com/iwonbigbro/gsync for updates, bug reports and answers

Environment variables:

   The configuration directory defaults to $HOME/.gsync.  This path can be
   overridden by specifying the environment variable GSYNC_CONFIG_DIR.  Any
   configuration files will be loaded from this directory.

   Individual configuration files can also be overridden by substituting any
   non-alphanumeric character in the filename with an underscore and adding
   the GSYNC_ prefix.  For example, to override the client.json configuration
   file, specify an environment variable named GSYNC_CLIENT_JSON.
"""
