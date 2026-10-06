---
title: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery
title_zh: 基于自动诊断与技能发现的数值智能训练框架
authors:
- Peter Chen
- Wotao Yin
affiliations:
- University of California, Berkeley
- Alibaba Group DAMO Academy US
arxiv_id: '2610.03872'
url: https://arxiv.org/abs/2610.03872
pdf_url: https://arxiv.org/pdf/2610.03872
published: '2026-10-01'
collected: '2026-10-06'
category: Agent
direction: Agent 无权重更新自优化
tags:
- Agent
- Self-Improvement
- Numerical Solver
- Skill Discovery
- Diagnosis
one_liner: 提出无需更新模型权重的诊断优先ADSD框架，提升LLM生成数值求解器的性能与泛化性
practical_value: '- 可复用「先诊断根因再定向技能升级」的无权重更新Agent优化范式，避免盲目试错迭代，适合推荐系统召回/排序策略的离线自动调优，无需重新训练大模型

  - 诊断环节的「症状-根因关联+验证集校验」机制可迁移到推荐bad case归因：先从埋点日志提取异常特征，再关联到召回/排序模块缺陷，验证后输出标准化修复方案

  - 领域知识库+执行反馈结合的技能构建流程，可复用到电商业务Agent的技能库建设：针对业务错误案例定向检索领域方案，验证后封装为可调用技能，提升Agent处理极端case的鲁棒性

  - 小样本训练的技能可跨场景泛化的结论，可用于降低推荐场景策略迭代的冷启动成本，从头部场景挖掘的优化技能可直接迁移到长尾场景生效'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前科学Agent生成数值求解器时，仅靠执行反馈只能发现性能异常，无法定位根因，只能盲目试错修改；同一个性能症状可能对应不同的数值缺陷，现有流程未将观测行为、诊断知识、可执行方案解耦，导致求解器优化效率低、泛化性差，难以适配极端数值场景。

### 方法关键点
- 提出ADSD无权重更新框架，遵循诊断优先范式，分为自动诊断、技能发现两个核心阶段，无需微调LLM权重
- 自动诊断阶段：冻结基线求解器，采集公开测试集上的执行行为，从领域文献库提取症状-数值根因关联构建诊断探针，多轮诊断后在验证集上校验得到可信根因假设
- 技能发现阶段：基于验证后的根因假设定向检索文献筛选适配方法，校验方法假设与基线求解器兼容性后实现代码，验证效果后封装为可复用的求解器技能，同基线Agent可直接调用生成优化后的求解器

### 关键实验
在潮流方程、AC最优潮流、刚性ODE、异质扩散PDE 4个高难度数值领域测试，对比GPT-5.5、Claude-Sonnet-5、Qwen3.8-2.4T三个基线Agent原生生成的求解器：GOC-500潮流任务上Qwen3.8基线误差降低71×，AC-OPF任务Qwen3.8通过率从14.42%提升到98.36%，刚性ODE任务Claude-Sonnet-5通过率从94%提升到100%，PDE任务GPT-5.5求解速度提升2.6×，技能可直接泛化到未见过的拓扑、极端工况场景，效果远超原生5轮自迭代。

**最值得记住的一句话：单纯靠LLM固有知识的多轮自迭代无法稳定提升复杂任务性能，先诊断根因再定向匹配领域知识的范式才能实现可复用、可泛化的性能提升**
