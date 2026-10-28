---
title: 'ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?'
title_zh: ParetoRSI-Gym：多域下AI代理迭代优化大模型能力基准
authors:
- Haojin Wang
- Yangzhen Wu
- Zeyi Chen
- Jian Xie
- Jiaying Ye
- Lili Meng
- Shuyun Tang
- Shangding Gu
- Dawn Song
affiliations:
- University of Illinois Urbana-Champaign
- University of California, Berkeley
- The Ohio State University
- University of Washington
- Google
arxiv_id: '2610.34386'
url: https://arxiv.org/abs/2610.34386
pdf_url: https://arxiv.org/pdf/2610.34386
published: '2026-10-24'
collected: '2026-10-28'
category: Agent
direction: Agent 递归自优化多域评测基准
tags:
- RSI
- Benchmark
- Data Curation
- Multi-Domain
- LoRA
one_liner: 首个多域反馈驱动的递归自优化数据 curation 基准，支持评估Agent自动提升大模型跨域能力
practical_value: '- 垂域大模型迭代可复用「proxy反馈+泛化校验」双评估框架：用公开基准做迭代反馈，内部held-out基准做最终校验，避免过拟合迭代过程的反馈信号，适配电商搜/推/广多场景SFT效果评估

  - 多目标SFT迭代时不要只用最后一轮checkpoint：实测7/9场景下最优性能出现在前几轮，需保留中间checkpoint池做最优选择，避免多目标权衡导致的效果倒退

  - Agent驱动的自动化数据curation场景中，同等骨干模型下harness设计对最终效果的影响可达4.1个绝对百分点，资源投入可优先倾斜到流程框架、prompt、工具链打磨，而非仅升级大模型骨干

  - 多目标迭代可采用Pareto前沿评估方法，避免单一目标加权导致的部分域效果大幅倒退，适合多业务线联合SFT的效果评估'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有递归自优化（RSI）相关基准均针对单域单指标设计，而真实工业场景下大模型post-training需要同时兼顾多域能力，提升某一域效果往往伴随其他域效果倒退，缺乏贴近真实场景的多域Agent自优化评测基准。

### 方法关键点
- 设定数学、代码、金融、医疗、科学5个目标域，采用控制变量设计：固定初始模型、SFT pipeline、工具集，Agent仅负责数据检索筛选、训练超参配置
- 5轮闭环迭代框架：每轮Agent基于前序反馈更新数据选择原则，从HuggingFace检索筛选数据，用LoRA SFT微调，返回5个域的proxy基准得分迭代优化
- 双评估体系：迭代过程中用可见的proxy基准做反馈，最终用完全不可见的泛化基准评估真实能力提升，规避过拟合和数据污染

### 关键实验结果
测试3类Agent、3款3B-7B base模型，最优Agent（Claude Code with Opus-5）的proxy最佳checkpoint相对初始模型泛化得分相对提升9.2%（绝对+2.3），单域最高相对提升63%（医疗域Ministral-3B）；7/9的实验配置中最优性能出现在前4轮而非最后一轮，同骨干模型下不同harness的效果差距可达4.1个绝对百分点，同Agent的数据集选择Jaccard相似度达0.24，远高于跨Agent的0.07。

> 最值得记住的结论：当前Agent驱动的多域大模型迭代的核心瓶颈不是骨干模型能力，而是harness框架设计和多目标迭代的checkpoint选择策略
