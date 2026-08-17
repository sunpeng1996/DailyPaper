---
title: 'The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning'
title_zh: 自适应流行度方法AdaPop：解决LLM高流行度事实难遗忘问题
authors:
- Anna Borisiuk
- Andrey Savchenko
- Alexander Panchenko
- Elena Tutubalina
affiliations:
- AIRI
- Sber AI Lab
- Skoltech
- ISP RAS Research Center for Trusted Artificial Intelligence
arxiv_id: '2608.14229'
url: https://arxiv.org/abs/2608.14229
pdf_url: https://arxiv.org/pdf/2608.14229
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM机器遗忘 · 自适应梯度优化
tags:
- LLM-Unlearning
- Adaptive-Gradient
- LoRA
- Knowledge-Removal
- Dual-Ascent
one_liner: 基于外部流行度信号调整遗忘梯度权重结合双上升控制器，大幅提升LLM事实遗忘效果与鲁棒性
practical_value: '- 电商/Agent场景下擦除高热度过时信息（如过期爆款规则、下架商品介绍）时，可参考AdaPop思路，用搜索量/曝光量作为流行度代理给高热度待擦除内容加权，解决均匀梯度下高热度内容擦除不彻底的问题，避免用户换个问法就泄露过时信息

  - 双上升自动调参机制可直接复用到所有需要平衡两类损失的LoRA微调场景（如合规内容擦除、个性化偏好对齐），无需逐数据集做超参搜索，大幅降低调参成本

  - 评估遗忘/擦除效果时不要仅看表层输出匹配度，可复用隐藏层相似度、token rank变化等内部指标，避免出现仅抑制表层输出、底层记忆仍可被诱导激活的问题

  - 流行度代理信号不需要高精度，只要有粗粒度的高低区分即可，落地成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM遗忘方法对所有待擦除事实施加均匀梯度，但预训练中出现频率更高的流行事实记忆更深，均匀梯度会导致罕见事实过度擦除、流行事实擦除不彻底，在paraphrase、对抗性提问下极易泄露已删除内容，存在严重合规风险。

### 方法关键点
- 引入外部流行度代理信号（如Wikidata站点链接数、LLM-as-Judge打分、语料出现频率），通过幂律映射为每个待擦除事实分配梯度权重指数：高流行度事实进入梯度持续增强的压力保持区间，保证深层记忆被擦除；低流行度事实进入梯度自动衰减的自限制区间，避免过擦除
- 设计epoch级双上升控制器，动态调整保留知识的损失权重，无需逐数据集调超参，避免遗忘过程中通用能力坍塌
- 基于LoRA微调实现，适配7-8B规模主流开源LLM，训练成本低

### 关键实验结果
在Llama3.1-8B、Qwen2.5-7B、Gemma-7B三个模型，DUET、RWKU两个事实遗忘基准上对比GA、GD、NPO、WGA等SOTA基线：
1. paraphrase查询下遗忘内容泄露量比基线低~5×，对抗性重构查询下泄露量低~1.6×
2. 待擦除事实的隐藏层表示偏移量远高于基线，证明是真遗忘而非表层输出抑制
3. MMLU、HellaSwag通用能力得分比预训练checkpoint下降不超过0.05，知识保留效果优异

**最值得记住的一句话**：仅依赖模型自身输出置信度的遗忘方法只能抑制表层输出，必须引入外部记忆深度相关信号才能真正擦除深度记忆的高流行度内容
