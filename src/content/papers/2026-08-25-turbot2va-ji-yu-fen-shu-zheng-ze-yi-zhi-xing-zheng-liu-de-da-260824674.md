---
title: 'TurboT2VA: Fast Large-Scale Text-to-Video-Audio Generation via Score-Regularized
  Consistency Distillation'
title_zh: TurboT2VA：基于分数正则一致性蒸馏的大规模文本音视频生成加速
authors:
- Xiaoda Yang
- Yuxiang Liu
- Kaiwen Zheng
- Yuan Liu
- Yibo Lai
- Shengpeng Ji
- Kai Jiang
- Jianfei Chen
- Xiaobin Hu
- Shuicheng Yan
arxiv_id: '2608.24674'
url: https://arxiv.org/abs/2608.24674
pdf_url: https://arxiv.org/pdf/2608.24674
published: '2026-08-25'
collected: '2026-08-26'
category: Multimodal
direction: 多模态生成 · 推理加速
tags:
- Consistency Distillation
- Inference Acceleration
- Multimodal Generation
- Quantization
- Text-to-Video-Audio
one_liner: 提出TurboT2VA框架，实现19B参数文本音视频生成模型最高54.67倍推理加速
practical_value: '- 电商/广告生成式短视频制作场景可复用分阶段一致性蒸馏方案，少量采样步即可保留生成质量，大幅降低推理成本

  - 多模态生成推理优化可借鉴架构感知栈设计：W8A8量化+算子融合+模态感知稀疏注意力，兼顾速度和跨模态对齐效果

  - 多模态联合训练的模态不平衡问题可采用per-modality归一化trick，稳定训练过程、平衡各模态生成质量'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前联合文本生成音视频的大模型采样轨迹长、多模态计算异构，推理成本极高难以落地；大规模蒸馏还面临模态优化不平衡、连续一致性训练难度大、质量与多样性难以权衡的问题。
### 方法关键点
1. 采用per-modality归一化解决模态优化不平衡问题；
2. 设计渐进式训练课程：离散一致性预热→连续一致性精调→联合一致性-分布匹配，先稳定生成轨迹再做分布级优化；
3. 配套架构感知推理栈，整合guarded W8A8量化、算子融合、填充文本压缩、模态感知稀疏注意力，保留跨模态对齐通路。
### 关键结果
512×768标准分辨率下4步蒸馏实现20.1倍加速，延迟从50.52s降至2.51s，保留生成质量、音视频同步性与多样性；1024×1792高分辨率下单NVIDIA H20上实现54.67倍加速，延迟从318.74s降至5.83s。
