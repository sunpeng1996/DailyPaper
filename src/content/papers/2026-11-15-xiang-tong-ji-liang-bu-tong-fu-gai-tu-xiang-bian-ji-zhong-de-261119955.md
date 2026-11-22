---
title: Equal Dose, Different Coverage:Tracing Rate and Duration in Image Editing
title_zh: 相同剂量不同覆盖：图像编辑中的速率与时长溯源
authors:
- Yi Liu
affiliations:
- 中国科学技术大学
arxiv_id: '2611.19955'
url: https://arxiv.org/abs/2611.19955
pdf_url: https://arxiv.org/pdf/2611.19955
published: '2026-11-15'
collected: '2026-11-22'
category: Multimodal
direction: 多模态图像编辑 误差溯源与优化
tags:
- Image Editing
- Diffusion Model
- FLUX
- Activation Patching
- Representation Tracing
one_liner: 通过激活补丁定位图像编辑剂量一致性误差来源，提出共享早期上下文表征的优化方案
practical_value: '- 激活补丁溯源误差的方法可迁移到LLM/GenRec错误归因，快速定位生成结果不一致的表征层、输入位置

  - 共享生成过程中不变上下文表征的trick，可用于电商商品图多属性变体生成、广告素材批量生产的一致性控制

  - 拆分一致性增益与准确率的校准评估方案，可用于生成式推荐/广告素材的效果度量，区分合规性和转化指标'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有科学图像编辑基准仅验证输出是否符合过程描述，未明确误差的表征载体，也无法衡量修正后的数量准确性，相同剂量下交换速率与时长会出现覆盖度不一致的问题。
### 方法关键点
1. 以固定沉积剖面的喷枪任务为测试场景，通过跨文本位置、去噪阶段的等范数激活补丁定位误差来源
2. 发现蒸馏版FLUX中未变化文本位置的早期上下文表征是不一致的核心来源，贡献3.51pp的符号路径差，远高于变化数字的0.09pp
3. 提出干预方案：不同路径间共享早期上下文表征，仅保留各自变化的数字表征
### 关键结果
独立英文布局测试中，蒸馏FLUX的绝对路径差从1.13pp降至0.60pp，效果优于早期数字共享方案，校准评估可有效分离一致性增益与准确率误差
