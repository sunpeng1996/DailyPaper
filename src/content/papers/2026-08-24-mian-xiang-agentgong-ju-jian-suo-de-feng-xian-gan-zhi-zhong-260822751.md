---
title: Risk-Aware Reranking for Agentic Tool Retrieval
title_zh: 面向Agent工具检索的风险感知重排序框架
authors:
- Qinfei Li
- Xiaoxuan Dong
- Jin Zhang
- Dexu Yu
- Wenhao Deng
- Junchen Fu
- Youhua Li
- Hanwen Du
- Chunxiao Li
affiliations:
- 中国科学技术大学
- 电子科技大学
- 兰州大学
- Fenz.AI
- 格拉斯哥大学
arxiv_id: '2608.22751'
url: https://arxiv.org/abs/2608.22751
pdf_url: https://arxiv.org/pdf/2608.22751
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent工具检索 · 执行前安全管控
tags:
- LLM Agents
- Tool Retrieval
- Reranking
- Agent Safety
- Retrieval Safety
one_liner: 在不修改上游召回器的前提下，通过轻量双权重排框架平衡工具检索的相关性与执行前安全风险
practical_value: '- 工具类召回重排场景可复用双分加权思路：冻结上游召回器，新增轻量风险头，通过λ参数灵活调优业务安全-效用平衡，无需全链路重训，落地成本极低

  - 可执行资产风险标注可复用三级校验机制：先3个LLM初标，标注跨度≤1取中位数，跨度≥2人工审核，适配电商API、运营工具等场景的风险打标需求

  - 安全优先的部署场景可叠加后置规则过滤：限制top-k高风险工具数量、权限重叠度、冗余度，作为执行前第一道安全屏障，比下游执行校验成本低一个量级

  - 检索侧安全评估可复用RVR/SRR指标：替代纯相关性指标NDCG/MRR，量化top-k结果中高风险条目的暴露率，适配Agent、电商智能客服工具调用等场景的安全评测'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent工具检索仅优化语义相关性，召回的可执行工具若存在高风险操作（如文件删除、敏感数据读写），会在执行前就暴露安全隐患；而现有安全评估多聚焦执行后故障，未在检索阶段管控风险，导致下游安全校验压力极大，高风险工具一旦进入top-k候选集极易引发不可逆损失。

### 方法关键点
- 轻量双头重排架构：冻结上游ToolRet-BGE召回器，新增query相关的相关性头、工具维度的风险头，组合得分公式为 $s(q,t) = f_{rel}(q,t) - \lambda f_{risk}(t)$，$\lambda$ 可在推理时动态调整，灵活平衡安全与效用，无需全链路重训
- 风险标注与评估体系：将工具风险划分为L1~L5共5个等级，标注6108个工具，定义RVR@k、SRR@k、sNDCG三类检索侧安全指标，量化top-k结果中高风险工具的暴露率
- ToolGraph分数平滑：构建含共现、语义、权限、风险共现四类边的工具关系图，做1跳分数传播优化排序效果
- 可选规则过滤层：对top-k中高风险工具数量、高权限工具数量、工具冗余度做硬限制，适配安全优先的部署场景

### 关键实验
在UltraTool（2032个工具）和Seal-Tools（4076个工具）数据集上对比8个主流重排基线，核心版框架NDCG@5较最优基线提升11.3%，RVR@5降低21.8%；叠加规则过滤后RVR@5进一步降低38.7%，SRR@5降低54.8%，仅损失少量相关性。

### 核心结论
工具检索是Agent执行前的第一道安全边界，检索阶段的风险过滤可大幅降低下游执行侧的安全压力，而非仅靠执行后校验
