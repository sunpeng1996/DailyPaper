---
title: 'Questioning the Questions: Sustaining Self-Evolution in Reasoning Models'
title_zh: 质疑生成问题：实现推理模型的持续自我进化
authors:
- Jinyuan Li
- Chengsong Huang
- Langlin Huang
- Donghong Cai
- Shiping Gao
- Yuyi Yang
- Jiaxin Huang
affiliations:
- Washington University in St. Louis
- University of Michigan, Ann Arbor
arxiv_id: '2610.04299'
url: https://arxiv.org/abs/2610.04299
pdf_url: https://arxiv.org/pdf/2610.04299
published: '2026-10-02'
collected: '2026-10-08'
category: Reasoning
direction: 大模型推理 · 自进化性能优化
tags:
- Self-Evolution
- Reasoning LLM
- GRPO
- Question Generation
- Training Stability
one_liner: 通过有效性和任务新奇度反馈解决自进化性能崩溃，跨12个推理基准SOTA，10轮进化超基线17.32分
practical_value: '- 做电商Query/商品文案/推荐语义ID的自循环生成训练时，可借鉴有效性校验机制，先训练模型识别无效生成内容（矛盾/歧义/无解的Query、违规文案），过滤后再进训练集，避免训练跑偏

  - 内容多样性评估不要仅依赖文本相似度（BLEU、 embedding余弦），可基于底层任务语义做配对判断，比如相同意图的不同Query改写算重复，避免训练集多样性崩塌

  - 自进化训练时可加入小比例的校验任务回放数据，避免模型在迭代中丢失无效内容识别能力，保持长期迭代稳定性

  - 多角色（生成/校验/消费）协同训练时，可复用GRPO的相对奖励设计，把有效性、多样性信号直接融入生成器的奖励函数，降低额外标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于提问者-求解者协同的大模型自进化框架，多轮迭代后易出现性能崩溃，根因来自自生成问题的两个核心缺陷：一是无效问题（矛盾、缺条件、歧义）占比随轮次持续升高，现有一致性过滤机制反而进一步放大无效问题在训练集的比例；二是基于词汇相似度的重复检测无法识别语义等价的任务变种，导致训练集多样性快速崩塌，无法支撑持续进化。
### 方法关键点
- 有效性感知求解器初始化：构造带有效性标注的数据集，用GRPO训练求解器识别无效问题并返回INVALID标识，加入对有效问题误拒的惩罚，避免过度拒答
- 语义级新奇度评估：用冻结的基模型做批量内问题配对语义判断，识别语义等价的重复任务，通过单样本K次采样比对将计算复杂度从O(B²)降至O(BK)
- 闭环自进化：将有效性、新奇度判断结果融入提问者奖励函数，仅有效且新奇的问题可获得不确定性奖励；求解器训练时加入10%的有效性标注数据回放，避免迭代中丢失无效识别能力
### 关键结果
在Qwen3-4B、OctoThinker-3B两个模型族的12个基准（数学推理、通用推理、代码生成）上，10轮自进化后数学推理平均得分超基线R-Zero 17.32分，代码生成相对基模型提升3.9~5.23分，全程无性能崩溃；自生成问题有效率稳定在94%以上，而R-Zero第10轮无效问题占比达51%。

最值得记住的结论：自进化性能崩溃的核心瓶颈不是训练策略，而是自生成数据的质量，对生成内容有效性与语义多样性的把控是长期迭代收益的核心前提。
