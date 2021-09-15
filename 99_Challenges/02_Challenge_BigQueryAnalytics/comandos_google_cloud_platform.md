# Comandos CLI Google Cloud Platform

Se muestran los comandos habituales en consola de Google Cloud Shell / Cloud SDK

## Bucket - Cloud Storage

***

```{shell}
# shell command
gsutil mb \
    -p <PROJECT-ID> \
    -c <STORAGE-CLASS> \ 
    -b on gs://<BUCKET-NAME> \
```

```{python}
# code sample in python
from google.cloud import storage


def create_bucket_class_location(bucket_name):
    """Create a new bucket in specific location with storage class"""
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket


```

-p = nombre projecto

-c = tipo de clase de almacenamiento:
 (
     STANDARD = none, 
     NEARLINE = 30 days, 
     COLDLINE = 90 days, 
     ARCHIVE = 365 days
)

-b = habilitar bucket-level access uniformado

***

### Bucket name requirements

Your bucket names must meet the following requirements:

- Bucket names must contain only lowercase letters, numbers, dashes (`-`),    underscores (`_`), and dots (`.`). Spaces are not allowed.    Names containing dots require [verification](https://cloud.google.com/storage/docs/domain-name-verification). 
- Bucket names must start and end with a number or letter.
- Bucket names must contain 3-63 characters. Names containing dots can contain up to    222 characters, but each dot-separated component can be no longer than 63 characters.
- Bucket names cannot be represented as an IP address in dotted-decimal notation    (for example, 192.168.5.4).
- Bucket names cannot begin with the "goog" prefix.
- Bucket names cannot contain "google" or close misspellings, such as "g00gle".

### Bucket name considerations

- Bucket names reside in a single Cloud Storage namespace.

  This means that:

  - Every bucket name must be unique.
  - Bucket names are publicly visible.

  If you try to create a bucket with a name that already belongs to an existing bucket, Cloud Storage responds with an error message.

- A bucket name can only be assigned during creation.

  You cannot change the name of an existing bucket. Instead, you should create a new bucket with the desired name and move the contents from the old bucket to the new bucket. See [Moving and Renaming Buckets](https://cloud.google.com/storage/docs/moving-buckets) for a step-by-step guide.

- Once you delete a bucket, anyone can reuse its name for a new bucket.

  The time it takes a deleted bucket's name to become available again is typically on the order of seconds; however, if you delete the project that contains the bucket, which effectively deletes the bucket as well, the bucket name may not be released for weeks or longer.

- You can use a bucket name in a DNS record as part of a `CNAME` or `A` redirect.

  In order to do so, your bucket name should conform to standard DNS naming conventions. This means that your bucket name should not use underscores (`_`) or have a period next to another period or dash. For example, ".." is not valid within DNS names and neither is "-." or ".-".

See also the [Naming Best Practices](https://cloud.google.com/storage/docs/best-practices#naming) section, which includes recommendations about excluding proprietary information from bucket names.

### Example bucket names

The following are examples of valid bucket names:

- `my-travel-maps`
- `0f75d593-8e7b-4418-a5ba-cb2970f0b91e`
- `test.example.com` (Requires verification of ownership for `example.com`)

The following are examples of invalid bucket names:

- `My-Travel-Maps` (contains uppercase letters)
- `my_google_bucket` (contains "google")
- `test bucket` (contains a space)



***

### Listar buckets

```shell
gsutil ls
```

```python
# code sample in python
from google.cloud import storage


def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)


```

***

### Get bucket information

```{shell}
# shell command
gsutil du -s gs://<BUCKET_NAME>
```

```{shell}
gsutil ls -L -b gs://<BUCKET_NAME>
```

```{python}
# python example

from google.cloud import storage


def bucket_metadata(bucket_name):
    """Prints out a bucket's metadata."""
    # bucket_name = 'your-bucket-name'

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    print("ID: {}".format(bucket.id))
    print("Name: {}".format(bucket.name))
    print("Storage Class: {}".format(bucket.storage_class))
    print("Location: {}".format(bucket.location))
    print("Location Type: {}".format(bucket.location_type))
    print("Cors: {}".format(bucket.cors))
    print(
        "Default Event Based Hold: {}".format(bucket.default_event_based_hold)
    )
    print("Default KMS Key Name: {}".format(bucket.default_kms_key_name))
    print("Metageneration: {}".format(bucket.metageneration))
    print(
        "Retention Effective Time: {}".format(
            bucket.retention_policy_effective_time
        )
    )
    print("Retention Period: {}".format(bucket.retention_period))
    print("Retention Policy Locked: {}".format(bucket.retention_policy_locked))
    print("Requester Pays: {}".format(bucket.requester_pays))
    print("Self Link: {}".format(bucket.self_link))
    print("Time Created: {}".format(bucket.time_created))
    print("Versioning Enabled: {}".format(bucket.versioning_enabled))
    print("Labels:")
    print(bucket.labels)


```

***

### Moving and renaming buckets

```{shell}
gsutil cp -r gs://<SOURCE_BUCKET>/* gs://<DESTINATION_BUCKET>
```

Where:

- `SOURCE_BUCKET` is the name of your original bucket. For example, `old-bucket`.
- `DESTINATION_BUCKET` is the name of the bucket you are moving your data to. For example, `my-bucket`.

***

### Utilizar labels

```shell
gsutil label ch -l KEY_1:VALUE_1 gs://BUCKET_NAME
```

Where

- `KEY_1` is the key name for your label. For example, `pet`.
- `VALUE_1` is the value for your label. For example, `dog`.
- `BUCKET_NAME` is the name of the bucket that the label applies to. For example, `my-bucket`.

Use multiple `-l` flags to add or edit multiple `key:value` pairs in a    single command.

Use the [`label set`](https://cloud.google.com/storage/docs/gsutil/commands/label#set) command to replace all existing labels with    new ones.

```{python}
# python sample code
import pprint

from google.cloud import storage


def add_bucket_label(bucket_name):
    """Add a label to a bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    labels = bucket.labels
    labels["example"] = "label"
    bucket.labels = labels
    bucket.patch()

    print("Updated labels on {}.".format(bucket.name))
    pprint.pprint(bucket.labels)


```

***

#### View bucket labels

```{shell}
gsutil ls -L -b gs://BUCKET_NAME
```

#### Remove a bucket label

```shell
gsutil label ch -d KEY_1 gs://BUCKET_NAME
```

***

### Eliminar un bucket

```{shell}
gsutil rm -r gs://BUCKET_NAME
```

```{python}
#python sample code

from google.cloud import storage


def delete_bucket(bucket_name):
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    print("Bucket {} deleted".format(bucket.name))


```

***

## Working with Objects

### Uploading objects

```{shell}
gsutil cp OBJECT_LOCATION gs://DESTINATION_BUCKET_NAME/
```

Where:

- `OBJECT_LOCATION` is the local path to your object. For example, `Desktop/dog.png`.
- `DESTINATION_BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example, `my-bucket`.



```{python}
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

```

***

### Downloading objects

```{shell}
gsutil cp gs://BUCKET_NAME/OBJECT_NAME SAVE_TO_LOCATION
```

Where:

- `BUCKET_NAME` is the name of the bucket containing the object you are downloading. For example, `my-bucket`.
- `OBJECT_NAME` is the name of object you are downloading. For example, `pets/dog.png`.
- `SAVE_TO_LOCATION` is the local path where you are saving your object. For example, `Desktop/Images`

***

### Listing objects

```{shell}
gsutil ls -r gs://BUCKET_NAME/**
```

Where:

- `BUCKET_NAME` is the name of the bucket whose objects you want to list. For example, `my-bucket`.

```{python}
# python sample code
from google.cloud import storage


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)


```



***

### Copying an object

```{shell}
gsutil cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/NAME_OF_COPY
```

Where:

- `SOURCE_BUCKET_NAME` is the name of the bucket containing the object you want to copy. For example, `my-bucket`.
- `SOURCE_OBJECT_NAME` is the name of the object you want to copy. For example, `pets/dog.png`.
- `DESTINATION_BUCKET_NAME` is the name of the bucket where you want to copy your object. For example, `another-bucket`.
- `NAME_OF_COPY` is the name you want to give the copy of your object. For example, `shiba.png`.

```{python}
# python sample code
from google.cloud import storage


def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name
):
    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


```

***

### Cleaning up a bucket

```{shell}
gsutil -m rm gs://example-bucket/**
```



### Habilitar permisos públicos al bucket

```{shell}
gsutil iam ch AllUsers:objectViewer gs://example-bucket
```

#### Permisos a un usuario

```{shell}
gsutil iam ch user:liz@gmail.com:objectViewer gs://example-bucket
```