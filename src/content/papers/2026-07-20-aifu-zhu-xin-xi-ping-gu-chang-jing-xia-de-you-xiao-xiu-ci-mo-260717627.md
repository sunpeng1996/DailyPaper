---
title: 'It Matters How You Say It: Exploring Rhetorical Patterns for AI-Assisted Information
  Evaluation'
title_zh: AI辅助信息评估场景下的有效修辞模式探索
authors:
- Sadra Sabouri
- Zeinabsadat Saghi
- Jordan Lee Boyd-Graber
- Jonathan May
- Jonathan K. Kummerfeld
- Souti Chattopadhyay
affiliations:
- University of Southern California
- University of Maryland
- University of Sydney
- Information Sciences Institute
arxiv_id: '2607.17627'
url: https://arxiv.org/abs/2607.17627
pdf_url: https://arxiv.org/pdf/2607.17627
published: '2026-07-20'
collected: '2026-07-22'
category: Agent
direction: 对话Agent · 回复修辞策略优化
tags:
- Conversational_Agent
- Rhetorical_Strategy
- Human_AI_Interaction
- Misinformation_Detection
- User_Study
one_liner: 系统对比8种AI回复修辞模式，揭示信息评估场景下用户准确率、满意度、反思度的权衡规律
practical_value: '- 电商/内容平台的事实核验类Agent（如商品真伪核查、虚假宣传识别助手）可优先采用Scaffold Explanation阶梯式推理回复结构，相比直接给结论的Oracle基线，准确率提升21.6%还能诱导用户主动反思，降低过度依赖AI错误结论的风险

  - 高风险场景（如理财、健康类咨询、消费维权）可适度引入Triggering Distrust类轻对抗修辞，通过加入少量可识别的荒谬信息触发用户主动校验，准确率可提升17.7%，注意需提前获得用户授权避免信任损耗

  - 不要完全依赖用户满意度反馈优化Agent回复策略，用户偏好最高的Alternative Framing模式准确率提升不显著，建议低风险场景（如通用咨询）对齐用户偏好，高风险场景优先对齐决策效果

  - 设计诱导反思的回复摩擦时需保证清晰性，无信息支撑的纯反问（如Socratic Questioning模式）不仅无准确率增益，还会增加18.3秒单轮耗时，拉高用户流失率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有AI辅助信息评估系统大多采用直接下结论的指令式修辞，用户容易被动接受AI输出，即便存在hallucination或关键信息遗漏也难以察觉。过往研究仅关注AI回复的信息内容，未系统探索修辞模式对用户反思能力、决策准确率的影响；在电商虚假宣传识别、不实健康/财经信息核验等高风险场景下，引导用户主动批判思考比直接给出结论的长期价值更高。
### 方法关键点
- 从语言学、心理学领域提取8种修辞模式：包括直接输出金标准结论的Oracle基线，以及Scaffold Explanation（阶梯式推理）、Socratic Questioning（引导反问）、Triggering Distrust（植入荒谬信息诱导不信任）等7种实验模式，所有模式信息内核一致，仅修辞结构不同
- 采用n=98的组内实验设计，被试完成40条事实核查任务，可主动请求AI建议，接收建议后可修改答案，全程记录准确率、置信度、任务耗时、主观偏好等指标
- 实验用claim从Fool-Me-Twice数据集随机抽取，难度均衡，覆盖35%真、65%假两类样本
### 关键结果
- 对比Oracle基线，Scaffold Explanation模式带来的准确率提升最高，达21.6%，同时能有效诱导用户深度反思；其次是Triggering Distrust模式，准确率提升17.7%
- 用户偏好与决策效果完全错位：最受用户欢迎的Alternative Framing模式准确率提升仅10.2%，统计上不显著；无信息支撑的Socratic Questioning模式无准确率增益，单轮任务耗时比基线高18.3秒
- 所有模式均会提升用户置信度，哪怕是未带来准确率提升的模式，存在明显的置信度校准偏差
### 核心结论
AI辅助信息评估场景下，优化回复的修辞模式与优化回复的信息内容同等重要，用户满意度不能作为系统效果的唯一评价指标。
