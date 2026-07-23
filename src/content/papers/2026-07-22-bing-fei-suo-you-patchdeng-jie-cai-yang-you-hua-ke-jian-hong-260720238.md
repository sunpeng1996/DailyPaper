---
title: 'Not All Patches are Equal: Sampling Matters for Visible-Infrared Pre-Training'
title_zh: 并非所有Patch等价：采样优化可见光-红外预训练
authors:
- Qiwei Ma
- Bin Deng
- Junjie Zhu
- Qiangjuan Huang
- Puhong Duan
- Ke Yang
- Xudong Kang
- Shutao Li
affiliations:
- 湖南大学人工智能与机器人学院
- 岳麓山工业创新中心
- 北京智能博弈与决策实验室
arxiv_id: '2607.20238'
url: https://arxiv.org/abs/2607.20238
pdf_url: https://arxiv.org/pdf/2607.20238
published: '2026-07-22'
collected: '2026-07-23'
category: Multimodal
direction: 多模态预训练 · 跨模态对比学习优化
tags:
- Multimodal Pre-training
- Contrastive Learning
- Curriculum Learning
- Cross-modal Alignment
- Patch Sampling
one_liner: 提出基于patch可靠性加权的可见光-红外预训练采样方法IAS，适配多种对齐范式下游普遍涨点
practical_value: '- 多模态商品表征预训练可借鉴patch加权思路，针对不同模态成像差异过滤无意义对齐区域，降低算力浪费同时提升表征质量

  - 轻量采样器+手工先验热启动的设计可直接插入现有预训练pipeline，无需修改主干架构，落地成本极低

  - 从易到难的课程学习采样策略可迁移到跨域推荐预训练，逐步扩大训练样本覆盖范围，提升下游泛化性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有可见光-红外（VIS-IR）预训练普遍采用均匀patch对比学习，但两者成像物理特性差异导致部分空间配对区域天然可比性低，等权对齐会拖累表征学习效果和下游迁移性能。
### 方法关键点
提出即插即用的重要性感知采样（IAS）：
1. 从红外结构线索生成patch权重，对对比学习目标重加权；
2. 用轻量采样器学习软重要性掩码，支持手工先验热启动；
3. 采用patch课程学习策略，从高可靠区域逐步扩展到难样本。
### 关键结果
在多个VIS-IR基准上，相比UNIV、ImageBind等强基线，在红外语义分割、红外目标检测、可见光语义分割、跨模态检索任务上均实现一致性能提升。
