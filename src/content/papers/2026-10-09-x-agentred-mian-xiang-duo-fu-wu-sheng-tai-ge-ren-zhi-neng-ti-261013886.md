---
title: 'X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems'
title_zh: X-AgentRed：面向多服务生态个人智能体的自动化红队测试框架
authors:
- Yeonsung Jung
- Zhiyuan Wang
- Zifan Wang
- Vítor Albiero
- Benjamin Newman
- Edoardo Debenedetti
- Ivan Evtimov
- Ninareh Mehrabi
affiliations:
- Meta Reality Labs Research
- Meta Superintelligence Labs
- FAIR at Meta
- Meta
arxiv_id: '2610.13886'
url: https://arxiv.org/abs/2610.13886
pdf_url: https://arxiv.org/pdf/2610.13886
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 安全 · 自动化红队测试
tags:
- Agent Safety
- Red Teaming
- Tool Use
- LLM Agent
- Multi-Service Ecosystem
one_liner: 基于HarmFlow工具依赖图的自进化红队框架，高效发现多服务生态中个人Agent的组合性危害
practical_value: '- 电商/服务类多工具Agent的安全测试可复用HarmFlow思路：先结构化标注每个工具的前置条件、执行效果、潜在危害，再通过反向游走生成风险路径，比纯LLM生成的路径覆盖度更高

  - 执行反馈迭代策略可直接复用：对成功触发危害的路径做工具替换扩增，对被阻断的路径补全前置条件重构，无需重训模型即可提升风险发现效率

  - 论文提出的10类危害+12类诱导因素分类体系可直接套用到电商Agent的安全巡检，覆盖敏感信息泄露、经济损失、越权操作等核心风险场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
个人Agent广泛接入多服务工具执行跨域任务时，单个工具调用均符合安全规则，但组合执行的效果累积可能触发非预期危害。现有红队方法依赖LLM生成风险路径，偏向训练数据中见过的工具组合，大量新型跨服务交互风险被漏检，无法适配快速扩张的多服务生态。
### 方法关键点
- 构建HarmFlow有向依赖图：每个节点对应一个工具，标注其执行前置条件、产出效果、潜在危害；边的判定规则为前序工具的效果可满足后序工具的执行前置条件，914个工具共生成29367条有效边
- 反向游走采样风险路径：从关联目标危害的工具节点出发反向随机游走，生成候选路径配方，再实例化为包含正常用户请求、初始环境状态的测试场景
- 执行反馈自进化：对成功触发危害的路径，替换非核心危害节点的关联工具实现路径扩增；对执行被阻断的路径，补全阻断步骤的前置条件重构路径，无需重训模型即可持续提升风险覆盖
### 关键实验
在包含30个服务、914个工具的模拟多服务生态上测试，对比STAC、TRACE两个主流红队基线，覆盖4款前沿Agent模型。平均有害路径率（HPR）达STAC的1.77倍、TRACE的10.36倍，平均工具覆盖率达STAC的2.99倍、TRACE的1.84倍，单场景生成成本仅为STAC的40%、TRACE的21%。
### 核心结论
多服务Agent的组合性危害无法仅依赖LLM的训练记忆发现，结构化工具依赖分析+反馈驱动的路径探索才能覆盖训练数据未出现的新型风险
