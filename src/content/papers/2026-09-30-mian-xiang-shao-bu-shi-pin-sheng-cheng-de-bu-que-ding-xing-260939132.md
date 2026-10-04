---
title: Uncertainty-Aware Consistency Distillation for Few-Step Video Generation
title_zh: 面向少步视频生成的不确定性感知一致性蒸馏方法
authors:
- Lingyu Liu
- Yaxiong Wang
- Li Zhu
- Zhedong Zheng
affiliations:
- Xi'an Jiaotong University
- Hefei University of Technology
- University of Macau
arxiv_id: '2609.39132'
url: https://arxiv.org/abs/2609.39132
pdf_url: https://arxiv.org/pdf/2609.39132
published: '2026-09-30'
collected: '2026-10-04'
category: Multimodal
direction: 多模态生成 · 一致性蒸馏优化
tags:
- Consistency Distillation
- LoRA
- Video Generation
- Uncertainty Estimation
- Diffusion Model
one_liner: 提出不确定性感知一致性蒸馏方法，实现4步视频生成的SOTA效果与更优用户偏好
practical_value: '- 电商营销短视频、商品展示素材的少步生成蒸馏可复用不确定性加权思路，降低高动态区域训练惩罚，兼顾生成效率与质量

  - 多模态生成任务做一致性蒸馏时，可借鉴双扰动教师路径构造无参数不确定性代理的方案，无需额外标注即可实现动态权重分配

  - 大模型少步推理加速场景，可复用LoRA适配+特征空间对抗训练的组合，大幅降低采样步数的同时保留语义一致性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多步视频扩散/流匹配模型采样需数十步，推理延迟高；常规一致性蒸馏未区分不同时空区域的监督可信度，高动态区域（如流水、移动光影）生成误差大。
### 方法关键点
1. 提出UACD框架，构造两条独立扰动的教师引导一致性路径，以学生预测与共识目标的差值作为无参数不确定性代理；
2. 对高不确定性区域指数放松一致性惩罚，其余区域保留全量惩罚，避免强制学习不可靠目标；
3. 融合特征空间对抗训练与语义对齐，搭配LoRA参数高效适配，保障大幅降步后的生成质量。
### 关键结果
基于50步Wan模型蒸馏得到的4步生成模型，在VBench 2.0上达到0.556的平均得分，为当前SOTA，用户偏好显著优于同类方法。
