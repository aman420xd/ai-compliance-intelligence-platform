import os

from utils.supabase_client import supabase


BUCKET_NAME = "compliance-files"


def upload_pdf_to_supabase(
    local_file_path,
    storage_filename
):

    with open(local_file_path, "rb") as f:

        supabase.storage.from_(BUCKET_NAME).upload(
            storage_filename,
            f,
            {
                "content-type": "application/pdf"
            }
        )

    file_url = supabase.storage.from_(BUCKET_NAME).get_public_url(
        storage_filename
    )

    return file_url