---
title: What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow
  Matching
title_zh: 像素空间流匹配v预测失效原因分析：基于分块PCA视角
authors:
- Tianze Luo
- Haofeng Huang
- Yuan Yao
affiliations:
- Tsinghua University
- Shanghai Qi Zhi Institute
arxiv_id: '2611.12852'
url: https://arxiv.org/abs/2611.12852
pdf_url: https://arxiv.org/pdf/2611.12852
published: '2026-11-09'
collected: '2026-11-11'
category: Other
direction: 生成建模 · 流匹配目标优化
tags:
- Flow Matching
- v-prediction
- Patch-wise PCA
- Raw-injected Transformer
- Generative Modeling
one_liner: 从分块PCA视角定位v预测训练瓶颈，提出RiT架构恢复像素空间流匹配v预测的训练效果
practical_value: '- 电商商品图、营销素材AIGC团队可复用RiT的「轻量原始条件解码器+输出侧shortcut」架构，降低端到端像素级生成的训练难度，提升生成质量

  - 采用流匹配做生成任务时，可参考分块PCA的带宽瓶颈分析结论，优先分配算力给主成分语义建模，避免次要成分信息保留挤占核心建模资源

  - 若需使用v-prediction简化流匹配推理逻辑，可直接复用RiT架构设计，不需要切换x-prediction目标即可达到可比训练效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Latent Diffusion Models存在两阶段训练复杂、预训练自编码器重建上限问题，像素空间Flow Matching是端到端替代方案，但标准v-prediction目标训练难度高，现有归因缺乏底层机制解释
### 方法关键点
1. 通过Patch-wise PCA分析定位v-prediction失效的带宽瓶颈：次要成分速度高度依赖原始噪声输入，backbone需同时保留原始信息和建模主成分，资源竞争导致训练失效
2. 揭示x-prediction有效的核心逻辑：参数化自带原始输入旁路，表征自发聚焦主成分，本质是隐式条件均值解码器
3. 提出Raw-injected Transformer（RiT）：轻量原始条件解码器+输出侧shortcut，分离语义建模和原始状态传播，恢复v-prediction训练有效性
### 关键结果
ImageNet 256×256数据集上，RiT各尺度模型FID-50K均优于基线JiT，其中H/16版本训练480epoch即可达到FID 1.79，优于同尺度基线训练600epoch的1.86
