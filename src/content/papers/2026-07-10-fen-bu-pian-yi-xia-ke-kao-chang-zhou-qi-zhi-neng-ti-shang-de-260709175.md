---
title: Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under
  Distribution Shift
title_zh: 分布偏移下可靠长周期智能体上下文演化的范围验证方法
authors:
- Dan C. Hsu
- Luke Lu
affiliations:
- RedMind Research
- National Taiwan University
arxiv_id: '2607.09175'
url: https://arxiv.org/abs/2607.09175
pdf_url: https://arxiv.org/pdf/2607.09175
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 长周期上下文演化优化
tags:
- Agent Context Evolution
- Graph Representation
- Distribution Shift
- Reliability
- Prompt Engineering
one_liner: 提出GRACE框架用带类型语义图做局部验证，提升分布偏移下长周期Agent上下文演化可靠性
practical_value: '- 电商客服/导购Agent的系统提示词迭代可参考GRACE的节点分类，将内容拆解为身份、规则、知识三类结构化节点管理，避免平文本迭代常见的规则冲突问题

  - 业务规则更新（如大促、物流规则变动）时可采用局部验证思路，仅检查修改节点的k跳邻域规则，无需全量重审所有历史规则，大幅降低验证成本

  - 上下文迭代优先采用增量编辑方案，基于结构变更生成文本增量修改，替代全量重写提示词，避免上下文崩塌导致的历史规则失效'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
部署的LLM Agent依赖外部上下文控制行为，长周期迭代时平文本维护的系统提示词会持续积累，规则冲突、冗余问题随迭代次数增加快速恶化，全量验证成本极高，且分布偏移下旧规则易失效，现有平文本演化方案无法支撑长周期稳定迭代。

### 方法关键点
- 将系统提示词拆解为带类型的语义图：节点分为identity（身份定义）、norm（行为规则）、knowledge（领域知识）三类，边定义supports、refines、sequence三种合法关系，形成固定schema约束
- 迭代流程：基于运行诊断结果生成符合schema的图编辑操作，仅对修改节点的k跳邻域做局部结构验证，检测冲突和冗余并修复
- 部署兼容：验证通过的图变更转换为文本增量编辑，不改动未修改的提示词内容，无需调整现有Agent调用逻辑

### 关键实验
在τ²-bench电信客服数据集上开展10轮分布偏移下的迭代实验，对比平文本基线HCE、无结构分析的GRACE消融版：GRACE最终严格可靠性指标pass^3从初始0.091提升到0.673±0.136，远超HCE的0.191±0.051，也优于Gemini 3.1 Pro零样本的0.242。

### 核心结论
长周期Agent上下文迭代的核心是让规则间关系显式化，用局部验证替代全量重审才能持续保证迭代可靠性。
