---
title: 'Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms'
title_zh: 跨域整合RLVR能力：三类融合范式的深度对比与实践指南
authors:
- Siye Wu
- Kai Yang
- Yuchen Cai
- Xin Xu
- Peng-Yuan Wang
- Jiaxuan Wang
- Jiashun Liu
- Jiafei Lyu
- Yangkun Chen
- Saiyong Yang
affiliations:
- Fudan University
- Tencent
arxiv_id: '2608.27409'
url: https://arxiv.org/abs/2608.27409
pdf_url: https://arxiv.org/pdf/2608.27409
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: LLM训练 · RLVR多域能力融合
tags:
- RLVR
- Model Fusion
- Task Vector
- GRPO
- Multi-teacher Distillation
- LoRA
one_liner: 系统对比Merge、Mix RL、MOPD三类RLVR跨域融合范式，给出落地选择指南
practical_value: '- 多场景RL微调能力融合选型参考：已有多个单场景LoRA/全量专家时优先选Merge，成本近乎为零；无专家需从零训练统一模型时选Mix
  RL，根据场景相关性调整数据采样比例；需严格保留单场景效果时选MOPD，避免能力遗忘

  - 跨域迁移规律可复用：推理类/工具调用类/指令遵循类任务的能力更新方向正交性强，混合训练时需给低迁移性任务分配更多数据配额，避免效果折损

  - 融合效果上限验证：RL微调融合仅重排基座已有的解空间，不会新增基座不具备的能力，也不会显著损伤未参与训练的通用能力（如事实recall、长上下文），无需过度担心能力退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RLVR是当前LLM能力对齐的主流方案，但单域训练的专家只能覆盖单一能力，多域部署需要路由或融合，现有三类融合范式（Merge、Mix RL、MOPD）缺乏统一框架下的对比，落地选型无明确依据。

### 方法关键点
- 按复用 artifacts 划分三类范式：Merge 合并多个专家的Task Vector，无需额外训练；Mix RL 混合多域数据做单次GRPO训练，无需预训练专家；MOPD 用多教师on-policy蒸馏，同时复用专家和训练数据
- 控制变量实验：基于Qwen3 4B/8B基座，统一训练Math、Science、Code、指令遵循、Agent五个单域专家，统一数据集和评测基准做对比

### 关键结果
三类范式平均效果差距不超过1.4个百分点，但单任务最大差距可达8.6个百分点；其中Merge成本最低（仅需数分钟权重运算），Mix RL端到端成本仅为单域训练总和的0.58~0.67倍，MOPD收敛最快但效果上限不超过教师专家。推理类域（Math、Science、Code）Task Vector相似度高，正向迁移强；指令遵循、Agent类与其他域正交性强，混合训练时效果折损最高可达9.2个百分点。所有融合范式仅提升单样本准确率，pass@32时与基座无显著差异，且不会损伤未参与训练的事实召回、长上下文能力。

最值得记住的一句话：RLVR跨域融合选型优先看专家可用性、成本要求、单域效果保留优先级，无需盲目追求复杂方案
