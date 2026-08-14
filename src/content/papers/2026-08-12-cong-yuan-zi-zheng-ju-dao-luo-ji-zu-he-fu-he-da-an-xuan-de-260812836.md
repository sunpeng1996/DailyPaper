---
title: 'From Atomic Evidence to Logical Composition: Structured Compositional Reasoning
  over Compound Answer Options'
title_zh: 从原子证据到逻辑组合：复合答案选项的结构化组合推理
authors:
- Obed Junias
- Maria Leonor Pacheco
affiliations:
- University of Colorado Boulder
arxiv_id: '2608.12836'
url: https://arxiv.org/abs/2608.12836
pdf_url: https://arxiv.org/pdf/2608.12836
published: '2026-08-12'
collected: '2026-08-14'
category: Reasoning
direction: LLM 复合逻辑推理结构化优化
tags:
- Logical Reasoning
- Compositional Reasoning
- Integer Linear Programming
- LLM Inference
- Calibration
one_liner: 拆分复合答案为原子判断+约束ILP组合，大幅提升LLM复合逻辑推理性能
practical_value: '- 多条件组合的用户意图判断、商品准入判定场景，可复用「拆分子问题独立判断+规则约束组合」框架，避免LLM直接处理复杂逻辑的失效

  - 原子判断阶段用正反假设成对对比prompt，比独立打分可靠性更高，可迁移到搜索Query意图识别、商品属性校验等二分类任务

  - 多候选打分场景可引入相对校准方法，加入同实例内分数排名、标准化等特征，修正全局校准无法适配单样本分布的问题

  - 涉及与/或/非硬逻辑约束的决策场景，可直接复用论文的ILP约束编码方案，保证最终输出符合逻辑规则，避免LLM幻觉'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM在处理带AND/OR/NEITHER/NOR等逻辑运算符的复合答案时，即使对单个原子判断正确，也常出现组合错误，尤其否定类逻辑表现极差。传统单步prompt/CoT无法分离语义理解与逻辑组合步骤，也无法保证逻辑约束不被违反，存在明显组合性gap。

### 方法关键点
- 拆分层：将每个复合答案选项自动拆解为原子答案+对应逻辑运算符，去重后所有原子作为独立判断单元
- 原子打分：对每个原子构造正反成对假设（符合/不符合上下文），用单prompt二选一对比打分，输出归一化置信度
- 校准层：除传统Platt、保序校准外，提出相对校准，加入单实例内分数标准化、排名、与最高分差值等特征训练逻辑回归，输出校准后分数
- 组合层：用整数线性规划(ILP)编码与/或/非的硬逻辑约束，全局优化选择符合所有规则且总置信度最高的答案

### 关键结果
在LOGICAL-COMMONSENSEQA人类验证集、新构建的LOGICAL-SATA阅读理解数据集上，对比0-3shot、零样本CoT基线，用Llama-3.1-8B-Instruct测试：整体Macro-F1分别从48.3提升至77.0、从47.0提升至75.6，其中提升最大的NEITHER/NOR类，Macro-F1从14.0升至76.8、12.6升至73.4，相对校准在算子混合场景下增益最明显。

### 核心结论
很多LLM逻辑推理失败不是因为缺乏知识，而是无法正确组合局部判断，将理解与组合解耦、用外部规则约束组合过程，可大幅降低组合性gap。
