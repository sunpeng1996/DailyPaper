---
title: 'An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal
  Complementarity: Decoupling Confidence and Consistency'
title_zh: 基于三信号互补解耦置信度与一致性的LLM Agent可解释记忆决策控制器
authors:
- Yiming Zhang
- Jinghong Zhang
- Haoran Zhao
- Yiren Ma
- Chunlei Zhao
affiliations:
- School of Computer Science and Engineering, Tianjin University of Technology
arxiv_id: '2609.22043'
url: https://arxiv.org/abs/2609.22043
pdf_url: https://arxiv.org/pdf/2609.22043
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 记忆信任决策 · 零参数可解释
tags:
- LLM Agent
- RAG
- Memory Controller
- Hallucination Mitigation
- Interpretability
one_liner: 在RAG检索与生成间插入零参数控制器，冲突记忆下幻觉率降56%，高风险场景近零幻觉
practical_value: '- 电商客服Agent、商品问答类RAG系统可直接插入MDL层，无训练成本、仅0.14ms延迟完全不影响线上性能，针对医药、母婴等高风险品类配置风险等级，可实现高风险咨询场景零幻觉

  - 三信号（相关性、记忆可靠性、任务风险）框架可迁移到推荐系统召回后粗排阶段：相关性对应召回得分、可靠性对应item历史行为一致性、风险对应合规等级，实现低质/冲突召回内容的前置过滤

  - 置信度C（范数）与一致性α（余弦）解耦思路可复用在QueryRec的query改写校验场景，C衡量改写置信度，α衡量改写与原query的意图一致性，避免改写偏航'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前RAG系统仅优化检索效率，不对召回记忆的可信度做判断，当记忆库存在冲突内容时，盲注记忆反而会放大幻觉：TruthfulQA数据集上冲突记忆下RAG幻觉率达53%，远高于无记忆基线的23%；现有后处理纠错方案在记忆污染发生后才补救，无法从根源避免错误注入，且LLM自评估延迟极高，无法满足线上高并发要求。

### 方法关键点
- 零参数记忆决策层MDL，插入检索与生成阶段之间，全部基于几何运算实现，无训练参数
- 核心三信号互补编码器：融合三类信号：1）相关性M：query与召回记忆的最大余弦相似度；2）可靠性R：召回记忆间冲突率倒数加权的相似度均值；3）任务风险A：业务预设的风险等级，高风险场景做反向编码
- 基于QR正交子空间投影融合信号，显式解耦置信度C（融合向量范数）和一致性α（融合向量与相关性向量的余弦值），结合风险反转机制，自动触发高风险/冲突记忆的拒答
- 输出四档动作：采纳、部分采纳、静默、拒答，可适配不同业务容错要求

### 关键实验
在TruthfulQA、HaluEval数据集上对比标准RAG、CRAG、Self-RAG等基线：通用场景下冲突记忆幻觉率从53%降至23.3%，下降约56.04%；医疗、法律、金融等高风险场景幻觉率降至0%；单决策延迟仅0.14ms，比embedding检索快50倍，比LLM自评估快4~5个数量级。

> 最值得记住的一句话：记忆系统必须拆分检索和决策两个独立阶段，零参数可解释的轻量决策层是高风险Agent业务落地的可行路径。
