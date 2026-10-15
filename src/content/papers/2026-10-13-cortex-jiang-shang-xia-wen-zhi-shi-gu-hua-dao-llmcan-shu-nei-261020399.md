---
title: 'Cortex: Consolidating Context into Parametric Memory'
title_zh: Cortex：将上下文知识固化到LLM参数内存的高效框架
authors:
- Jintian Zhang
- Feng He
- Xinnian Liang
- Ziwen Xu
- Haoming Xu
- Haojing Huang
- Shuangzhi Wu
- Ningyu Zhang
affiliations:
- Zhejiang University
- ByteDance Seed
- Tsinghua University
arxiv_id: '2610.20399'
url: https://arxiv.org/abs/2610.20399
pdf_url: https://arxiv.org/pdf/2610.20399
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: LLM内存固化 · 低秩/结构FFN更新
tags:
- Memory Consolidation
- LoRA
- MoE
- Knowledge Editing
- FFN Tuning
- Continual Learning
one_liner: 提出LLM内存固化框架Cortex，可将上下文带来的性能增益持久化到模型参数中
practical_value: '- 电商/推荐场景高频用到的垂域知识、最新商品信息、活动规则，可通过Cortex的prospective query生成+FFN定向更新方案固化到小参数中，无需每次推理携带对应上下文，大幅降低KV
  cache开销与推理延迟，替代部分高频RAG场景

  - 电商客服Agent、商家运营Agent的历史交互经验、工具API文档、平台规则，可通过Cortex的rehearsal蒸馏方案固化到参数，无需每次都将长文档/历史经验放入prompt，缩短prompt长度的同时提升Agent执行准确率

  - 需频繁更新知识的场景（如每日更新新品信息、活动规则），可采用Cortex的Structural更新+query replay方案，每次仅训练新增的小参数，旧参数全冻结，99.8%的能力保留率基本不影响原有推荐/问答效果，避免增量更新导致的能力退化

  - MoE底座的推荐/大模型迭代，优先采用Cortex的共享分支结构更新方案，相比独立专家更新训练效率更高、泛化性更好，用极小的参数量增量即可实现新知识的高效固化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM依赖上下文才能获得性能增益，上下文移除后增益立即消失；RAG方案需要推理时检索相关内容，容易遗漏间接相关信息且增加推理开销；传统参数更新方案易导致原有能力遗忘，缺乏统一框架实现上下文收益的持久化，同时最小化对原有能力的影响。

### 方法关键点
- 定义Memory Consolidation (MC)任务，核心指标为Consolidation Rate (CR，上下文增益的恢复比例)和Retention Rate (RR，原有非目标能力的保留比例)
- 设计Prospective Rehearsal机制，基于输入上下文自动生成未来可能的查询及对应上下文下的回答作为训练数据，无需访问测试集
- 仅在FFN层做定向更新，提供两种模式：Synaptic为现有FFN参数加低秩更新（类似LoRA），Structural为新增独立非线性通道，原有参数全冻结；针对MoE模型设计共享更新分支，所有token均经过该分支提升训练效率
- 采用上下文蒸馏训练：带上下文的冻结模型作为教师，无上下文的更新模型作为学生，对齐输出分布KL散度与FFN输出隐状态MSE；序列更新时仅训练新增参数，搭配历史query回放避免旧知识遗忘

### 关键结果
实验覆盖4B~120B稠密与MoE模型，测试5类任务（Agent经验固化、新API学习、persona调整、知识抑制、事实编辑），对比AlphaEdit、MEMIT、ROME等10+基线。14B模型完成50轮序列事实编辑时，Cortex-Structural实现88.9% CR与99.8% RR，CR比AlphaEdit高66.2个百分点，RR高3.8个百分点，在绝大多数测试场景下处于CR-RR帕累托前沿。

### 核心结论
仅针对FFN层做定向更新+匹配上下文应用场景的训练数据生成，可在几乎不损失原有模型能力的前提下，实现上下文收益的高比例持久化，效果显著优于全参数/注意力层更新方案。
