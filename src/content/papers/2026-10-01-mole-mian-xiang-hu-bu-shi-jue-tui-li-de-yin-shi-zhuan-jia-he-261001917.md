---
title: 'MoLE: Mixture of Latent Experts for Complementary Visual Reasoning'
title_zh: MoLE：面向互补视觉推理的隐式专家混合框架
authors:
- Yingcheng Liu
- Tianyi Jiang
- Yujuan Ding
- jiangbo Ai
- Xun Jiang
- Guoqing Wang
- Wei Ye
- Yi Bin
affiliations:
- Tongji University
- Hong Kong Polytechnic University
- Alibaba Group
- University of Electronic Science and Technology of China
arxiv_id: '2610.01917'
url: https://arxiv.org/abs/2610.01917
pdf_url: https://arxiv.org/pdf/2610.01917
published: '2026-10-01'
collected: '2026-10-03'
category: Reasoning
direction: 视觉推理 · 隐式专家混合优化
tags:
- MoE
- Visual Reasoning
- VLM
- Latent Token
- Multi-Expert
one_liner: 提出混合隐式专家框架MoLE，通过专家隔离提取互补视觉信息，无需预定义角色提升推理性能
practical_value: '- 多模态电商搜推场景可借鉴专家隔离思路，降低商品图特征提取冗余度，提升多模态特征多样性，减少重复计算

  - 两阶段训练pipeline可直接复用：先强制特征走专家通路后放开访问，无需预定义专家角色，降低多专家模型落地成本

  - 多模态Agent的商品图属性识别、图搜推理模块可复用「专家隔离+汇总专家」架构，提升复杂视觉推理准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有隐式视觉推理方法通过共享投影让多个隐式token访问相同视觉证据，无互补信息提取机制，单纯增加隐式token规模只会产生冗余表示，无法有效提升推理性能。
### 方法关键点
1. 提出MoLE隐式专家混合框架，证据提取阶段隔离各隐式视觉专家，独立控制每个专家的视觉证据访问范围与变换逻辑，再通过专用汇总专家聚合各专家输出的互补表示。
2. 采用两阶段训练pipeline：第一阶段强制视觉证据全部走隐式通路，第二阶段恢复模型直接视觉访问能力，无需预定义专家角色或中间视觉标注信号。
### 关键结果
在5个视觉推理基准上平均得分78.6，较同数据量监督微调高4.9，较相同隐式token预算下的最优基线高3.6；遮挡隐式通路后模型平均性能下降9.2，验证了专家分工的有效性
