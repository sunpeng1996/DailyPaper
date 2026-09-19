---
title: 'RISC-V and machine learning: a survey'
title_zh: RISC-V与机器学习研究综述
authors:
- Shriman Keshri
- Apparna Singh
- Chinmaya Kumar Palo
- Shreya Adya
- Subhankar Mishra
affiliations:
- National Institute of Science Education and Research, Bhubaneswar
- Sri Sri University, Cuttack
- Gandhi Institute of Engineering and Technology University, Gunupur
- Homi Bhabha National Institute, Mumbai
arxiv_id: '2609.20677'
url: https://arxiv.org/abs/2609.20677
pdf_url: https://arxiv.org/pdf/2609.20677
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 机器学习硬件 · RISC-V生态调研
tags:
- RISC-V
- ML Accelerator
- Edge Inference
- ISA Extension
- Open Source Hardware
one_liner: 系统梳理RISC-V机器学习生态现状与性能权衡，给出统一分类体系和未来研发路线
practical_value: '- 端侧个性化推荐/轻量Agent部署场景，可参考文中RISC-V ML性能权衡数据评估低功耗硬件方案，降低边缘推理成本

  - 大模型/生成式推荐模型离线端侧部署时，可复用文中RISC-V编译器优化、专用指令扩展的设计思路做适配优化

  - 若业务涉及智能零售终端、线下推荐硬件自研，可跟进文中梳理的低功耗多域架构、神经扩展方向做技术预研'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
闭源硬件无法满足机器学习场景对可定制、低功耗、低成本部署的需求，RISC-V开源指令集的灵活性成为潜在解决方案，但业界缺乏系统的全栈生态梳理与落地参考。
### 方法关键点
覆盖学术、工业界RISC-V ML全链路实现，从指令集扩展、核心设计、编译器优化到部署策略展开分析，构建RISC-V ML实现的统一分类体系，横向对比不同方案的性能与设计权衡，评估现有软件工具链成熟度。
### 关键结果
当前RISC-V ML在能效、专用指令开发、框架集成上已有明确进展，但仍存在标准化不足、验证复杂度高、生态碎片化三大核心挑战；梳理得出专用神经处理扩展、自适应模块化处理器架构、安全框架、低功耗跨域架构四大研发方向，为下一代ML硬件落地提供路线图。
