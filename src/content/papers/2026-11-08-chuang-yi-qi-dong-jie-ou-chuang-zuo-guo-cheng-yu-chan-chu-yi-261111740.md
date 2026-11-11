---
title: 'Creative Priming: Decoupling Process from Product to Escape the Creative Paradox'
title_zh: 创意启动：解耦创作过程与产出以突破创意悖论
authors:
- Alon Albalak
- Sebastian Gabriel
- David B. D&#39;Ambrosio
- Joel Lehman
- Kenneth O. Stanley
affiliations:
- Lila Sciences
arxiv_id: '2611.11740'
url: https://arxiv.org/abs/2611.11740
pdf_url: https://arxiv.org/pdf/2611.11740
published: '2026-11-08'
collected: '2026-11-11'
category: LLM
direction: LLM创意生成 · 过程解耦训练
tags:
- Creative Generation
- GRPO
- Prompt Priming
- Decoupled Learning
- Novelty Optimization
one_liner: 提出解耦创意过程与生成的创意启动框架，大幅提升LLM创意产出的新颖性、多样性与质量
practical_value: '- 可复用创意启动架构，训练独立轻量priming模型引导大模型生成电商文案、营销创意、个性化推荐理由，无需fine-tune基座，适配任意闭源API大模型，节省训练成本

  - 奖励设计可迁移到生成式推荐、Query推荐的多样性优化，采用「质量×多样性×新颖度」乘积奖励，避免单维度优化的顾此失彼，同时用GRPO做组相对优化缓解样本bias

  - 解决生成同质化问题的思路可直接复用：解耦引导逻辑和生成逻辑，避免直接fine-tune基座导致的创意悖论（重复历史高优样本反而损失多样性），尤其适合新品营销、小众兴趣内容推荐等需要高新颖度的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM训练方法直接优化生成结果，会陷入创意悖论：学习重复历史成功创意样本会提高同类输出概率，反而抑制真正的新颖创意生成，而AI在营销文案、新品创意、内容创作等高价值业务场景的核心需求恰好是持续的创造性输出，现有方法无法突破该瓶颈。

### 方法关键点
- 架构解耦：训练独立的Creative Priming（CP）模型生成prompt专属引导语，输入给冻结的基座响应模型生成结果，仅优化CP模型不修改基座，实现创意过程和最终产出的解耦
- 奖励设计：采用乘积形式的多层奖励，包括响应层（创意度=新颖度×质量、组内/组间多样性）和priming层（引导语质量、同prompt/跨prompt引导语多样性），所有指标归一化到[0,1]区间，仅当所有维度达标才获得高奖励
- 训练策略：基于GRPO（组相对策略优化）训练CP模型，避免直接强化具体生成结果，仅强化引导创意生成的过程

### 关键实验
在NoveltyBench数据集上测试，对比直接fine-tune基座的DGRPO、DARLING两个基线：CP生成同时满足新颖、高质量、语义独特的响应数比基线高39%~200%；仅在Qwen3-8B小模型上训练的CP模型可直接迁移到Claude、GPT等前沿闭源API模型，提升语义独特响应数4.5~10倍、多样性2.5~4.6倍，同时质量持平或微升；直接fine-tune基座的方法增加训练样本量后创意性能先升后降，验证了创意悖论的存在。

### 核心结论
避免创意悖论的核心是学习创意生成的底层原则，而非重复过往的具体创意产出。
