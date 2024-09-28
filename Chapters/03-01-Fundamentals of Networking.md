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

## CIDR - Classless inter-domain routing

It is a method used for allocating and routing IP addresses on the internet. It is a compact method for specifying IP address ranges and network masks. It is widely used in network configuration and management.

An IP address consists of 4 octets, each containing 8 bits that represent values from 0 to 255. In CIDR notation, a forward slash (/) followed by a number indicates the length of the network prefix in bits. For example:

When you see an IP address followed by a slash and a number, such as `192.168.1.0/24`, this is CIDR notation.

Let’s break down `192.168.1.0/24`:

The IP address: `192.168.1.0`
The number after the slash: `24`

Here is a CIDR calculator to understand how CIDR method works:

<a href="https://cidr.xyz/#192.168.1.0/24"><img src="https://github.com/yuvadm/cidr.xyz/raw/master/cidr.png" heigth=300/></a>

This means that `/24` network will accommodate `256` addresses in total. The network address `(192.168.1.0)` and the broadcast address `(192.168.1.255)` are typically not usable for host addresses, leaving 254 addresses `(192.168.1.1 to 192.168.1.254)` available for devices on the network

Read more on:

- [Understanding CIDR](https://www.howtouselinux.com/post/understanding-cidr-24)
- [Video: Understanding CIDR Block in AWS VPC : Classless Interdomain Routing](https://youtu.be/I_LXaIg6mkM?si=UkarOqgyGiEHH5Px)
- [Understanding Subnet address](https://www.howtouselinux.com/post/understanding-cidr-24)
- Creating VPC, subnets in AWS

## Creating a VPC and Subnet in AWS
