---
title: 'Recipes for Creativity: Iterative Generation and Evaluation in Large Language
  Models'
title_zh: LLM创意内容迭代生成与评估方法：以食谱生成为例
authors:
- Rens Anderson
- Tessa Verhoef
- Amirhossein Zohrehvand
affiliations:
- Leiden University, LIACS
arxiv_id: '2608.07243'
url: https://arxiv.org/abs/2608.07243
pdf_url: https://arxiv.org/pdf/2608.07243
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM创意生成 · 迭代优化评估
tags:
- LLM
- Iterative Generation
- Creative Generation
- LLM-as-Judge
- FunSearch
one_liner: 将FunSearch适配到主观创意生成场景，验证评估器设计对输出质量的影响远大于迭代次数与采样温度
practical_value: '- 做电商营销文案、商品标题、种草话术等主观创意生成时，优先优化in-loop评估器设计，而非盲目增加迭代次数或调高采样温度，可大幅降低算力浪费

  - 主观类生成任务的in-loop评估器不一定要用最大参数模型，中小模型对新颖性的容忍度更高，更易产出有差异化的创意结果，适配营销等需要新鲜感的场景

  - 迭代生成框架可借鉴多island候选池设计，保留不同风格的候选分支，避免过早收敛到平庸结果，适合需要多风格产出的个性化推荐物料生成场景

  - LLM自动评估时强制先输出评估依据再给分、限定JSON输出格式，可大幅提升评分稳定性和可解析性，可直接复用在业务的自动评估链路中'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM创意生成多聚焦单次输出评估，而人类创意本质是迭代生成、评估、优化的循环过程；此前FunSearch等迭代搜索框架仅用于数学等可量化的客观任务，主观创意场景下迭代优化的关键影响因子尚不明确，亟需明确各设计变量的优先级。
### 方法关键点
- 适配FunSearch到食谱生成场景，基于2024年Pillsbury烘焙大赛规则定义食谱骨架约束，采用多island候选池设计保留生成多样性，每轮基于高评分候选做best-shot prompt生成新候选
- in-loop筛选采用Pillsbury官方评分规则（食谱占70%、配套故事占30%），最终创意质量基于TTCT框架的4个维度（流畅性、灵活性、原创性、精细化）做LLM自动评估，评估时强制先输出rationale再打分，提升评分稳定性
- 两组控制变量实验：实验1控制迭代次数（1/5/15/30轮），实验2控制生成器温度（0.5/1.0/1.5）和in-loop评估器大小（Meta-8B/Meta-17B）
### 关键结果
- 迭代生成的食谱平均创意得分3.92，超过人类参赛基准的3.64，达到人类可比水平；但迭代次数从5轮提升到30轮时，得分无显著提升（3.92→3.927）
- in-loop评估器对结果影响最大：8B小评估器的平均创意得分比17B大评估器高0.16，在流畅性、灵活性、精细化维度均显著更高，仅原创性无差异
- 温度仅对原创性有显著影响：0.5低温度比1.5高温度的原创性得分低0.14，中高温度对各维度无显著影响

**最值得记住的结论：主观创意搜索场景下，评估器设计是第一优先级的优化变量，单纯增加迭代次数或采样随机性无法有效提升输出质量**
