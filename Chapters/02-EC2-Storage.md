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

Features

- We can create our own AMI where we can customize the OS, applications etc.
- Or else we can directly use publicly available AMIs which are prebuilt
- Or we can use AMIs from marketplace which are mostly paid. Also we can create our own AMIs and sell in the marketplace.
- When AMI is created, it is created for a specific region but we can copy the AMI when creating a new VM in different reigion
