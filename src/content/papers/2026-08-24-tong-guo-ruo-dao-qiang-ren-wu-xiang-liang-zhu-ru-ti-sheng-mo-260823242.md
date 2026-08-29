---
title: Mind the Couch! Eliciting MLLM Reasoning in Interior Design via Weak-to-Strong
  Task Vector Injection
title_zh: 通过弱到强任务向量注入提升多模态大模型室内设计推理能力
authors:
- Yuxuan Yang
- Jingyao Wang
- Luntian Mou
affiliations:
- Nanjing Forestry University
- Institute of Software Chinese Academy of Sciences
- University of the Chinese Academy of Sciences
- Beijing University of Technology
arxiv_id: '2608.23242'
url: https://arxiv.org/abs/2608.23242
pdf_url: https://arxiv.org/pdf/2608.23242
published: '2026-08-24'
collected: '2026-08-29'
category: Reasoning
direction: 多模态大模型 · 推理优化
tags:
- MLLM
- Task Vector
- Weak-to-Strong
- Latent Injection
- Multimodal Reasoning
one_liner: 提出DART-I机制，无需微调冻结MLLM，通过任务向量注入解决室内设计场景模态错位与推理幻觉
practical_value: '- 多模态垂类场景（家居电商导购、AI设计Agent）可复用「轻量弱专家提取确定性规则特征→转任务向量注入冻结大模型隐空间」范式，无需微调即可降低幻觉，节省算力

  - 涉及空间约束、美学约束的垂类生成任务，可参考弱到强规则锚定思路，用低成本确定性先验约束大模型推理，减少物理冲突、审美错位类bad case

  - 任务向量动态残差注入方案可直接迁移到垂类MLLM优化场景，避免微调带来的灾难性遗忘和高计算成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有MLLM在高密度约束的室内设计场景存在严重模态错位问题：视觉编码阶段丢失高频局部拓扑细节、细粒度美学特征，导致推理幻觉频发，输出存在空间物理碰撞、视觉审美不协调等错误；传统微调MLLM方案计算成本高、易引发灾难性遗忘。
### 方法关键点
提出双先验激活残差任务向量注入机制DART-I，范式从有损文本prompt转向直接隐空间干预：1. 用极轻量弱专家从图像显式提取连续空间距离、色彩排版两类确定性先验特征；2. 经线性投影网络将先验转换为定向任务向量；3. 向量作为残差项动态注入冻结MLLM的隐空间，锚定推理逻辑，全程无需微调大模型。
### 关键结果
多组室内设计推理公开基准实验验证，DART-I性能显著优于传统prompting、轻量微调等基线方案，无灾难性遗忘问题，计算成本远低于微调方案。
