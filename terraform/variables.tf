variable "rg_name" {
  type    = string
  default = "todo-aks-rg"
}

variable "location" {
  type    = string
  default = "southeastasia"
}

variable "aks_name" {
  type    = string
  default = "todo-aks"
}

variable "node_count" {
  type    = number
  default = 1
}

variable "node_size" {
  type    = string
  default = "Standard_B2s"
}

variable "ssh_public_key_path" {
  type    = string
  default = "~/.ssh/id_rsa.pub"
}

variable "acr_name_prefix" {
  type    = string
  default = "ayushtodoacr"
}
