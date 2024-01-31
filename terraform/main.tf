terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  project     = var.project
}


resource "google_storage_bucket" "demo-bucket" {
  name          = format("%s-%s", var.project, var.gcs_bucket_name)
  location      = var.location
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "demo-dataset" {
  dataset_id = format("%s", var.bq_dataset_name)
  location   = var.location
}