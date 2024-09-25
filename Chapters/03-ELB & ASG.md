# ELB & ASG - Elastic Load Balancing and Auto Scaling Groups

## Scalability

Scalability is definded as the ability to accomodate larger load by making the hardware stronger (scale up) or by adding nodes (scale out)

There are two types of scalability:

1. Vertical scalability: means upgrading the existing instances/resources, for example upgrading the EC2 instance from t2.micro to t2.large or u-1 2tb1.metal - 12.3 TB RAM, 448 vCPUs

Vetical scaling is very common in non-distributed systems such as database.

2. Horizontal scalability: means increasing the number of instances/resources, for example creating more EC2 instances, distributed systems. This is very common for web applications/modern applications. Also can be used for heavy ETL jobs distributing the task to different Ec2 systems and combining them later on.

To achieve horizontal scalability, we will use:

- Auto scaling group
- Load Balancer

## High Availability

High availability means running your application in atleast two availability zones.
The goal of high availability is to survive a data center loss (in case of disaster)

We will use Auto scaling group with multi AZ

## Elasticity

Once the system is scalable, elasticity means that there will be some auto-scaling so that system can be used based on the demand load. This is "cloud-friendly": pay as you go model.

## Elastic Load Balancing (ELB)

It is managed load balancer; It automatically distributes incoming application traffic accross multiple targets such as EC2 instances, containers etc. in one or more AZ in a manner that it optimizes the speed and performance.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200616180117/UntitledDiagram2.jpg" height=200/>

### Advantages of ELB

- ELB automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses, to achieve high availability.
- It can automatically scale to handle changes in traffic demand, allowing you to maintain consistent application performance.
- It can monitor the health of its registered targets and route traffic only to the healthy targets.
- Load Balancer allows you to configure health checks for the registered targets. In case any of the registered targets (Autoscaling group) fails the health check, the load balancer will not route traffic to that unhealthy target. Thereby ensuring your application is highly available and fault tolerant

### Network Protocols

Before we jump into the types of load balancers, it is important to know about the fundamentals of network protocols:

#### What is it?

Network protocols are sets of rules and conventions that determine how data is transmitted and received across a network. They ensure that devices, regardless of their internal structures or processes, can communicate effectively and reliably.

#### Key Aspects of Network Protocols:

- Syntax: Defines the structure and format of the data packets.
- Semantics: Specifies the meaning of each section of bits in the data packet.
- Synchronization: Coordinates the timing of data transmission and reception.
- Error Handling: Ensures data integrity and reliability by detecting and correcting errors during transmission

#### Common Network Protocols:

- **TCP/IP (Transmission Control Protocol/Internet Protocol)**: The foundational protocols for the internet, enabling reliable communication between devices.
- **HTTP/HTTPS (Hypertext Transfer Protocol/Secure)**: Used for transmitting web pages over the internet, with HTTPS providing secure, encrypted communication.
- **FTP (File Transfer Protocol)**: Facilitates the transfer of files between computers on a network.
- **SMTP (Simple Mail Transfer Protocol)**: Used for sending emails.
- **Ethernet**: A protocol for wired local area networks (LANs), defining how data is transmitted over physical cables.

There are 3 types of load balancers in AWS based on the network protocols:

1. Application Load Balancer (ALB): This type of Load Balancer is used when decisions are to be made related to HTTP and HTTPS traffic routing
2. Network Load Balancer (NLB): It is mainly used for load-balancing TCP traffic, High performance (millions of requests per second)
3. Gateway Load Balancer: GENEVE Protocol on IP Packets (Layer 3) - Route traffic to fire wall, intrusion detection

Read more on this [link](https://www.geeksforgeeks.org/elastic-load-balancer-in-aws/)
Also can read more on [What is OSI](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/)

## Auto Scaling group

Autoscaling group helps in automatically scale horizontally by adding for example one more EC2 instances to match an increasing in load

In real-life, the load on our application might vary, for example during the day time the load might be very high and at night time it may be less. So with the help of Auto-Scaling group, we can automatically scale our server horizontally based on the load. This way it efficiently utilises the resources optimizing the processing and cost.

So in summary, goal of the auto-scaling group is to

- scale out (add EC2 instances) to match increasing load
- scale in (remove EC2 instances) to match decreasing load
- Ensure we have a minimum and a maximum number of machines running
- Automatically register a new instances to our load balancer
- Replace unhealthy instances if any

Cost savings: only run at an optimal capacity

Next Learn about AWS components: VPC, Subnet and basics of networking
