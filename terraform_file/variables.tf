variable "project_id" {
  description = "The project ID to deploy resources."
  type        = string
  default     = "gke-user"
}

variable "region" {
  description = "The region to deploy resources."
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The zone to deploy resources."
  type        = string
  default     = "us-central1-a"
}