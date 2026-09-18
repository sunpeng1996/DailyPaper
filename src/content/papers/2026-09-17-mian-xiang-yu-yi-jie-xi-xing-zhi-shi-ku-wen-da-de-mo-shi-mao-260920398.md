---
title: Schema-Anchored Latent Reasoning for Semantic Parsing-Based Knowledge Base
  Question Answering
title_zh: 面向语义解析型知识库问答的模式锚定隐式推理方法
authors:
- Guangze Gao
- Zixuan Li
- Sikui Zhang
- Chunfeng Yuan
- Wenjuan Li
- Bing Li
- Xiaolong Jin
- Weiming Hu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2609.20398'
url: https://arxiv.org/abs/2609.20398
pdf_url: https://arxiv.org/pdf/2609.20398
published: '2026-09-17'
collected: '2026-09-18'
category: Reasoning
direction: 语义解析KBQA · 隐式推理优化
tags:
- Semantic Parsing
- KBQA
- Latent Reasoning
- Schema Alignment
- LLM
one_liner: 提出SALR模式锚定隐式推理方法，延迟知识库模式显式决策，提升语义解析型KBQA效果
practical_value: '- 电商导购Agent/知识图谱问答场景可借鉴延迟离散schema决策思路，避免中间选错商品属性/类目导致的多跳推理错误，提升复杂查询准确率

  - 可复用schema码本对齐方案，将业务自定义的类目、属性、商品关系等元信息编码后注入大模型推理链路，降低无关schema干扰

  - 隐式推理无需输出显式CoT轨迹，可减少推理token消耗，适配高并发的搜索问答、商品咨询等在线业务场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
基于语义解析的KBQA需生成可执行逻辑形式（LF）回答自然语言问题，现有LLM方法在大规模异构知识库场景下，会在推理早期对schema元素（关系、类）做出离散决策，错误的中间决策会传播导致最终LF生成错误。
### 方法关键点
1. 提出SALR模式锚定隐式推理框架，在模型隐状态层生成连续思考向量，延迟LF的显式决策，避免早期错误扩散；
2. 基于黄金LF导出的schema trace构造监督对齐目标，将连续思考向量与KB schema元素码本做对齐；
3. 将对齐后的schema编码注入后续推理步骤输入，无需显式输出CoT文本轨迹即可引导LF生成。
### 关键结果
在GrailQA、WebQSP数据集上全面优于强基线，其中GrailQA的组合问题上，F1值比强基线TIARA高2.86个点，验证了隐状态可恢复schema信息，schema介导反馈有效。
