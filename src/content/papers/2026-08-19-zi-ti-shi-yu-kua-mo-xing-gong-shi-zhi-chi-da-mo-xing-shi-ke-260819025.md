---
title: Self-prompting and cross-model consensus enable reproducible data extraction
  from scientific literature with large language models
title_zh: 自提示与跨模型共识支持大模型实现科学文献可复现数据提取
authors:
- Valentin Romanov
- Monique Bax
- Steven Niederer
affiliations:
- Imperial College London
- University of Cambridge
- Stanford University
arxiv_id: '2608.19025'
url: https://arxiv.org/abs/2608.19025
pdf_url: https://arxiv.org/pdf/2608.19025
published: '2026-08-19'
collected: '2026-08-20'
category: LLM
direction: LLM 信息提取工作流优化
tags:
- Prompt Engineering
- Data Extraction
- Cross-model Consensus
- LLM Workflow
- Human-in-the-loop
one_liner: 验证自提示生成prompt、跨模型共识校验的文献提取工作流，性能接近专家手写prompt效果
practical_value: '- 电商商品属性打标、用户评价/客服对话结构化提取场景可复用自提示方案：仅需给LLM简单的提取规则说明，让其自动生成场景适配的prompt，替代专家手动编写prompt，大幅降低prompt优化成本

  - 高准确率要求的信息提取任务（如广告合规校验、敏感内容识别）可引入跨模型共识校验机制，多个LLM独立提取结果取交集，有效降低 hallucination 率

  - 复杂自动化数据处理pipeline可保留human-in-the-loop设计，仅调度人工处理模型有分歧的case，在保证准确率的前提下最大化提效'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
科研文献高上下文关联信息的人工提取耗时极长、成本极高，现有LLM提取方案依赖专家编写prompt、易出现科学语境理解偏差与幻觉，缺乏可复现的标准化工作流。
### 方法关键点
设计4组递进工作流开展对比验证：① 专家撰写定制化prompt+LLM直接执行提取；② LLM基于简单指令自主生成适配任务的prompt后完成提取；③ 端到端Agent自主检索文献并执行信息提取；④ 跨多LLM共识校验+人在回路的数据集生产链路。
### 关键结果
LLM自生成prompt的提取效果接近专家手写prompt水平；跨模型共识生成的数据集标注结果与人类专家匹配度达90%+；Agent自主文献检索存在漏召、幻觉问题，暂无法脱离人工校验；最终人机分工方案可降低90%以上的人工文献处理工作量，同时保留专家质控能力。
