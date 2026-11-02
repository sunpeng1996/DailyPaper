---
title: When Should AI Agents Ask? Clarification Requests Under Limited Human Attention
title_zh: 有限人类注意力约束下多AI Agent澄清请求的最优决策框架
authors:
- Hanzhao Wang
- Shengjie Liu
- Zhengchao Wang
affiliations:
- The University of Sydney
- Amazon
arxiv_id: '2610.41129'
url: https://arxiv.org/abs/2610.41129
pdf_url: https://arxiv.org/pdf/2610.41129
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: 多Agent · 人-AI协作 · 澄清请求调度
tags:
- AI Agent
- Human-AI Collaboration
- Clarification Request
- Dynamic Programming
- Attention Allocation
one_liner: 提出PCP策略实现有限人类注意力下多Agent的提问、检索、任务调度全局协调
practical_value: '- 电商/企业内部多Agent集群（如客服Agent、运营Agent、商品上新Agent）调度可直接复用PCP的成对注意力定价思路，平衡自主检索、任务推进、求助人类的决策，相比单Agent独立决策平均降本18%~31%

  - 单个Agent的提问逻辑可复用单任务双阈值结论：有大量不依赖缺失信息的独立工作时可更早发起提问，利用工作时间并行等待人类回复，提问后仍可继续检索，找到答案自动撤回请求降低人类负担

  - 多Agent的人类请求排序不要用单任务优先级打分，要全局考虑任务间的阻塞影响，例如大促时优先处理无法通过历史记录检索到答案的请求，避免高优先级但可自主解决的请求占用稀缺人力'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前多AI Agent并行处理任务的场景快速普及，单个人类常需同时监管多个Agent的澄清请求，现有单Agent独立决策提问时机的方案未考虑多请求对人类注意力的争抢，要么过度打扰人类导致高优先级请求阻塞，要么盲目自主检索导致任务延迟高，缺乏全局协调的决策机制。

### 方法关键点
- 构建动态规划模型，每个Agent可选三类动作：自主检索缺失信息、推进不依赖缺失信息的独立工作、提交澄清请求，请求等待期间可继续检索，找到答案可主动撤回请求；
- 提出Pairwise Coordination Policy (PCP)，通过精确求解单任务、双任务子问题计算成对任务共享人类注意力的额外成本（成对注意力价格），近似全局最优决策，避免状态空间随任务数指数爆炸；
- 理论保证：最多2个未解决需求时PCP完全最优，所有需求必须人类解决时PCP成本不超过最优解的2倍。

### 关键结果
- 864组3-4任务合成基准测试：PCP相对最优解的平均成本gap仅0.07%，比Always Ask、随机提问、检索1次再提问三类通用规则平均降本18%~31%；
- LLM Agent采购任务实测算例：PCP在所有测试场景下取得最低平均成本，相对单Agent独立决策最高降本11.2%；
- 48任务大规模场景下，PCP相对单Agent独立决策平均降本12.1%，单步决策耗时仅44ms。

**最值得记住的结论**：不要仅用Agent的提问频率评估其性能，有独立工作可并行时更早提问、允许撤回请求，反而能降低总任务成本、提升整体效率。
