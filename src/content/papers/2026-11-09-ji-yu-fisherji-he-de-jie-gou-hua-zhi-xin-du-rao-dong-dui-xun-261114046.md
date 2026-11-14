---
title: Structured Confidence Perturbation via Fisher Geometry for Adversarial Training
title_zh: 基于Fisher几何的结构化置信度扰动对抗训练方法
authors:
- Chenlong Wei
- Hanling Wang
- Chong Zhang
- Qinkai Yu
- Fangyu Wu
- Xiaobo Jin
affiliations:
- Xi’an Jiaotong-Liverpool University
- University of California, San Diego
- University of Exeter
arxiv_id: '2611.14046'
url: https://arxiv.org/abs/2611.14046
pdf_url: https://arxiv.org/pdf/2611.14046
published: '2026-11-09'
collected: '2026-11-14'
category: Training
direction: 对抗训练 · 模型鲁棒性优化
tags:
- Adversarial Training
- Fisher Information Matrix
- Robustness
- KL Divergence
- Perturbation
one_liner: 提出融合混合损失与Fisher几何的结构化扰动方法，解决对抗训练伪攻击问题，提升模型鲁棒性
practical_value: '- 推荐/广告模型对抗训练可复用交叉熵+KL散度混合损失目标，避免伪攻击导致的鲁棒性虚高，提升模型对输入扰动的抗性

  - 高置信度样本扰动优化可借鉴Fisher信息矩阵主特征向量的扰动方向设计思路，直接复用论文提供的高效算法规避高维矩阵计算开销

  - Agent/LLM推理鲁棒性优化可参考置信度流形上分布距离最大化思路，构造针对性扰动做对抗训练，降低幻觉/误判率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
对抗训练普遍存在「伪攻击」问题：扰动仅提升损失值，未真正改变模型置信度结构，导致鲁棒性提升效果虚高。
### 方法关键点
1. 设计融合交叉熵与KL散度的混合优化目标，让对抗样本同时破坏预测准确率与分布一致性；
2. 基于Fisher几何重构对抗训练流程，生成在置信度流形上最大化分布距离的扰动，理论证明最优扰动方向对齐Fisher信息矩阵主特征向量，配套高效算法避免高维矩阵计算开销。
### 关键结果
多数据集、多模型架构实验显示，方法优于现有对抗训练方案，对抗鲁棒性、鲁棒迁移性均有提升，尤其在高置信度区域的结构扰动效果表现突出。
