import streamlit as st

def run():
    st.title("Telecommunication Systems")

    st.markdown("""
    ### What is a Telecommunication System?
    A **telecommunication system** is an infrastructure that enables the transmission of information over distances using various technologies such as wired, wireless, optical, or satellite communication. It facilitates voice, data, video, and other forms of communication between individuals, devices, or systems.

    ### How Does It Work?
    1. **Signal Generation**: Information (voice, video, data) is converted into signals (analog or digital).
    2. **Transmission**: These signals are transmitted over communication channels like cables, radio waves, or fiber optics.
    3. **Switching/Routing**: The system routes the signals to the intended recipient.
    4. **Reception**: The recipient's device receives the signal and converts it back into usable information.
    5. **Feedback and Control**: Systems like OSS (Operational Support Systems) monitor and optimize performance.

    ### Core Components of a Telecommunication System

    #### 1. **RAN (Radio Access Network)**
    - **Definition**: The interface between user devices and the core network.
    - **Function**: Manages radio connections, handles data transmission, and ensures connectivity.
    - **Examples**: Cellular towers, antennas, base stations.

    #### 2. **Core (Core Network)**
    - **Definition**: The central part of the telecommunication network that manages communication sessions and data routing.
    - **Function**: Provides services like authentication, call switching, data routing, and mobility management.
    - **Examples**: Mobile Switching Center (MSC), Packet Core Network (EPC for 4G, 5GC for 5G).

    #### 3. **OSS (Operational Support Systems) and SOC (Service Operations Center)**
    - **OSS**:
      - Manages network operations, configuration, and fault management.
      - Provides tools for network monitoring and optimization.
    - **SOC**:
      - Focuses on managing and monitoring service quality and security.
      - Ensures customer satisfaction by resolving service-related issues.

    #### 4. **Transmission**
    - **Definition**: The medium and technology used to carry signals between different parts of the network.
    - **Function**: Facilitates the transport of data over long distances.
    - **Examples**: Fiber optics, microwave links, satellites.

    #### 5. **RSS (Remote Subscriber Station)**
    - **Definition**: The endpoint devices or systems used by subscribers to access telecommunication services.
    - **Function**: Acts as the interface for users to connect to the network.
    - **Examples**: Mobile phones, routers, modems.

    ### Advanced Concepts in Telecommunication
    - **5G Networks**: Features ultra-low latency, massive device connectivity, and high-speed data transfer.
    - **Network Virtualization**: Uses software-defined networking (SDN) and network function virtualization (NFV) to make networks more flexible and cost-efficient.
    - **Internet of Things (IoT)**: Integrates billions of connected devices, enabling smart homes, cities, and industries.
    - **Cybersecurity**: Ensures the protection of data and infrastructure against threats like hacking and data breaches.

    ### Challenges in Telecommunication Systems
    - **Scalability**: Handling an ever-increasing number of users and devices.
    - **Interference**: Mitigating signal interference in wireless communication.
    - **Infrastructure Costs**: Building and maintaining networks, especially in rural areas.
    - **Energy Efficiency**: Reducing power consumption, particularly in 5G and IoT networks.
    - **Regulatory Compliance**: Adhering to laws and standards across different regions.
    
    Telecommunication systems are a dynamic and essential part of modern society, continually evolving to meet the demands of global connectivity and emerging technologies.
    """)
