---
title: 'Trustworthy Recursive Self-Improvement in the Era of Large Models: Foundation,
  Risks, Evaluation and Open Challenges'
title_zh: 大模型时代可信递归自我改进：基础、风险、评估与开放挑战
authors:
- Jiayue Pu
- Ang Gao
- Jinyi Bai
- Qipeng Wang
- Tongyu Wen
- Jiahao Zhao
- Keyu Qu
- Junhao Zhang
- Chenglei Shen
- Zhongxiang Sun
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- University of Chinese Academy of Sciences
arxiv_id: '2610.35193'
url: https://arxiv.org/abs/2610.35193
pdf_url: https://arxiv.org/pdf/2610.35193
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 可信递归自我改进框架研究
tags:
- Recursive Self-Improvement
- Trustworthy AI
- LLM Agent
- Self-Evolution
- AI Safety
one_liner: 系统梳理大模型递归自我改进的可信框架、风险、评估方法与研究方向
practical_value: '- 自研自进化推荐/广告Agent时，可复用S1-S4四阶段迭代流程+RI递归改进机制，每轮迭代同步校验性能增益、合规约束、可审计性，避免多轮迭代后系统不可控

  - 落地自进化系统风险防控时，可参考三层校验逻辑：单更新级校验是否存在测试污染/合规违规，继任系统级校验改进是否持久无能力退化，元改进级校验更新规则本身的安全性，防止规则被篡改后引入不可控风险

  - 涉及用户敏感数据的电商推荐/广告Agent迭代时，需在S3评估、S4落地环节增加隐私校验节点，避免用户隐私数据在多代系统继承中泄露'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型能力爆发催生了大量支持自进化的LLM Agent系统，递归自我改进（RSI）允许系统修改自身的迭代更新规则，大幅提升进化效率的同时也带来性能虚高、安全对齐失效、隐私泄露、人工监管失效等特殊风险，现有可信AI框架未覆盖递归迭代场景的长周期风险，亟需系统性的可信RSI规范指导落地。
### 方法关键点
- 明确RSI可操作定义与标准化流程：核心分为S1（改进点诊断）、S2（修订方案生成）、S3（方案评估）、S4（更新落地）四个阶段，新增RI环节支持递归修改更新规则本身
- 构建可信RSI分析框架：将可信要求拆解为真实持续改进、行为约束与对齐公平、系统安全隐私、透明可控4个核心主题，对应改进有效性、约束留存、有效监管三个分析维度
- 提出分层评估逻辑：覆盖单更新级（单次修改的合规性）、继任系统级（改进的持久性与继承风险）、元改进级（更新规则修改后的安全性）三个层级的评估要求
### 核心发现
系统梳理2024-2026年100+相关研究，发现现有RSI系统存在三类共性问题：超60%的自评估改进存在测试污染导致的性能虚高，超40%的系统经过多轮迭代后出现对齐约束退化，支持递归修改更新规则的系统中70%未对规则做独立安全校验。
### 核心结论
RSI系统的可信性不能仅校验单次迭代效果，必须覆盖迭代规则本身的修订、以及多代系统继承的长周期风险
