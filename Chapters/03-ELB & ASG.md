# ELB & ASG - Elastic Load Balancing and Auto Scaling Groups

## Fundamentals of Networking in AWS

Before proceeding with the load balancing and auto scaling groups, we need to familarize with the fundamentals of the networking. If you are already familiar with this then you can skip to the next section.

Here are some of the components you would find across when working with load balancing and autoscaling or even initiating an EC2 instance:

### 1. What is a VPC?

VPC - virtual private cloud, is like your own private network section in AWS cloud. Like VPN in our local system, we can control who can access them.

### 2. What is Subnet?

Subnet - subnetwork is a smaller network withing a VPC.
Dividing your private network into subnets has several important benefits

- **Easier management**: By dividing your network into smaller subnets, you can manage and organize your resources more effectively. For example, you can separate your web servers, database servers, and application servers into different subnets
- **Enhanced Security**: Subnets allow you to apply different security rules to different parts of your network. For instance, you can create a public subnet for resources that need to be accessible from the internet and a private subnet for resources that should not be directly accessible from the internet.
- **Improved Performance**: By segmenting your network, you can reduce congestion and improve performance. Traffic within a subnet is often faster and more efficient than traffic between subnets. -**Fault Isolation**: If a problem occurs in one subnet, it can be isolated and won’t necessarily affect the other subnets. This helps in maintaining the overall stability of your network.
- **Regulatory Compliance**: Some regulations require that certain types of data be isolated from others. Subnets can help you comply with these requirements by keeping sensitive data in a separate, secure subnet.

By using subnets, you can create a more organized, secure, and efficient network within your VPC

### 3. What is IP ?

Internet protocol: is a way of identifying devices on network using numerical addresses. Its like postal address for your computer/server.

There are two versions to represent:

- IPv4: An IPv4 address looks something like this: `192.168.1.1`
- IPv6: is the newer version of IPv4. It was created because we were running out of IPv4 addresses. IPv6 addresses are longer and look like this: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.

#### Which IP version to use in AWS?

- Setting up IPv4 is relatively easier and also well documented.
- But only drawing when using it in AWS it charges a premium, as IPv4 are limited
- Setting up IPv6 can be difficult as it requires an additional learning and adaptation
- IPv6 since it is relatively new, it can have compatibility with older applications and devices which doesnot support the newer IPv6 address.

Advantages of using IPv6 :

- No Additional Cost: IPv6 addresses are not subject to the same scarcity and additional costs as IPv4 addresses1.
- Scalability: IPv6 provides a virtually unlimited number of addresses, which can simplify network management and reduce the need for complex configurations like Network Address Translation (NAT)2.
- Future-Proofing: As more devices and services adopt IPv6, using it can ensure your infrastructure is ready for future growth and compatibility2.

[Here is a detailed comparison for Ipv4 vs Ipv6](https://aws.amazon.com/compare/the-difference-between-ipv4-and-ipv6/)

### How They Are Related:

- VPC: Your private network in AWS.
- Subnets: Smaller sections within your VPC.
- IPv4 and IPv6: Addressing systems to identify devices within your VPC and subnets.

### Putting It All Together:

- You create a VPC to have a private network.
- Within that VPC, you create subnets to organize your resources.
- Each resource (like a server) in your subnets gets an IPv4 or IPv6 address so it can communicate with other resources.

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
