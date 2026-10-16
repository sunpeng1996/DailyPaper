---
title: 'Not X, but When: Diagnosing a Mandarin LLM Writing Tic through Contextual
  Appropriateness'
title_zh: 中文大模型「不是X而是Y」句式的语境适配性缺陷诊断
authors:
- Yihang Peng
- Yi Jing
- Dewen Liu
- Weihan Meng
- Ying Liu
affiliations:
- Tsinghua University
- Fudan University
arxiv_id: '2610.22249'
url: https://arxiv.org/abs/2610.22249
pdf_url: https://arxiv.org/pdf/2610.22249
published: '2026-10-15'
collected: '2026-10-16'
category: Eval
direction: LLM生成评估 · 语境适配性诊断
tags:
- LLM
- Pragmatics
- Contextual Appropriateness
- RLHF
- Evaluation
one_liner: 基于语用学决策树诊断LLM句式过度使用问题，追溯其来自奖励模型与训练偏好
practical_value: '- 做电商文案生成、客服Agent话术生成时，可借鉴该决策树逻辑做规则化校验，避免无语境支撑的「不是X而是Y」类冗余表达降低用户好感

  - 优化垂直领域LLM的SFT、DPO训练数据时，可针对性过滤无上下文依据的偏好表达样本，避免奖励模型重表面句式轻语境的偏差传导到生成端

  - 搭建LLM回答质量评估体系时，需新增语境适配性维度的打分规则，不要仅因表达流畅、有文采就给高分，减少评估偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM生成文本的重复表达常被当做机器生成特征直接按频率压制，但这类表达本身多有合法语用价值，一刀切压制会同时消除合理使用场景；当前对LLM语用能力的评估多偏向理解侧，生成侧的语境适配性（即知道「什么时候用某表达」而非仅能「正确使用某表达」）长期被忽略，而这是人类交际能力的核心。

### 方法关键点
- 基于格莱斯语用学和纠正性否定理论，设计决策树将「不是X而是Y」的使用分为三类：实质性（语境确实需要纠正）、可选（语法正确但无必要）、缺陷（使用错误），判断逻辑先排查事实冲突、观点错配等缺陷，再校验语境是否存在X的合理替代、纠正是否能推进当前讨论
- 配套对比实验：通过最小化编辑生成仅移除/调整该句式的对照版本，测试奖励模型、LLM评委的偏好，同时追踪Base/SFT/DPO不同训练阶段模型的句式使用频率变化

### 关键实验结果
测试集包含5款商用LLM针对1061条中文prompt生成的5285条回答，人类参考语料来自社区回答、学生作文、公开考试答案等。核心结论：商用LLM的句式使用密度是人类的2.5~9.2倍；307条标注样本中仅1.3%是错误使用，52.8%是可选使用（正确但无必要）；3款主流奖励模型在质量匹配的变体中68.3%~76.8%偏好保留该句式，LLM评委对无语境支撑的使用也没有惩罚，SFT和DPO阶段都会提升该句式的使用频率。

最值得记住的一句话：压制表面表达频率会同时消除合理使用，要减少这类无意义的AI写作tic，需要让评估和训练信号能识别表达是否符合语境需要。
