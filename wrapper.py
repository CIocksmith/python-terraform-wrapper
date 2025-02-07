import os
import json

class TerraformWrapper:
    def __init__(self, var_file='mockvariables.tf'):
        self.var_file = var_file

    def generate_terraform(self):
        variables = self._parse_variables()
        terraform_config = f"""
provider "aws" {{
  region = "{variables['region']}"
}}

resource "aws_instance" "example" {{
  ami = "{variables['ami']}"
  instance_type = "{variables['instance_type']}"
}}
"""
        with open('generated_terraform.tf', 'w') as f:
            f.write(terraform_config)
        print("Terraform configuration has been generated and saved to 'generated_terraform.tf'.")

    def _parse_variables(self):
        return {
            'region': 'us-west-2',
            'ami': 'ami-00000000000000000',
            'instance_type': 't2.micro'
        }

    def apply(self):
        from python_terraform import Terraform
        tf = Terraform(working_dir=os.getcwd())
        init_result, init_stderr, init_stdout = tf.init()

        if init_result != 0:
            print(f"Error initializing Terraform: {init_stderr}")
            return

        apply_result, apply_stderr, apply_stdout = tf.apply(no_color=True, skip_plan=True)

        if apply_result == 0:
            print("Terraform apply was successful!")
        else:
            print(f"Error applying Terraform: {apply_stderr}")
