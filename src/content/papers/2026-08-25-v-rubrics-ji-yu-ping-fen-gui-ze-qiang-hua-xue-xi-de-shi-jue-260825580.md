---
title: 'V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning'
title_zh: V-Rubrics：基于评分规则强化学习的视觉忠实度优化方法
authors:
- Shulin Tian
- Minglun Li
- Yuhao Dong
- Hao Ding
- Jiarui Yao
- Haiwen Diao
- Jingkang Yang
- Hongyuan Zhu
- Ziwei Liu
affiliations:
- S-Lab, Nanyang Technological University
- A*STAR
- UIUC
- Independent Researcher
arxiv_id: '2608.25580'
url: https://arxiv.org/abs/2608.25580
pdf_url: https://arxiv.org/pdf/2608.25580
published: '2026-08-25'
collected: '2026-08-27'
category: Multimodal
direction: 多模态LLM训练 · 细粒度RL奖励设计
tags:
- VLM
- GRPO
- Reinforcement Learning
- Visual Faithfulness
- Fine-grained Reward
one_liner: 提出基于视觉评分规则的GRPO框架，细粒度奖励提升VLM视觉推理忠实度
practical_value: '- 电商多模态Agent（商品图问答、直播内容理解）可复用三维度细粒度评分规则设计，将输出拆解为视觉符合度、逻辑一致性、指令遵循度打分，替代单一结果正误奖励，提升推理链可信度

  - 生成式推荐场景（基于商品图生成卖点文案、穿搭推荐理由）可借鉴前缀本地化奖励分配思路，将奖励信号锚定到对应输出片段，避免全局奖励模糊导致的局部幻觉

  - 小样本RL对齐训练可复用V-Rubrics 50K的数据构建流程：先规则粗过滤、再通过模型拒绝采样划分难度、最后用大模型标注原子评分规则，低成本构建高质量对齐数据集'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前视觉语言模型（VLM）生成回复流畅但常出现视觉幻觉，传统RL对齐采用的标量奖励仅能判断整体结果正误，无法定位哪部分视觉事实未对齐、哪步推理存在错误、哪条指令未被遵循，导致多模态推理任务的信用分配失效；尤其在图表、商品图、文档等高密度视觉信息场景下，局部错误会直接导致最终结果完全不可用。
### 方法关键点
- 设计三维度视觉评分规则（Rubric）框架：将参考回复拆解为原子命题，分别从Visual Faithfulness（VF，内容是否匹配图像）、Reasoning Consistency（RC，推理是否符合视觉证据）、Instruction Following（IF，是否满足指令要求）三个维度打分，每个规则项绑定权重，支持局部信用分配
- 构建V-Rubrics 50K数据集：从17个公开视觉推理数据源中，经规则过滤、拒绝采样划分难度、Gemini-3-Pro结构化标注，得到50248条带细粒度评分规则的训练样本
- 改进GRPO训练机制：将标量最终答案奖励与细粒度评分规则奖励加权融合，支持前缀本地化信用分配，将每个规则项的奖励信号锚定到对应输出片段，避免全局奖励的模糊性
### 关键结果
基于Qwen3-VL-8B-Instruct做SFT初始化，对比SFT基线、答案级GRPO基线：在MMMU/MMMU-Pro等知识类推理基准上Overall Avg. 比答案级GRPO提升1.79点；在视觉数学、图表、逻辑推理任务上Overall Avg. 比SFT基线提升4.00点（相对提升6.8%）；其中组件级+前缀本地化奖励设计比纯序列级规则聚合再提升0.3点。
### 核心结论
多模态模型对齐的核心不是奖励整体结果正确，而是把监督单位从最终答案拆解为与视觉证据绑定的原子事实、推理步骤和指令约束，让信用分配精准对应错误发生的位置。
