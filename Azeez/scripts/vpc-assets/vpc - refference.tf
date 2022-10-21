# Create VPC
# terraform aws create vpc
resource "aws_vpc" "vpc" {
  cidr_block              = 
  instance_tenancy        = 
  enable_dns_hostnames    = 

  tags      = {
    Name    = 
  }
}

# Create Internet Gateway and Attach it to VPC
# terraform aws create internet gateway
resource "aws_internet_gateway" "internet-gateway" {
  vpc_id    =

  tags      = {
    Name    = 
  }
}

# Create Public Subnet 1
# terraform aws create subnet
resource "aws_subnet" "public-subnet-1" {
  vpc_id                  = 
  cidr_block              = 
  availability_zone       = 
  map_public_ip_on_launch = 

  tags      = {
    Name    = 
  }
}

# Create Public Subnet 2
# terraform aws create subnet
resource "aws_subnet" "public-subnet-2" {
  vpc_id                  = 
  cidr_block              = 
  availability_zone       = 
  map_public_ip_on_launch = 

  tags      = {
    Name    = 
  }
}

# Create Route Table and Add Public Route
# terraform aws create route table
resource "aws_route_table" "public-route-table" {
  vpc_id       = 

  route {
    cidr_block =
    gateway_id = 
  }

  tags       = {
    Name     =
  }
}

# Associate Public Subnet 1 to "Public Route Table"
# terraform aws associate subnet with route table
resource "aws_route_table_association" "public-subnet-1-route-table-association" {
  subnet_id           = 
  route_table_id      =
}

# Associate Public Subnet 2 to "Public Route Table"
# terraform aws associate subnet with route table
resource "aws_route_table_association" "public-subnet-2-route-table-association" {
  subnet_id           = 
  route_table_id      = 
}

# Create Private Subnet 1
# terraform aws create subnet
resource "aws_subnet" "private-subnet-1" {
  vpc_id                   = 
  cidr_block               = 
  availability_zone        = 
  map_public_ip_on_launch  = 

  tags      = {
    Name    =
  }
}

# Create Private Subnet 2
# terraform aws create subnet
resource "aws_subnet" "private-subnet-2" {
  vpc_id                   = 
  cidr_block               = 
  availability_zone        = 
  map_public_ip_on_launch  =

  tags      = {
    Name    =
  }
}

# Create Private Subnet 3
# terraform aws create subnet
resource "aws_subnet" "private-subnet-3" {
  vpc_id                   = 
  cidr_block               = 
  availability_zone        = 
  map_public_ip_on_launch  =

  tags      = {
    Name    = 
  }
}

# Create Private Subnet 4
# terraform aws create subnet
resource "aws_subnet" "private-subnet-4" {
  vpc_id                   = 
  cidr_block               = 
  availability_zone        =
  map_public_ip_on_launch  =

  tags      = {
    Name    =
  }
}