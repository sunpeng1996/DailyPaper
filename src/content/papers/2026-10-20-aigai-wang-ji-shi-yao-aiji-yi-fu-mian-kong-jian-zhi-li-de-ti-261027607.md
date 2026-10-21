---
title: What should AI forget? A design and taxonomy for negative space governance
  in AI memory
title_zh: AI该忘记什么？AI记忆负面空间治理的分类体系与设计
authors:
- Eryue Xu
- Ke Ding
- Ting-Yu Chang
- Tianshi Li
- Masooda Bashir
affiliations:
- University of Illinois Urbana-Champaign
- Northeastern University
arxiv_id: '2610.27607'
url: https://arxiv.org/abs/2610.27607
pdf_url: https://arxiv.org/pdf/2610.27607
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent 记忆隐私治理
tags:
- AI Memory
- Privacy Taxonomy
- Conversational Agent
- Memory Governance
- User Study
one_liner: 提出15类用户希望AI遗忘的信息分类，构建策略级记忆门FENCE提升AI记忆治理的易用性与可信度
practical_value: '- 做带记忆的电商导购/服务Agent时，可复用本文15类敏感信息分类，默认拦截敏感对话进入用户长期记忆池，降低隐私合规风险与用户信任顾虑

  - 记忆治理可采用「分类配置默认保护+单对话人工覆写」的设计，平衡隐私安全与个性化记忆需求，比纯事后删除/临时会话模式用户体验更好

  - 敏感信息分类任务可优先选用轻量开源模型（如Qwen3.5-9B），在保障80%+召回的前提下实现本地部署，避免敏感数据外传'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有AI记忆管理存在明显短板：全局禁用记忆会完全牺牲个性化体验，事后手动删除操作门槛高、用户信任度低，临时会话模式需提前开启无法覆盖事后才意识到的敏感披露，且常规PII敏感分类远不能覆盖用户真实的记忆排斥需求（如情绪脆弱披露、负面自我认知、职业敏感信息等），用户对AI记忆的可控性感知普遍较差。

### 方法关键点
- 基于146名用户上报的179个希望AI遗忘的真实事件，迭代编码得到15类需排除在AI持久记忆外的敏感信息分类，覆盖常规敏感信息与语境敏感的情感、关系类披露
- 设计FENCE记忆门模块，用户可提前配置需保护的敏感分类，对话时自动检测匹配分类的内容，默认拦截对应内容进入持久记忆，仅保留当前会话可用，支持单对话手动调整保护等级（临时消失/保留对话不进记忆/正常进记忆）
- 敏感分类检测支持本地部署开源模型或调用前沿闭源模型，默认策略优先保障召回降低漏判风险

### 关键实验
- 分类任务测试集包含1300条标注数据，Gemini 3.8 Flash平衡准确率达0.944、召回0.944；开源Qwen3.5-9B平衡准确率0.886、召回0.817，精度0.682为所有测试模型最高
- 15人组内对照用户研究显示，FENCE比传统事后记忆管理可用性提升8.7%，信任度提升33.3%，记忆行为可解释性提升28.6%，仅脑力负荷无显著下降

### 核心结论
AI记忆治理的核心不是让用户去管理已经记住的内容，而是提前定义哪些内容从一开始就不该被记住
