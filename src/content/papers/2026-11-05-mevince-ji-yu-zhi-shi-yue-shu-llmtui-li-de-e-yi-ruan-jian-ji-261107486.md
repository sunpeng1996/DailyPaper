---
title: 'MEvince: Knowledge-Constrained LLM Reasoning for Technique Identification
  from Malware Reports'
title_zh: MEvince：基于知识约束LLM推理的恶意软件报告技术识别框架
authors:
- Hongyu She
- Yiling He
- Mengda Xie
- Yiping Liu
- Xingzhi Qian
- Zhan Qin
- Lorenzo Cavallaro
affiliations:
- 浙江大学
- 伦敦大学学院
- 江苏警官学院
- 阿里巴巴集团
arxiv_id: '2611.07486'
url: https://arxiv.org/abs/2611.07486
pdf_url: https://arxiv.org/pdf/2611.07486
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent推理优化 · 知识约束证据校验
tags:
- Knowledge-Constrained Reasoning
- LLM Grounding
- Evidence Verification
- Agentic Pipeline
- RAG Optimization
one_liner: 提出知识约束LLM推理框架，无需参数更新即可提升恶意软件技术识别的准确率与可解释性
practical_value: '- 可复用「行为原语提取+统一表示匹配」的RAG优化思路：电商场景下从用户长评论/咨询中提取动作、对象、目标、机制四元组，再匹配召回商品/服务，提升RAG匹配准确率，减少假阳性。

  - 可落地「两阶段证据校验」机制：在生成式推荐/LLM导购Agent的输出环节，先校验提取的用户需求是否有原文依据，再校验推荐结果是否匹配需求特征，大幅降低幻觉推荐比例。

  - 无需参数更新的离线证据记忆适配方法：可迁移到多品类推荐冷启动场景，用小样本标注的正例记忆库动态调整候选集优先级，无需重新SFT即可提升小众品类的推荐准确率。

  - 分散证据聚合思路：处理用户跨会话/跨页面的行为序列时，可通过语义组聚合分散的行为线索，还原完整用户意图，解决长周期用户建模的意图碎片化问题。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
将恶意软件分析报告中的行为智能映射到ATT&CK技术库是威胁分析防御的核心环节，但现有方案存在两大痛点：一是报告长、证据分散，相近技术仅靠细微特征区分，常规分类/SFT方案依赖大量标注且适配新攻击技术的成本极高；二是直接Prompt/RAG方案要么漏检分散的弱线索，要么将检索相关性等同于证据充分性，产生大量假阳性，结果无溯源性，无法满足安全审计要求。
### 方法关键点
- 离线构建共享行为表示层：通过Agent自动化挖掘技术文档，定义动作、对象、目标、机制四类行为原语，统一报告观测与技术定义的表示空间，解决跨域表示不匹配问题。
- 在线双阶段推理流水线：第一阶段原语引导提取，从报告中抽取结构化证据单元，关联原文出处，聚合分散的弱线索；第二阶段证据对齐检索，用统一原语匹配技术档案，同时召回易混淆候选供LLM对比区分。
- 双控校验+无参数适配：提取后校验证据的原文溯源性，映射后校验技术的证据充分性，过滤幻觉输出；离线证据记忆库用小样本正例动态调整候选集优先级，无需SFT即可适配新场景。
### 关键实验结果
在610份MITRE ATT&CK引用的公开恶意软件报告数据集上，对比11个涵盖分类、NER、SFT、上下文驱动LLM四类的基线方案：Exact-ID F1比最强基线（Llama-3.1-70B SFT）高17.4%，概念引导检索将金标候选覆盖率从31.6%提升到47.9%，叠加证据记忆后无需参数更新即可进一步提升F1，超过所有适配后的基线方案。

最值得记住的结论：外部知识仅用于引导解释，所有LLM决策必须绑定可溯源的原始观测证据，是平衡检索召回率与输出准确率、降低幻觉的核心路径。
