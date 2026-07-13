---
title: Foveation-Guided Dynamic Token Selection for Robust and Efficient Vision Transformers
title_zh: 面向鲁棒高效视觉Transformer的中心凹引导动态Token选择方法
authors:
- Ibrahim Batuhan Akkaya
- Kishaan Jeeveswaran
- Bahram Zonooz
- Elahe Arani
affiliations:
- NavInfo Europe Advanced Research Lab
- Eindhoven University of Technology Department of Mathematics and Computer Science
arxiv_id: '2607.09480'
url: https://arxiv.org/abs/2607.09480
pdf_url: https://arxiv.org/pdf/2607.09480
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 视觉Transformer 动态Token效率优化
tags:
- Vision Transformer
- Dynamic Token Selection
- Adversarial Robustness
- Efficient Inference
- HVS-inspired
one_liner: 受人类视觉系统启发提出FDT架构，通过动态Token选择兼顾ViT的推理效率、精度与原生鲁棒性
practical_value: '- 多模态电商推荐/广告系统处理图像输入时，可借鉴动态Token选择思路过滤冗余视觉信息，降低ViT推理开销，提升多模态特征抽取效率

  - Agent系统处理含噪声的多模态输入时，可复用中心凹多尺度embedding机制，无需额外对抗训练即可提升特征鲁棒性

  - 端侧推荐场景（如短视频feed流端侧预处理）可参考固定预算下高价值Token筛选逻辑，平衡推理精度与算力消耗'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前Vision Transformer（ViT）推理计算开销高，且对噪声、对抗攻击鲁棒性差，需额外训练才能提升鲁棒性；人类视觉系统（HVS）通过中心凹采样+眼动实现高效感知，能耗低且鲁棒性强，可借鉴该机制优化ViT。
### 方法关键点
提出Foveated Dynamic Transformer（FDT）架构，包含两个核心模块：① 固定模块：单前向传播过程中识别高价值固定点，过滤无关信息，动态选择有效Token；② 中心凹模块：生成携带多尺度上下文的中心凹embedding，支撑自适应注意力计算，无需额外对抗/噪声训练即可获得原生鲁棒性。
### 关键结果
50%固定预算设置下，FDT ImageNet Top-1精度达81.9%，超过基线DeiT-S的80.9%，同时乘累加运算量（MACs）降低34.57%，在精度-效率权衡上表现更优；对多种噪声、对抗攻击具备强泛化鲁棒性。
