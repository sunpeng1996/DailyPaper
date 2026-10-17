---
title: 'Improving Environment-Agnostic Coding Agents: The Role of Scaffolding'
title_zh: 环境无关编码Agent优化：通用脚手架的作用研究
authors:
- Sergey Rodionov
affiliations:
- SingularityNET
arxiv_id: '2610.22289'
url: https://arxiv.org/abs/2610.22289
pdf_url: https://arxiv.org/pdf/2610.22289
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: 通用Agent · 跨环境性能优化
tags:
- LLM Agent
- Environment-Agnostic
- Scaffolding
- Prompt Engineering
- Agent Evaluation
one_liner: 通过单条Prompt修改引导Agent遇困返还控制权，无需环境定制即可跨场景提升编码Agent性能
practical_value: '- 可复用Stop-and-report Prompt技巧：给Agent添加「遇不确定场景主动返还控制权、系统自动重入并提示目标」的规则，可在不定制业务逻辑的前提下提升推荐/搜索/运营类Agent的任务完成率，尤其适合复杂多步决策场景。

  - 通用Agent架构设计可参考EnvTraverse的交互契约，标准化Agent与业务环境的初始化、动作、终止接口，降低多场景（电商多品类运营、多渠道广告投放）Agent的适配成本。

  - 不要盲目给Agent加前置教程/历史样本数据：实验证明低能力模型下前置教程反而会降低性能，业务中可先做A/B测试验证样本引入的收益，避免负向效果。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent性能提升多依赖环境定制的脚手架，开发成本高且难以跨场景复用；随着LLM能力提升，是否存在无需环境定制的通用优化手段、能在多个场景下稳定生效，是降低Agent落地成本的核心问题。

### 方法关键点
- 拆分Agent架构为三层：backbone LLM、环境无关脚手架（通用工具、上下文管理、控制器）、环境定制脚手架，本次仅优化环境无关层，无任何场景定制逻辑
- 仅修改1条Prompt规则：在基线基础上增加「遇到问题/不确定性时先停止并上报，再继续执行」的要求，控制器接上报后自动恢复会话并提示目标，不提供任何任务特定反馈
- 设计EnvTraverse通用框架，标准化Agent与多环境的交互契约，无需修改Agent代码即可接入不同任务场景

### 关键实验
在ARC-AGI-3、AGI Maze、Terminal-Bench三个跨领域基准测试，对比基线Agent：
- Stop-and-report策略使ARC-AGI-3 RHAE提升1.37~7.29个百分点，AGI Maze RHAE70提升0.37~4.95个百分点，仅Terminal-Bench有±2.25个百分点的小幅波动
- 新增ARC-AGI-3专属脚本化RESET控制，可收回34%~60%的通用Agent与专用Agent的性能差距
- 低能力模型下前置教程会降低AGI Maze性能，高能力模型下才有正向收益

### 核心结论
Agent有能力获取信息和工具，不代表能有效使用它们，通用脚手架的规则设计对性能的影响远超预期
