---
title: 'Beyond Component Testing: Validating Agentic AI Systems'
title_zh: 超越组件测试：Agentic AI系统的验证框架与研究综述
authors:
- Fabio Orazio Mirto
- Luca D'Agati
- Giuseppe Tricomi
- Stefano Silvestri
- Francesco Longo
- Antonio Puliafito
- Giovanni Merlino
affiliations:
- University of Messina
- ICAR-CNR, Italy
- National Interuniversity Consortium for Informatics (CINI)
arxiv_id: '2607.29405'
url: https://arxiv.org/abs/2607.29405
pdf_url: https://arxiv.org/pdf/2607.29405
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent系统全生命周期验证与可信保障
tags:
- Agentic_AI
- System_Validation
- Runtime_Assurance
- Software_Testing
- Multi_Agent
- Regulatory_Compliance
one_liner: 系统梳理257篇文献，提出Agentic系统五维验证框架，识别缺口并给出落地研究路线
practical_value: '- 搭建电商/广告场景LLM Agent（如智能导购、投放优化Agent）时，需将端到端执行轨迹作为核心验证单元，重点校验工具调用顺序、状态传递、异常恢复的合理性，避免仅以最终输出正确性作为验收标准

  - 可直接复用论文提出的五维验证框架搭建内部Agent质量保障体系，尤其要落地时间维度的证据刷新机制，定期重测避免上游商品库、用户标签更新导致Agent行为退化

  - 部署多Agent协作的推荐/运营链路（如选品Agent+投放Agent+客服Agent联动）时，需额外覆盖多Agent交互风险测试，可引入故障注入模拟链路异常，提前识别指令冲突、重复调用、死锁等隐藏问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Agentic AI系统通过多步规划、工具调用、记忆迭代与环境动态交互实现目标，传统组件测试仅验证单模块输入输出一致性，无法覆盖轨迹路径依赖、环境动态变化、多智能体 emergent 故障等问题；同时欧盟、美国已出台自适应AI监管要求，对全生命周期可追溯性提出明确约束，但当前领域缺乏统一的Agent系统验证框架，相关研究分散在软件工程、CPS验证、监管合规等多个领域，难以支撑业务落地的可信要求。

### 方法关键点
- 遵循PRISMA系统综述规范，从5个学术数据库检索7197篇相关文献，最终纳入257篇2019-2026年的核心研究，覆盖软件工程测试、智能体评估、CPS验证、运行时保障、监管合规5个交叉领域
- 提出Agentic系统五维验证分类框架：行为维度（轨迹合理性、工具调用正确性）、安全维度（风险边界、异常降级能力）、时间维度（验证证据随环境/模型/记忆更新的存续性）、合规维度（审计可追溯性、监管要求对齐）、多智能体维度（多角色交互协同合理性）
- 明确传统测试方法与Agent验证的5类核心不匹配：确定性不匹配、分解性不匹配、规格不匹配、环境不匹配、时间不匹配

### 关键结果
- 纳入的257篇文献中，仅27.6%聚焦行为维度验证，时间维度（24.1%）、多智能体维度（19.5%）、安全维度（16.3%）、合规维度（12.5%）的研究均存在显著缺口
- 两名独立标注者对五维分类的Cohen's κ达0.759，分类框架一致性较高
- 2025-2026年发表的相关文献占比达81.3%，该领域研究近期爆发式增长

> 最值得记住的结论：可信Agentic AI的落地不依赖孤立组件的正确性，而要基于上下文对整个执行轨迹做全生命周期验证。
