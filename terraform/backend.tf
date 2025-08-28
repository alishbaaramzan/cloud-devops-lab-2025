terraform {
  backend "s3" {
    bucket         = "buck-buck-bucket-liz"   
    key            = "terraform/state.tfstate"   
    region         = "us-east-1"                   
    dynamodb_table = "terraform-locks"           
    encrypt        = true
  }
}
