---
title: On Potentiality and Actuality Of Foundation Models
title_zh: 大模型的潜能与实现：任务适配仅需输入无关的层级常数偏移
authors:
- Fabian Gröger
- Shuo Wen
- Maria Brbić
affiliations:
- EPFL
arxiv_id: '2611.32991'
url: https://arxiv.org/abs/2611.32991
pdf_url: https://arxiv.org/pdf/2611.32991
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: 大模型参数高效微调 · 适配机制
tags:
- LoRA
- Parameter-Efficient Fine-Tuning
- Foundation Model
- Activation Steering
- Fine-Tuning
one_liner: 揭示大模型预训练已内置多数任务潜能，仅需层级输入无关常数偏移即可复现LoRA/全微调效果
practical_value: '- 做LLM4Rec/电商文案生成等垂直领域适配时，可优先用shift adapter替代LoRA，参数量降2个数量级的同时性能持平，大幅降低多场景（不同类目、营销活动）的模型存储与切换成本

  - 做多场景Agent的行为对齐时，无需为每个场景训练独立LoRA，仅需训练对应场景的shift向量，推理时直接加载向量即可切换场景，延迟远低于动态切换LoRA权重

  - 做LLM激活steering控制输出风格/格式时，无需使用CAA/PCA等启发式方向提取方法，直接训练shift adapter获得的目标方向，行为对齐准确率比传统方法提升4倍以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有大模型适配方案（LoRA、全微调、ICL等）的底层作用机制尚未明确，为何仅需更新极小比例参数就能让大模型获得任务能力一直缺乏统一解释，业界也需要更轻量的适配方案降低落地成本。
### 方法关键点
- 将适配带来的隐状态更新拆分为两个分量：所有输入共享的常数分量、随输入变化的残差分量
- 提出shift adapter：仅为每一层学习一个输入无关的常数向量，直接加在所有输入的层输出隐状态上，总参数量仅为层数×隐层维度，比LoRA低2个数量级
- 设计对比实验验证不同适配方案对共享/残差分量的依赖程度，以及shift adapter的性能表现
### 关键实验结果
- 实验覆盖18个不同架构、0.5B~27B参数的大模型，26个基准（17个推理/知识任务、9个行为对齐任务）
- 对比基线：不同rank的LoRA、全微调、CAA等传统激活steering方法
- 核心数据：LoRA的共享分量可保留85%的适配增益；shift adapter在17个任务上平均准确率0.746，与rank8的LoRA（0.745）持平，比全微调高2.8pct；shift adapter的行为对齐准确率达0.68，是传统激活steering最优方法（0.17）的4倍
### 核心结论
大模型的绝大多数任务能力在预训练阶段已经以潜能形式存在，适配不需要注入新能力，仅需用极小的输入无关常数偏移激活已有能力即可
