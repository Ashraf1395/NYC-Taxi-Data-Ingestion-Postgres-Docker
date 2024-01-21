variable "location" {
  description = "My location"
  default = "EU"
}

variable "bq_dataset_name"{
    description = "Bigquery Dataset name"
    default = "terraform_bigquery"
}

variable "gcs_storage_class" {
  description = "GCS storage class name"
  default = ""

}

variable "gcs_bucket_name" {
  description = "GCS storage bucket name"
  default = "api-to-bigquery-411507-terraform-bucket"
}

