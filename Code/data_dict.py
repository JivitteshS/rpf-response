from langchain_core.prompts import ChatPromptTemplate


storagegrid_dict = {

   "Get started with_StorageGRID system" :[
    "What is StorageGRID:NetApp StorageGRID is a software-defined object storage solution. Supports public, private, and hybrid multicloud environments with native Amazon S3 API support.Focuses on automated lifecycle management to manage unstructured data cost-effectively." ,
    "Core Features: Massively scalable, metadata-driven lifecycle management.Integration with AWS, Azure, and OpenStack Swift (support for Swift is deprecated).Flexible data protection with replication and erasure coding." ,
    "Hybrid Cloud Capabilities: Policy-driven data management for storage optimization.Integration with external storage like Amazon S3 Glacier, Google Cloud, and Azure Blob Storage.CloudMirror replication and event notifications for external service integration." ,
    "Data Protection: Supports replication and erasure coding to protect object data.ILM (Information Lifecycle Management) for data storage, protection, and deletion policies.S3 Object Lock for data retention and legal holds." ,
    "Networking & Management:Three network types: Grid Network (mandatory), Admin Network (optional), Client Network (optional).High availability and virtual IP support for redundancy.Grid Manager for configuration and monitoring, Tenant Manager for storage account management."
],
    "Install, Upgrade and Hotfix StorageGRID": [
        "Installation Overview: Describes the steps required to install the StorageGRID system, including configuring nodes and downloading the recovery package.",
        "Post-Installation Guidelines: Provides instructions for tasks such as DHCP addressing and network configuration changes after completing grid node deployment and configuration.",
        "Virtual Machine Resource Reservation: Details the process of adjusting resources for virtual machines to ensure sufficient RAM and CPU for each grid node.",
        "Temporary Installation Password: Explains how to set and manage a temporary installation password during the deployment of a VMware node.",
        "Upgrading StorageGRID Software: Offers an overview and step-by-step instructions for upgrading the StorageGRID system to a new release.",
        "StorageGRID Installation API: Introduces the API used for performing installation tasks, including sections like config, grid, nodes, provision, recovery, recovery-package, schemas, and sites.",
        "Configuring and Managing Nodes: Discusses creating and placing node configuration files for Ubuntu or Debian deployments, including naming conventions and the content of configuration files.",
        "Troubleshooting Installation Issues: Provides guidance on accessing installation log files and troubleshooting installation problems.",
        "Integration and Configuration Tasks: Lists required and optional tasks after installation, such as creating tenant accounts, configuring groups and user accounts, integrating S3 or Swift API client applications, and configuring ILM rules and policies.",
        "Documentation and Support: Mentions the documentation site for appliances and support for FIPS 140-2 validated cryptography."
    ],
    "Configure and Manage a StorageGRID": [
        "Grid Management API: Describes the use of the Swagger API platform to perform real-time operations in StorageGRID.",
        "Monitoring Data Migration: Provides guidelines for monitoring attributes and managing data migration in the StorageGRID system.",
        "Information Lifecycle Management (ILM): Covers ILM rules and policies for managing object data throughout its lifecycle in StorageGRID.",
        "Admin Group Permissions: Explains the creation and management of admin user groups, including assigning permissions and managing access modes.",
        "Log Files and System Status: Details various log files and system status files, including their contents and how to interpret them."
    ],
    "Use StorageGRID Tenants and Clients": [
        "Tenant Account Overview: Describes the purpose and capabilities of a tenant account in StorageGRID.",
        "Creating a Tenant Account: Steps and requirements for a StorageGRID grid administrator to create a tenant account.",
        "Configuring S3 Tenants: Tasks that can be performed using the Tenant Manager for S3 tenant accounts.",
        "Configuring Swift Tenants: Tasks that can be performed using the Tenant Manager for Swift tenant accounts.",
        "Signing In and Out: Procedures for signing in and out of the Tenant Manager, including both SSO and non-SSO methods.",
        "Tenant Manager Dashboard: Overview of the dashboard's features and the information it displays about tenant accounts.",
        "Storage and Quota Usage: Details on how storage usage and quotas are monitored and managed."
    ],
    "Monitor and Troubleshoot a StorageGRID": [
        "Monitor StorageGRID System: Regular monitoring of the StorageGRID system ensures optimal performance and early detection of issues.",
        "View and Manage the Dashboard: The dashboard provides an overview of system activities and allows for customization to fit specific monitoring needs.",
        "View the Nodes Page: The Nodes page offers detailed metrics for the entire grid, each site, and individual nodes, helping in deeper analysis of system performance.",
        "View Log Files: Log files can be accessed and reviewed to diagnose and troubleshoot issues within the StorageGRID system.",
        "Manage Alerts: Alerts help in detecting, evaluating, and resolving issues with customizable notifications and rules for better system management.",
        "Use SNMP for Monitoring: SNMP can be configured to monitor the StorageGRID system and send notifications based on specific events or thresholds.",
        "Configure Audit Messages and Log Destinations: Audit messages and log destinations can be set up to track system activities and store logs for compliance and review.",
        "Use an External Syslog Server: An external syslog server can be used to collect audit information for centralized logging and monitoring.",
        "Tenant Activity: Monitoring tenant activity helps in understanding resource usage and managing tenant-specific performance issues.",
        "Networking and System Resources: Keeping an eye on networking and system resources ensures that the infrastructure supports the StorageGRID operations effectively."
    ],
    "Expand a StorageGRID": [
        "Plan StorageGRID Expansion: Strategies and considerations for planning an effective expansion of the StorageGRID system.",
        "Guidelines for Adding Storage Volumes: Detailed instructions and limitations on how to add storage volumes to different types of Storage Nodes.",
        "Guidelines for Adding Storage Nodes: Best practices and limitations for adding new Storage Nodes to existing sites.",
        "Guidelines for ADC Service on Storage Nodes: Recommendations for configuring the Administrative Domain Controller (ADC) service on new Storage Nodes.",
        "Add Storage Capacity for Replicated Objects: Considerations for expanding storage to support replicated object data according to the ILM policy.",
        "Add Storage Capacity for Erasure-Coded Objects: Planning and guidelines for adding storage to support erasure-coded object data.",
        "Considerations for Rebalancing Erasure-Coded Data: Insights into the EC rebalance procedure necessary when adding new Storage Nodes to handle erasure-coded data.",
        "Add Metadata Capacity: Instructions on expanding metadata capacity by adding new Storage Nodes to each site."
    ],
    "Maintain a StorageGRID": [
        "Grid Maintenance Overview: Covers tasks like decommissioning nodes, renaming the grid, and maintaining networks.",
        "Maintenance Procedures for Appliances: Provides guidelines for maintaining StorageGRID appliances according to specific hardware instructions.",
        "Download Recovery Package: Instructions on downloading a Recovery Package to restore the system in case of a failure.",
        "Decommission Nodes or Site: Steps to permanently remove grid nodes or an entire site from the StorageGRID system.",
        "Grid Node Decommission Overview: Detailed process for removing one or more grid nodes, except the primary Admin Node.",
        "Considerations for Decommissioning Storage Nodes: Important factors to consider before decommissioning Storage Nodes to ensure proper system functioning.",
        "Connected and Disconnected Site Decommission: Differentiates between removing a connected operational site and a disconnected failed site.",
        "Add or Update Display Names: Procedures for renaming the grid, sites, or nodes without affecting StorageGRID operations.",
        "Monitoring Erasure-Coded Data Repairs: Steps to monitor and retry repairs for erasure-coded data to ensure data integrity.",
        "Decommissioning Connected Grid Nodes: Guidelines for safely decommissioning nodes that are still connected to the grid."
    ],
    "Recovery or Replace Nodes": [
        "Repairing Node Failures: Instructions for repairing failed nodes and tracking repair status using specific commands and tools.",
        "Checking Storage State After Recovery: Steps to verify that the desired state of a recovered storage node is set to online and remains online after a server restart.",
        "Recovering from Storage Volume Failures: Procedures for recovering software-based storage nodes with failed volumes while the system drive remains intact.",
        "Warnings for Storage Volume Recovery: Important warnings and considerations to review before beginning the recovery of failed storage volumes.",
        "Rebuilding the Cassandra Database: Steps to rebuild the Cassandra database as part of the volume recovery process.",
        "Using Recovery Scripts: Details on running specific recovery scripts like sn-remount-volumes and sn-recovery-postinstall.sh to remount, reformat storage volumes, and start services on the storage node.",
        "Restoring Object Data: Guidelines for restoring object data using Grid Manager and monitoring the restoration process.",
        "Monitoring Repair Jobs: Methods to monitor the status of repair jobs for both replicated and erasure-coded data, including using specific commands and tools within the Grid Manager.",
        "Erasure-Coded Data Repair: Specific instructions to monitor and retry failed erasure-coded data repair requests.",
        "Restoration Progress and History: Viewing the progress and history of volume restorations within Grid Manager, including handling failed restoration attempts."
    ]
}


storagegrid_dict.values()
sentences=[]
for i in storagegrid_dict.values():
    sentences=sentences+i

sentence_identifier=sentences




