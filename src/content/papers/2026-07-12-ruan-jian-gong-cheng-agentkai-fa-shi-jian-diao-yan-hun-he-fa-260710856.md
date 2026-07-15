---
title: How Do Practitioners Build SE Agents? Insights from a Mixed-Methods Study
title_zh: 软件工程Agent开发实践调研：混合方法研究的核心洞察
authors:
- Yunbo Lyu
- David Williams
- Jieke Shi
- Zhensu Sun
- Chao Peng
- Zhou Yang
- Federica Sarro
- David Lo
affiliations:
- Singapore Management University
- University College London
- Tencent
- University of Alberta
- Alberta Machine Intelligence Institute
arxiv_id: '2607.10856'
url: https://arxiv.org/abs/2607.10856
pdf_url: https://arxiv.org/pdf/2607.10856
published: '2026-07-12'
collected: '2026-07-15'
category: Agent
direction: LLM Agent开发流程与实践调研
tags:
- Agent Development
- LLMOps
- SE Agent
- Mixed Methods Study
- EDD
one_liner: 通过20份访谈+80份从业者调研，总结SE Agent开发的工作流、变革、挑战与实践
practical_value: '- 开发电商/推荐/广告Agent时可复用7阶段迭代工作流，采用cheapest-first模型策略：先调用外部API做prompt工程，再逐步升级到LoRA微调、自训练模型，降低前期试错成本

  - 优先落地Evaluation-Driven Development模式，提前定义离线+线上多维度评价指标，将prompt、技能定义、上下文规则作为核心版本化资产和代码同步迭代

  - 针对依赖第三方大模型的Agent服务，区分持久化脚手架（上下文管理、权限校验、工具调用拦截）和临时模型缺陷补偿逻辑，避免基础模型更新后旧逻辑成为性能瓶颈

  - 遇到Agent生成的业务逻辑代码可读性差的问题，可优先保留需求、测试用例、业务规则等可复现资产，必要时让Agent重新生成代码而非人工阅读维护'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
SE Agent（基于LLM的自动化软件工程Agent）已进入大规模落地阶段，但其开发逻辑和传统软件、普通LLM应用存在本质差异，现有研究极少关注从业者实际开发SE Agent的流程、痛点与最佳实践，无法为工业界提供可参考的开发范式。

### 方法关键点
- 采用探索性混合研究方法：先对12家机构的20名SE Agent开发从业者开展半结构化访谈，通过主题分析和混合卡片分类提取核心发现，经过成员校验后再面向80名从业者开展在线调研验证结论普适性
- 访谈覆盖从初创公司到大型科技企业的SE Agent开发全链路角色，包括应用层开发、模型训练、基础设施搭建、任务定制Agent等多个方向

### 关键结果
- 总结出SE Agent开发的7阶段迭代工作流，91%的调研受访者认可该工作流的合理性
- 识别5项核心流程变革：实现成本大幅降低（受访开发者普遍表示1天工作量抵过去2-4周）、工作重心从编码转向输出审核与效果评估、Evaluation驱动开发成为主流（82%受访者认同）、角色边界模糊化、prompt/技能规则等成为核心版本化资产
- 提炼6类普遍挑战，其中理解债务（Agent生成代码速度远超人工理解速度）和第三方模型更新波动的认同度最高，分别达82%和80%

### 最值得记住的一句话
今天的脚手架设计模式，可能就是明天的反模式。
