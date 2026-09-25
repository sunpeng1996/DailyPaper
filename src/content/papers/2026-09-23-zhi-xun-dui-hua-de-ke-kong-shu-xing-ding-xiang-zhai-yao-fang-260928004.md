---
title: Controlled Attribute-Specific Summarization of Interrogative Dialogues
title_zh: 质询对话的可控属性定向摘要生成方法
authors:
- A Aditya Bhardwaj
- Arjit Singh Arora
- Md Shad Akhtar
affiliations:
- Department of Computer Science and Engineering, IIIT Delhi
arxiv_id: '2609.28004'
url: https://arxiv.org/abs/2609.28004
pdf_url: https://arxiv.org/pdf/2609.28004
published: '2026-09-23'
collected: '2026-09-25'
category: MultiAgent
direction: 多Agent协作 · 可控文本摘要
tags:
- Controllable Summarization
- Multi-Agent Evaluation
- Prompt Engineering
- Dialogue Processing
- Dataset Construction
one_liner: 提出带多角色分层评估的CASPER可控摘要框架，配套6k样本的MINDSum质询对话数据集
practical_value: '- 多角色分层迭代评估机制可复用在电商推荐文案生成校验场景，如商品卖点、直播话术生成后按运营、审核、用户三类角色维度迭代，提升合规性与转化效率

  - 属性定向结构化提示词+反馈回路的设计，可迁移到电商用户评价定向摘要生成，按物流、质量、售后等维度抽取核心信息用于商品页展示，降低用户决策成本

  - 高准确率要求的文本生成场景可参考先实体抽取再生成的流程，有效降低事实错误，可落地在客服对话摘要、售后投诉定向摘要等业务模块'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
司法场景下质询对话摘要要求极高的事实准确性、属性相关性，现有通用摘要模型易遗漏关键信息、产生事实错误，无法满足高风险场景的业务要求。
### 方法关键点
1. 构建MINDSum标注数据集，扩展MIND语料，包含6000组带事件详情、事实陈述、角色描述等标注的质询对话对；
2. 提出CASPER框架，采用属性定向CoT结构化提示词生成摘要初稿，搭配RoleEval分层多角色评估机制，通过实体抽取+结构化反馈回路迭代优化输出；
3. 模拟警员、督察、高级督察三类角色按预设规则交叉校验，保障摘要符合不同维度的业务要求。
### 关键结果
ROUGE（lexical）、BERTScore（semantic）两类核心指标均显著优于通用摘要基线模型，人工评估显示其生成结果与司法专家推理逻辑高度对齐，事实一致性提升超20%。
