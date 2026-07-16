---
title: 'ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation'
title_zh: ShortOPD：基于短到长On-Policy蒸馏恢复剪枝大模型生成能力
authors:
- Qingyu Zhang
- Qianhao Yuan
- Hongyu Lin
- Yaojie Lu
- Xianpei Han
- Le Sun
- Xiang Li
- Ming Xu
- Jiarui Li
- Xiuyin Zhao
affiliations:
- ByteDance
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2607.13124'
url: https://arxiv.org/abs/2607.13124
pdf_url: https://arxiv.org/pdf/2607.13124
published: '2026-07-13'
collected: '2026-07-16'
category: Training
direction: 大模型压缩 · 剪枝后蒸馏恢复
tags:
- structured_pruning
- on_policy_distillation
- LLM_compression
- knowledge_distillation
- generation_recovery
one_liner: 提出动态长度调度的on-policy自蒸馏方案，低成本恢复剪枝LLM的自由生成能力
practical_value: '- 业务侧落地轻量化LLM（如电商文案生成、query推荐、Agent意图理解/回复）时，结构化剪枝后的模型若生成效果崩溃，可直接复用ShortOPD的无标注自蒸馏方案恢复能力，仅需保留原大模型作为frozen
  teacher，无需额外标注数据

  - 蒸馏训练时可直接复用动态rollout调度trick：实时检测重复后缀动态调整生成长度，早期用短序列节省算力，后期恢复长序列能力，实测可减少71%的rollout
  token消耗，训练速度提升3倍左右，大幅降低训练成本

  - 蒸馏恢复的训练语料必须覆盖核心业务场景：ablation显示缺对应场景的prompt，该场景的生成能力恢复会下降80%以上，做业务适配时优先保证核心场景prompt的覆盖度

  - 剪枝后模型生成能力下降无需直接丢弃：其能力只是被降级而非删除，通过ShortOPD可恢复70%+的原模型生成能力，可大幅降低小参数LLM的部署推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
结构化剪枝是硬件友好的LLM压缩方案，无需特殊内核支持即可降低推理成本，但现有方案大多仅在选择题类评测上表现良好，实际部署需要的自由生成能力会直接崩溃。传统恢复方法（SFT、普通KD）效果差，且早期训练生成的大量重复后缀几乎没有蒸馏信号，白白消耗算力。

### 方法关键点
- 基于On-Policy Distillation（OPD）框架：剪枝后的学生模型自行采样生成rollout，以未剪枝的原模型为frozen teacher，每个token位置对齐teacher的分布，无需标注数据
- 新增动态预算控制器：实时统计rollout的后缀重复率、有效长度、截断率，高重复时缩小rollout长度，低重复且截断率高时增大长度，避免算力浪费在无意义的重复后缀上
- 蒸馏损失采用α=0.5的广义JSD，平衡前向/反向KL的优缺点，适配剪枝后模型与原模型的能力gap

### 关键实验
测试对象为剪去25%参数的Qwen3-4B-Instruct，训练语料覆盖数学、代码、开放域指令共4.5万条prompt，对比SFT w/o KD、SeqKD、普通KD、RLVR等baseline：
- ShortOPD生成得分是未恢复模型的9倍，是传统恢复方案的1.6-4.4倍，1轮训练即可恢复原模型64.5%的生成能力，3轮训练可达73.7%
- 对比固定8192-token的OPD，ShortOPD仅用1/4训练时间，少生成71%的rollout token，得分差距小于2个点

### 核心结论
剪枝后LLM的生成能力下降是被降级而非消失，用on-policy自蒸馏加动态长度调度可以低成本恢复大部分能力，大幅降低小模型部署门槛
