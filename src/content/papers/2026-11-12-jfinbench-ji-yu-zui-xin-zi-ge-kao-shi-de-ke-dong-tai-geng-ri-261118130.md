---
title: 'JFinBench: A Continuously Refreshable Japanese Financial Benchmark from the
  Latest Certification Exams'
title_zh: JFinBench：基于最新资格考试的可动态更新日语金融评测基准
authors:
- Issa Sugiura
- Taro Makino
- Takashi Ishida
affiliations:
- Sakana AI
- Institute of Science Tokyo
arxiv_id: '2611.18130'
url: https://arxiv.org/abs/2611.18130
pdf_url: https://arxiv.org/pdf/2611.18130
published: '2026-11-12'
collected: '2026-11-16'
category: Eval
direction: 金融领域LLM评测基准构建
tags:
- LLM
- Benchmark
- Finance
- Human-in-the-loop
- Agent
- Evaluation
one_liner: 提出采用人在环Agent管线构建的可定期刷新日语金融领域LLM评测基准JFinBench
practical_value: '- 垂类数据集构建可复用「人在环+Coding Agent」管线：构建电商合规、商品资质审核类评测集/训练集时，让Agent自动生成格式转换代码、可视化审核页，人工仅做校验反馈，可大幅降低人力成本，还支持定期更新规避数据污染

  - LLM选型可参考评测结论：垂类业务场景中即使给模型配置RAG、联网搜索等工具，基座本身的垂类知识储备仍会显著影响最终效果，不能完全依赖工具补齐能力短板

  - 动态评测集构建思路可迁移：电商大促、新监管规则落地后需高频更新合规审核、客服话术评测集的场景，可复用该周期性更新的管线设计'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有金融领域LLM评测基准对国别化金融规则覆盖不足，公开后易被训练数据污染，难以持续迭代适配最新监管要求。
### 方法关键点
1. JFinBench样本来自日本6类2026版金融资格考试（会计、税务、理财、银行等）共321条；
2. 采用人在环Agent构建管线：Coding Agent自动生成单考试格式转换代码与审核页，人工逐样本校验并反馈修正，适配异构考试格式，支持定期刷新缓解数据污染。
### 关键结果数字
12款主流LLM评测显示，Claude Fable 5、GPT-6 Astra整体准确率超93%，最优开源模型Kimi K3.1 Pro较Claude Fable 5低12个百分点；开通终端、网页访问权限后所有模型效果提升，但仍存在4个点差距，模型排名基本不变，基座自身知识储备即使搭配工具仍有价值。
