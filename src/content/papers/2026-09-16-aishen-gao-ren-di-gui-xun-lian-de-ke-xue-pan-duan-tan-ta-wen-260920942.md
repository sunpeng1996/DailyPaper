---
title: 'When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation'
title_zh: AI审稿人递归训练的科学判断坍塌问题与双阶段缓解方案
authors:
- Sy-Tuyen Ho
- Minghui Liu
- Furong Huang
affiliations:
- University of Maryland, College Park
arxiv_id: '2609.20942'
url: https://arxiv.org/abs/2609.20942
pdf_url: https://arxiv.org/pdf/2609.20942
published: '2026-09-16'
collected: '2026-09-21'
category: LLM
direction: LLM训练 · 模型坍塌缓解
tags:
- LLM
- Recursive Training
- Model Collapse
- Activation Steering
- Synthetic Data
one_liner: 发现AI审稿人递归训练的判断坍塌现象，提出双阶段干预的开源TrustReviewer系统
practical_value: '- 做生成式推荐/广告文案/Agent决策的训练时，若混入LLM生成的合成数据，需严格控制合成数据占比，优先保留高质量真实标注数据，避免输出同质化（比如推荐理由、文案越来越趋同，用户新鲜感下降）

  - 可复用论文的训练语料过滤规则：去除过短文本、重复n-gram样本、结构不符合要求的生成内容，能从源头降低输出同质化风险，无需调整模型结构即可见效

  - 测试阶段的成对activation steering技术可快速对齐真实数据分布，无需重新SFT即可提升生成内容的多样性与对齐度，适合推荐/广告场景的快速迭代需求

  - 评估生成内容多样性时，可引入同输入语义余弦距离、语料级语义扩散度两个指标，比传统perplexity、BLEU更能捕捉同质化问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM越来越多参与科学审稿等评价类任务，生成的输出进入公开数据集后会被用于训练下一代LLM，形成递归训练闭环，但现有模型坍塌研究很少关注条件生成场景下的判断同质化问题，可能导致AI的评价/生成结果越来越趋同，失去多样性，严重影响生成类任务的用户体验。

### 方法关键点
- 控制变量实验设计：基于Llama 3.1 8B先在2018-2023年ICLR官方审稿数据上用LoRA SFT得到初代审稿人，再用0%/33%/66%/100%不同比例的合成审稿数据混合2024年官方数据训练下一代审稿人，完全隔离合成数据的影响
- TrustReviewer双阶段缓解方案：训练阶段对2018-2025年ICLR审稿语料做严格过滤，去除低质量、重复、过短、结构异常的样本，单阶段SFT得到核心模型；测试阶段用成对activation steering，基于同论文的官方审稿和生成审稿的隐层表示差构造steering向量，推理时注入调整输出，无需额外训练或标注

### 关键结果
- 控制实验显示：100%合成数据训练的模型相比0%合成数据基线，同论文语义多样性下降11%，语料级语义多样性下降5%，评分分布明显压缩
- 对比Llama 3.1 8B、OpenReviewer、Qwen3.6-35B-A3B等基线，TrustReviewer的推荐精确匹配率达75.4%，比次优的OpenReviewer高2.3个百分点，评分熵达2.18，更接近官方数据的2.38；activation steering无需额外训练就能提升1.55个百分点的匹配率，同时提升评分熵

### 核心结论
递归训练中合成数据占比越高，模型的条件输出越容易出现同质化坍塌，而非单纯的精度下降，缓解需要同时从训练数据质量治理和推理阶段轻量干预两个维度入手。
