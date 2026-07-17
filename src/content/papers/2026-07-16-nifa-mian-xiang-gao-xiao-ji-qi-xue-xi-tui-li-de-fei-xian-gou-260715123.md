---
title: 'NIFA: Nonlinear IMC enhanced FPGA for efficient ML inference'
title_zh: NIFA：面向高效机器学习推理的非线性IMC增强FPGA架构
authors:
- Jiajun Hu
- Ruthwik Reddy Sunketa
- Lei Zhao
- Archit Gajjar
- Luca Buonanno
- Aman Arora
affiliations:
- Arizona State University
- Hewlett Packard Enterprise Labs
arxiv_id: '2607.15123'
url: https://arxiv.org/abs/2607.15123
pdf_url: https://arxiv.org/pdf/2607.15123
published: '2026-07-16'
collected: '2026-07-17'
category: Other
direction: FPGA 机器学习推理硬件架构优化
tags:
- FPGA
- IMC
- Inference Acceleration
- Transformer Inference
- ACAM
one_liner: 提出无ADC的非线性内存计算增强FPGA架构NIFA，显著提升Transformer等模型推理能效
practical_value: '- 大模型/Transformer类推荐推理侧部署可参考该架构做FPGA加速选型，长序列attention场景能效提升显著

  - KV cache、矩阵乘密集的RAG/Agent推理业务，可复用无ADC IMC的设计思路优化硬件加速方案

  - 边缘端电商推荐/广告推理低功耗部署需求下，该架构的高能效比可作为硬件选型参考'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有集成ReRAM IMC的FPGA仅支持静态权重VMM，非线性运算、动态矩阵乘（DIMM）仍需FPGA fabric处理，Transformer类模型收益有限；且IMC块内ADC占70%以上面积与功耗，限制系统扩展性。
### 方法关键点
1. 提出NIFA架构，用原生支持非线性运算的ACAM替代传统ADC，打造无ADC的IMC块
2. 开展FPGA感知的设计空间探索，平衡面积、灵活性与深度学习性能确定最优交叉bar尺寸
3. 设计ACAM适配的DIMM映射方法，将IMC适用范围扩展到attention计算
### 关键结果
CNN基准下能效最高提升40×、面积效率提升4.1×；Transformer基准下能效提升1.9×、面积效率提升2.5×，长输入序列下仍保持稳定增益。
