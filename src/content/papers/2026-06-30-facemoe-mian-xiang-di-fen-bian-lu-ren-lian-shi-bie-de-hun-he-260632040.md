---
title: 'FaceMoE: Mixture of Experts for Low-Resolution Face Recognition'
title_zh: FaceMoE：面向低分辨率人脸识别的混合专家模型
authors:
- Kartik Narayan
- Vishal M. Patel
affiliations:
- Johns Hopkins University
arxiv_id: '2606.32040'
url: https://arxiv.org/abs/2606.32040
pdf_url: https://arxiv.org/pdf/2606.32040
published: '2026-06-30'
collected: '2026-07-02'
category: Other
direction: 低分辨率人脸识别 · MoE动态路由
tags:
- MoE
- Dynamic Routing
- Face Recognition
- Domain Adaptation
- Sparse Activation
one_liner: 首次将MoE架构应用于低分辨率人脸识别，通过动态路由实现分辨率感知特征提取，性能显著优于现有SOTA
practical_value: '- MoE训练的联合损失设计（识别损失+router z-loss+负载均衡损失）可直接迁移到推荐系统MoE大模型训练，避免专家坍塌，保障分工合理性

  - 稀疏激活的top-k路由设计可复用在推荐大模型扩容场景，在提升模型容量的同时控制推理 latency 无线性上涨

  - 跨域微调保留预训练知识的思路可借鉴到推荐模型跨场景迁移任务，缓解灾难性遗忘问题

  - 若业务涉及人脸核验、用户肖像内容审核等多模态能力，可直接复用FaceMoE开源实现优化低质人脸识别效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
低分辨率人脸识别面临特征提取质量差、高低分辨率样本域差距大的问题，单一编码器在低分辨率数据集微调时泛化性差，且易出现灾难性遗忘。

### 方法关键点
1. 基于MoE架构搭建FaceMoE，引入多个FFN专家+top-k路由器，动态为token分配对应专家，自发形成人脸不同语义区域的专家分工，实现分辨率感知特征提取；
2. 采用稀疏激活机制，微调低分辨率数据时可保留预训练知识，扩容模型容量不会带来比例增长的计算开销；
3. 联合人脸识别损失、router z-loss、负载均衡损失训练，保障专家分工有效性与训练稳定性。

### 关键结果
在11个涵盖高分辨率、混合质量、低分辨率的基准数据集上，效果显著优于现有SOTA方法
