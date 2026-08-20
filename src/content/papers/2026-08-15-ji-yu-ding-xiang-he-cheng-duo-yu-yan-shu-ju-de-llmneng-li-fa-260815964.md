---
title: LLMs Get Smarter from Targeted Synthetic Multilingual Data
title_zh: 基于定向合成多语言数据的LLM能力增强方法
authors:
- Ishika Agarwal
- Arkajyoti Charaborty
- Tanner Sorensen
- Neha Gupta
- Andreas Stolcke
affiliations:
- UIUC
- Uniphore
arxiv_id: '2608.15964'
url: https://arxiv.org/abs/2608.15964
pdf_url: https://arxiv.org/pdf/2608.15964
published: '2026-08-15'
collected: '2026-08-20'
category: Training
direction: 多语言LLM · 合成训练数据生成
tags:
- SyntheticData
- MultilingualLLM
- GRPO
- FineTuning
- CrossLingualAlignment
one_liner: 提出HOTFIXR靶向多语言合成数据框架，提升LLM多语言能力同时最小化通用性能损失
practical_value: '- 多语言场景Agent/推荐系统的LLM微调可复用HOTFIXR的缺陷探测思路：通过语言无关不确定性+跨语言隐态距离两个指标定位模型薄弱点，定向生成训练数据，避免全量多语言微调导致的英文能力下降

  - 做定制化SFT数据合成时，可参考用GRPO优化数据生成器的方案，仅需500条种子数据即可训练出靶向数据生成器，降低高质量训练数据的获取成本，同时控制奖励黑客风险

  - 跨境电商多语言客服、商品标题生成等场景，可复用该框架在不损失模型通用能力的前提下，提升小语种任务表现，OOD语言性能下降可控制在1.4%以内，远低于普通微调方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多语言LLM存在明显语言特定能力差异（LSC），同一语义问题用不同语言提问得到的回答质量差异大，现有两种解决方案均有缺陷：一是把所有query转成英语处理，限制非英语表达能力；二是用语言平衡数据训练，会拉低整体性能，尤其是英语任务的表现，亟需既能提升多语言一致性又不损失通用能力的方案。

### 方法关键点
- 提出HOTFIXR数据合成框架，核心是基于学生模型的缺陷信号用GRPO优化问题生成器，定向生成能填补模型缺陷的训练数据
- 定义两种缺陷度量指标：语言无关缺陷（LAI）用英语推理时的回答token平均置信度倒数，衡量模型通用能力短板；语言特定缺陷（LSI）用同一问题分别用英语和目标语言推理时最后一个推理token的隐态余弦距离，衡量跨语言表征对齐缺陷
- 训练时仅用500条种子数据作为问题生成器的上下文示例，避免训练样本过多导致的奖励黑客问题，生成5000条训练数据后用SFT微调学生模型

### 关键实验结果
在Qwen2.5 7B/14B、Llama3.1 8B三个模型上验证，覆盖Nemotron推理、MMMLU事实知识、mHotPotQA多语言RAG、OPUS-100翻译4类任务，对比7种基线：分布内任务平均性能提升6.2%，OOD任务上比其他训练基线平均高5.6%，仅比base模型下降0.9%；OOD语言上比其他训练基线平均高7.1%，性能下降仅1.4%，远低于其他方案的3.1%-12.5%；多语言性能标准差仅0.11，为所有方法最低，跨语言一致性最好。

**最值得记住的一句话**：定向合成针对模型缺陷的训练数据，比简单增加多语言训练数据量的效率高得多，能在最小化通用能力损失的前提下大幅提升多语言表现。
