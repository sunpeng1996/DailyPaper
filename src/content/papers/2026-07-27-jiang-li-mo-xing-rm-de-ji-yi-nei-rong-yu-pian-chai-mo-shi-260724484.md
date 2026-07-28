---
title: What do Reward Models Memorize?
title_zh: 奖励模型（RM）的记忆内容与偏差模式研究
authors:
- Ivo Verhoeven
- Pushkar Mishra
- Ekaterina Shutova
affiliations:
- University of Amsterdam
- Google DeepMind
arxiv_id: '2607.24484'
url: https://arxiv.org/abs/2607.24484
pdf_url: https://arxiv.org/pdf/2607.24484
published: '2026-07-27'
collected: '2026-07-28'
category: Training
direction: 大语言模型对齐 · 奖励模型训练
tags:
- Reward Model
- RLHF
- Counterfactual Memorization
- Alignment
- Spurious Correlation
one_liner: 通过反事实记忆度量揭示判别式训练奖励模型的三类记忆偏差，解释奖励黑客的来源
practical_value: '- 训练业务场景RM（如用户满意度打分、推荐排序奖励、Agent工具调用奖励）时，需补充OOD测试集（跨品类、跨用户群、跨生成模型样本），避免RM学到商品ID、商家ID等伪特征导致线上效果退化

  - RM训练可采用课程学习策略，优先喂入低margin难样本（如用户打分接近的偏好对、歧义query的响应对），避免模型浪费容量记忆高margin简单样本，提升泛化性

  - 用RLHF调优生成式推荐文案、Agent回复时，需针对性抑制RM的表层启发式偏差（如偏好长文本、格式化内容），可加入规则约束或多目标奖励，避免生成无价值的冗长内容刷分

  - 可复用反事实记忆（CM）的度量方法，对业务RM做泛化性评估，通过SHAP归因定位RM学到的非因果特征，快速迭代训练数据和目标'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RLHF是当前LLM对齐的核心范式，但RM作为人类偏好的代理，经常出现奖励黑客问题，比如生成冗长、奉承、刻板的输出，根源在于RM训练时的记忆偏差，此前没有研究专门分析RM的记忆内容，因此需要系统拆解RM的记忆模式，解决对齐鲁棒性问题。

### 方法关键点
- 采用**反事实记忆（CM）**作为核心度量，等于样本在训练集内的分类准确率（TM）减去训练集外的分类准确率（TG），值越高代表记忆越强、泛化越差
- 基于PRISM、COMMUNITY两个公开人类偏好数据集，训练Llama-3.2-1B作为base的RM，用25次随机子集拆分统计TM、TG，构建记忆地图
- 结合84个人工设计特征（长度、合规性、情绪、用户属性、模型ID等）+ SAE稀疏自编码器提取的隐特征，用SHAP值做特征归因，定位影响记忆的因素

### 关键结果
在两个数据集上，回归模型预测TM的R²分别达0.56/0.63，预测TG达0.52/0.38，预测CM达0.39/0.33，证明RM的表现大部分可被浅层特征解释；发现三类核心记忆模式：1）优先记忆高margin的容易偏好对，容量错配；2）记忆数据集无关的伪特征（如模型ID、用户招募批次），这类特征占CM解释度的Top3；3）对长度、合规性等启发式特征过泛化，违背启发式的样本必须靠记忆才能正确分类。

### 最值得记住的一句话
判别式训练的RM学到的大多是数据集捷径和表层相关性，而非人类偏好的真正因果机制，直接用于OOD场景对齐会引发严重的奖励黑客风险。
