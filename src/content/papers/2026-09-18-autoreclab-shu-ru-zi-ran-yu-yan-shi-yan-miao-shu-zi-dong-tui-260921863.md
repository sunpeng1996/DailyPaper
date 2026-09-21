---
title: 'AutoRecLab: Describe the Experiment, Get the Code!'
title_zh: AutoRecLab：输入自然语言实验描述自动生成推荐系统可执行代码
authors:
- Moritz Baumgart
- Philipp Meister
- Justus Krell
- Michael Schmidt
- Bela Gipp
- Joeran Beel
affiliations:
- University of Siegen
- University of Göttingen
arxiv_id: '2609.21863'
url: https://arxiv.org/abs/2609.21863
pdf_url: https://arxiv.org/pdf/2609.21863
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 推荐系统实验自动化
tags:
- Recommender-Systems
- Autonomous-Agent
- Code-Generation
- RAG
- LLM
one_liner: 提出融合RAG与执行导向搜索的RecSys实验自动化工具，支持自然语言转可执行实验代码
practical_value: '- 可借鉴RAG+静态类型校验+执行导向树搜索的代码生成工作流，搭建内部推荐算法实验代码自动生成工具，减少baseline代码人工编写量

  - 执行导向树搜索的代码迭代优化思路可复用在AB实验代码自动生成、策略上线代码校验等业务场景，降低代码出错率

  - 做实验效率优化时，可参考需求拆解→原型验证→完整扩展的三段式流程，搭建内部自动化实验框架'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
RecSys研究与工业算法迭代中，将实验设计转化为可执行代码需大量人工操作，流程繁琐且易引入错误，缺乏端到端自动化方案。
### 方法关键点
1. 推出Python框架AutoRecLab，支持输入自然语言实验描述，自动输出完整可执行的RecSys实验代码；
2. 工作流融合RAG做库文档检索、静态类型校验做语法检查、执行导向树搜索做代码迭代优化，分需求拆解、原型验证、完整实验扩展三个阶段推进。
### 关键结果
在6种算法、3个数据集的基线对比任务中，9次运行共8次成功；基于GPT-5.4-mini实现，平均单次运行成本约1美元，可自主完成显式转隐式反馈转换类实验的代码实现。
