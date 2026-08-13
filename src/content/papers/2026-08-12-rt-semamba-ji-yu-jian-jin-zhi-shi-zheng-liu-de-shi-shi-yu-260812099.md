---
title: 'RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation'
title_zh: RT-SEMamba：基于渐进知识蒸馏的实时语音增强Mamba模型
authors:
- Rong Chao
- Sung-Feng Huang
- Moreno La Quatra
- Sabato Marco Siniscalchi
- Wen-Huang Cheng
- Szu-Wei Fu
- Yu Tsao
affiliations:
- Academia Sinica, Taiwan
- National Taiwan University, Taiwan
- Kore University of Enna, Italy
- University of Palermo, Italy
- NVIDIA
arxiv_id: '2608.12099'
url: https://arxiv.org/abs/2608.12099
pdf_url: https://arxiv.org/pdf/2608.12099
published: '2026-08-12'
collected: '2026-08-13'
category: Other
direction: 实时语音增强 · Mamba落地优化
tags:
- Mamba
- Knowledge Distillation
- Real-time Inference
- Speech Enhancement
- State Space Model
one_liner: 基于因果时频Mamba块与渐进知识蒸馏，实现低延迟高推理效率的实时语音增强
practical_value: '- 低延迟实时场景可参考Mamba固定大小循环状态设计，替代Transformer KV cache，降低长序列推理内存/带宽开销，适配直播实时分析、语音交互Agent等场景

  - 大模型压缩可复用渐进知识蒸馏策略，同时蒸馏输出层与中间层表征，可在不损失推理速度的前提下提升小模型效果，适配端侧/边缘侧部署

  - 延迟敏感的在线服务可参考本文质量-延迟权衡思路，在核心指标可控下降范围内通过蒸馏实现数倍推理提速，降低在线服务成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
实时语音增强对AR/VR、会议、语音交互等场景的延迟、内存开销要求极高，传统Transformer架构依赖随序列长度增长的KV cache，长序列推理效率低、成本高，直接训练小模型效果难以达标。
### 方法关键点
1. 基于因果时频Mamba块构建全因果语音增强模型，每层仅传播固定大小的循环状态，无需动态扩容的KV cache
2. 提出渐进知识蒸馏策略，同时蒸馏教师模型的复杂频谱输出和中间层表征，将8层教师模型压缩为1层浅层学生模型
### 关键结果
- 8层RT-SEMamba在25ms算法延迟约束下，Voicebank-DEMAND数据集PESQ达3.32
- 蒸馏后的1层学生模型PESQ从 naive 基线3.06提升至3.18，推理速度是教师模型的2.75倍，且稳态实时因子（RTF）保持不变
