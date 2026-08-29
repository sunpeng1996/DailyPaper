---
title: 'Data Citation for Large Language Models: A Challenge'
title_zh: 大语言模型的数据引用：一项开放性挑战
authors:
- Gianmaria Silvello
affiliations:
- Department of Information Engineering, University of Padua
arxiv_id: '2608.25663'
url: https://arxiv.org/abs/2608.25663
pdf_url: https://arxiv.org/pdf/2608.25663
published: '2026-08-26'
collected: '2026-08-29'
category: LLM
direction: 大语言模型 · 数据引用与来源追溯
tags:
- LLM
- Data Citation
- RAG
- Knowledge Graph
- Data Provenance
one_liner: 明确LLM数据引用是比文档级引用更难的开放问题，提出三大核心研究方向
practical_value: '- 搭建业务RAG系统时，可参考粒度对齐思路给检索到的商品库/知识库片段绑定固定粒度的来源标识，方便结果溯源与版权合规校验

  - 开发Agent调用外部工具（商品库查询、KG检索等）时，可在推理链路增加数据引用埋点，快速定位错误输出的来源，提升badcase排查效率

  - 自研垂直领域LLM时，可参考训练数据归因思路，将训练样本影响度评估与版权标识绑定，规避训练数据版权纠纷风险'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM输出引用仅聚焦文档级内容验证，未覆盖学术引用的版权确权、来源追溯两大核心功能；且LLM输出来源涵盖训练语料、推理时RAG召回内容、KG调用结果、工具返回数据等多动态链路，现有文档级引用方案完全无法适配。
### 核心方向
LLM数据引用需突破三大核心模块：
1. 训练数据归因：将训练样本对模型输出的影响度评估转化为可标准化引用的语料标识
2. 推理阶段数据引用：对齐数据集/子集/查询结果的粒度与固定性，生成对应规范引用
3. KG事实引用：明确三元组引用规则与版权传导路径
### 结论
当前LLM数据引用仍是未解决的开放挑战，难度远高于文档级引用，需跨数据库、信息检索、知识表示、AI多领域联合攻关。
