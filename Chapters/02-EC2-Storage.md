# EBS - Elastic Block Storage

<img src="https://digitalcloud.training/wp-content/uploads/2022/01/Amazon-EBS-600x300.jpg" height=200/>

## Overview

EBS is a network drive that can be attached with our EC2 instance

Some features of the EBS:

- It is a network drive not a physical drive
- Persistent: Data in the EBS drive never gets deleted even on termination of EC2 which it was attached to
- With the Free tier accout we get: 30GB of storage. It can be increased but with a cost
- One EBS instance can be attached to only one EC2 instance at a time and given that then belong to same availability zones

    <img src="https://cloudiofy.com/wp-content/uploads/2021/01/amazon-ebs.png" height=200/>

Except for the io1 and io2 EBS type volumes which are classified as multi-attach EBS.

[Read more on EBS](https://www.linkedin.com/pulse/ebs-elastic-block-storage-aws-ec2-yandapalli-chandana/)

## EBS Snapshots

You can back up the data on your Amazon EBS volumes by making point-in-time copies, known as Amazon EBS snapshots. A snapshot is an incremental backup, which means that we save only the blocks on the device that have changed since your most recent snapshot. This minimizes the time required to create the snapshot and saves on storage costs by not duplicating data

<img src="https://www.w3schools.com/aws/images/ebs_snapshots.jpg" height=200/>

Features

1. Snapshot Archive: they are 75% cheaper but takes 24-72 hours to recover, recommended for backing up data that are not so important
2. Recycle Bin for EBS Snapshot: Quickly restores the backup, good for important data
3. If you want to copy a same EBS volume in a different EC2 instance, Creating a snapshot of the old volume and attaching it to the new EC2 instance

## EBS Recycle Bins

Protect your Amazon EBS Snapshots and Amazon Machine Images (AMIs) from accidental deletion

Use Recycle Bin to protect your business-critical EBS Snapshots and AMIs from accidental deletion. With Recycle Bin, you specify a configurable retention period within which you can recover these resources after they have been deleted

<img src="https://a.b.cdn.console.awsstatic.com/a/v1/NKMCRF3YYOHFPTSD2Q5LOS3HP6PAE3HJUOEBLAW7LIPVNXSKQH6Q/f8eae9c8d72566f61cb3e7d325627d7f.png" height=200/>

## AMI

Amazon Machine Image: It is a template that is used to create VM instances in AWS. It includes configurations such as the OS, application server and applications required to launch an instance in Amazon VM i.e. EC2 instance.

**Features**

- We can create our own AMI where we can customize the OS, applications etc.
- Or else we can directly use publicly available AMIs which are prebuilt
- Or we can use AMIs from marketplace which are mostly paid. Also we can create our own AMIs and sell in the marketplace.
- When AMI is created, it is created for a specific region but we can copy the AMI when creating a new VM in different reigion
- Creating an AMI can speed up the bootup time when initiating an EC2 instance. For example if I want to create an instance with python and some environment variables preinstalled, we can use the template to create more EC2 instances which will save time, and no need to install the requirements.

## EC2 Image Builder

EC2 Image Builder simplifies the building, testing, and deployment of Virtual Machine and container images for use on AWS or on-premises.

<img src="https://d1.awsstatic.com/re19/image-builder/Product-Page-Diagram_Image-Factory.cbf8db591ca6de1c5d9149f3cd6ccfe6c6a64f33.png" height=200/>

Keeping Virtual Machine and container images up-to-date can be time consuming, resource intensive, and error-prone. Currently, customers either manually update and snapshot VMs or have teams that build automation scripts to maintain images.

Image Builder significantly reduces the effort of keeping images up-to-date and secure by providing a simple graphical interface, built-in automation, and AWS-provided security settings. With Image Builder, there are no manual steps for updating an image nor do you have to build your own automation pipeline.

Image Builder is offered at no cost, other than the cost of the underlying AWS resources used to create, store, and share the images.

## Local EC2 Instance store

- Instance Store is a storage volume that acts as a physical hard drive.
- It provides temporary storage for Amazon EC2 instance.
- The data in an instance store persists during the lifetime of its instance.
- If an instance reboots, data in the instance store will persist.
- When the instance hibernates or terminates, you lose any data in the instance store.

<img src="https://i.ytimg.com/vi/F7bhICTuz6k/maxresdefault.jpg" height=300/>

## EFS - Elastic File System

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*veGPUDYqaETLy0P2.png" height=200/>

- AWS EFS is also called AWS Elastic File System. It is basically share file system over network
- EFS is a file system.
- Data in EFS is accessed via file paths.
- Compared to AWS EBS, AWS EFS saves the data in many Availability Zones.
- Scaling AWS EFS does not disrupt applications.
- A single instace of EFS can be attached to multiple EC2 instances unlike EBS
- EFS is comparetively expensive than EBS
- With EFS-IA, we can optimized the storage by storing unused files in the storage to a different storage called EFS-IA. This can save up to 92% cost. This will be done behind the scenes

## AWS FSx

Launch, run, and scale feature-rich and highly-performant file systems with just a few clicks. Amazon’s fully managed native File Server service called Amazon FSx.

- Integrated with AWS
- Third party
- Fully managed drive means we no longer need to manage the hardware and the software to provide the file server services to our users
- Hardware, it manages the setting up of hardware, volumes,
- Software: maintaining the servers, creating backups, configuring softwares

Benefits of using AWS FSx:

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210604132120/Group7.png" height=300/>

AWS FSx provides two file systems to choose from :

1. Amazon FSx for Windows file server for enterprise workload: Amazon FSx for Windows file server is a native Microsoft Windows file system

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210604134810/Group8.png" height=200/>

2. Amazon FSx for Lustre

The Lustre file system is an open-source, parallel file system that supports many requirements of leadership class HPC(High-Performance Computing) simulation environment

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210604135422/Group9.png" height=200/>
