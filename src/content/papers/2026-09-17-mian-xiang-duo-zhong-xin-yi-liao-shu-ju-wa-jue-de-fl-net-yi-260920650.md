---
title: Multi-center Medical Data Mining with FL-Net - A One-stop Shop for Federated
  Learning
title_zh: 面向多中心医疗数据挖掘的FL-Net：一站式联邦学习框架
authors:
- Simon Süwer
- Julian Klemm
- Elisa Acitelli
- Mathieu Almeida
- Lucia Altucci
- Zsolt Bagyura
- Michelangela Barbieri
- Zsolt-Zoltán Bedő
- Rosaria Benedetti
- Béla Bihari
affiliations:
- Institute for Computational Systems Biomedicine, University of Hamburg
- Sapienza University of Rome
- University of Campania Luigi Vanvitelli
- Semmelweis University
- LMU München
arxiv_id: '2609.20650'
url: https://arxiv.org/abs/2609.20650
pdf_url: https://arxiv.org/pdf/2609.20650
published: '2026-09-17'
collected: '2026-09-19'
category: Training
direction: 联邦学习 · 隐私保护多中心训练
tags:
- Federated Learning
- Privacy Preserving
- Multi-center Training
- Workflow Orchestration
one_liner: 提出满足全链路需求的一站式联邦学习框架FL-Net，支持多中心隐私合规协作训练
practical_value: '- 跨商家/跨平台的隐私合规联合推荐建模可借鉴FL-Net的模块化数据对齐、披露控制方案，数据不出域即可完成跨域模型训练

  - 容器化可复用联邦工作流的设计思路可复用到电商跨区域、跨部门的推荐模型训练工程落地，降低重复开发成本

  - 多并发客户端联邦训练的验证方法可用于大规模商家侧联合推荐模型训练的性能优化，提升多参与方训练稳定性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
联邦学习可在不共享原始用户数据的前提下实现多中心协作训练，但现有框架大多停留在模拟阶段，无法覆盖数据对齐、隐私控制、工作流复用等全链路需求，调研14款现有FL框架均无法满足文献提出的5项核心要求。
### 方法关键点
提出一站式FL框架FL-Net，整合模块化数据对齐、数据发现、披露控制、带版本的安全工具链、容器化联邦工作流执行能力，对齐后的数据和工作流可跨研究复用，构建持久化联邦训练网络。
### 关键结果数字
在MIMIC、US-130数据集上完成跨研究患者发现验证，支持最高50个并发客户端的可复现、可审计联邦工作流；目前已在2个欧盟项目落地，覆盖9国10家医院超80万患者数据。
