---
title: 'Gacha Decoding: Eliciting Diverse Generations Through Instruction Following'
title_zh: Gacha Decoding：基于指令跟随的大模型多样化生成推理方法
authors:
- Scott Geng
- Yufei Zhang
- Joseph Lee
- Jerry Li
- Marjan Ghazvininejad
- Pang Wei Koh
affiliations:
- University of Washington
- Meta Superintelligence Labs
arxiv_id: '2610.01382'
url: https://arxiv.org/abs/2610.01382
pdf_url: https://arxiv.org/pdf/2610.01382
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: 大模型推理 · 多样化生成解码
tags:
- Decoding
- Diversity
- Instruction Following
- Inference Optimization
- LLM Generation
one_liner: 将多样化生成重构为指令跟随任务，用外部随机数实现无token熵依赖的高多样性生成
practical_value: '- 电商营销文案、商品标题、创意素材生成场景可直接复用该框架，通过外部RNG随机选择语义决策轴，在不降低内容质量的前提下提升输出多样性，避免同质化推送导致的用户疲劳

  - 生成式推荐场景可将Semantic ID生成拆解为品类、风格、价格区间等语义决策轴，通过外部随机选择扩展召回池多样性，解决大模型推荐的模式塌陷问题

  - Agent任务规划、探索类场景可复用「语义决策轴枚举+外部随机选择+自回归条件生成」范式，提升规划路径多样性，避免陷入局部最优解

  - 仅为推理层prompt harness架构，无需修改模型参数，工程落地成本极低，可快速嵌入现有LLM调用链路'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型生成多样性高度依赖token熵，而模型能力越强（对齐度越高）token熵越低，导致生成多样性随模型能力提升反而下降，在创意写作、多模态规划、科学发现等开放域场景下极易出现模式塌陷，无法满足需要多样化输出的业务需求，传统调整采样参数、修改训练目标的方式难以解决这一固有矛盾。

### 方法关键点
- 核心思路将多样化生成重构为指令跟随任务，不依赖token熵，利用大模型的指令跟随能力结合外部RNG实现多样性，彻底反转多样性与模型能力的负相关tradeoff
- 三阶段推理流程：1）规划阶段：指令LM识别出决定输出的T个语义决策轴（如写故事的背景设定、角色身份、叙事视角）；2）自回归采样阶段：对每个决策轴，指令LM枚举符合前置决策的语义选项，用外部RNG均匀随机选择一个，后续决策基于已选结果条件枚举；3）生成阶段：基于所有采样的决策生成符合要求的最终输出
- 仅为推理层框架，无需修改模型参数，可作为轻量harness套在任意现有LM外层使用

### 关键实验
覆盖4类开放域场景：野生聊天、创意写作、文生图prompt生成、蛋白质设计，对比Direct Sampling、List Prompting、Verbalized Sampling等7种基线方法，核心结果：1）同等质量下Vendi多样性最高超次优方法2.4倍；2）达到相同模式覆盖所需样本量比基线少11.0倍；3）是唯一一种多样性随模型指令跟随能力提升而上升的方法，即使在greedy解码（零token熵）下仍能保持95%以上的多样性。

### 最值得记住的一句话
大模型的多样性不需要内置在token分布里，外部随机数结合指令跟随能力即可实现高质量、可扩展的多样化生成
