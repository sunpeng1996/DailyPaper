---
title: 'Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts'
title_zh: 域算术：环境偏移下的单样本视觉语言动作模型适配
authors:
- Taewook Kang
- Taeheon Kim
- Donghyun Shin
- Jonghyun Choi
affiliations:
- Seoul National University
arxiv_id: '2607.00666'
url: https://arxiv.org/abs/2607.00666
pdf_url: https://arxiv.org/pdf/2607.00666
published: '2026-06-30'
collected: '2026-07-03'
category: Multimodal
direction: 多模态VLA模型 · 单样本域适配
tags:
- VLA
- One-shot Adaptation
- Domain Shift
- Weight Arithmetic
- Subspace Alignment
one_liner: 提出基于权重向量算术的DART方法 仅需单样本即可实现VLA模型环境偏移适配
practical_value: '- 权重向量算术+子空间对齐思路可迁移至推荐跨域冷启动场景，新商家/新类目适配无需大量样本微调，通过源域与目标域权重运算快速实现适配

  - 单样本域适配框架可复用给多模态导购Agent的环境适配，线下场景切换/传感器参数调整时仅需1个样本即可完成快速适配

  - 奇异分量过滤噪声的trick可用于大模型LoRA微调的权重后处理，降低小样本微调时的噪声干扰，提升小样本微调稳定性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLA模型在部署时遭遇环境偏移（如相机位姿变化、机器人实体形态切换）会出现性能骤降，现有适配方法需要采集大量目标域演示样本，数据标注与训练成本极高，小样本微调泛化性难以保障。

### 方法关键点
通过类比式权重向量算术实现域适配，仅需采集1个目标域演示样本即可完成适配；通过权重向量奇异分量的子空间对齐过滤噪声，精准提取域专属信息注入模型，无需大规模全参数/增量微调。

### 关键结果
仿真与真实世界实验中，在多种视觉偏移、实体形态偏移的单样本适配场景下，性能全面优于现有SOTA VLA适配方法。
