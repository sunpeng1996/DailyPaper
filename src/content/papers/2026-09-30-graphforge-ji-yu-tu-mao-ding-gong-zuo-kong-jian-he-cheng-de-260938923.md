---
title: 'GraphForge: Training Working Agents with Graph-Anchored Workspace Synthesis'
title_zh: GraphForge：基于图锚定工作空间合成的工作型Agent训练框架
authors:
- Qisheng Su
- Hanchen Wang
- Guanru Zhu
- Huicheng Jiang
- Qiuyinzhe Zhang
- Kou Shi
- Zhen Fang
- Ziao Zhang
- Qingnan Ren
- Zehui Chen
affiliations:
- University of Science and Technology of China
- Fudan University
- Shanghai Innovation Institute
- Shanghai AI Laboratory
arxiv_id: '2609.38923'
url: https://arxiv.org/abs/2609.38923
pdf_url: https://arxiv.org/pdf/2609.38923
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: 工作型Agent · 训练数据自动合成
tags:
- Agent Training
- Data Synthesis
- Evidence Graph
- Workspace Agent
- LLM Fine-tuning
one_liner: 提出基于证据图的工作型Agent训练数据合成框架，任务与验证均锚定真实文件
practical_value: '- 电商运营/数据分析类Agent训练可复用该框架：基于业务场景种子（如客服、投放效果分析）爬取真实业务文件，构建证据图生成可验证的训练任务，避免合成数据脱离业务实际

  - 多源文件推理的Agent评估可借鉴证据锚定的rubric设计：每条评估标准锚定对应数据源，大幅降低评估偏差，尤其适合电商多模态报表、用户反馈、商品数据联动的任务评估

  - 可复用其RFT筛选逻辑：用锚定证据的rubric做best-of-N轨迹筛选，比随机筛选或无锚定评分的效果更稳定，能低成本提升Agent在垂直业务场景的表现'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有工作型Agent训练数据合成方案要么生成的文件真实度、多样性不足，要么基于真实文件构建的任务缺乏可落地的验证规则，无法系统校验输出质量，导致训练出的Agent在真实长周期办公、业务处理场景表现差，难以落地到电商运营、数据分析等垂直场景。

### 方法关键点
- 采用O*NET职业数据库生成任务种子，控制任务的职业、任务类型、执行模式、输入文件类型四个维度的覆盖度，避免任务分布向高频场景塌陷
- 每个种子对应爬取真实公开文件构建工作空间，给文件分配核心、支撑、干扰、背景四类隐藏角色，还原真实工作场景的文件冗余性
- 基于工作空间文件的关联关系构建证据图，从证据图编译生成任务描述和评分规则，每条评分标准锚定对应证据文件，确保任务可验证
- 新增执行校验环节：用教师模型预跑任务，通过修正Agent迭代优化任务和评分规则，仅保留得分>0.9的高质量轨迹用于训练

### 关键结果
用2169条GraphForge生成的轨迹微调Qwen3.6-27B，在三个主流工作Agent基准上均取得大幅提升：GDPVal Elo达1445.7（+65.7），Workspace-Bench-Lite得分63.7（+7.7），SpreadsheetBench II准确率24.0（+13.7）；基于证据锚定规则的拒绝微调（RFT）比随机筛选轨迹的方案进一步提升效果，且能力可跨底座模型、跨Agent框架迁移。

### 核心结论
训练数据的可验证性比数据规模更重要，锚定真实证据的任务和评估规则是工作型Agent落地的核心前提。
