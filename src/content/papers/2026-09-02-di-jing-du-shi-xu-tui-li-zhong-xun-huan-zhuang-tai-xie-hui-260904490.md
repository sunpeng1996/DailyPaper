---
title: 'When Quantization Breaks Memory: Recurrent-State Write-Back in Low-Precision
  Temporal Inference'
title_zh: 低精度时序推理中循环状态写回导致量化失效的机制与优化
authors:
- Ismail Erbas
- Xavier Intes
- Vikas Pandey
affiliations:
- Rensselaer Polytechnic Institute
- Department of Biomedical Engineering
- Center for Modeling, Simulation, and Imaging in Medicine
arxiv_id: '2609.04490'
url: https://arxiv.org/abs/2609.04490
pdf_url: https://arxiv.org/pdf/2609.04490
published: '2026-09-02'
collected: '2026-09-08'
category: Training
direction: 循环网络 · 低精度量化推理优化
tags:
- Quantization
- RNN
- GRU
- LSTM
- Low-Precision Inference
one_liner: 揭示低精度循环推理中状态写回规则的核心影响，提出三种无需重训的精度恢复方案
practical_value: '- 基于GRU/LSTM做用户行为序列建模的推荐/广告模型量化部署时，需重点校验循环状态写回阈值，避免小梯度更新被截断导致的效果暴跌

  - 量化后RNN类模型出现效果骤降时，可直接复用论文提出的误差反馈、残差记忆、方向记忆三种方案，无需重新训练即可恢复精度

  - 对LSTM做量化裁剪时，可给cell状态分配更高存储位宽、给hidden状态分配更低位宽，在不损失效果的前提下降低整体算力开销'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
量化是降低神经网络推理内存与算力开销的核心手段，但循环网络中量化后的状态需跨时间步存储传递，状态写回规则会显著影响后续推理效果，现有量化方案对该环节的影响缺乏系统性研究。
## 方法关键点
定义循环状态写回规则概念，在GRU/LSTM架构上开展控制变量实验，定位量化失效根因为低于写回阈值的小更新被持续截断，提出误差反馈、残差记忆、方向记忆三种无需重训的精度修复方案。
## 关键结果数字
固定训练完成的GRU模型，采用4位精度存储循环状态时，τ1/τ2估计误差分别升高70倍、300倍；三种修复方案可基本恢复原模型精度；实验验证LSTM的cell状态对写回精度的敏感度远高于hidden state，适配写回规则的训练可进一步提升量化模型兼容性。
