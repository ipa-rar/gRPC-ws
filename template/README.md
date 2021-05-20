# Template for creating gRPC projects
## Steps to use this template
1. Create the proto file 
2. Run the shell script to generate client.py, server.py and generate boiler plate code for gRPC project.
    ````
    sh generate_proto.sh
    ````
3. Enter the name of the proto file you have created in step 1.
4. Now, you have all the files to get started with the gRPC project.
## Note: This script works perfectly when proto file names that does not contain `space`, `_` and `-`
