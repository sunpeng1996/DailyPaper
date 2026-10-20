---
title: Consistent Distribution Matching for Data-Free Diffusion Distillation
title_zh: 面向无数据扩散模型蒸馏的一致性分布匹配方法
authors:
- Yuxiang Fu
- Qi Yan
- Zike Wu
- Yongxing Zhang
- Purang Abolmaesumi
- Lele Wang
- Renjie Liao
affiliations:
- University of British Columbia
- Vector Institute for AI
- Canada CIFAR AI Chair
arxiv_id: '2610.09221'
url: https://arxiv.org/abs/2610.09221
pdf_url: https://arxiv.org/pdf/2610.09221
published: '2026-10-05'
collected: '2026-10-20'
category: Training
direction: 扩散模型 · 无数据蒸馏推理加速
tags:
- Diffusion Distillation
- Data-Free Training
- Generative Model
- Distribution Matching
- Inference Acceleration
one_liner: 提出无数据无模拟的扩散蒸馏框架，仅需双模型单目标，少步生成效果超SOTA且显存更低
practical_value: '- 生成式推荐场景中用Diffusion生成商品图、营销素材时，可复用该无数据蒸馏方法加速推理，无需额外收集蒸馏数据集，降低训练成本

  - 该仅需冻结教师+可训学生双模型、单优化目标的轻量蒸馏架构，可直接迁移到LLM、多模态生成模型的轻量化任务，简化训练链路

  - 针对生成式推荐少步高保真输出需求，可借鉴其分布匹配的Wasserstein收敛约束，在蒸馏时平衡推理速度与生成质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Diffusion、流生成模型推理依赖耗时的数值积分，现有蒸馏方法需定制蒸馏数据集、高成本教师rollout或辅助代理网络，训练链路复杂难以规模化。
### 方法关键点
提出一致性分布匹配的无模拟无数据蒸馏方案，单学生网络统一样本生成与score estimation，仅用冻结教师+可训学生两个模型，优化单一目标，理论证明目标最小化可实现学生流映射输出与教师边缘分布的Wasserstein收敛。
### 关键结果
ImageNet 256×256任务上训练40epoch即可收敛：1-NFE下FID达2.04，4-NFE下FID达1.37，超过现有无数据蒸馏SOTA；单A100 80G训练显存仅20GB，较同类方法降低40%以上。
