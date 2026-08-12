---
title: Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding
title_zh: Agent编码场景下灾难性记忆问题的成因分析与优化方案
authors:
- Kushal Chakrabarti
affiliations:
- South Park Commons
arxiv_id: '2608.11095'
url: https://arxiv.org/abs/2608.11095
pdf_url: https://arxiv.org/pdf/2608.11095
published: '2026-08-11'
collected: '2026-08-12'
category: Agent
direction: Agent长期记忆 · 提示工程优化
tags:
- Agent Memory
- Prompt Engineering
- Catastrophic Remembering
- LLM Agent
- Agentic Coding
one_liner: 揭示Agent提示无界增长的灾难性记忆现象，提出带推理注释的提示维护方案
practical_value: '- 维护电商/广告推荐Agent的系统规则库时，每条新增规则必须附带注释写明触发场景、问题根因、验证结果，避免规则无限堆积导致指令遵循率下降

  - Agent记忆清理不要仅依赖时间戳、调用频率等浅层特征，只有可追溯潜层推理逻辑的记忆/规则才可安全删除，避免业务效果出现无预期回退

  - 评估Agent提示质量时可借鉴反演IFEval的方法，构造已知最优提示的基准测试集，量化评估提示冗余度和业务效果的权衡

  - 跨团队协作维护的Agent规则（如通用投放Agent、导购Agent）强制要求规则带注释，可大幅降低后续维护成本，减少无效规则堆积'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agent编码场景下CLAUDE.md、AGENTS.md等提示文件会无界增长，仅会在全量重写时临时降量，规则过多会直接导致LLM指令遵循率下降，此前无法解释增长根因，也没有低成本的落地解法。

### 方法关键点
- 追踪1867个GitHub仓库、24.7万条指令的完整生命周期，通过删除风险的log-hazard斜率验证根因：指令添加时的潜层推理随时间衰减，删除旧指令的验证成本指数级上升，该现象命名为灾难性记忆，是灾难性遗忘的反向问题。
- 提出带潜层推理注释的提示维护方案，注释仅对后续维护者可见，执行前自动剥离，注释内容包含指令对应的失败场景、假设、验证结果。
- 反演IFEval基准构造已知最优提示长度的评估场景，可量化计算提示的冗余度和指令遵循率，解决最优提示不可观测的评估难题。

### 关键结果数字
- 观测数据：Agent提示文件生命周期内指令数平均增长226%，每提交净增4.9条指令，指令越旧删除概率越低，log-hazard斜率为-0.032/提交，76.8%的指令删除来自全量重写，且重写后很快恢复原有增长速率。
- 控制实验：添加注释后51步时提示冗余度从211.3%降至1.4%，消除99.3%的冗余，指令遵循率与无注释组持平；真实场景下注释可将指令遵循率提升最多23.1%。

### 最值得记住的一句话
如果自然语言是新的代码，那我们为什么还不给它加注释？
