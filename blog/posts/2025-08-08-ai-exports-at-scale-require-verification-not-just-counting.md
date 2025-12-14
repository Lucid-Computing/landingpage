---
title: AI Exports at Scale Require Verification, Not Just Counting
slug: ai-exports-at-scale-require-verification-not-just-counting
date: 2025-08-08
author: Kristian Rönn
tags:
  - National Security
  - AI Trade Policy
  - AI Security
  - Export Controls
image: /media/wbfAO30etTdjdRF5oESER55KaA.png
description: To fulfill the promise of the AI Action Plan, export controls must evolve beyond physical counting and embrace scalable, hardware-rooted verification.
---

# AI Exports at Scale Require Verification, Not Just Counting

## Introduction: The Gap Between Policy Assumptions and Technical Reality

In his July 30, 2025 address at the Center for Strategic and International Studies, White House Office of Science and Technology Policy Director Michael Kratsios outlined the Trump Administration's approach to AI export control enforcement. While acknowledging resource constraints at the Bureau of Industry and Security (BIS), Kratsios expressed confidence that physical chip tracking presents manageable challenges, characterizing AI hardware as "massive racks that are tons in weight" that are difficult to relocate and easy to monitor—implying that simple physical inspections could suffice.

This assessment, while reflecting legitimate policy optimism with the sensible aim of scaling American AI exports rapidly and securely, appears to underestimate both the technical portability of export-controlled AI accelerators and the effective methods already being used to circumvent those export controls. Recent high-profile cases of AI chip smuggling and transshipment efforts  reveal a more complex enforcement challenge that requires technological solutions beyond traditional physical inspection approaches. Fortunately, there are scalable technical solutions that can effectively verify the location and status of AI chips, providing the "tools that BIS needs to do the enforcement activities" which Kratsios rightly signalled is necessary to secure American AI dominance.

## The Portability Reality: Individual Components, Not Integrated Systems

### Technical Specifications Contradict Immobility Claims

The characterization of AI chips as immobile infrastructure misconstrues their actual technical attributes. Export-controlled AI accelerators are individual, highly portable components rather than integrated rack systems. As one customs official noted in recent smuggling case documentation, individual AI accelerators are "comparable in size to a Nintendo Switch" rather than massive installations requiring industrial equipment for transport.

**NVIDIA H100 PCIe Specifications:**
- **Weight**: 2-5 pounds per card
- **Form Factor**: Standard dual-slot PCIe component
- **Power Draw**: 350W (within desktop system envelopes)
- **Dimensions**: Comparable to a large graphics card

This modularity has real enforcement implications. Modern server architectures specifically enable hot-swappable accelerator modules. Of a typical $50,000 AI server cost, approximately $40,000 represents the accelerator cards themselves—components that can be removed in minutes while leaving empty enclosures that appear fully operational during casual inspection. With accelerator modules accounting for the bulk of server value, actors on the BIS entity list can readily remove or transship controlled components through global gray markets while leaving enclosures behind that appear operational.

### Documented Cases of Physical Diversion Demonstrate Practical Challenges

These challenges aren't theoretical. Enforcement authorities have uncovered multiple instances in recent months that demonstrate just how easily AI chips can be diverted and the sophisticated methods already employed to circumvent the current export control system.

**Singapore Smuggling Network (2025):** Authorities charged three individuals with smuggling $390 million worth of NVIDIA chips, including H100 and B200 models. The operation successfully transported individual accelerator cards through standard commercial channels before detection.

**Student Transport Methods:** Documentation reveals students successfully transported 6 NVIDIA compute cards in personal luggage, declaring them at $100 each to customs authorities. The compact nature of individual accelerators enables concealment within routine travel patterns.

**Commercial-Scale Evasion:** Reuters reported that "over $1 billion worth of banned NVIDIA chips entered China in Q2 2025 alone" through various smuggling networks. These operations relied on the portability of individual components rather than attempting to relocate entire server systems.

## The Chinese AI Training Ecosystem: Built on Smuggled Hardware

### DeepSeek and the Underground Economy

Recent analysis suggests that Chinese AI capabilities, including breakthrough models like DeepSeek, rely heavily on smuggled NVIDIA hardware. A [recent report from the Center for a New American Security](https://www.cnas.org/publications/reports/countering-ai-chip-smuggling-has-become-a-national-security-priority) showed that over 100,000 export controlled chips were smuggled into China in 2024 alone, with a median estimate of 140,000 chips. Public reporting cited documents individual graymarket orders worth up to $120 million for shipments of thousands of H100 chips.

**Gray Market Pricing Indicates Robust Demand:** Market signals corroborate these findings. Smuggled H100s in China sell in gray markets for significant markups—often exceeding 50% over U.S. MSRP—commanding prices of $45,000 or more per chip. This price differential indicates both substantial demand and successful supply networks operating beyond regulatory oversight.

**Training Infrastructure Adaptation:** Chinese research institutions have developed sophisticated techniques for maximizing training efficiency using smaller, distributed clusters of smuggled hardware. As one industry analyst observed, "Chinese labs are training 90% of their models using smuggled components integrated into seemingly legitimate research infrastructure."

### Underground Support Networks

**Shenzhen Repair Services:** Underground repair services in Shenzhen now handle "500 banned GPU repairs monthly," indicating a mature support ecosystem for smuggled hardware. These services provide the technical infrastructure necessary to maintain operational capability for components obtained through illicit channels.

**Shell Company Aggregation:** Chinese firms have established "multiple shell companies placing small orders across third countries to aggregate restricted hardware," according to CNAS research. This approach exploits regulatory thresholds while building substantial computational capabilities.

## BIS Resource Constraints: The Enforcement Reality

**Personnel and Capability Limitations:** Several policymakers have expressed unwarranted optimism about the ease of AI export control enforcement—often grounded in technical misunderstandings about how modular, high-value AI accelerators can be moved, hidden, or repurposed. With only [a portion of 585 positions overseeing $486.4 billion](https://www.gao.gov/assets/gao-25-107431.pdf?utm_source=chatgpt.com) in annual licensed exports, BIS and its other government partners operate under real-world constraints. The task of overseeing hundreds of billions of dollars in dual-use technologies with limited personnel and global reach is an inherently difficult mission. And despite the dedication of its staff, BIS must operate in a system where traditional tools—periodic inspections, documentation audits, and license compliance checks—were not designed with modular AI accelerators in mind. The Government Accountability Office noted that BIS field offices "lack analytical tools and personnel for systematic risk analyses" and have "no systematic approach to identifying high-risk entities." In short, physical counting approaches simply exceed current BIS operational capabilities.

Compounding the challenge, frontline export control officers—of which BIS has only dozens to monitor global compliance—often lack access to real-time risk assessments or specialized inspection tools. Field inspections may catch obvious violations, but they are not well-equipped to detect partial diversion, distributed system assembly, or chip-level concealment. Legitimate industry stakeholders, meanwhile, frequently voice concern about the operational burden of traditional compliance mechanisms, especially when physical inspections risk downtime or data disruption. These constraints reflect systemic design gaps, not lack of effort.

To succeed in this new environment, enforcement strategies must evolve alongside the technology landscape they are meant to secure.

**Customer Impact and Operational Challenges**

**Industry Resistance to Intrusive Monitoring:** Many legitimate customers consider physical counting "invasive and an operational hindrance." This resistance creates pressure to minimize inspection frequency and thoroughness, potentially enabling evasion through timing manipulation.

**Detection Reliability Problems:** Empty server enclosures can be fitted with "cheap PCB replicas" that appear operational during visual inspection while containing no actual processing capability. Without sophisticated technical inspection equipment, physical counting may provide false confidence in compliance verification.

## Technical Evasion Capabilities: Beyond Physical Smuggling

### Distributed Training Approaches

Recent research demonstrates viable approaches for training large models across globally distributed, smaller GPU clusters that appear as routine cloud usage rather than concentrated training operations.

**Geographic Distribution:** Google trained Gemini Ultra across multiple data centers using geographic distribution methods that major technology companies routinely employ. Similar approaches enable sophisticated actors to utilize distributed smuggled hardware while appearing to comply with concentration-based detection methods.

**OpenDiLoCo Research:** Academic research projects like OpenDiLoCo enable "training across poorly connected clusters by reducing synchronization frequency," demonstrating practical approaches for utilizing smuggled hardware through distributed networks that evade traditional monitoring approaches.

### Advanced Obfuscation Techniques

**Power Signature Manipulation:** Engineers have developed "power smoothing commands specifically designed to obscure training signatures," making detection through power consumption analysis unreliable. Empirical measurements show AI training creates "instant fluctuations of power consumption across the datacenter on the order of tens of megawatts," complicating steady-state detection approaches.

**Traffic Pattern Obfuscation:** Modern distributed training uses encrypted protocols that generate "elevated rates of false positives" in detection systems. Collective communication operations create irregular patterns difficult to distinguish from other high-bandwidth applications.

## The Path Forward: Technology-Enabled Verification

### Hardware-Rooted Authentication

Rather than relying solely on physical counting, robust export control enforcement requires hardware-level verification systems that cannot be circumvented through component substitution or geographic relocation.

**Cryptographic Attestation:** Modern AI accelerators incorporate Trusted Execution Environments (TEEs) capable of generating unforgeable location and usage attestations. These systems provide continuous verification rather than periodic inspection snapshots.

**Real-Time Monitoring:** Location verification systems can provide continuous, automated monitoring that supplements rather than replaces traditional enforcement approaches while addressing the resource constraints Director Kratsios correctly identified.

### Policy Integration Opportunities

The Trump Administration's emphasis on reducing regulatory burden while maintaining security creates opportunities for technology-enabled compliance that reduces both enforcement costs and industry operational impact.

**Automated Compliance:** Hardware-rooted verification systems can provide the "tools that BIS needs to do the enforcement activities" while reducing the invasive inspection requirements that concern legitimate customers.

**Strategic Resource Allocation:** By automating routine compliance verification, BIS resources can focus on sophisticated evasion attempts and strategic enforcement priorities rather than manual counting activities.

## Conclusion: Bridging Policy Optimism with Technical Realities

Characterizing AI chip tracking as a simple physical counting exercise underestimates both the technical sophistication of evasion methods and the portable nature of the hardware itself.

The documented success of smuggling efforts, the reliance of Chinese AI development on illicit hardware, and the inherent limitations of manual inspection approaches suggest that effective export control enforcement requires technological solutions that complement traditional regulatory approaches.

The Trump Administration's AI Action Plan creates opportunities to deploy verification technologies that address these challenges while supporting the broader goal of American AI dominance. Rather than choosing between regulatory effectiveness and industry cooperation, technology-enabled approaches can enhance both enforcement capability and operational efficiency.

The strategic imperative remains clear: ensuring that America's AI leadership translates into sustained competitive advantage requires verification systems adequate to the technical sophistication of both the technology and those who seek to circumvent controls. Physical counting, while important, represents only the foundation of a comprehensive approach that must evolve alongside the threats it seeks to address.

The challenge is not whether export controls matter—they clearly do—but whether enforcement approaches can keep pace with the technical realities of an increasingly sophisticated global technology landscape. *If America wants to lead in building the AI stack for the world, it must also lead in verifying that stack is protected.*
