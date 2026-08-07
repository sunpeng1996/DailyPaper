---
title: 'FinanceHarness: Autonomous Financial Deep Research Framework'
title_zh: FinanceHarness：面向金融领域的自主深度研究Agent框架
authors:
- Yijia Xiao
- Rujun Han
- Yanfei Chen
- Zifeng Wang
- Ke Jiang
- Zhongying CuiZhu
- Vishy Tirumalashetty
- Wei Wang
- Burak Gokturk
- Tomas Pfister
affiliations:
- Google Cloud AI Research
- University of California, Los Angeles
arxiv_id: '2607.27853'
url: https://arxiv.org/abs/2607.27853
pdf_url: https://arxiv.org/pdf/2607.27853
published: '2026-07-29'
collected: '2026-08-07'
category: Agent
direction: 金融领域深度研究Agent框架与评测
tags:
- Agent
- Financial LLM
- Benchmark
- Tool Use
- Evaluation
one_liner: 构建金融领域点-in-time评测基准FinanceGym与专家引导的端到端深度研究Agent框架
practical_value: '- 做垂直领域Agent时可复用分层工具设计：核心工具常驻prompt、扩展工具懒加载，既控制prompt长度，又覆盖领域专属能力（如电商的库存/价格/券计算工具）

  - 垂直领域Agent评测可参考双层rubric设计：拆分历史事实检索、未来预测验证两个维度，配合带时间cutoff的检索沙箱，彻底避免评测中的数据穿越问题，适合电商大促预判、活动效果预估等时序敏感场景

  - 同基座下优化领域脚手架性价比远高于盲目升级大模型：本文27B基座下，适配金融场景的FinanceHarness比纯搜索模型得分从25.3%提升至32.4%，效果追平更大参数的开源模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用深度研究Agent生成的泛用报告无法满足金融研究对专业知识、历史规律分析、未来事件预判的需求；现有金融NLP评测仅覆盖孤立能力，也没有避免未来信息泄露的时序约束机制，无法衡量完整的金融深度研究报告质量。

### 方法关键点
- 构建点-in-time（PIT）金融检索沙箱：收录1亿+带明确发布时间的网页文章，用Qwen3-Embedding-4B向量化，FAISS索引支持按问题指定的cutoff日期过滤检索结果，彻底杜绝未来信息泄露
- 搭建FinanceGym评测基准：从金融实体图中采样真实研究场景，生成400个专家验证的研究问题，配套pre-cutoff（历史事实检索）、post-cutoff（未来预测验证）双层可校验rubric，覆盖9个主题、9个行业、6种推理类型
- 提出FinanceHarness框架：采用分层设计，工具层拆分核心常驻工具、懒加载扩展工具，运行时层管控Agent执行流与资源预算，封装金融专属分析工具与工作流，支持与评测体系对齐的GRPO强化学习优化

### 关键结果
在FinanceGym上测试17个基线系统，所有系统整体得分均低于40%；同27B开源基座下，FinanceHarness比纯搜索模型整体得分从25.3%提升至32.4%，效果优于所有开源基线与主流Agent脚手架，接近专有大模型水平；所有系统pre-cutoff得分普遍是post-cutoff得分的3~4倍，未来预测是金融研究的核心难点。

### 核心结论
垂直领域Agent的效果提升，基座模型能力是基础，适配领域特性的脚手架设计与对齐的评测体系，往往能带来更高的投入产出比
