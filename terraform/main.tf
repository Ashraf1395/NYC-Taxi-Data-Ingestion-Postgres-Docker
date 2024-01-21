terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}
provider "google" {
  credentials = "../data/keys/terraform-key.json"
  project     = "api-to-bigquery-411507"
  region      = "us-central1"
}

resource "google_storage_bucket" "auto-expire" {
  name          = "api-to-bigquery-411507-terraform-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }

    action {
      type = "Delete"
    }
  }
}

