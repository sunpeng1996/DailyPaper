---
title: 'Structure for Reading, Prose for Writing: Asymmetric Structural Conditioning
  in Multi-Agent Document Authoring'
title_zh: 多Agent文档创作的非对称结构适配：阅读用结构，写作用散文
authors:
- Cheng Yu
- Nikhil Mathew
- Zhengjie Wang
affiliations:
- ML Research Labs, Canberra, Australia
arxiv_id: '2608.20786'
url: https://arxiv.org/abs/2608.20786
pdf_url: https://arxiv.org/pdf/2608.20786
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: 多Agent长文档生成系统优化
tags:
- MultiAgent
- LongDocumentGeneration
- PromptEngineering
- LLM-as-Judge
- StructuredParsing
one_liner: 揭示多Agent文档创作的结构适配不对称性，落地标书生成系统效果对标人类提交结果
practical_value: '- 做Agent任务拆解时，阅读类任务（商品详情结构化抽取、用户评论信息提取等）优先采用嵌套结构化表示，可大幅提升准确率和运行稳定性

  - 生成类任务（商品文案、营销话术生成等）的指令输入不要使用结构化标记，改用自然语言散文形式，避免结构化标签抬升非预期内容的显著性

  - Prompt中不要直接命名禁止的内容，会导致该类错误更集中；应改为要求模型对输出做自检，比如输出后删掉来自要求的重复内容，无剩余有效信息则重写，可用于广告合规、内容风控等场景

  - 多Agent流水线的窗口/分块逻辑要基于原始无标注文本，不要基于模型输出的带标注文本，避免上游随机标注的波动被下游确定性分块放大，可适配搜索召回、长文本理解等场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
正式文档（标书、合规文件）生成要求严格遵循输入要求、无幻觉，现有多Agent方案仅验证结构化表示对阅读类任务的增益，未验证其对生成环节指令适配的影响，同时私有部署生成系统的真实效果缺乏与人类提交结果的客观对标，信息缺口与生成能力缺陷的归因模糊。
### 方法关键点
- 43个单角色Agent+1个多轮起草Agent组成DAG流水线，分6个阶段加3个人工校验gate，输入文档解析为带唯一eid的层级结构，要求文本全程不做模型改写
- 槽位识别用echo-diff机制：模型原封不动回显输入，仅给待填写槽加标记，代码对比输入输出差值得槽位，避免幻觉
- 起草采用4轮固定流程：自问规划→召回相似历史问题生成草稿→合规校验→质量优化，优化阶段仅允许新增/标记问题，禁止删除内容
- 评估时将与人类输出的gap分为4类：信息未提供、可用未使用、政策差异、非必要额外内容，区分输入缺口与生成缺陷
### 关键结果
- 无样例盲测：LLM judge判定73%（40/55）章节至少和人类提交标书质量相当，仅1个无依据声明；排除输入信息缺失导致的gap后，占比提升至89%，68%的gap源于系统未拿到对应信息，非生成能力问题
- 阅读类任务用结构化表示：注释路由准确率从61%升至97.8%，工作表槽位识别波动从124降至1-2，历史标书分段从不稳定到完全可复现
- 生成任务指令用结构化XML时，答案合格率从74%降至48%；prompt明确命名禁止表达时，96%的残留错误为被禁止类型

**最值得记住的一句话**：结构属于模型阅读的环节，生成环节要用散文和自校验规则。
