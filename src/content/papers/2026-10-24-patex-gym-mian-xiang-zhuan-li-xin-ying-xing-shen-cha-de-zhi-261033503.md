---
title: 'Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in
  Patent Examination'
title_zh: PatEx-Gym：面向专利新颖性审查的智能体现有技术检索框架
authors:
- Qiyao Wang
- Xinyi Chen
- Hongbo Wang
- Jiayuan Lu
- Jianhang Li
- Minghuan Tan
- Yuan Lin
- Min Yang
affiliations:
- 中国科学院深圳先进技术研究院
- 中国科学院大学
- 大连理工大学
- 深圳先进技术大学
arxiv_id: '2610.33503'
url: https://arxiv.org/abs/2610.33503
pdf_url: https://arxiv.org/pdf/2610.33503
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: 智能体检索 · 垂直领域落地
tags:
- Agentic Search
- Trajectory Synthesis
- SFT
- Information Retrieval
- Vertical Domain LLM
one_liner: 首个专利审查智能体评测框架，用无标注轨迹训练4B基线性能媲美30B大模型
practical_value: '- 漏斗式召回评估框架可迁移到电商检索场景：从召回、点击、转化全链路评估效果，替代单一TopK召回率指标，更贴合业务实际价值

  - PASS无标注轨迹合成方法可复用：把用户点击/浏览作为隐式相关性锚点，分层建模查询迭代质量，自动生成高质量训练轨迹，大幅降低领域Agent标注成本

  - 轻量化Agent训练范式可借鉴：小参数模型在领域合成轨迹上做SFT即可媲美大10倍的通用大模型，适合电商本地化低延迟部署需求

  - 多检索工具组合收益得到验证：业务中不需要盲目升级单一检索模型，布尔+BM25+稠密检索互补组合即可显著提升检索覆盖'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有专利审查基准多基于静态候选集，无法覆盖真实场景下迭代检索、证据校验、结论生成的完整流程；同时通用大模型在垂直领域检索场景下推理成本高、检索到证据落地的链路效果不可控，亟需一套完整的基准框架和低成本的领域智能体训练方案。

### 方法关键点
- 构建PatEx-Bench基准：包含1K真实专利审查任务，1M专利+52K论文的检索语料，支持迭代检索、文档访问、推理、审查通知书生成的完整runtime
- 提出PASS无标注轨迹合成框架：把文档访问作为隐式相关性锚点，分层建模轮内查询行为、轮间搜索进展、轨迹级证据和结果质量，筛选出3K高质量轨迹得到PatEx-SynData
- 基于Qwen3.5-4B做SFT训练得到PatEx-Agent轻量化基线，训练时仅对模型输出的推理和工具调用token计算损失，环境返回结果不参与损失计算

### 关键结果
对比13款不同参数规模的开源/闭源大模型，4B的PatEx-Agent较基线提升42.7%的审查文档质量分，现有技术搜索召回达38.7%，性能媲美30B参数通用模型；非专利文献检索召回达69.4%，接近最强闭源模型Qwen3.8-Max的69.6%；即使是最强闭源模型Claude-Opus-5的最终证据选择召回也仅32.4%，说明检索到证据落地的链路仍有巨大优化空间。

### 核心结论
最终决策准确率无法完全反映检索类任务的质量，从检索、访问到最终证据选择的全链路优化才是垂直领域智能体检索的核心。
