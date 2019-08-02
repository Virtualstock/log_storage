# Changelog for `log_storage`.


## v0.8.1

### Changed

Make determination of desired filename internal to `BaseLog`,
only save actual filename in `BaseLog`.


## v0.8.0

### Changed

Use django_private_storage to proved storage backend thus enabling use of
S3 based backends.


## v0.7.0

### Changed

Start to require PRIVATE_STORAGE_ROOT setting to be set instead of DATA_ROOT.


## v0.6.0

### Added

- Abstract `Log` model functionality into abstract base model: `BaseLog`.
